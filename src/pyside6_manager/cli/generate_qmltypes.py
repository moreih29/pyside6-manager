import os
import re
import glob

import typer
from pydantic import BaseModel

router = typer.Typer()


QOBJECT_DERIVED_CLASSES = [
    "QObject",
    "QQuickItem",
    "QQuickPaintedItem",
    "QQuickFramebufferObject",
    "QOpenGLFunctionsQGraphicsItem",
    "QAbstractItemModel",
    "QAbstractListModel",
    "QAbstractTableModel",
    "QSortFilterProxyModel",
]


class SignalInfo(BaseModel):
    name: str
    parameters: list[dict[str, str]]


class PropertyInfo(BaseModel):
    name: str
    type: str
    notify: str | None = None
    index: int = 0


class SlotInfo(BaseModel):
    name: str
    type: str
    parameters: list[dict[str, str]]


class ClassInfo(BaseModel):
    file: str
    name: str
    accessSemantics: str
    prototype: str
    exports: list[str]
    isCreatable: bool = True
    isSingleton: bool = False
    exportMetaObjectRevisions: list[int]
    property: list[PropertyInfo] = []
    signal: list[SignalInfo] = []
    method: list[SlotInfo] = []


def parse_property(prop_name: str, source_code: str) -> PropertyInfo:
    """
    클래스에서 Property 데코레이터가 적용된 속성 정보를 추출합니다.

    Args:
        prop_name (str): 속성 이름
        source_code (str): 소스 코드

    Returns:
        PropertyInfo: 속성 정보
    """
    # Property의 타입 정보 추출
    prop_type = "QVariant"
    notify_signal = None

    # 소스 코드에서 Property 정보 추출
    prop_pattern = r"@Property\(([^,]+),\s*notify=([a-zA-Z0-9_]+)\)"
    prop_matches = re.finditer(prop_pattern, source_code)

    for match in prop_matches:
        if match and re.search(
            rf"def {prop_name}\(", source_code[match.start() : match.start() + 200]
        ):
            prop_type = match.group(1).strip()
            notify_signal = match.group(2).strip()
            prop_type = _convert_python_type_to_qml(prop_type)
            break

    result = PropertyInfo(
        name=prop_name,
        type=prop_type,
        notify=notify_signal,
    )

    return result


def parse_signal(signal_name: str, source_code: str) -> SignalInfo:
    """
    클래스에서 Signal 객체의 정보를 추출합니다.

    Args:
        signal_name (str): 시그널 이름
        source_code (str): 소스 코드

    Returns:
        SignalInfo: 시그널 정보
    """
    # 시그널 파라미터 추출 (소스 코드 파싱)
    signal_pattern = rf"{signal_name}\s*=\s*Signal\(([^)]*)\)"
    matches = re.search(signal_pattern, source_code)

    parameters: list[dict[str, str]] = []
    if matches and matches.group(1).strip():
        param_types = matches.group(1).split(",")
        for i, param_type in enumerate(param_types):
            param_type = param_type.strip()
            if param_type:
                parameters.append(
                    {"name": f"arg{i}", "type": _convert_python_type_to_qml(param_type)}
                )

    result = SignalInfo(name=signal_name, parameters=parameters)

    return result


