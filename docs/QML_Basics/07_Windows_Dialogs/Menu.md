# Menu

**모듈:** `import QtQuick.Controls`

## 개요

`Menu`는 컨텍스트 메뉴나 드롭다운 메뉴를 구현하는 데 사용되는 팝업 컨트롤입니다. `Popup`을 기반으로 하며, 내부에 `MenuItem`, `MenuSeparator`, 또는 다른 `Menu`(서브 메뉴)들을 포함하여 계층적인 메뉴 구조를 만들 수 있습니다.

일반적으로 버튼 클릭이나 마우스 오른쪽 버튼 클릭과 같은 사용자 액션에 의해 특정 위치에 표시됩니다.

## 기반 클래스

*   `Popup`

## 주요 프로퍼티

`Popup`의 모든 프로퍼티 (`opened`, `x`, `y`, `modal`, `focus`, `closePolicy` 등)를 상속받습니다.

`Menu`에 추가된 주요 프로퍼티는 다음과 같습니다.

| 이름        | 타입        | 기본값 | 설명                                                                                              |
| :---------- | :---------- | :----- | :------------------------------------------------------------------------------------------------ |
| `title`     | `string`    | ""   | (서브 메뉴의 경우) 부모 메뉴에 표시될 이 메뉴의 제목.                                                   |
| `contentData`| `list<Object>`| (자동)| 메뉴에 추가된 `MenuItem`, `MenuSeparator`, `Menu` 객체들의 리스트.                               |
| `contentModel`| `Object`  | (자동)| `contentData`를 기반으로 생성된 내부 모델. `ListView`와 유사하게 `delegate`과 함께 사용될 수 있습니다 (고급 사용법). |
| `delegate`  | `Component` | (스타일 의존)| 각 메뉴 항목(`MenuItem` 등)을 시각적으로 표현하는 델리게이트. 일반적으로 스타일에서 제공하는 것을 사용합니다.    |
| `cascade`   | `bool`      | `false`| `true`이면 서브 메뉴가 부모 메뉴 옆에 계단식으로 표시됩니다.                                            |
| `overlap`   | `real`      | (스타일 의존)| `cascade`가 `true`일 때 서브 메뉴가 부모 메뉴와 겹치는 정도 (픽셀 단위).                                |

## 주요 시그널

`Popup`의 모든 시그널 (`opened`, `closed`, `aboutToShow`, `aboutToHide`)을 상속받습니다.

`Menu` 자체에는 특별한 추가 시그널이 적지만, 내부에 포함된 `MenuItem`의 `triggered` 시그널을 주로 사용합니다.

## 주요 메소드

`Popup`의 모든 메소드 (`open`, `close`)를 상속받습니다.

| 이름           | 파라미터 | 반환타입 | 설명                                                              |
| :------------- | :------- | :------- | :---------------------------------------------------------------- |
| `popup(pos?)`  | `QPointF`| -        | 메뉴를 지정된 위치(`pos`, 전역 좌표)에 엽니다. 위치를 생략하면 현재 마우스 위치에 엽니다. |
| `addMenu(menu)`| `Menu`   | -        | 이 메뉴에 서브 메뉴(`menu`)를 추가합니다.                               |
| `addItem(item)`| `MenuItem`| -       | 이 메뉴에 `MenuItem`을 추가합니다.                                |
| `addSeparator()`| -       | `MenuSeparator` | 이 메뉴에 구분선(`MenuSeparator`)을 추가하고 반환합니다.             |
| `insertMenu(...)`|         | -        | 지정된 위치에 서브 메뉴를 삽입합니다.                               |
| `insertItem(...)`|         | -        | 지정된 위치에 `MenuItem`을 삽입합니다.                             |
| `insertSeparator(...)`|     | `MenuSeparator` | 지정된 위치에 구분선을 삽입하고 반환합니다.                          |
| `remove(...)`   |         | -        | 메뉴 항목을 제거합니다.                                           |
| `clear()`      | -        | -        | 메뉴의 모든 항목을 제거합니다.                                    |

## MenuItem 및 MenuSeparator

`Menu`의 내용은 주로 `MenuItem`과 `MenuSeparator`로 구성됩니다.

*   **`MenuItem`**: 메뉴 내의 개별 항목을 나타냅니다.
    *   `text`: 메뉴 항목에 표시될 텍스트.
    *   `icon`: 아이콘 관련 프로퍼티 (`icon.name`, `icon.source` 등).
    *   `checkable`: 체크 가능한 메뉴 항목인지 여부.
    *   `checked`: 현재 체크 상태.
    *   `enabled`: 항목 활성화 여부.
    *   `action`: 연결된 `Action` 객체.
    *   `triggered()`: 사용자가 항목을 클릭(선택)했을 때 발생하는 시그널.
    *   `font`: 텍스트 글꼴.
    *   `shortcut`: 메뉴 항목 옆에 표시될 단축키 텍스트 (실제 단축키 기능은 `Action`이나 다른 방법으로 구현 필요).
