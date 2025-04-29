# FileDialog

**모듈:** `import QtQuick.Dialogs`

## 개요

`FileDialog`는 사용자가 로컬 파일 시스템에서 파일을 선택하거나(열기), 파일 이름을 지정하여 저장할 위치를 선택하는 데 사용되는 표준 대화상자입니다. 이 대화상자는 일반적으로 시스템의 네이티브 파일 선택기 UI를 사용합니다.

파일 열기, 파일 저장, 여러 파일 선택, 폴더 선택 등의 기능을 제공합니다.

## 기반 클래스

*   `Dialog` (`QtQuick.Dialogs` 내부 구현)

## 주요 프로퍼티

| 이름              | 타입            | 기본값        | 설명                                                                                                                                                             |
| :---------------- | :-------------- | :------------ | :--------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `title`           | `string`        | ""          | 대화상자의 제목 표시줄 텍스트. 기본값은 작업 종류(열기/저장)에 따라 자동으로 설정될 수 있습니다.                                                                            |
| `file`            | `url`           | `""`        | 사용자가 선택한 단일 파일의 로컬 경로 (URL 형식). 파일 저장 시에는 사용자가 입력한 파일 경로. (`selectExisting`이 `true`일 때 유효).                                            |
| `files`           | `list<url>`     | `[]`          | (읽기 전용) 사용자가 선택한 여러 파일의 로컬 경로 목록 (URL 형식). (`selectMultiple`이 `true`일 때 유효).                                                               |
| `folder`          | `url`           | (현재 디렉토리) | 대화상자가 처음 열릴 때 표시될 디렉토리 경로 또는 사용자가 선택한 폴더 경로 (`selectFolder`가 `true`일 때).                                                               |
| `selectExisting`  | `bool`          | `true`        | `true`이면 파일 열기 대화상자 모드, `false`이면 파일 저장 대화상자 모드.                                                                                              |
| `selectMultiple`| `bool`          | `false`       | 사용자가 여러 파일을 동시에 선택할 수 있는지 여부 (`selectExisting`이 `true`일 때 유효).                                                                                   |
| `selectFolder`    | `bool`          | `false`       | 파일 대신 폴더를 선택하는 모드.                                                                                                                                  |
| `nameFilters`     | `list<string>`  | `[]`          | 파일 형식 필터 목록. 각 문자열은 "설명 (*.확장자)" 형식입니다 (예: `["Image files (*.png *.jpg)", "Text files (*.txt)"]`).                                         |
| `selectedNameFilter`| `string`     | (첫 번째 필터)| 사용자가 현재 선택한 이름 필터.                                                                                                                                 |
| `sidebarVisible`  | `bool`          | `false`       | (macOS, Linux) 파일 대화상자의 사이드바(즐겨찾기 등) 표시 여부.                                                                                                     |
| `options`         | `enum flags`    | `0`           | 추가 옵션 플래그 (`FileDialog.DontUseNativeDialog`, `FileDialog.HideNameFilterDetails`, `FileDialog.ReadOnly` 등). `DontUseNativeDialog`는 Qt 기본 대화상자를 사용하게 합니다. |
| `visible`         | `bool`          | `false`       | 대화상자를 표시할지 여부. `open()` 및 `close()` 메서드로 제어됩니다.                                                                                                   |
| `modality`        | `Qt.WindowModality` | `Qt.WindowModal`| 대화상자의 모달(modal) 동작 방식.                                                                                                                                 |

## 주요 시그널

| 이름         | 파라미터 | 설명                                                              |
| :----------- | :------- | :---------------------------------------------------------------- |
| `accepted()` | -        | 사용자가 '열기', '저장' 또는 'Accept' 역할의 버튼을 클릭했을 때 발생합니다. |
| `rejected()` | -        | 사용자가 '취소' 또는 'Reject' 역할의 버튼을 클릭했을 때 발생합니다.  |
| `fileChanged`| `url`    | `file` 프로퍼티가 변경될 때 발생합니다.                             |
| `filesChanged`| `list<url>` | `files` 프로퍼티가 변경될 때 발생합니다.                            |
| `folderChanged`| `url`   | `folder` 프로퍼티가 변경될 때 발생합니다.                           |
| `currentFolderChanged`| `url`| 사용자가 대화상자 내에서 디렉토리를 이동할 때 발생합니다.             |
| `filterChanged`| `string`| `selectedNameFilter` 프로퍼티가 변경될 때 발생합니다.                |
| `visibleChanged`| `bool`  | `visible` 프로퍼티가 변경될 때 발생합니다.                         |