def parse_slot(method_name: str, source_code: str) -> SlotInfo:
    """
    클래스에서 Slot 데코레이터가 적용된 메소드 정보를 추출합니다.

    Args:
        method_name (str): 메소드 이름
        source_code (str): 소스 코드

    Returns:
        SlotInfo: 메소드 정보
    """
    # Slot 데코레이터 정보 추출 (소스 코드 파싱)
    slot_pattern = rf"@Slot\(([^)]*)\)[^@]*def\s+{method_name}\s*\("
    slot_return_pattern = (
        rf"@Slot\([^)]*result=([a-zA-Z0-9_]+)[^)]*\)[^@]*def\s+{method_name}\s*\("
    )
    param_pattern = rf"def\s+{method_name}\s*\(self(?:,\s*([^)]*))?\)"
    return_type_annotation_pattern = (
        rf"def\s+{method_name}\s*\([^)]*\)\s*->\s*([a-zA-Z0-9_]+)"
    )

    # 반환 타입과 파라미터 타입 추출
    return_type = "void"

    # Slot 반환 타입 추출 (@Slot(result=xxx)) - 수정된 정규식
    return_matches = re.search(slot_return_pattern, source_code)
    if return_matches and return_matches.group(1).strip():
        return_type = _convert_python_type_to_qml(return_matches.group(1).strip())
    else:
        # 파이썬 타입 힌트에서 반환 타입 추출 (-> xxx)
        return_type_annotation = re.search(return_type_annotation_pattern, source_code)
        if return_type_annotation and return_type_annotation.group(1).strip():
            return_type = _convert_python_type_to_qml(
                return_type_annotation.group(1).strip()
            )
        else:
            # 반환 타입 추정 시도
            method_body_pattern = rf"def\s+{method_name}\s*\([^)]*\)(?:\s*->.*?)?:\s*(.*?)(?=\n\s*@|\n\s*def|\Z)"
            method_body_match = re.search(method_body_pattern, source_code, re.DOTALL)
            if method_body_match:
                method_body = method_body_match.group(1)
                # return 문 찾기
                return_statements = re.findall(r"return\s+([^#\n]+)", method_body)
                if return_statements:
                    # 첫 번째 return 문 분석
                    return_expr = return_statements[0].strip()
                    if return_expr.startswith("int("):
                        return_type = "int"
                    elif return_expr.startswith("bool("):
                        return_type = "bool"
                    elif return_expr.startswith("str("):
                        return_type = "QString"
                    elif return_expr.startswith("float("):
                        return_type = "double"
                    elif return_expr in ["True", "False"]:
                        return_type = "bool"
                    elif return_expr.isdigit():
                        return_type = "int"
                    elif return_expr.startswith('"') or return_expr.startswith("'"):
                        return_type = "QString"
                    elif (
                        "==" in return_expr
                        or ">" in return_expr
                        or "<" in return_expr
                        or "and" in return_expr
                        or "or" in return_expr
                    ):
                        # 비교 연산자는 보통 bool을 반환
                        return_type = "bool"

    # 파라미터 추출
    parameters: list[dict[str, str]] = []
    params_match = re.search(param_pattern, source_code)

    if params_match and params_match.group(1):
        param_str = params_match.group(1).strip()
        if param_str:
            param_parts = param_str.split(",")

            # Slot 파라미터 타입 추출
            slot_matches = re.search(slot_pattern, source_code)
            slot_types = []
            if slot_matches and slot_matches.group(1).strip():
                slot_types = [
                    t.strip()
                    for t in slot_matches.group(1).split(",")
                    if "result=" not in t
                ]

            for i, param in enumerate(param_parts):
                param = param.strip()
                if not param:
                    continue

                param_name = param.split(":")[0].strip()
                param_type = "QVariant"

                # 타입 힌트 확인
                type_hint_match = re.search(rf"{param_name}\s*:\s*([^=,)]+)", param)
                if type_hint_match:
                    param_type = _convert_python_type_to_qml(
                        type_hint_match.group(1).strip()
                    )
                elif i < len(slot_types):
                    param_type = _convert_python_type_to_qml(slot_types[i])

                parameters.append({"name": param_name, "type": param_type})

    result = SlotInfo(name=method_name, type=return_type, parameters=parameters)
    return result


