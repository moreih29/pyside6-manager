# FileDialog

## 모듈 정보

```qml
import QtQuick.Dialogs
```

## 개요

`FileDialog`는 사용자가 로컬 파일 시스템에서 파일을 선택하거나(열기), 파일 이름을 지정하여 저장할 위치를 선택하는 데 사용되는 표준 대화상자입니다. 이 대화상자는 일반적으로 시스템의 네이티브 파일 선택기 UI를 사용합니다. Qt 6.2부터 `QtQuick.Dialogs` 모듈에 포함되었습니다.

파일 열기(`OpenFile`), 여러 파일 열기(`OpenFiles`), 파일 저장(`SaveFile`) 모드를 지원합니다. 폴더 선택 기능은 Qt 6.2부터 별도의 `FolderDialog`로 분리되었습니다.

## 기반 클래스

*   `Dialog` (`QtQuick.Dialogs`)

## 주요 프로퍼티

`Dialog`의 프로퍼티 (`title`, `visible`, `modality`, `flags` 등)를 상속받습니다.

| 이름                 | 타입            | 기본값                 | 설명                                                                                                                                                              |
| :------------------- | :-------------- | :--------------------- | :---------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `fileMode`           | `enumeration`   | `FileDialog.OpenFile`  | 대화상자 모드를 설정합니다 (`OpenFile`: 단일 파일 열기, `OpenFiles`: 다중 파일 열기, `SaveFile`: 파일 저장).                                                           |
| `selectedFile`       | `url`           | `""`                 | 사용자가 선택한 마지막 파일의 로컬 경로 (URL 형식). 대화상자 열 때 초기 선택 파일 설정에도 사용 가능. `SaveFile` 모드에서는 저장할 파일 경로.                                    |
| `selectedFiles`      | `list<url>`     | `[]`                   | (읽기 전용) `fileMode`가 `OpenFiles`일 때 사용자가 선택한 여러 파일의 로컬 경로 목록 (URL 형식).                                                                    |
| `currentFolder`      | `url`           | (플랫폼 의존적)        | 대화상자가 처음 열릴 때 표시될 디렉토리 경로 (URL 형식).                                                                                                             |
| `nameFilters`        | `list<string>`  | `[]`                   | 파일 형식 필터 목록. "설명 (*.확장자)" 형식 (예: `["Image files (*.png *.jpg)", "All files (*)"]`). `*.*` 대신 `*` 사용 권장.                                |
| `selectedNameFilter` | `group`         | (읽기 전용, index 제외) | 현재 선택된 이름 필터 정보 그룹 (`index`: 설정 가능, `name`, `extensions`, `globs`: 읽기 전용).                                                                     |
| `defaultSuffix`      | `string`        | `""`                 | `SaveFile` 모드에서 확장자 없이 파일 이름을 입력했을 때 자동으로 추가될 기본 확장자 (예: `"txt"`).                                                                         |
| `options`            | `enum flags`    | `0`                    | 추가 옵션 플래그 (`DontResolveSymlinks`, `DontConfirmOverwrite`, `ReadOnly`, `HideNameFilterDetails`, `DontUseNativeDialog`). `|` 연산자로 조합.             |
| `acceptLabel`        | `string`        | `""`                 | '열기'/'저장' 버튼에 표시될 텍스트. 비워두면 시스템 기본값 사용.                                                                                                     |
| `rejectLabel`        | `string`        | `""`                 | '취소' 버튼에 표시될 텍스트. 비워두면 시스템 기본값 사용.                                                                                                         |

## 주요 시그널

`Dialog`의 시그널 (`accepted()`, `rejected()`, `visibleChanged` 등)을 상속받습니다.

| 이름                      | 파라미터    | 설명                                                            |
| :------------------------ | :---------- | :-------------------------------------------------------------- |
| `accepted()`              | -           | 사용자가 '열기', '저장' 또는 'Accept' 역할의 버튼을 클릭했을 때 발생합니다. | 
| `rejected()`              | -           | 사용자가 '취소' 또는 'Reject' 역할의 버튼을 클릭했을 때 발생합니다.  |
| `selectedFileChanged`     | `url`       | `selectedFile` 프로퍼티가 변경될 때 발생합니다.                   |
| `selectedFilesChanged`    | `list<url>` | `selectedFiles` 프로퍼티가 변경될 때 발생합니다.                  |
| `currentFolderChanged`    | `url`       | `currentFolder` 프로퍼티가 변경될 때 발생합니다.                  |
| `selectedNameFilterChanged`| `Filter`    | `selectedNameFilter` 그룹의 프로퍼티가 변경될 때 발생합니다.        |

## 주요 메소드

`Dialog`의 메소드 (`open()`, `close()`)를 상속받습니다.

| 이름      | 파라미터 | 반환타입 | 설명                                            |
| :-------- | :------- | :------- | :---------------------------------------------- |
| `open()`  | -        | -        | 대화상자를 엽니다 (`visible = true`).           |
| `close()` | -        | -        | 대화상자를 닫습니다 (`visible = false`).        |

## 예제 (파일 열기 및 저장)

