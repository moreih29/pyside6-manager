# ApplicationWindow

**모듈:** `import QtQuick.Controls`

## 개요

`ApplicationWindow`는 일반적인 데스크톱 애플리케이션의 메인 창을 쉽게 구성할 수 있도록 `Window` (`QtQuick.Window`)를 확장한 컨트롤입니다. 기본적인 창 기능(`title`, `width`, `height`, `visible` 등) 외에도 메뉴 바(`menuBar`), 툴 바(`toolBar`), 스테이터스 바(`statusBar`)를 편리하게 추가하고 관리하는 기능을 제공합니다.

복잡한 애플리케이션의 기본 틀을 잡는 데 유용하며, `QtQuick.Controls`의 스타일 시스템과 통합되어 일관된 모양과 느낌을 제공합니다.

## 기반 클래스

*   `Window` (`QtQuick.Window`)

## 주요 프로퍼티

`Window`의 모든 프로퍼티 (`visible`, `width`, `height`, `title`, `x`, `y`, `color`, `opacity`, `flags`, `active` 등)를 상속받습니다.

`ApplicationWindow`에 추가된 주요 프로퍼티는 다음과 같습니다.

| 이름          | 타입    | 기본값 | 설명                                                                                                                               |
| :------------ | :------ | :----- | :--------------------------------------------------------------------------------------------------------------------------------- |
| `menuBar`     | `MenuBar` | `null` | 창 상단에 표시될 메뉴 바 컴포넌트. `MenuBar` 객체를 할당하여 메뉴를 구성합니다.                                                          |
| `toolBar`     | `ToolBar` | `null` | 창 상단 (메뉴 바 아래) 또는 다른 위치에 표시될 수 있는 툴 바 컴포넌트. `ToolBar` 객체를 할당하여 툴 버튼 등을 추가합니다.                               |
| `statusBar`   | `StatusBar`| `null` | 창 하단에 상태 메시지 등을 표시하기 위한 스테이터스 바 컴포넌트. `StatusBar` 객체를 할당합니다.                                                  |
| `header`      | `Item`  | `null` | 메뉴 바와 툴 바를 포함하는 창 상단 영역 아이템. 사용자 정의 헤더를 구현할 때 사용될 수 있습니다.                                                 |
| `footer`      | `Item`  | `null` | 스테이터스 바를 포함하는 창 하단 영역 아이템. 사용자 정의 푸터를 구현할 때 사용될 수 있습니다.                                                   |
| `contentItem` | `Item`  | (읽기 전용) | `Window`에서 상속. 헤더, 푸터, 메뉴 바, 툴 바, 스테이터스 바를 제외한 창의 주 내용 영역을 나타내는 루트 아이템. 여기에 애플리케이션의 주 UI를 배치합니다. |

## 주요 시그널

`Window`의 모든 시그널 (`closing`, `visibleChanged`, `widthChanged`, `heightChanged` 등)을 상속받습니다.

## 주요 메소드

`Window`의 모든 메소드 (`show`, `hide`, `close`, `requestActivate` 등)를 상속받습니다.

## 예제

```qml
import QtQuick
import QtQuick.Controls
import QtQuick.Layouts

ApplicationWindow {
    id: appWindow
    width: 640
    height: 480
    visible: true
    title: "ApplicationWindow Example"

    // 메뉴 바 정의
    menuBar: MenuBar {
        Menu {
            title: qsTr("&File") // 앰퍼샌드(&)는 니모닉(단축키 Alt+F) 지정
            Action {
                text: qsTr("&New")
                shortcut: "Ctrl+N"
                onTriggered: console.log("New action triggered")
            }
            Action {
                text: qsTr("&Open...")
                shortcut: "Ctrl+O"
                onTriggered: console.log("Open action triggered")
            }
            MenuSeparator { }
            Action {
                text: qsTr("E&xit")
                onTriggered: Qt.quit()
            }
        }
        Menu {
            title: qsTr("&Help")
            Action { text: qsTr("About..."); onTriggered: aboutDialog.open() }
        }
    }

    // 툴 바 정의
    toolBar: ToolBar {
        RowLayout {
            anchors.fill: parent
            ToolButton {
                text: qsTr("New")
                icon.name: "document-new" // 테마 아이콘 이름 사용 (시스템에 따라 다름)
                onClicked: console.log("New toolbar button clicked")
            }
            ToolButton {
                text: qsTr("Open")
                icon.source: "qrc:/images/open.png" // 직접 이미지 파일 지정
                onClicked: console.log("Open toolbar button clicked")
            }
        }
    }

    // 스테이터스 바 정의
    statusBar: StatusBar {
        RowLayout {
            anchors.fill: parent
            Label {
                id: statusLabel
                text: "Ready"
                Layout.fillWidth: true
            }
        }
    }

    // 메인 내용 영역 (contentItem에 해당)
    TextArea {
        id: mainTextArea
        anchors.fill: parent
        placeholderText: "Enter text here..."
        onTextChanged: statusLabel.text = "Editing..." // 상태바 메시지 변경
    }

    // About 대화상자 (예시)
    Dialog {
        id: aboutDialog
        title: "About"
        standardButtons: Dialog.Ok
        modal: true
        Label {
            text: "Simple ApplicationWindow Example\nUsing QtQuick.Controls"
            padding: 20
        }
    }
}
```

## 참고 사항

*   `ApplicationWindow`는 `QtQuick.Controls` 모듈에 속하므로 해당 모듈을 임포트해야 합니다.
*   `menuBar`, `toolBar`, `statusBar` 프로퍼티에 각각 `MenuBar`, `ToolBar`, `StatusBar` 타입의 객체를 할당하여 해당 UI 요소를 구성합니다.
*   메뉴 항목은 주로 `Action` 요소를 사용하여 정의하며, `Action`은 텍스트, 아이콘, 단축키, 활성화 상태 등을 포함하고 `triggered` 시그널을 통해 동작을 실행합니다.
*   툴 바에는 `ToolButton` 등을 배치하여 자주 사용하는 기능을 빠르게 실행할 수 있도록 합니다.
*   창의 주 내용은 `ApplicationWindow`의 루트 아이템으로 직접 배치하면 자동으로 `contentItem`의 자식으로 처리됩니다.
*   `header`와 `footer` 프로퍼티를 사용하면 메뉴 바, 툴 바, 스테이터스 바 영역을 포함하는 더 복잡한 사용자 정의 헤더/푸터를 만들 수 있습니다.
*   Fluent UI와 같은 외부 UI 라이브러리를 사용하는 경우, 해당 라이브러리에서 제공하는 자체적인 창 컴포넌트(예: `FluentWindow`)를 사용하는 것이 스타일 일관성 측면에서 더 권장될 수 있습니다. 