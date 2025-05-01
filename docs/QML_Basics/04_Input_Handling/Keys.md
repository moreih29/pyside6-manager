# Keys Attached Property

## 모듈 정보

```qml
import QtQuick
```

## 개요

`Keys`는 QML의 Attached Property 메커니즘을 통해 특정 `Item` 기반 컴포넌트에 키보드 이벤트 처리 기능을 추가하는 데 사용됩니다. 아이템이 키보드 포커스(`activeFocus`가 `true`)를 가지고 있을 때, 사용자가 누르는 키에 따라 특정 동작을 수행하도록 정의할 수 있습니다.

`Keys` 자체는 컴포넌트가 아니라, 포커스를 받을 수 있는 아이템(예: `Item`, `Rectangle`, `FocusScope`, 또는 `QtQuick.Controls`의 대부분 컨트롤)에 `Keys.` 접두사를 사용하여 프로퍼티와 시그널 핸들러를 추가하는 방식입니다.

## 주요 Attached Properties

| 이름      | 타입    | 기본값 | 설명                                                                          |
| :-------- | :------ | :----- | :---------------------------------------------------------------------------- |
| `enabled` | `bool`  | `true` | 키보드 이벤트 처리를 활성화할지 여부. `false`이면 해당 아이템의 키 이벤트 핸들러가 동작하지 않음. |
| `forwardTo` | `list<Item>` | `[]`   | 처리되지 않은 키 이벤트를 전달할 아이템 목록.                                      |
| `priority`| `enum`  | `Keys.NormalPriority` | 여러 아이템이 동일 키 이벤트를 처리할 경우 우선순위 (`BeforeItem`, `NormalPriority`, `AfterItem`). |

## 주요 Attached Signal Handlers

`on<KeyName>Pressed` 형식의 시그널 핸들러를 사용하여 특정 키가 눌렸을 때 실행될 코드를 정의합니다. `event` 파라미터를 통해 키 이벤트에 대한 상세 정보(눌린 키, 수정자 키 등)에 접근할 수 있습니다.

| 이름                  | 파라미터       | 설명                                                                 |
| :-------------------- | :------------- | :------------------------------------------------------------------- |
| `onPressed`           | `KeyEvent event` | 아무 키나 눌렸을 때 발생. 가장 일반적인 핸들러.                         |
| `onReleased`          | `KeyEvent event` | 아무 키나 떼어졌을 때 발생.                                          |
| `onReturnPressed`     | `KeyEvent event` | Enter 키 (또는 Return 키)가 눌렸을 때 발생.                         |
| `onEnterPressed`      | `KeyEvent event` | 숫자 패드의 Enter 키가 눌렸을 때 발생.                               |
| `onSpacePressed`      | `KeyEvent event` | 스페이스바가 눌렸을 때 발생.                                         |
| `onTabPressed`        | `KeyEvent event` | Tab 키가 눌렸을 때 발생.                                             |
| `onBackPressed`       | `KeyEvent event` | Backspace 키가 눌렸을 때 발생.                                     |
| `onDeletePressed`     | `KeyEvent event` | Delete 키가 눌렸을 때 발생.                                        |
| `onEscapePressed`     | `KeyEvent event` | Esc 키가 눌렸을 때 발생.                                           |
| `onUpPressed`         | `KeyEvent event` | 위쪽 화살표 키가 눌렸을 때 발생.                                     |
| `onDownPressed`       | `KeyEvent event` | 아래쪽 화살표 키가 눌렸을 때 발생.                                   |
| `onLeftPressed`       | `KeyEvent event` | 왼쪽 화살표 키가 눌렸을 때 발생.                                     |
| `onRightPressed`      | `KeyEvent event` | 오른쪽 화살표 키가 눌렸을 때 발생.                                   |
| `onDigitPressed`      | `KeyEvent event` | 숫자 키(0-9)가 눌렸을 때 발생. `event.text`로 실제 숫자 확인 가능.   |
| `onLetterPressed`     | `KeyEvent event` | 문자 키(a-z, A-Z)가 눌렸을 때 발생. `event.text`로 실제 문자 확인 가능. |
| `onShortcutOverride`  | `KeyEvent event` | `Shortcut` 아이템과 충돌할 때 우선권을 갖기 위해 사용 (고급).          |
| `onSequencePressed`   | `KeyEvent event` | 입력 메소드(IME) 등에서 여러 키 입력이 조합될 때 발생 (고급).           |
| `onTextEdited`        | `KeyEvent event` | `onPressed`와 유사하지만, 텍스트 입력 위젯에 더 적합하게 동작 (고급). |
| `onTextInput`         | `KeyEvent event` | 최종적으로 입력될 텍스트가 결정되었을 때 발생 (IME 처리 포함).         |