```qml
import QtCore
import QtQuick
import QtQuick.Controls // Button, Label 사용
import QtQuick.Layouts // ColumnLayout 사용
import QtQuick.Dialogs // FileDialog, StandardPaths 사용

Window {
    width: 400; height: 300
    visible: true
    title: "FileDialog Example (Qt 6.2+)"

    // 파일 열기 대화상자
    FileDialog {
        id: openDialog
        title: "Open Image File"
        fileMode: FileDialog.OpenFile // 파일 열기 모드
        nameFilters: [ "Image files (*.png *.jpg *.jpeg)", "All files (*)" ]
        currentFolder: StandardPaths.writableLocation(StandardPaths.PicturesLocation) // 초기 폴더: 사진

        onAccepted: {
            // selectedFile 프로퍼티로 선택된 파일 경로(URL) 얻기
            console.log("File selected (URL):", openDialog.selectedFile)
            resultLabel.text = "Opened: " + openDialog.selectedFile.toString()
            // image.source = openDialog.selectedFile // 예: 이미지 로딩
        }
        onRejected: {
            console.log("File selection cancelled.")
            resultLabel.text = "Open cancelled."
        }
    }

    // 파일 저장 대화상자
    FileDialog {
        id: saveDialog
        title: "Save Text File"
        fileMode: FileDialog.SaveFile // 파일 저장 모드
        nameFilters: [ "Text files (*.txt)", "All files (*)" ]
        defaultSuffix: "txt" // 기본 확장자
        currentFolder: StandardPaths.writableLocation(StandardPaths.DocumentsLocation) // 초기 폴더: 문서
        // selectedFile 프로퍼티로 제안할 파일 이름 설정 가능
        // selectedFile: "untitled.txt"

        onAccepted: {
            // selectedFile 프로퍼티로 사용자가 지정한 저장 경로(URL) 얻기
            console.log("Save as (URL):", saveDialog.selectedFile)
            resultLabel.text = "Save to: " + saveDialog.selectedFile.toString()
            // 실제 파일 저장 로직은 별도 구현 필요
        }
        onRejected: {
            console.log("Save cancelled.")
            resultLabel.text = "Save cancelled."
        }
    }

    // 메인 창 내용
    ColumnLayout {
        anchors.centerIn: parent
        spacing: 15

        Label {
            id: resultLabel
            text: "Dialog result will be shown here."
            Layout.alignment: Qt.AlignHCenter
            wrapMode: Text.WordWrap
            width: parent.width - 20
        }

        Button {
            text: "Open File..."
            Layout.alignment: Qt.AlignHCenter
            onClicked: openDialog.open()
        }
        Button {
            text: "Save File As..."
            Layout.alignment: Qt.AlignHCenter
            onClicked: {
                // 저장 대화상자 열기 전에 제안 파일명 설정 (선택적)
                saveDialog.selectedFile = Qt.resolvedUrl("untitled.txt") // URL로 설정
                saveDialog.open()
            }
        }
        // 폴더 선택 버튼은 FolderDialog 예제에서 다룸
    }
}
```

## 참고 사항

*   `FileDialog`는 `QtQuick.Dialogs` 모듈을 임포트해야 사용할 수 있습니다 (Qt 6.2 이상).
*   `open()` 메소드를 호출하여 대화상자를 표시합니다.
*   `fileMode` 프로퍼티를 사용하여 대화상자 모드(`OpenFile`, `OpenFiles`, `SaveFile`)를 설정합니다. **폴더 선택은 별도의 `FolderDialog`를 사용해야 합니다.**
*   `accepted()` 시그널 핸들러 내에서 `selectedFile` (단일 파일/저장 경로) 또는 `selectedFiles` (`OpenFiles` 모드) 프로퍼티를 통해 사용자의 선택 결과를 얻을 수 있습니다. 반환되는 경로는 로컬 파일 시스템 경로를 나타내는 URL 형식 (예: `file:///path/to/file`) 입니다.
*   `nameFilters` 프로퍼티를 사용하여 특정 파일 형식만 표시하도록 필터링할 수 있습니다.
*   `currentFolder` 프로퍼티를 사용하여 대화상자가 처음 열릴 때 보여줄 디렉토리를 지정할 수 있습니다. `StandardPaths.writableLocation()` (또는 `standardLocations()`)을 사용하면 문서, 사진, 홈 등 표준 시스템 폴더 경로를 얻는 데 유용합니다 (`StandardPaths`는 `QtQuick.Dialogs` 또는 `QtQml` 모듈을 통해 접근 가능).
*   기본적으로 네이티브 파일 대화상자를 사용하지만, `options: FileDialog.DontUseNativeDialog`를 설정하면 플랫폼에 관계없이 Qt에서 제공하는 기본 대화상자를 사용합니다.
*   실제 파일 읽기/쓰기 작업은 `FileDialog`가 처리하지 않으므로, `accepted()` 시그널 이후에 선택된 파일 경로를 사용하여 별도의 로직(예: C++ 함수 호출, JavaScript 파일 I/O API - 제한적)을 구현해야 합니다.

## 공식 문서 링크

* [FileDialog QML Type | Qt Quick Dialogs 6.9](https://doc.qt.io/qt-6/qml-qtquick-dialogs-filedialog.html)
* [FolderDialog QML Type | Qt Quick Dialogs 6.9](https://doc.qt.io/qt-6/qml-qtquick-dialogs-folderdialog.html) (폴더 선택용)
* [StandardPaths QML Type | Qt QML 6.9](https://doc.qt.io/qt-6/qml-qtqml-qtcore-standardpaths.html) (표준 경로 접근용) 