## 주요 메소드

| 이름      | 파라미터 | 반환타입 | 설명                                            |
| :-------- | :------- | :------- | :---------------------------------------------- |
| `open()`  | -        | -        | 대화상자를 엽니다 (`visible = true`).           |
| `close()` | -        | -        | 대화상자를 닫습니다 (`visible = false`).        |

## 예제

```qml
import QtQuick
import QtQuick.Controls
import QtQuick.Layouts
import QtQuick.Dialogs

Window {
    width: 400; height: 300
    visible: true
    title: "FileDialog Example"

    // 파일 열기 대화상자
    FileDialog {
        id: openDialog
        title: "Open Image File"
        selectExisting: true // 파일 열기 모드
        selectMultiple: false // 단일 파일 선택
        nameFilters: [ "Image files (*.png *.jpg *.jpeg)", "All files (*)" ]
        folder: StandardPaths.standardLocations(StandardPaths.PicturesLocation)[0] // 초기 폴더: 사진

        onAccepted: {
            console.log("File selected:", openDialog.file)
            // QML에서 로컬 파일 URL 사용 시 'file:///' 접두사 필요 여부 확인
            // 예: imagePreview.source = openDialog.file
            resultLabel.text = "Opened: " + openDialog.file
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
        selectExisting: false // 파일 저장 모드
        selectMultiple: false
        nameFilters: [ "Text files (*.txt)", "All files (*)" ]
        // file: "untitled.txt" // 제안할 기본 파일 이름 (경로 포함 가능)
        folder: StandardPaths.standardLocations(StandardPaths.DocumentsLocation)[0] // 초기 폴더: 문서

        onAccepted: {
            console.log("Save as:", saveDialog.file)
            resultLabel.text = "Saved to: " + saveDialog.file
            // 실제 파일 저장 로직 구현 필요 (예: C++ 연동)
        }
        onRejected: {
            console.log("Save cancelled.")
            resultLabel.text = "Save cancelled."
        }
    }

    // 폴더 선택 대화상자
    FileDialog {
        id: folderDialog
        title: "Select Folder"
        selectFolder: true // 폴더 선택 모드
        folder: StandardPaths.standardLocations(StandardPaths.HomeLocation)[0] // 초기 폴더: 홈

        onAccepted: {
            console.log("Folder selected:", folderDialog.folder)
            resultLabel.text = "Selected folder: " + folderDialog.folder
        }
        onRejected: {
            console.log("Folder selection cancelled.")
            resultLabel.text = "Folder selection cancelled."
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
            onClicked: saveDialog.open()
        }
        Button {
            text: "Select Folder..."
            Layout.alignment: Qt.AlignHCenter
            onClicked: folderDialog.open()
        }
    }
}
```

## 참고 사항

*   `FileDialog`는 `QtQuick.Dialogs` 모듈을 임포트해야 사용할 수 있습니다.
*   `open()` 메소드를 호출하여 대화상자를 표시합니다.
*   `selectExisting`, `selectMultiple`, `selectFolder` 프로퍼티를 조합하여 원하는 대화상자 모드(파일 열기, 파일 저장, 다중 파일 선택, 폴더 선택)를 설정합니다.
*   `accepted()` 시그널 핸들러 내에서 `file` (단일 파일/저장 경로), `files` (다중 파일), `folder` (폴더 선택) 프로퍼티를 통해 사용자의 선택 결과를 얻을 수 있습니다. 반환되는 경로는 로컬 파일 시스템 경로를 나타내는 URL 형식 (예: `file:///path/to/file`) 입니다.
*   `nameFilters` 프로퍼티를 사용하여 특정 파일 형식만 표시하도록 필터링할 수 있습니다.
*   `folder` 프로퍼티를 사용하여 대화상자가 처음 열릴 때 보여줄 디렉토리를 지정할 수 있습니다. `StandardPaths.standardLocations()` (`QtQml` 모듈)를 사용하면 문서, 사진, 홈 등 표준 시스템 폴더 경로를 얻는 데 유용합니다.
*   기본적으로 네이티브 파일 대화상자를 사용하지만, `options: FileDialog.DontUseNativeDialog`를 설정하면 플랫폼에 관계없이 Qt에서 제공하는 기본 대화상자를 사용합니다.
*   실제 파일 읽기/쓰기 작업은 `FileDialog`가 처리하지 않으므로, `accepted()` 시그널 이후에 선택된 파일 경로를 사용하여 별도의 로직(예: C++ 함수 호출, JavaScript 파일 I/O API - 제한적)을 구현해야 합니다. 