import os
import re
import sys
import glob
from typing import Any


def parse_property(prop_name: str, source_code: str) -> dict[str, Any]:
    """클래스에서 Property 데코레이터가 적용된 속성 정보를 추출합니다."""
    result = {"name": prop_name, "type": "QVariant"}

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

    result["type"] = prop_type
    if notify_signal:
        result["notify"] = notify_signal

    return result


def parse_signal(signal_name: str, source_code: str) -> dict[str, Any]:
    """클래스에서 Signal 객체의 정보를 추출합니다."""
    result: dict[str, Any] = {"name": signal_name}

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

    if parameters:
        result["parameters"] = parameters

    return result


def parse_slot(method_name: str, source_code: str) -> dict[str, Any]:
    """클래스에서 Slot 데코레이터가 적용된 메소드 정보를 추출합니다."""
    result: dict[str, Any] = {"name": method_name}

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

    result["type"] = return_type
    if parameters:
        result["parameters"] = parameters

    return result


def parse_qobject_class_from_source(
    file_path: str, cls_name: str
) -> dict[str, Any] | None:
    """소스 코드 파일에서 직접 QObject 파생 클래스 정보를 추출합니다."""
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            source_code = f.read()

        # QObject 또는 그 파생 클래스 목록
        qobject_derived_classes = [
            "QObject",
            "QQuickPaintedItem",
            "QQuickItem",
            "QQuickFramebufferObject",
            "QWidget",
            "QMainWindow",
            "QDialog",
            "QApplication",
            "QGuiApplication",
            "QAction",
            "QLayout",
            "QGraphicsItem",
            "QAbstractItemModel",
            "QAbstractListModel",
            "QSettings",
        ]

        # 파일에서 import된 PySide6 모듈 분석
        imports = re.findall(r"from\s+PySide6\.\w+\s+import\s+([^#\n]+)", source_code)
        imported_classes = []
        for import_stmt in imports:
            imported_classes.extend([cls.strip() for cls in import_stmt.split(",")])

        # 파일에 import된 QObject 파생 클래스 찾기
        qobject_classes_in_file = [
            cls for cls in imported_classes if cls in qobject_derived_classes
        ]

        # 상속 패턴에 사용할 클래스 목록 작성
        inheritance_patterns = "|".join(
            qobject_classes_in_file + qobject_derived_classes
        )

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

        # 모듈 경로 분석 (exports 용)
        module_path = _get_module_path(file_path)

        # 클래스 정보 생성
        class_info: dict[str, Any] = {
            "file": os.path.basename(file_path),
            "name": cls_name,
            "accessSemantics": "reference",
            "prototype": "QObject",  # 기본값으로 QObject 사용
            "exports": [f'"{module_path}/{cls_name} 1.0"'],
            "exportMetaObjectRevisions": [256],
        }

        # 실제 상속 클래스에 따라 prototype 업데이트
        for qcls in qobject_derived_classes:
            if qcls in bases:
                class_info["prototype"] = qcls
                break

        # 싱글톤 여부 확인 - 파일의 시작부터 클래스 정의 시작점까지만 검사
        prefix_code = source_code[: class_match.start()]
        is_singleton = "@Singleton" in prefix_code.split("\n")[-5:]

        # isCreatable과 isSingleton 설정 (싱글톤이면 isCreatable은 false)
        class_info["isSingleton"] = is_singleton
        class_info["isCreatable"] = not is_singleton

        # Property, Signal, Slot 찾기
        properties: list[dict[str, Any]] = []
        signals: list[dict[str, Any]] = []
        methods: list[dict[str, Any]] = []

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
            prop["index"] = i

        # 정보 추가
        if properties:
            class_info["Property"] = properties
        if signals:
            class_info["Signal"] = signals
        if methods:
            class_info["Method"] = methods

        return class_info

    except Exception as e:
        print(f"Error parsing class {cls_name} from source: {str(e)}")
        import traceback

        traceback.print_exc()
        return None


def _get_module_path(file_path: str) -> str:
    """파일 경로에서 QML에서 사용할 적절한 모듈 경로를 추출합니다."""
    # 파일이 위치한 디렉토리 이름 사용
    dir_name = os.path.basename(os.path.dirname(os.path.abspath(file_path)))
    return dir_name


def _convert_python_type_to_qml(python_type: Any) -> str:
    """Python 타입을 QML 타입으로 변환합니다."""
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