def parse_qobject_class_from_source(
    path: str, cls_name: str, module_name: str
) -> ClassInfo | None:
    """
    소스 코드 파일에서 직접 QObject 파생 클래스 정보를 추출합니다.

    Args:
        path (str): 소스 코드 파일 경로
        cls_name (str): 클래스 이름
        module_name (str): 모듈 이름

    Returns:
        ClassInfo | None: 클래스 정보
    """
    try:
        with open(path, "r", encoding="utf-8") as f:
            source_code = f.read()

        # QObject 또는 그 파생 클래스 목록
        qobject_derived_classes = QOBJECT_DERIVED_CLASSES

        # 상속 패턴에 사용할 클래스 목록 작성
        inheritance_patterns = _get_inheritance_patterns(source_code)

        # 클래스 정의 찾기 (QObject 또는 파생 클래스를 상속)
        class_pattern = rf"class\s+{cls_name}\s*\(([^)]*)\):.*?(?=class\s+|$)"
        class_match = re.search(class_pattern, source_code, re.DOTALL)

        if not class_match:
            print(f"  Warning: Could not find class definition for {cls_name}")
            return None

        # 클래스가 QObject 파생 클래스를 상속하는지 확인
        bases = class_match.group(1)
        if not any(qcls in bases for qcls in qobject_derived_classes):
            # 정규식으로 한 번 더 확인
            if inheritance_patterns and not re.search(
                rf"class\s+{cls_name}\s*\([^)]*({inheritance_patterns})[^)]*\):",
                source_code,
            ):
                print(
                    f"  Warning: Class {cls_name} does not inherit from any QObject-derived class"
                )
                return None

        class_code = class_match.group(0)

        class_info = ClassInfo(
            file=os.path.basename(path),
            name=cls_name,
            accessSemantics="reference",
            prototype="QObject",
            exports=[f'"{module_name}/{cls_name} 1.0"'],
            exportMetaObjectRevisions=[256],
        )

        # 실제 상속 클래스에 따라 prototype 업데이트
        for qcls in qobject_derived_classes:
            if qcls in bases:
                class_info.prototype = qcls
                break

        # 싱글톤 여부 확인 - 파일의 시작부터 클래스 정의 시작점까지만 검사
        prefix_code = source_code[: class_match.start()]
        is_singleton = "@Singleton" in prefix_code.split("\n")[-5:]

        # isCreatable과 isSingleton 설정 (싱글톤이면 isCreatable은 false)
        class_info.isSingleton = is_singleton
        class_info.isCreatable = not is_singleton

        # Property, Signal, Slot 찾기
        properties: list[PropertyInfo] = []
        signals: list[SignalInfo] = []
        methods: list[SlotInfo] = []

        # Signal 찾기
        signal_pattern = r"(\w+)\s*=\s*Signal\("
        signal_matches = re.finditer(signal_pattern, class_code)
        for match in signal_matches:
            signal_name = match.group(1)
            signals.append(parse_signal(signal_name, class_code))

        # Property 찾기
        prop_pattern = r"@Property\([^)]+\)\s*def\s+(\w+)\s*\("
        prop_matches = re.finditer(prop_pattern, class_code)
        for match in prop_matches:
            prop_name = match.group(1)
            properties.append(parse_property(prop_name, class_code))

        # Slot 찾기
        slot_pattern = r"@Slot\([^)]*\)\s*def\s+(\w+)\s*\("
        slot_matches = re.finditer(slot_pattern, class_code)
        for match in slot_matches:
            method_name = match.group(1)
            methods.append(parse_slot(method_name, class_code))

        # 프로퍼티에 인덱스 추가
        for i, prop in enumerate(properties):
            prop.index = i

        class_info.property = properties
        class_info.signal = signals
        class_info.method = methods

        return class_info

    except Exception as e:
        print(f"Error parsing class {cls_name} from source: {str(e)}")
        import traceback

        traceback.print_exc()
        return None


