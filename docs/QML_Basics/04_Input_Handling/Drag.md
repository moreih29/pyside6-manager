# Drag Attached Property

**모듈:** `import QtQuick`

## 개요

`Drag`는 QML의 Attached Property 메커니즘을 통해 `Item` 기반 컴포넌트가 마우스나 터치로 드래그될 수 있도록 기능을 추가합니다. 사용자가 아이템을 눌러 드래그하면, `Drag` 속성이 적용된 아이템이 드래그 이벤트를 감지하고 관련 정보를 제공하여 **드래그 작업의 시작점(Source)** 역할을 합니다.

주로 아이템을 화면 내에서 자유롭게 이동시키거나, **`DropArea` 컴포넌트(드롭 대상)와 함께 사용하여 완전한 드래그 앤 드롭(Drag and Drop) 기능을 구현**하는 데 사용됩니다. `Drag`는 드래그할 데이터(`mimeData`)와 지원하는 액션(`supportedActions`)을 정의하고, `DropArea`는 이 정보를 바탕으로 드롭을 수락하거나 거절합니다.

## 주요 Attached Properties

| 이름           | 타입                 | 기본값        | 설명                                                                                              |
| :------------- | :------------------- | :------------ | :------------------------------------------------------------------------------------------------ |
| `active`       | `bool`               | `false`       | (읽기 전용) 현재 드래그 작업이 진행 중인지 여부.                                                      |
| `target`       | `Item`               | `null`        | 드래그 작업의 대상 아이템. 지정하지 않으면 `Drag`이 부착된 아이템 자체가 대상이 됩니다. 드래그 시 이 `target` 아이템이 이동될 수 있습니다. |
| `source`       | `Item`               | `null`        | 드래그 작업을 시작한 아이템 (`MouseArea` 등).                                                      |
| `startX`, `startY` | `real`             | -             | (읽기 전용) 드래그가 시작된 지점의 X, Y 좌표 (`Drag`이 부착된 아이템 기준).                               |
| `x`, `y`       | `real`               | -             | (읽기 전용) 현재 드래그 중인 포인터의 X, Y 좌표 (`Drag`이 부착된 아이템 기준).                               |
| `hotSpot.x`, `hotSpot.y` | `real`         | `0`           | 드래그 시작 시 포인터 위치와 `target` 아이템의 좌상단 모서리 간의 오프셋. 드래그 중 `target`의 위치 계산에 사용됨. |
| `minimumX`, `maximumX` | `real`           | `-Infinity`, `Infinity` | `target` 아이템이 드래그될 수 있는 X 좌표의 최소/최대값.                                             |
| `minimumY`, `maximumY` | `real`           | `-Infinity`, `Infinity` | `target` 아이템이 드래그될 수 있는 Y 좌표의 최소/최대값.                                             |
| `axis`         | `enum`               | `Drag.XandYAxis` | 드래그가 가능한 축 (`XAxis`, `YAxis`, `XandYAxis`).                                               |
| `filterChildren`| `bool`              | `false`       | `true`이면, 자식 아이템에서 시작된 마우스/터치 이벤트는 무시하고 `Drag`이 부착된 아이템 자체에서 시작된 이벤트만으로 드래그 시작. |
| `dragType`     | `enum`               | `Drag.Automatic`| 드래그 시작 조건 (`Automatic`, `Manual`). `Manual`은 `startDrag()` 호출 필요.                      |
| `threshold`    | `real`               | -             | 드래그를 시작하기 위해 움직여야 하는 최소 거리 (픽셀). 시스템 기본값 사용.                              |
| `supportedActions`| `Qt::DropActions` | `Qt::MoveAction` | 이 드래그 소스가 지원하는 액션 종류 (복사, 이동, 링크 등). **`DropArea`는 이 정보를 보고 어떤 액션으로 드롭을 수락할지 결정합니다.** |
| `proposedAction`| `Qt::DropAction`  | `Qt::IgnoreAction` | (읽기 전용) 현재 포인터 아래의 **`DropArea`가 제안하는 드롭 액션.** `DropArea`의 `onEntered` 핸들러 등에서 설정됩니다. |
| `overrideCursor`| `bool`              | `false`       | `true`이면 드래그 중 시스템 기본 커서 대신 지정된 커서(`cursorShape`) 사용.                           |
| `cursorShape`  | `Qt::CursorShape`    | `Qt::ArrowCursor` | `overrideCursor`가 `true`일 때 사용할 마우스 커서 모양.                                            |
| `mimeData`     | `Object` (QMimeData) | `{}`          | 드래그 앤 드롭 시 전달할 데이터. `text`, `urls`, `html`, `color`, 사용자 정의 데이터(`application/x-mycustomdata` 등)를 포함할 수 있습니다. **`DropArea`는 이 데이터를 보고 드롭을 수락할지 결정합니다.** |

