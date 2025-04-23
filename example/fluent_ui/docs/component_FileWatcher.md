# `FileWatcher.py` 문서

이 파일은 지정된 파일 또는 디렉토리의 변경 사항을 감지하는 QML 컴포넌트를 정의합니다.

## `FileWatcher` 클래스

`QObject`를 상속받아 QML에서 사용 가능한 컴포넌트를 제공합니다.

**주요 기능:**

*   `QFileSystemWatcher`를 사용하여 지정된 경로(`path` 속성)의 파일 또는 디렉토리 변경을 감시합니다.
*   `path` 속성: 감시할 파일 또는 디렉토리의 경로를 설정합니다. QML에서 바인딩 가능합니다.
*   `fileChanged` 시그널: 감시 대상의 내용이 변경되었을 때 발생합니다.
*   `pathChanged` 시그널: `path` 속성이 변경되었을 때 발생하며, 감시 대상을 업데이트합니다.

**메서드:**

*   `__init__(self)`: 클래스 생성자. `QFileSystemWatcher`를 초기화하고 시그널-슬롯 연결을 설정합니다.
*   `clean(self)`: 현재 감시 중인 모든 경로를 `QFileSystemWatcher`에서 제거합니다. `path`가 변경되거나 파일이 변경된 후 다시 감시를 시작하기 전에 호출됩니다.

**사용 예 (QML):**

```qml
import example 1.0

FileWatcher {
    id: fileWatcher
    path: "file:///path/to/your/file.txt" // 감시할 파일 경로
    onFileChanged: {
        console.log("File content changed!")
        // 파일 변경 시 수행할 작업
    }
}
``` 