**KeyEvent 파라미터 주요 속성:**
*   `accepted`: (bool) 이벤트를 처리했는지 여부. `true`로 설정하면 이벤트 전파 중단.
*   `key`: (Qt.Key) 눌린 키의 식별자 (예: `Qt.Key_Enter`, `Qt.Key_A`).
*   `modifiers`: (Qt.KeyboardModifiers) 함께 눌린 수정자 키 (예: `Qt.ShiftModifier`, `Qt.ControlModifier`).
*   `text`: (string) 해당 키 입력으로 생성된 문자열 (예: 'a', 'A', '#').
*   `count`: (int) 자동 반복(auto-repeat) 등으로 인해 한 번에 발생한 키 이벤트 수.
*   `isAutoRepeat`: (bool) 자동 반복으로 생성된 이벤트인지 여부.

## 예제

```qml
import QtQuick
import QtQuick.Controls // 표준 컨트롤 사용을 위해 추가
import QtQuick.Layouts // Row 사용을 위해 추가 (예제에서는 Row가 있으므로 유지)

Window {
    width: 300
    height: 200
    visible: true
    title: "Keys Attached Property Example"

    FocusScope { // 포커스 관리를 위한 컨테이너
        id: focusScope
        anchors.fill: parent

        RowLayout { // Row 대신 RowLayout 사용 권장
            anchors.centerIn: parent
            spacing: 10

            // 예제 1: Rectangle에 직접 Keys 적용
            Rectangle {
                id: rect1
                width: 80; height: 80
                color: activeFocus ? "orange" : "lightblue" // 포커스 받으면 색 변경
                focus: true // 포커스를 받을 수 있도록 설정
                Text { anchors.centerIn: parent; text: "Rect 1" }

                MouseArea {
                    anchors.fill: parent
                    onClicked: rect1.forceActiveFocus() // 클릭하면 포커스 받기
                }

                Keys.onPressed: (event) => { // 모든 키 누름 이벤트 처리
                    console.log("Rect1 - Key pressed:", event.key, "Text:", event.text)
                    if (event.key === Qt.Key_Space) {
                        color = Qt.rgba(Math.random(), Math.random(), Math.random(), 1)
                        console.log("Rect1 - Space pressed, color changed")
                        event.accepted = true // 스페이스바 이벤트는 여기서 처리 완료
                    }
                }
            }

            // 예제 2: Button 컨트롤에 Keys 적용
            Button { // 표준 Button 컨트롤 사용
                id: button1
                text: "Button 1"
                focusPolicy: Qt.StrongFocus // Button은 기본적으로 focus 가능
                // Button은 내부적으로 Space, Enter 키 처리가 되어있을 수 있음
                // 필요시 Keys.onPressed 등으로 오버라이드 가능

                Keys.onReturnPressed: (event) => {
                    console.log("Button1 - Enter/Return pressed")
                    // 기본 동작(onClicked 등)을 막으려면 accepted = true
                    // event.accepted = true
                }
                Keys.onRightPressed: {
                    // 오른쪽 화살표 누르면 rect1으로 포커스 이동 시도
                    console.log("Button1 - Right pressed, focusing rect1")
                    rect1.forceActiveFocus()
                    event.accepted = true
                }
                // 포커스 시각화 (Button 스타일에 따라 다를 수 있음)
                background: Rectangle {
                    color: parent.activeFocus ? "orange" : "lightgray"
                    border.color: "gray"
                }
            }
        }
    }
}
```

## 참고 사항

*   키보드 이벤트를 받으려면 해당 아이템의 `focus` 프로퍼티가 `true`이고, 현재 `activeFocus` 상태여야 합니다.
*   `activeFocus`는 현재 활성화된 포커스를 가진 단 하나의 아이템을 의미하며, `Window`나 `FocusScope` 단위로 관리됩니다.
*   `forceActiveFocus()` 메소드를 사용하여 특정 아이템에 프로그래밍 방식으로 포커스를 줄 수 있습니다.
*   이벤트 핸들러 내에서 `event.accepted = true`를 호출하여 이벤트 처리를 완료했음을 알리고, 상위 아이템이나 다른 핸들러로 이벤트가 전파되는 것을 막는 것이 중요합니다.
*   특정 키 조합(단축키)을 전역적으로 처리하려면 `Shortcut` 아이템을 사용하는 것이 더 편리할 수 있습니다.

## 공식 문서 링크

*   [Qt Quick Keys Attached Property](https://doc.qt.io/qt-6/qml-qtquick-keys.html) 