## 주요 Attached Signal Handlers

| 이름            | 파라미터 | 설명                                                                 |
| :-------------- | :------- | :------------------------------------------------------------------- |
| `onDragStarted` | -        | 드래그 작업이 시작되었을 때 발생. 시각적 피드백 (예: 투명도 조절)을 시작하기 좋습니다. |
| `onDragFinished`| `DropAction dropAction` | 드래그 작업이 완료되었을 때(드롭 또는 취소) 발생. `dropAction`은 **`DropArea`에서 최종 결정된 액션 또는 `Qt.IgnoreAction`(취소/실패)입니다.** 이동(Move) 액션이 성공적으로 완료된 경우, 여기서 원본 아이템을 처리(예: 숨기기)할 수 있습니다. |

## 주요 Attached Methods

| 이름         | 파라미터                   | 반환타입 | 설명                                                                     |
| :----------- | :------------------------- | :------- | :----------------------------------------------------------------------- |
| `startDrag()`| `Qt::DropActions supportedActions` (선택 사항) | `void`   | `dragType`이 `Manual`일 때 프로그래밍 방식으로 드래그 시작.              |
| `cancelDrag()`| -                        | `void`   | 현재 진행 중인 드래그 작업을 취소.                                        |

## 예제

이 예제는 `MouseArea`에 `Drag` Attached Property를 사용하여 `Rectangle`을 드래그 가능하게 만들고, `DropArea`를 사용하여 드롭을 처리하는 방법을 보여줍니다.