def _convert_python_type_to_qml(python_type: str | type) -> str:
    """Python 타입을 QML 타입으로 변환합니다.

    Args:
        python_type (str | type): Python 타입

    Returns:
        str: QML 타입
    """
    type_str = str(python_type)
    # 기본 타입 변환
    basic_types = {
        "str": "QString",
        "int": "int",
        "float": "double",
        "bool": "bool",
        "list": "QVariantList",
        "dict": "QVariantMap",
        "tuple": "QVariantList",
        "None": "void",
    }

    # 타입 힌트 문자열 정리
    type_str = type_str.replace("<class '", "").replace("'>", "")

    if type_str in basic_types:
        return basic_types[type_str]

    # 제네릭 타입 처리
    if "typing.List" in type_str or "list[" in type_str:
        return "QVariantList"
    if "typing.Dict" in type_str or "dict[" in type_str:
        return "QVariantMap"
    if "typing.Optional" in type_str:
        # Optional[Type] 형태에서 Type 추출
        inner_type = re.search(r"Optional\[(.*?)\]", type_str)
        if inner_type:
            return _convert_python_type_to_qml(inner_type.group(1))
    if "typing.Union" in type_str:
        # Union[Type1, Type2] 형태에서 가장 일반적인 타입 사용
        return "QVariant"

    # 커스텀 클래스 또는 알 수 없는 타입
    return "QVariant"


def _get_inheritance_patterns(source_code: str) -> str:
    """
    컨텐츠에서 상속 패턴을 추출합니다.

    Args:
        source_code (str): 소스 코드

    Returns:
        str: 상속 패턴
    """

    # QObject 또는 그 파생 클래스 목록
    qobject_derived_classes = QOBJECT_DERIVED_CLASSES

    # 파일에서 import된 PySide6 모듈 분석
    imports: list[str] = re.findall(
        r"from\s+PySide6\.\w+\s+import\s+([^#\n]+)", source_code
    )
    imported_classes: list[str] = []
    for import_stmt in imports:
        imported_classes.extend([cls.strip() for cls in import_stmt.split(",")])

    # 파일에 import된 QObject 파생 클래스 찾기
    qobject_classes_in_file: list[str] = [
        cls for cls in imported_classes if cls in qobject_derived_classes
    ]

    # 상속 패턴에 사용할 클래스 목록 작성
    inheritance_patterns = "|".join(qobject_classes_in_file + qobject_derived_classes)

    return inheritance_patterns


def find_qobject_classes_from_file(path: str) -> list[str]:
    """
    파일에서 QObject 파생 클래스를 상속받는 클래스 이름 목록을 찾습니다.

    Args:
        path (str): .py 파일 경로

    Returns:
        list[str]: QObject 파생 클래스 이름 목록
    """
    try:
        with open(path, "r", encoding="utf-8") as f:
            source_code = f.read()

        # QObject 또는 그 파생 클래스 목록
        qobject_derived_classes = QOBJECT_DERIVED_CLASSES

        # 상속 패턴에 사용할 클래스 목록 작성
        inheritance_patterns = _get_inheritance_patterns(source_code)

        # 모든 클래스 정의 찾기
        class_defs: list[tuple[str, str]] = re.findall(
            r"class\s+(\w+)\s*\(([^)]+)\):", source_code
        )

        # QObject 또는 그 파생 클래스를 상속받는 클래스 필터링
        filtered_classes: list[str] = []
        for cls_name, bases in class_defs:
            # PySide6 기본 클래스 제외
            if cls_name in qobject_derived_classes:
                continue

            # 상속받는 클래스 목록
            base_classes: list[str] = [base.strip() for base in bases.split(",")]

            # QObject 또는 파생 클래스 상속 확인
            for base in base_classes:
                if any(qcls in base for qcls in qobject_derived_classes):
                    filtered_classes.append(cls_name)
                    break

            # 2차 검사: 정규식으로 상속 관계 확인
            if cls_name not in filtered_classes and inheritance_patterns:
                if re.search(
                    rf"class\s+{cls_name}\s*\([^)]*({inheritance_patterns})[^)]*\):",
                    source_code,
                ):
                    filtered_classes.append(cls_name)

        return filtered_classes

    except Exception as e:
        print(f"Error finding QObject classes in {path}: {str(e)}")
        import traceback

        traceback.print_exc()
        return []


