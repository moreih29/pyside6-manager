# `TranslateHelper.py` 문서

이 파일은 애플리케이션의 다국어 지원(번역) 기능을 관리하는 헬퍼 클래스를 정의합니다.

## `TranslateHelper` 클래스 (싱글톤)

`QObject`를 상속하고 `@Singleton` 데코레이터를 사용하여 애플리케이션 내에서 단일 인스턴스로 관리됩니다.

**주요 기능:**

*   Qt의 번역 시스템(`QTranslator`)을 사용하여 QML 및 Python 코드의 문자열을 번역합니다.
*   현재 설정된 언어와 사용 가능한 언어 목록을 관리하고 QML에 노출합니다.
*   설정 파일(`SettingsHelper` 사용)에서 현재 언어 설정을 읽어옵니다.

**속성:**

*   `current`: 현재 애플리케이션에 적용된 언어 코드 (예: "en_US", "zh_CN"). QML에서 접근 가능하며 변경 시 `currentChanged` 시그널이 발생합니다.
*   `languages`: 애플리케이션에서 지원하는 언어 코드 목록. QML에서 접근 가능하며 변경 시 `languagesChanged` 시그널이 발생합니다.

**시그널:**

*   `currentChanged`: `current` 속성 값이 변경될 때 발생합니다.
*   `languagesChanged`: `languages` 속성 값이 변경될 때 발생합니다.

**메서드:**

*   `__init__(self)`: 생성자. `QObject`를 초기화하고, 지원 언어 목록(`_languages`)을 설정하며, `SettingsHelper`를 통해 저장된 현재 언어 설정을 `_current`에 로드합니다.
*   `init(self, engine: QQmlEngine)`:
    *   QML 엔진(`engine`)을 저장합니다.
    *   `QTranslator` 객체(`_translator`)를 생성하고 애플리케이션에 설치합니다 (`QGuiApplication.installTranslator`).
    *   현재 설정된 언어(`_current`)에 해당하는 `.qm` 번역 파일을 리소스 경로(`:/example/i18n/`)에서 로드합니다.
    *   번역 파일 로딩에 성공하면 QML 엔진의 `retranslate()`를 호출하여 UI 문자열을 즉시 업데이트합니다.

**사용:**

1.  `main.py` 등 애플리케이션 시작 지점에서 `TranslateHelper` 인스턴스를 생성하고 `init()` 메서드를 호출하여 QML 엔진과 연결합니다.
2.  QML에서는 `TranslateHelper`의 `current` 속성을 변경하여 언어를 전환할 수 있습니다. 언어 변경 시 `init()` 또는 유사한 로직을 다시 호출하여 새 번역 파일을 로드하고 `retranslate()`를 실행해야 합니다 (현재 코드에는 언어 변경 후 자동 리로드 로직은 명시적으로 보이지 않으나, `current` 속성의 setter에서 관련 로직을 추가할 수 있습니다).
3.  QML에서는 `qsTr("Text to translate")` 와 같은 함수를 사용하여 번역될 문자열을 지정합니다.

**참고:**

*   실제 번역 파일(`.qm`)은 Qt Linguist 도구를 사용하여 `.ts` 파일로부터 생성됩니다.
*   `.ts` 파일은 소스 코드에서 번역 대상 문자열을 추출하여 생성됩니다. 