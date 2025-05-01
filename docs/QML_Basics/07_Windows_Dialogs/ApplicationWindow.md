# ApplicationWindow

**모듈:** `import QtQuick.Controls`

## 개요

`ApplicationWindow`는 일반적인 데스크톱 애플리케이션의 메인 창을 쉽게 구성할 수 있도록 `Window` (`QtQuick.Window`)를 확장한 컨트롤입니다. 기본적인 창 기능(`title`, `width`, `height`, `visible` 등) 외에도 메뉴 바(`menuBar`), 헤더(`header`), 푸터(`footer`)를 편리하게 추가하고 관리하는 기능을 제공합니다. 예를 들어, `header`에 `ToolBar`를, `footer`에 상태 메시지를 표시하는 `ToolBar`나 다른 아이템을 배치할 수 있습니다.

복잡한 애플리케이션의 기본 틀을 잡는 데 유용하며, `QtQuick.Controls`의 스타일 시스템과 통합되어 일관된 모양과 느낌을 제공합니다.

## 기반 클래스

*   `Window` (`QtQuick.Window`)

## 주요 프로퍼티

`Window`의 모든 프로퍼티 (`visible`, `width`, `height`, `title`, `x`, `y`, `color`, `opacity`, `flags`, `active` 등)를 상속받습니다.

`ApplicationWindow`에 추가된 주요 프로퍼티는 다음과 같습니다.

| 이름          | 타입        | 기본값 | 설명                                                                                                                               |
| :------------ | :---------- | :----- | :--------------------------------------------------------------------------------------------------------------------------------- |
| `menuBar`     | `Item`      | `null` | 창 상단에 표시될 메뉴 바 아이템. 일반적으로 `MenuBar` 객체를 할당하여 메뉴를 구성합니다.                                                     |
| `header`      | `Item`      | `null` | 메뉴 바 아래, 창 상단에 표시될 헤더 아이템. `ToolBar` 등을 배치하는 데 자주 사용됩니다.                                                    |
| `footer`      | `Item`      | `null` | 창 하단에 표시될 푸터 아이템. 상태 메시지를 표시하는 `ToolBar`, `Label` 등을 배치하여 상태바(Status bar)처럼 사용할 수 있습니다.                     |
| `contentItem` | `Item`      | (읽기 전용) | `Window`에서 상속. `menuBar`, `header`, `footer`를 제외한 창의 주 내용 영역을 나타내는 루트 아이템. 여기에 애플리케이션의 주 UI를 배치합니다. |
| `background`  | `Item`      | `null` | `contentItem` 뒤에 배치될 배경 아이템. 이미지나 그라데이션 배경 등에 사용됩니다.                                                      |
| `activeFocusControl` | `Control`| (읽기 전용) | 현재 활성 포커스를 가진 `Control`. `Window.activeFocusItem`과 달리 컨트롤 자체를 가리킵니다.                                        |
| `font`        | `font`      | (시스템 기본값)| 창과 자식 컨트롤에 적용될 기본 글꼴.                                                                                              |
| `locale`      | `Locale`    | (시스템 기본값)| 창과 자식 컨트롤에 적용될 로케일.                                                                                                |
| `contentData` | `list<QtObject>` | (기본 프로퍼티) | 창의 자식으로 선언된 모든 객체 목록. 시각적 아이템은 `contentItem`의 자식이 됩니다.                                                   |
| `topPadding`, `leftPadding`, `rightPadding`, `bottomPadding` | `real` | (Safe Area 반영) | (Qt 6.9+) `contentItem`의 패딩. 기본적으로 창의 Safe Area 여백을 반영합니다.                                                       |

## 주요 시그널

`Window`의 모든 시그널 (`closing`, `visibleChanged`, `widthChanged`, `heightChanged` 등)을 상속받습니다.

## 주요 메소드

`Window`의 모든 메소드 (`show`, `hide`, `close`, `requestActivate` 등)를 상속받습니다.

## 예제

