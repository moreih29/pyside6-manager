# `SettingsHelper.py` 문서

이 파일은 애플리케이션 설정을 저장하고 불러오는 기능을 제공하는 헬퍼 클래스를 정의합니다.

## `SettingsHelper` 클래스 (싱글톤)

`QObject`를 상속하고 `@Singleton` 데코레이터를 사용하여 애플리케이션 내에서 단일 인스턴스로 관리됩니다.

**주요 기능:**

*   `QSettings`를 사용하여 `.ini` 파일 형식으로 애플리케이션 설정을 저장하고 로드합니다.
*   설정 파일은 사용자의 로컬 애플리케이션 데이터 위치 (`QStandardPaths.StandardLocation.AppLocalDataLocation`) 아래 `example.ini` 이름으로 저장됩니다.
*   다크 모드, 시스템 앱 바 사용 여부, 언어 설정 등 특정 설정 값에 대한 접근 및 저장을 위한 슬롯(Slot) 메서드를 제공합니다.

**메서드:**

*   `__init__(self)`: 생성자. `QSettings` 객체를 초기화하고 저장될 `.ini` 파일 경로를 설정합니다.
*   `_save(self, key, val)`: 내부 헬퍼 메서드. 주어진 키(key)와 값(val)을 설정 파일에 저장합니다.
*   `_get(self, key, default)`: 내부 헬퍼 메서드. 주어진 키(key)에 해당하는 값을 설정 파일에서 읽어옵니다. 값이 없으면 기본값(default)을 반환합니다.

**슬롯 (QML에서 호출 가능):**

*   `getDarkMode(self) -> int`: 저장된 다크 모드 설정을 정수(int)로 반환합니다 (예: 0 - 자동, 1 - 라이트, 2 - 다크). 기본값은 0입니다.
*   `saveDarkMode(self, darkMode: int)`: 주어진 다크 모드 설정 값을 저장합니다.
*   `getUseSystemAppBar(self) -> bool`: 시스템 기본 앱 바 사용 여부 설정을 불리언(bool) 값으로 반환합니다. 기본값은 `False`입니다.
*   `saveUseSystemAppBar(self, useSystemAppBar: bool)`: 주어진 시스템 앱 바 사용 여부 값을 저장합니다.
*   `getLanguage(self) -> str`: 저장된 언어 설정 코드를 문자열(str)로 반환합니다 (예: "en_US"). 기본값은 "en_US"입니다.
*   `saveLanguage(self, language: str)`: 주어진 언어 설정 코드를 저장합니다.

**사용:**

*   다른 Python 모듈이나 QML에서 `SettingsHelper` 인스턴스를 통해 슬롯 메서드를 호출하여 설정을 읽거나 저장할 수 있습니다.
*   예를 들어, QML에서 언어 변경 버튼을 누르면 `SettingsHelper.saveLanguage("zh_CN")`를 호출하여 설정을 변경하고, `TranslateHelper` 등을 통해 실제 언어 적용을 트리거할 수 있습니다.

**참고:**

*   `QSettings`는 플랫폼에 따라 레지스트리(Windows)나 `plist`(macOS) 등 다른 저장 방식을 사용할 수도 있지만, 여기서는 명시적으로 `.ini` 형식을 지정했습니다. 