*   **`MenuSeparator`**: 메뉴 항목들 사이에 시각적인 구분선을 추가합니다.

## 예제

```qml
import QtQuick
import QtQuick.Controls
import QtQuick.Layouts

ApplicationWindow {
    width: 400; height: 300
    visible: true
    title: "Menu Example"

    // 컨텍스트 메뉴 정의
    Menu {
        id: contextMenu
        title: "Edit"

        MenuItem {
            text: "Cut"
            icon.name: "edit-cut"
            onTriggered: console.log("Cut clicked")
        }
        MenuItem {
            text: "Copy"
            icon.name: "edit-copy"
            onTriggered: console.log("Copy clicked")
        }
        MenuItem {
            text: "Paste"
            icon.name: "edit-paste"
            enabled: false // 비활성화 예시
            onTriggered: console.log("Paste clicked")
        }
        MenuSeparator { }
        MenuItem {
            text: "Select All"
            onTriggered: console.log("Select All clicked")
        }
        // 서브 메뉴 예시
        Menu {
            title: "More Options"
            MenuItem { text: "Option 1" }
            MenuItem { text: "Option 2" }
        }
    }

    // 메인 창 내용
    Rectangle {
        anchors.fill: parent
        color: "lightgray"

        // 마우스 오른쪽 버튼 클릭 시 컨텍스트 메뉴 표시
        MouseArea {
            anchors.fill: parent
            acceptedButtons: Qt.RightButton
            onClicked: (mouse) => {
                if (mouse.button === Qt.RightButton) {
                    // 전역 좌표로 변환하여 메뉴 표시
                    contextMenu.popup(parent.mapToGlobal(mouse.x, mouse.y))
                }
            }
        }

        Label {
            text: "Right-click here for context menu."
            anchors.centerIn: parent
        }

        // 버튼 클릭 시 드롭다운 메뉴 표시
        Button {
            id: menuButton
            text: "File Menu"
            anchors.horizontalCenter: parent.horizontalCenter
            anchors.bottom: parent.bottom
            anchors.bottomMargin: 20

            // 버튼 아래에 표시될 드롭다운 메뉴
            Menu {
                id: fileMenu
                // 팝업 위치: 버튼 바로 아래
                x: 0
                y: menuButton.height
                // 부모를 버튼으로 설정하여 함께 이동
                // parent: menuButton // Popup의 parent 설정 방식 (Qt 6+) 또는 다른 방식 필요

                MenuItem { text: "New"; onTriggered: console.log("New") }
                MenuItem { text: "Open..."; onTriggered: console.log("Open") }
                MenuItem { text: "Save"; onTriggered: console.log("Save") }
            }

            onClicked: {
                // 팝업 위치를 버튼 기준으로 설정하고 열기 (간단 버전)
                // var pos = menuButton.mapToGlobal(0, menuButton.height)
                // fileMenu.popup(pos)
                // 또는 opened 프로퍼티 사용
                fileMenu.parent = menuButton // 팝업의 부모를 버튼으로 설정 (위치 계산 용이)
                fileMenu.open() // open()만 호출하면 버튼 아래에 나타나는 경우가 많음 (스타일 의존)
            }
        }
    }
}
```

## 참고 사항

*   `Menu`는 `QtQuick.Controls` 모듈에 속합니다.
*   메뉴 내용은 `MenuItem`, `MenuSeparator`, 다른 `Menu`(서브 메뉴) 객체들을 자식으로 추가하여 구성합니다.
*   `MenuItem`의 `triggered` 시그널을 사용하여 사용자가 메뉴 항목을 선택했을 때의 동작을 정의합니다.
*   `popup()` 메소드를 사용하면 특정 전역 좌표에 메뉴를 표시할 수 있습니다. 컨텍스트 메뉴 구현 시 `MouseArea`에서 마우스 좌표를 `mapToGlobal()`로 변환하여 사용합니다.
*   `open()` 메소드를 호출하여 `Popup`처럼 열 수도 있습니다. 이때 `x`, `y`, `parent` 프로퍼티를 사용하여 위치를 조절합니다. 드롭다운 메뉴의 경우, 메뉴를 여는 버튼을 `parent`로 설정하고 `y`를 버튼 높이로 설정하는 방식이 일반적입니다.
*   `cascade: true`를 설정하면 서브 메뉴가 부모 메뉴 옆에 계단식으로 나타납니다.
*   `Action` 객체를 `MenuItem`과 연결하면 액션의 상태(텍스트, 아이콘, 활성화 여부 등)가 메뉴 항목에 자동으로 반영되고, 액션의 `triggered` 시그널이 메뉴 항목 선택 시 발생합니다. 