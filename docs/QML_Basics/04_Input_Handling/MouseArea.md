# MouseArea

**모듈:** `import QtQuick`

## 개요

`MouseArea`는 특정 영역 내에서 발생하는 마우스 이벤트(클릭, 더블클릭, 누름, 뗌, 이동, 들어옴, 나감, 휠)와 기본적인 터치 이벤트를 감지하고 처리하는 데 사용되는 보이지 않는(non-visual) 아이템입니다.

일반적으로 시각적 아이템(예: `Rectangle`, `Image`)의 자식으로 배치되어 해당 아이템에 대한 사용자 상호작용을 가능하게 합니다. `MouseArea`는 자신이 덮고 있는 영역 전체에 대해 마우스 이벤트를 받습니다.

## 주요 프로퍼티

| 이름               | 타입           | 기본값    | 설명                                                                                                |
| :----------------- | :------------- | :-------- | :-------------------------------------------------------------------------------------------------- |
| `acceptedButtons`  | `Qt.MouseButtons` | `Qt.LeftButton` | 처리할 마우스 버튼을 지정합니다 (`Qt.LeftButton`, `Qt.RightButton`, `Qt.MiddleButton`, `Qt.AllButtons` 등 조합 가능). |
| `containsMouse`    | `bool`         | `false`   | (읽기 전용) 마우스 커서가 현재 `MouseArea` 영역 안에 있는지 여부. (`hoverEnabled: false`일 경우, 누른 상태에서만 true가 될 수 있으며, `onPressed`에서 `accepted=false`하면 false 유지) |
| `containsPress`    | `bool`         | `false`   | (읽기 전용) `acceptedButtons` 중 하나가 눌렸고 동시에 마우스 커서가 영역 안에 있는지 여부 (`pressed && containsMouse`). |
| `cursorShape`      | `Qt.CursorShape`| `Qt.ArrowCursor` | `MouseArea` 위에 마우스 커서가 있을 때 표시될 커서 모양. `Qt.NoButton`과 함께 사용하여 이벤트 처리 없이 커서만 변경 가능. |
| `drag`             | `QtObject`     | -         | (그룹 프로퍼티) 아이템을 드래그 가능하게 만드는 속성 그룹 (`target`, `active`, `axis`, `minimum/maximumX/Y` 등 포함). 상세 내용은 [Drag Attached Property](./Drag.md) 참조. |
| `enabled`          | `bool`         | `true`    | `MouseArea`가 활성화되어 이벤트를 받을지 여부.                                                       |
| `hoverEnabled`     | `bool`         | `false`   | 마우스 버튼을 누르지 않아도 마우스 커서 위치/진입/이탈 (`containsMouse`, `positionChanged`, `entered`, `exited`)을 감지할지 여부. 기본값은 `false`. 성능을 위해 필요할 때만 `true`로 설정. |
| `mouseX`           | `real`         | -         | (읽기 전용) `MouseArea` 내에서의 마우스 X 좌표. `hoverEnabled: true` 이거나 버튼이 눌린 상태여야 유효.                   |
| `mouseY`           | `real`         | -         | (읽기 전용) `MouseArea` 내에서의 마우스 Y 좌표. `hoverEnabled: true` 이거나 버튼이 눌린 상태여야 유효.                   |
| `pressAndHoldInterval`| `int`        | 800       | `pressAndHold` 시그널이 발생하기까지 눌린 상태를 유지해야 하는 시간 (밀리초). 기본값 800ms.                        |
| `pressed`          | `bool`         | `false`   | (읽기 전용) `acceptedButtons` 중 하나가 현재 눌린 상태인지 여부 (영역 밖으로 나가도 유지).                                    |
| `pressedButtons`   | `Qt.MouseButtons`| `Qt.NoButton` | (읽기 전용) 현재 눌려있는 모든 마우스 버튼 플래그.                                                |
| `preventStealing`  | `bool`         | `false`   | `true`로 설정하면, 이 `MouseArea`가 마우스 이벤트를 받은 후 다른 아이템(예: `Flickable`)이 이벤트를 가로채지 못하도록 시도합니다. 기본값 `false`. |
| `propagateComposedEvents`| `bool` | `false`   | `true`이면, `clicked`, `doubleClicked`, `pressAndHold` 이벤트 발생 시 `accepted=false`로 설정하여 아래에 있는 다른 `MouseArea`로 이벤트를 전파할 수 있습니다. 기본값 `false`. |
| `scrollGestureEnabled`| `bool`   | `true`    | 트랙패드의 두 손가락 스크롤 같은 제스처에 반응할지 여부. `false`이면 실제 마우스 휠 이벤트만 `wheel` 시그널을 발생시키고 제스처는 통과시킵니다. 기본값 `true`. |

## 주요 시그널