def find_all_python_files(paths: list[str]) -> list[str]:
    """
    주어진 패턴에 매칭되는 모든 Python 파일 목록을 반환합니다.
    파일이 발견되지 않을 경우 기본 디렉토리를 추가로 검색합니다.

    Args:
        paths (list[str]): 파일 경로 패턴 또는 경로 목록

    Returns:
        list[str]: .py 파일 경로 목록
    """
    all_files: list[str] = []

    # * 문자가 포함된 패턴을 정확한 파일 경로로 분리
    exact_files: list[str] = []
    pattern_searches: list[str] = []

    for pattern in paths:
        if "*" in pattern:
            pattern_searches.append(pattern)
        else:
            # 정확한 파일 경로인 경우
            if os.path.isfile(pattern) and pattern.endswith(".py"):
                exact_files.append(pattern)
            elif os.path.isdir(pattern):
                # 디렉토리인 경우 모든 .py 파일 추가
                pattern_searches.append(os.path.join(pattern, "**", "*.py"))

    # 패턴 검색 수행
    for pattern in pattern_searches:
        files = glob.glob(pattern, recursive=True)
        if files:
            all_files.extend(files)
        else:
            print(f"Warning: No files match the pattern '{pattern}'")

            # 패턴을 분석하여 기본 디렉토리 추가 검색
            if os.path.sep in pattern:
                base_dir = pattern.split(os.path.sep)[0]
                if os.path.isdir(base_dir):
                    # 디렉토리 내 모든 .py 파일 검색
                    for root, _, files in os.walk(base_dir):
                        for file in files:
                            if file.endswith(".py"):
                                all_files.append(os.path.join(root, file))

    # 정확한 파일 경로 추가
    all_files.extend(exact_files)

    # 중복 제거 및 정렬
    return sorted(set(all_files))


def generate_qmldir(output_file: str, module_name: str) -> bool:
    """
    qmldir 파일을 생성합니다.

    Args:
        output_file (str): qmldir 파일 경로
        module_name (str): 모듈 이름

    Returns:
        bool: 성공 여부
    """
    content = f"module {module_name}\n"
    content += f"typeinfo {module_name}.qmltypes\n"

    with open(output_file, "w") as f:
        f.write(content)

    print(f"Generated qmldir file: {output_file}")
    return True