```qml
import QtQuick

Window {
    width: 400
    height: 300
    visible: true
    title: "Drag and Drop Example (Drag + DropArea)"

    // 드래그될 아이템
    Rectangle {
        id: draggableItem
        x: 20; y: 20
        width: 80; height: 80
        color: dragArea.pressed ? "steelblue" : "lightblue"
        border.color: "gray"

        Text {
            anchors.centerIn: parent
            text: "Drag Me"
        }

        // 드래그를 감지하고 시작할 MouseArea
        MouseArea {
            id: dragArea
            anchors.fill: parent
            // 드래그 대상 지정: 이 MouseArea의 드래그가 draggableItem을 움직이도록 설정
            drag.target: draggableItem
            // drag.axis: Drag.YAxis // 특정 축으로만 드래그 제한 가능
            // drag.minimumY: 0; drag.maximumY: parent.height - height // 드래그 범위 제한 가능

            // 드래그 앤 드롭을 위한 MIME 데이터 설정
            // DropArea에서 이 데이터를 사용하여 드롭 가능 여부 판단 및 처리
            drag.mimeData: { "text/plain": "Dragged Text!", "color": "blue", "application/x-mycustomdata": { value: 123 } }
            drag.supportedActions: Qt.CopyAction | Qt.MoveAction // 이 드래그는 복사 또는 이동 액션을 지원함

            onPressed: console.log("Mouse pressed on draggable")

            // Drag Attached Property 시그널 핸들러
            Drag.onDragStarted: {
                console.log("Drag started")
                // 드래그 시작 시 시각적 효과 추가 가능 (예: 그림자)
                draggableItem.opacity = 0.7
            }
            Drag.onDragFinished: (dropAction) => {
                console.log("Drag finished with action:", dropAction)
                draggableItem.opacity = 1.0 // 드래그 종료 시 원래대로
                // dropAction 값: Qt.IgnoreAction(취소/실패), Qt.CopyAction, Qt.MoveAction 등
                // DropArea에서 MoveAction을 수락했다면, 여기서 원본 아이템 처리
                if (dropAction === Qt.MoveAction) {
                    // draggableItem.visible = false; // 예시: 이동 완료 시 원본 숨기기
                }
            }
        }
    }

    // 드롭 영역: DropArea 컴포넌트 사용
    DropArea {
        id: dropTarget
        anchors.right: parent.right
        anchors.bottom: parent.bottom
        anchors.margins: 20
        width: 150; height: 150

        // DropArea의 시각적 표현 (드래그 상태에 따라 변경)
        Rectangle {
            anchors.fill: parent
            color: parent.containsDrag ? "palegreen" : "lightgray" // 드래그 아이템이 위에 있으면 색 변경
            border.color: parent.containsDrag ? "green" : "darkgray"
            radius: 5

            Text {
                anchors.centerIn: parent
                text: parent.containsDrag ? "Drop Here" : "Drop Area"
                font.bold: parent.containsDrag
            }
        }

        // DropArea 시그널 핸들러
        onEntered: (drag) => {
            // 드래그된 아이템(drag 파라미터)이 영역 안으로 들어왔을 때 호출됨
            console.log("Drag entered drop area.")
            // 전달된 MIME 데이터 타입 확인
            console.log("  MIME types:", drag.formats)
            console.log("  Has text:", drag.hasText, "Has color:", drag.hasColor)
            console.log("  Supported actions by source:", drag.supportedActions)

            // DropArea가 어떤 타입의 데이터를 받을지, 어떤 액션을 수락할지 결정
            if (drag.hasFormat("text/plain")) {
                drag.acceptProposedAction() // 드래그 소스가 제안한 액션(기본값: supportedActions 중 첫번째) 수락
                // 또는 특정 액션 강제 지정:
                // if (drag.supportedActions & Qt.CopyAction) { // 드래그 소스가 복사를 지원하면
                //     drag.accept(Qt.CopyAction) // 복사 액션으로 받겠다고 명시
                //     console.log("Accepting drag with CopyAction")
                // } else {
                //     drag.accept() // 지원하는 다른 액션으로 받기
                // }
                 console.log("Accepting drag. Proposed Action: " + drag.proposedAction)
            } else {
                 console.log("Rejecting drag (unsupported format)")
                 drag.accepted = false // 받을 수 없는 타입이므로 거절
            }
        }

        onPositionChanged: (drag) => {
            // 드롭 영역 내에서 드래그 포인터 위치가 변경될 때 호출됨
            // console.log("Drag position inside DropArea:", drag.x, drag.y)
        }

        onDropped: (drag) => {
            // 사용자가 마우스/터치를 놓아 드롭이 발생했을 때 호출됨 (onEntered에서 accept된 경우)
            console.log("Item dropped! Final action:", drag.dropAction)
            // MIME 데이터 접근하여 사용
            if (drag.hasText) {
                console.log("  Dropped Text:", drag.text)
            }
            if (drag.hasColor) {
                console.log("  Dropped Color:", drag.color)
            }
            if (drag.hasFormat("application/x-mycustomdata")) {
                console.log("  Dropped Custom Data:", drag.getData("application/x-mycustomdata").value)
            }
            // drag.dropAction (최종 결정된 액션) 값에 따라 실제 작업 수행
            if (drag.dropAction === Qt.MoveAction) {
                 console.log("  --> Performing Move Action (e.g., placing item here)")
            } else if (drag.dropAction === Qt.CopyAction) {
                 console.log("  --> Performing Copy Action (e.g., creating a copy here)")
            }
        }

        onExited: {
            // 드래그된 아이템이 영역 밖으로 나갔을 때
            console.log("Drag exited drop area")
        }
    }
}
```

## 참고 사항

*   `Drag` Attached Property는 일반적으로 `MouseArea` 내부에 정의되어, `MouseArea`가 감지한 마우스/터치 이벤트를 기반으로 드래그 작업을 시작합니다.
*   `drag.target`을 명시적으로 설정하지 않으면, `MouseArea` 자체가 드래그 대상이 되려고 시도할 수 있습니다 (보통 원하는 동작이 아님). 드래그하려는 시각적 아이템을 `drag.target`으로 지정해야 합니다.
*   간단한 아이템 이동에는 `drag.target`만 사용해도 충분하지만, 애플리케이션 간 또는 복잡한 내부 드래그 앤 드롭에는 `mimeData`, `supportedActions`, `DropArea` 등을 함께 사용해야 합니다.
*   **드롭을 처리하는 방법에 대한 자세한 내용은 [`DropArea`](./DropArea.md) 문서를 참조하십시오.** `Drag`와 `DropArea`는 함께 동작하여 드래그 앤 드롭 상호작용을 완성합니다. 