| 이름            | 파라미터                                   | 반환타입 | 설명                                                                                                                               |
| :-------------- | :----------------------------------------- | :------- | :--------------------------------------------------------------------------------------------------------------------------------- |
| `canceled`      | -                                          | -        | (핸들러: `onCanceled`) 다른 아이템(예: `Flickable`)이 마우스 이벤트 처리를 가로챘을 때 발생. `onReleased`와 함께 처리하여 상태 초기화 필요. |
| `clicked`       | `MouseEvent mouse`                         | -        | (핸들러: `onClicked`) `acceptedButtons` 중 하나가 영역 내에서 눌렀다 떼어졌을 때 발생.                                                      |
| `doubleClicked` | `MouseEvent mouse`                         | -        | (핸들러: `onDoubleClicked`) `acceptedButtons` 중 하나가 빠르게 두 번 클릭되었을 때 발생.                                                      |
| `entered`       | -                                          | -        | (핸들러: `onEntered`) 마우스 커서가 영역 안으로 들어왔을 때 발생. (`hoverEnabled: true` 필요)                                       |
| `exited`        | -                                          | -        | (핸들러: `onExited`) 마우스 커서가 영역 밖으로 나갔을 때 발생. (`hoverEnabled: true` 필요)                                            |
| `positionChanged`| `MouseEvent mouse`                         | -        | (핸들러: `onPositionChanged`) 마우스 커서 위치가 영역 내에서 변경될 때 발생. (`hoverEnabled: true` 필요)                                |
| `pressAndHold`  | `MouseEvent mouse`                         | -        | (핸들러: `onPressAndHold`) `acceptedButtons` 중 하나를 `pressAndHoldInterval` 동안 누르고 있을 때 발생.                                |
| `pressed`       | `MouseEvent mouse`                         | -        | (핸들러: `onPressed`) `acceptedButtons` 중 하나가 영역 내에서 눌렸을 때 발생. 여기서 `mouse.accepted = false` 설정 가능.                |
| `released`      | `MouseEvent mouse`                         | -        | (핸들러: `onReleased`) 눌렸던 `acceptedButtons` 중 하나가 영역 내 또는 밖에서 떼어졌을 때 발생.                                       |
| `wheel`         | `WheelEvent wheel`                         | -        | (핸들러: `onWheel`) 마우스 휠 또는 스크롤 제스처(`scrollGestureEnabled: true`일 때)가 영역 내에서 발생했을 때.                               |

**MouseEvent 파라미터 주요 속성:**
*   `accepted`: (bool) 이벤트를 처리했는지 여부. `true`로 설정하면 상위 아이템으로 이벤트 전파 중단. (일부 시그널에서는 설정 효과 없음)
*   `button`: (Qt.MouseButton) 이벤트를 발생시킨 버튼.
*   `buttons`: (Qt.MouseButtons) 현재 눌린 모든 버튼.
*   `modifiers`: (Qt.KeyboardModifiers) 이벤트 발생 시 함께 눌린 키보드 수정자(Shift, Ctrl 등).
*   `x`, `y`: (real) `MouseArea` 좌표계 기준 이벤트 발생 위치.

**WheelEvent 파라미터 주요 속성:**
*   `angleDelta`: (point) 휠 각도 변화량 (수직/수평).
*   `pixelDelta`: (point) 픽셀 단위 휠 변화량 (일부 마우스 지원).
*   기타 `MouseEvent` 속성 상속.

## 예제

```qml
import QtQuick

Window {
    width: 200
    height: 200
    visible: true
    title: "MouseArea Example"

    Rectangle {
        id: rect
        width: 100; height: 100
        anchors.centerIn: parent
        color: area.containsMouse ? "lightsteelblue" : "lightblue" // 마우스 올리면 색 변경

        Text {
            id: statusText
            anchors.centerIn: parent
            text: "Click Me"
        }

        MouseArea {
            id: area
            anchors.fill: parent // 부모(Rectangle) 영역 채우기
            hoverEnabled: true // 마우스 위치 및 진입/이탈 감지 활성화
            cursorShape: Qt.PointingHandCursor // 손가락 모양 커서

            onClicked: {
                statusText.text = "Clicked!"
                // mouse.button, mouse.x, mouse.y 등을 사용할 수 있음
                console.log("Clicked at:", mouse.x, mouse.y)
                mouse.accepted = true // 이벤트 처리 완료, 상위 전파 중단
            }

            onPressed: {
                rect.color = "steelblue" // 누르면 색 진하게
            }

            onReleased: {
                rect.color = area.containsMouse ? "lightsteelblue" : "lightblue" // 떼면 원래대로
            }

            onEntered: {
                console.log("Mouse entered")
            }

            onExited: {
                console.log("Mouse exited")
                statusText.text = "Click Me" // 나가면 텍스트 초기화
            }
        }
    }
}
```

## 참고 사항

*   `MouseArea`는 기본적으로 이벤트를 받으면 `accepted`를 `true`로 설정하여 상위 아이템으로의 이벤트 전파를 막습니다. 이를 원치 않으면 시그널 핸들러 내에서 `mouse.accepted = false`로 설정해야 합니다.
*   여러 `MouseArea`가 겹쳐 있을 경우, Z 순서(stacking order)가 가장 높은 `MouseArea`가 우선적으로 이벤트를 받습니다. `preventStealing` 프로퍼티로 동작을 변경할 수 있습니다.
*   터치스크린에서는 `TapHandler`, `DragHandler`, `PinchHandler` 등 `QtQuick.InputHandlers` 모듈의 핸들러를 사용하는 것이 더 권장됩니다.

## 공식 문서 링크

*   [Qt Quick MouseArea QML Type](https://doc.qt.io/qt-6/qml-qtquick-mousearea.html)
