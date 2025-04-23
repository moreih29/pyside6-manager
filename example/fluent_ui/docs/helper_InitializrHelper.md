# `InitializrHelper.py` 문서

이 파일은 새로운 PySide6 FluentUI 프로젝트의 기본 구조와 파일들을 생성하는 기능을 제공하는 헬퍼 클래스 및 함수들을 정의합니다. Spring Initializr와 유사한 역할을 수행하는 것으로 보입니다.

## 전역 함수

*   **`copyFile(src: str, dest: str)`**: 파일을 복사하고 대상 파일에 쓰기 권한을 설정합니다. 대상 디렉토리가 없으면 생성합니다.
*   **`templateToFile(src: str, dest: str, mapping)`**: 템플릿 파일(`src`)을 읽어 `mapping` 딕셔너리에 있는 값으로 플레이스홀더(`{key}`)를 치환한 후, 대상 파일(`dest`)에 저장합니다. `CustomFormatter` 클래스를 사용하여 정의되지 않은 키는 그대로 `{key}` 형태로 남깁니다. 대상 디렉토리가 없으면 생성합니다.
*   **`extractSourceFile(out: str, password=None)`**: 프로젝트 루트 근처에 있는 `source.zip` 압축 파일의 내용을 지정된 `out` 경로에 압축 해제합니다. 비밀번호가 필요한 경우 `password` 인자를 사용합니다 (코드에는 "zhuzichu988" 하드코딩되어 있음).

## `CustomFormatter` 클래스

*   `string.Formatter`를 상속받아 사용자 정의 포매팅 로직을 구현합니다.
*   주어진 `mapping`에 키가 존재하면 해당 값으로 치환하고, 없으면 `{key}` 문자열 그대로 반환합니다.

## `InitializrHelper` 클래스 (싱글톤)

`QObject`를 상속하고 `@Singleton` 데코레이터를 사용하여 애플리케이션 내에서 단일 인스턴스로 관리됩니다.

**주요 기능:**

*   새로운 PySide6 FluentUI 프로젝트 생성을 위한 핵심 로직을 제공합니다.
*   QML에서 호출 가능한 `generate` 슬롯을 통해 프로젝트 이름과 생성 경로를 받아 프로젝트를 초기화합니다.

**시그널:**

*   `error(str)`: 프로젝트 생성 중 오류가 발생했을 때 오류 메시지와 함께 발생합니다.
*   `success(str)`: 프로젝트 생성이 성공적으로 완료되었을 때, 생성된 프로젝트의 시작 스크립트 경로와 함께 발생합니다.

**메서드:**

*   `copyDir(self, fromDir: QDir, toDir: QDir, coverIfFileExists: bool) -> bool`: 디렉토리의 내용을 재귀적으로 복사합니다. (현재 `generate` 메서드 내에서 직접 사용되지는 않는 것으로 보입니다.)
*   `generate(self, name: str, path: str)`: **핵심 프로젝트 생성 메서드.**
    1.  입력값 검증 (프로젝트 이름, 경로 유효성 및 존재 여부, 대상 경로에 같은 이름의 폴더 존재 여부).
    2.  지정된 경로에 프로젝트 이름으로 새 디렉토리 생성 (`projectDir.mkpath`).
    3.  `extractSourceFile` 함수를 호출하여 `source.zip` 파일의 내용을 새 프로젝트 디렉토리에 압축 해제.
    4.  `templateToFile` 및 `copyFile` 함수를 반복적으로 호출하여 프로젝트의 기본 구조와 파일들을 생성:
        *   환경 설정 파일 (`env.py`)
        *   아이콘 파일 (`favicon.*`)
        *   PyInstaller 설정 파일 (`main.spec`)
        *   빌드 및 실행 관련 스크립트 (`script-*.py`)
        *   주요 애플리케이션 코드 (`{name}/main.py`)
        *   번역 파일 (`{name}/{name}_*.ts`)
        *   리소스 파일 (`{name}/imports/resource.qrc`)
        *   QML 파일 (`{name}/imports/{name}/qml/App.qml`, `main.qml`)
        *   기본 로고 이미지
    5.  성공 시 `success` 시그널을 발생시켜 생성된 프로젝트의 시작 스크립트 경로를 전달합니다.
    6.  실패 시 `error` 시그널을 발생시켜 오류 메시지를 전달합니다.

**사용:**

*   QML 인터페이스 등에서 사용자로부터 프로젝트 이름과 경로를 입력받아 `InitializrHelper.generate(name, path)` 슬롯을 호출하여 새 프로젝트를 생성할 수 있습니다.

**참고:**

*   `source.zip` 파일에는 프로젝트의 기본 템플릿 파일들이 포함되어 있을 것으로 예상됩니다.
*   비밀번호가 하드코딩되어 있는 점은 보안상 유의해야 합니다. 