def find_qobject_classes_from_file(file_path: str) -> list[str]:
    """파일에서 QObject 파생 클래스를 상속받는 클래스 이름 목록을 찾습니다."""
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            content = f.read()

        # QObject 또는 그 파생 클래스 목록
        qobject_derived_classes = [
            "QObject",
            "QQuickPaintedItem",
            "QQuickItem",
            "QQuickFramebufferObject",
            "QWidget",
            "QMainWindow",
            "QDialog",
            "QApplication",
            "QGuiApplication",
            "QAction",
            "QLayout",
            "QGraphicsItem",
            "QAbstractItemModel",
            "QAbstractListModel",
            "QSettings",
        ]

        # 파일에서 import된 PySide6 모듈 분석
        imports = re.findall(r"from\s+PySide6\.\w+\s+import\s+([^#\n]+)", content)
        imported_classes = []
        for import_stmt in imports:
            imported_classes.extend([cls.strip() for cls in import_stmt.split(",")])

        # 파일에 import된 QObject 파생 클래스 찾기
        qobject_classes_in_file = [
            cls for cls in imported_classes if cls in qobject_derived_classes
        ]

        # 상속 패턴에 사용할 클래스 목록 작성
        inheritance_patterns = "|".join(
            qobject_classes_in_file + qobject_derived_classes
        )

        # 모든 클래스 정의 찾기
        class_defs = re.findall(r"class\s+(\w+)\s*\(([^)]+)\):", content)

        # QObject 또는 그 파생 클래스를 상속받는 클래스 필터링
        filtered_classes: list[str] = []
        for cls_name, bases in class_defs:
            # PySide6 기본 클래스 제외
            if cls_name in qobject_derived_classes:
                continue

            # 상속받는 클래스 목록
            base_classes = [base.strip() for base in bases.split(",")]

            # QObject 또는 파생 클래스 상속 확인
            for base in base_classes:
                if any(qcls in base for qcls in qobject_derived_classes):
                    filtered_classes.append(cls_name)
                    break

            # 2차 검사: 정규식으로 상속 관계 확인
            if cls_name not in filtered_classes and inheritance_patterns:
                if re.search(
                    rf"class\s+{cls_name}\s*\([^)]*({inheritance_patterns})[^)]*\):",
                    content,
                ):
                    filtered_classes.append(cls_name)

        return filtered_classes

    except Exception as e:
        print(f"Error finding QObject classes in {file_path}: {str(e)}")
        import traceback

        traceback.print_exc()
        return []


def find_all_python_files(patterns: str | list[str]) -> list[str]:
    """
    주어진 패턴에 매칭되는 모든 Python 파일 목록을 반환합니다.
    파일이 발견되지 않을 경우 기본 디렉토리를 추가로 검색합니다.
    """
    all_files: list[str] = []

    # 패턴으로 파일 검색
    if isinstance(patterns, str):
        pattern_list = [patterns]
    else:
        pattern_list = patterns

    # * 문자가 포함된 패턴을 정확한 파일 경로로 분리
    exact_files: list[str] = []
    pattern_searches: list[str] = []

    for pattern in pattern_list:
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


def generate_qmltypes(
    file_paths: str | list[str], output_file: str = "generated.qmltypes"
) -> bool:
    """
    주어진 Python 파일들에서 QObject 파생 클래스를 파싱하여 .qmltypes 파일을 생성합니다.

    Args:
        file_paths: 파싱할 Python 파일 경로 또는 경로 목록 (glob 패턴 지원)
        output_file: 생성할 qmltypes 파일 경로

    Returns:
        성공 여부
    """
    # 파일 경로 목록 생성 - 개선된 검색 로직 사용
    py_files = find_all_python_files(file_paths)

    if not py_files:
        print(f"Error: No Python files found with pattern(s): {file_paths}")
        return False

    print(f"Found {len(py_files)} Python files to process")

    # 모든 QObject 클래스 정보 수집
    all_class_infos: list[dict[str, Any]] = []
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
                    class_info = parse_qobject_class_from_source(py_file, cls_name)
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
        print(f"Adding class to qmltypes: {class_info['name']}")
        qmltypes_content += "\tComponent {\n"

        # 컴포넌트 기본 정보
        for key, value in class_info.items():
            if key in ["Property", "Signal", "Method"]:
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
        if "Property" in class_info:
            for prop in class_info["Property"]:
                qmltypes_content += "\t\tProperty { "
                prop_parts: list[str] = []
                for k, v in prop.items():
                    if isinstance(v, int):
                        prop_parts.append(f"{k}: {v}")
                    else:
                        prop_parts.append(f'{k}: "{v}"')
                qmltypes_content += "; ".join(prop_parts)
                qmltypes_content += " }\n"

        # 시그널 정보
        if "Signal" in class_info:
            for signal in class_info["Signal"]:
                qmltypes_content += f'\t\tSignal {{ name: "{signal["name"]}" '
                if "parameters" in signal:
                    qmltypes_content += "\n"
                    for param in signal["parameters"]:
                        qmltypes_content += f'\t\t\tParameter {{ name: "{param["name"]}"; type: "{param["type"]}" }}\n'
                    qmltypes_content += "\t\t"
                qmltypes_content += "}\n"

        # 메소드 정보
        if "Method" in class_info:
            for method in class_info["Method"]:
                qmltypes_content += "\t\tMethod { "
                if "type" in method:
                    qmltypes_content += (
                        f'name: "{method["name"]}"; type: "{method["type"]}" '
                    )
                else:
                    qmltypes_content += f'name: "{method["name"]}" '

                if "parameters" in method and method["parameters"]:
                    qmltypes_content += "\n"
                    for param in method["parameters"]:
                        qmltypes_content += f'\t\t\tParameter {{ name: "{param["name"]}"; type: "{param["type"]}" }}\n'
                    qmltypes_content += "\t\t"
                qmltypes_content += "}\n"

        qmltypes_content += "\t}\n"

    qmltypes_content += "}\n"

    # 파일로 저장
    with open(output_file, "w") as f:
        f.write(qmltypes_content)

    print(f"Generated qmltypes file: {output_file}")
    return True