@router.command(name="genqml")
def generate_qmltypes(
    paths: list[str] = typer.Argument(help="Python 파일 경로 또는 경로 목록"),
    output_file: str = typer.Option(
        "generated.qmltypes",
        "--output",
        "-o",
        help="생성할 qmltypes 파일 경로",
    ),
    module_name: str = typer.Option(
        "module",
        "--module",
        "-m",
        help="qmldir 파일에 사용할 모듈 이름",
    ),
    qmldir: bool = typer.Option(
        False,
        "--qmldir",
        "-q",
        help="qmldir 파일을 함께 생성합니다.",
    ),
) -> bool:
    """
    주어진 Python 파일들에서 QObject 파생 클래스를 파싱하여 .qmltypes 파일을 생성합니다.

    Args:
        paths: 파싱할 Python 파일 경로 또는 경로 목록 (glob 패턴 지원)
        output_file: 생성할 qmltypes 파일 경로
        module_name: qmldir 파일에 사용할 모듈 이름
        qmldir: qmldir 파일을 함께 생성합니다.

    Returns:
        성공 여부
    """
    # 파일 경로 목록 생성 - 개선된 검색 로직 사용
    py_files = find_all_python_files(paths)

    if not py_files:
        print(f"Error: No Python files found with pattern(s): {paths}")
        return False

    print(f"Found {len(py_files)} Python files to process")

    # 모든 QObject 클래스 정보 수집
    all_class_infos: list[ClassInfo] = []
    processed_files = 0
    qobject_files = 0

    for py_file in py_files:
        print(f"Processing file: {py_file}")

        try:
            # 파일에서 QObject 클래스 이름 찾기
            class_names = find_qobject_classes_from_file(py_file)

            if class_names:
                print(f"  Found {len(class_names)} QObject classes: {class_names}")
                qobject_files += 1

                # 각 클래스 정보 추출
                for cls_name in class_names:
                    class_info = parse_qobject_class_from_source(
                        py_file, cls_name, module_name
                    )
                    if class_info:
                        all_class_infos.append(class_info)

                processed_files += 1
            else:
                print(f"  No QObject classes found in {py_file}, skipping...")
        except Exception as e:
            print(f"  Error processing file {py_file}: {str(e)}")
            print("  Skipping this file and continuing with others...")
            import traceback

            traceback.print_exc()

    if not all_class_infos:
        if qobject_files > 0:
            print(
                "Warning: Found QObject classes but failed to parse them. Check for errors above."
            )
        else:
            print(
                "Error: No QObject-derived classes found in any of the specified files."
            )
        return False

    print(f"Successfully processed {processed_files} files with QObject classes")

    # qmltypes 파일 생성
    qmltypes_content = "import QtQuick.tooling 1.2\n\n"
    qmltypes_content += "Module {\n"

    for class_info in all_class_infos:
        print(f"Adding class to qmltypes: {class_info.name}")
        qmltypes_content += "\tComponent {\n"

        # 컴포넌트 기본 정보
        for key, value in class_info.model_dump().items():
            if key in ["property", "signal", "method"]:
                continue

            if isinstance(value, list):
                if key == "exports":
                    value_str = "[" + ", ".join(value) + "]"  # pyright: ignore[reportUnknownArgumentType]
                else:
                    value_str = "[" + ", ".join(map(str, value)) + "]"  # pyright: ignore[reportUnknownArgumentType]
                qmltypes_content += f"\t\t{key}: {value_str}\n"
            elif isinstance(value, bool):
                qmltypes_content += f"\t\t{key}: {str(value).lower()}\n"
            else:
                qmltypes_content += f'\t\t{key}: "{value}"\n'

        # 속성 정보
        if class_info.property:
            for prop in class_info.property:
                qmltypes_content += "\t\tProperty { "
                prop_parts: list[str] = []
                for k, v in prop.model_dump().items():
                    if isinstance(v, int):
                        prop_parts.append(f"{k}: {v}")
                    else:
                        prop_parts.append(f'{k}: "{v}"')
                qmltypes_content += "; ".join(prop_parts)
                qmltypes_content += " }\n"

        # 시그널 정보
        if class_info.signal:
            for signal in class_info.signal:
                qmltypes_content += f'\t\tSignal {{ name: "{signal.name}" '
                if signal.parameters:
                    qmltypes_content += "\n"
                    for param in signal.parameters:
                        qmltypes_content += f'\t\t\tParameter {{ name: "{param["name"]}"; type: "{param["type"]}" }}\n'
                    qmltypes_content += "\t\t"
                qmltypes_content += "}\n"

        # 메소드 정보
        if class_info.method:
            for method in class_info.method:
                qmltypes_content += "\t\tMethod { "
                if method.type != "void":
                    qmltypes_content += f'name: "{method.name}"; type: "{method.type}" '
                else:
                    qmltypes_content += f'name: "{method.name}" '

                if method.parameters:
                    qmltypes_content += "\n"
                    for param in method.parameters:
                        qmltypes_content += f'\t\t\tParameter {{ name: "{param["name"]}"; type: "{param["type"]}" }}\n'
                    qmltypes_content += "\t\t"
                qmltypes_content += "}\n"

        qmltypes_content += "\t}\n"

    qmltypes_content += "}\n"

    # 파일로 저장
    with open(output_file, "w") as f:
        f.write(qmltypes_content)

    print(f"Generated qmltypes file: {output_file}")

    if qmldir:
        generate_qmldir(
            os.path.join(os.path.dirname(output_file), "qmldir"),
            module_name,
        )

    return True