```qml
import QtQuick
import QtQuick.Controls // ApplicationWindow, MenuBar, ToolBar, Dialog, Label 등 사용
import QtQuick.Layouts // RowLayout 사용

ApplicationWindow {
    id: appWindow
    width: 640
    height: 480
    visible: true
    title: "ApplicationWindow Example (Corrected Footer)"

    // 메뉴 바 정의
    menuBar: MenuBar {
        Menu {
            title: qsTr("&File")
            Action {
                text: qsTr("&New")
                shortcut: "Ctrl+N"
                onTriggered: {
                    console.log("New action triggered");
                    // footer의 Label에 접근하기 위해 id 사용
                    statusLabel.text = "New Action";
                }
            }
            Action {
                text: qsTr("&Open...")
                shortcut: "Ctrl+O"
                onTriggered: {
                    console.log("Open action triggered");
                    statusLabel.text = "Open Action";
                }
            }
            MenuSeparator { }
            Action { text: qsTr("E&xit"); onTriggered: Qt.quit() }
        }
        Menu {
            title: qsTr("&Help")
            Action {
                text: qsTr("About...")
                onTriggered: {
                    aboutDialog.open();
                    statusLabel.text = "About Action";
                }
            }
        }
    }

    // 헤더 정의 (ToolBar 사용)
    header: ToolBar {
        RowLayout {
            ToolButton {
                text: qsTr("New")
                icon.source: "qrc:/qt-project.org/imports/QtQuick/Controls/images/document-new.png" // 경로 확인 필요
                focusPolicy: Qt.NoFocus
                onClicked: {
                     console.log("New toolbar button clicked");
                     statusLabel.text = "New Button Clicked";
                }
            }
            ToolButton {
                text: qsTr("Open")
                icon.source: "qrc:/qt-project.org/imports/QtQuick/Controls/images/document-open.png" // 경로 확인 필요
                focusPolicy: Qt.NoFocus
                onClicked: {
                    console.log("Open toolbar button clicked");
                    statusLabel.text = "Open Button Clicked";
                }
            }
        }
    }

    // 푸터 정의 (상태바 역할로 ToolBar 사용)
    footer: ToolBar {
        // ToolBar는 기본 배경과 패딩을 가짐
        Label {
            id: statusLabel // 상태 메시지 표시용 Label
            text: "Ready"
            anchors.verticalCenter: parent.verticalCenter // ToolBar 중앙에 배치 (선택 사항)
            anchors.left: parent.left
            anchors.leftMargin: 5 // 왼쪽 여백
        }
        // 필요시 오른쪽에 다른 아이템 추가 가능 (예: Spacer)
    }

    // 메인 내용 영역
    TextArea {
        id: mainTextArea
        anchors.top: parent.header ? parent.header.bottom : parent.top
        anchors.bottom: parent.footer ? parent.footer.top : parent.bottom
        anchors.left: parent.left
        anchors.right: parent.right
        placeholderText: "Enter text here..."
        wrapMode: Text.WordWrap
        onTextChanged: {
            statusLabel.text = mainTextArea.length > 0 ? "Editing..." : "Ready";
        }
    }

    // About 대화상자
    Dialog {
        id: aboutDialog
        title: "About ApplicationWindow"
        standardButtons: Dialog.Ok
        modal: true
        Label {
            text: "Simple ApplicationWindow Example (Corrected Footer)\\nUsing QtQuick.Controls"
            padding: 20
        }
    }
}
```

## 참고 사항

*   `ApplicationWindow`는 `QtQuick.Controls` 모듈에 속하므로 해당 모듈을 임포트해야 합니다.
*   `menuBar`, `header`, `footer` 프로퍼티에 각각 `MenuBar`, `ToolBar`, 또는 다른 `Item` 기반 컴포넌트를 할당하여 창의 구조를 정의합니다.
*   메뉴 항목은 주로 `Action` 요소를 사용하여 정의하며, `Action`은 텍스트, 아이콘, 단축키, 활성화 상태 등을 포함하고 `triggered` 시그널을 통해 동작을 실행합니다.
*   `header`에는 주로 `ToolBar`를 배치하여 자주 사용하는 기능을 빠르게 실행할 수 있도록 합니다.
*   `footer`에는 `ToolBar`나 `Rectangle` 안에 `Label` 등을 배치하여 상태 메시지를 표시하는 등 상태바(status bar)와 유사한 UI를 구성할 수 있습니다.
*   창의 주 내용은 `ApplicationWindow`의 루트 아이템으로 직접 배치하면 자동으로 `contentItem`의 자식으로 처리됩니다.
*   Fluent UI와 같은 외부 UI 라이브러리를 사용하는 경우, 해당 라이브러리에서 제공하는 자체적인 창 컴포넌트(예: `FluentWindow`)를 사용하는 것이 스타일 일관성 측면에서 더 권장될 수 있습니다.

## 공식 문서 링크

* [ApplicationWindow QML Type ](https://doc.qt.io/qt-6/qml-qtquick-controls-applicationwindow.html) 