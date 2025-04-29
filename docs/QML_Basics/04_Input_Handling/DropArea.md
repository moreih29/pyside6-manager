# DropArea

**모듈:** `import QtQuick`

## 개요

`DropArea`는 드래그 앤 드롭(Drag and Drop) 작업을 위한 **대상(Target) 영역**을 정의하는 보이지 않는 아이템입니다. 사용자가 **`Drag` Attached Property가 적용된 아이템(드래그 소스)**을 드래그하여 `DropArea` 영역 위로 가져오면, `DropArea`는 관련 시그널(`onEntered`, `onPositionChanged`, `onDropped`, `onExited`)을 발생시켜 드롭 가능 여부 판단, 시각적 피드백 제공, 드롭 시 데이터 처리 등의 로직을 구현할 수 있도록 합니다.

`DropArea`는 **드래그 소스(`Drag` 쪽)**에서 전달하는 `mimeData`를 확인하고, 자신이 처리할 수 있는 데이터 형식인지, 어떤 드롭 액션(이동, 복사 등)을 수락할지 결정하는 **수신 측(Receiver)** 역할을 합니다.

## 주요 프로퍼티

| 이름           | 타입             | 기본값 | 설명                                                                                                |
| :------------- | :--------------- | :----- | :-------------------------------------------------------------------------------------------------- |
| `enabled`      | `bool`           | `true` | `DropArea`가 활성화되어 드롭 이벤트를 받을지 여부.                                                     |
| `containsDrag` | `bool`           | `false`| (읽기 전용) 현재 드래그 중인 아이템이 `DropArea` 영역 내에 있는지 여부. 시각적 피드백에 유용.          |
| `keys`         | `list<string>`   | `[]`   | (고급) 드롭을 수락하기 위해 필요한 특정 키(데이터 형식 식별자) 목록. 비어 있으면 모든 드롭을 고려.      |

## 주요 시그널

모든 드롭 관련 시그널 핸들러는 `drag`라는 파라미터를 받습니다. 이 `drag` 파라미터는 현재 드래그 작업 **(시작된 `Drag` Attached Property에 의해 제공됨)** 에 대한 정보를 담고 있는 객체이며, 드래그 소스가 정의한 속성들(`mimeData`, `supportedActions` 등)과 드롭 수락/거절을 위한 메소드(`accept()`, `acceptProposedAction()`)를 제공합니다.

| 이름              | 파라미터       | 반환타입 | 설명                                                                                                                               |
| :---------------- | :------------- | :------- | :--------------------------------------------------------------------------------------------------------------------------------- |
| `onEntered`       | `DropEvent drag` | -        | 드래그 중인 아이템이 `DropArea` 영역 안으로 처음 들어왔을 때 발생. 여기서 **`drag` 파라미터의 정보를 확인하고** `drag.accept()` 등을 호출하여 드롭 수락 여부를 결정해야 함. |
| `onPositionChanged`| `DropEvent drag` | -        | 드래그 중인 아이템이 `DropArea` 영역 내에서 위치를 변경할 때마다 발생.                                                               |
| `onDropped`       | `DropEvent drag` | -        | 사용자가 `DropArea` 영역 내에서 드래그를 종료(마우스/터치 떼기)했을 때 발생. `onEntered`에서 드롭이 수락된 경우에만 발생. **`drag.dropAction`을 통해 최종 결정된 액션을 확인하고 데이터를 처리합니다.** |
| `onExited`        | -              | -        | 드래그 중인 아이템이 `DropArea` 영역 밖으로 나갔을 때 발생.                                                                         |

**DropEvent (drag 파라미터) 주요 속성 및 메소드:**

*   `accepted`: (bool) 드롭이 수락되었는지 여부. `onEntered` 핸들러 등에서 설정.
*   `acceptedButtons`: (Qt.MouseButtons) 드롭을 시작한 마우스 버튼.
*   `dropAction`: (Qt.DropAction) 최종적으로 결정된 드롭 액션 (읽기 전용, `onDropped`에서 확인).
*   `proposedAction`: (Qt.DropAction) `DropArea`가 제안/수락한 드롭 액션. `onEntered`에서 설정 가능.
*   `supportedActions`: (Qt.DropActions) 드래그 소스가 지원하는 액션 목록 (읽기 전용).
*   `formats`: (list<string>) 드래그 소스가 제공하는 MIME 타입 목록 (읽기 전용).
*   `hasFormat(string format)`: (메소드) 특정 MIME 타입 데이터가 있는지 확인.
*   `hasText`, `hasUrls`, `hasHtml`, `hasColor`: (bool) 표준 MIME 타입 데이터 존재 여부 확인.
*   `text`, `urls`, `html`, `color`: 해당 표준 MIME 타입 데이터 접근.
*   `getData(string format)`: (메소드) 사용자 정의 MIME 타입 데이터 접근.
*   `x`, `y`: (real) `DropArea` 기준 드롭/드래그 위치.
*   `source`: (Item) 드래그 소스 아이템 (같은 QML 엔진 내 드래그인 경우).
*   `accept(Qt::DropAction action)`: (메소드) 특정 드롭 액션으로 드롭을 수락. `onEntered`에서 호출.
*   `acceptProposedAction()`: (메소드) 드래그 소스가 제안한 액션(기본값)으로 드롭을 수락. `onEntered`에서 호출.

## 예제

```qml
import QtQuick

Window {
    width: 400
    height: 300
    visible: true
    title: "DropArea Example"

    // 드래그 가능한 아이템 (Drag.md 예제와 유사)
    Rectangle {
        id: draggableItem
        x: 20; y: 20; width: 80; height: 80
        color: "lightblue"
        Text { anchors.centerIn: parent; text: "Drag Me" }
        MouseArea {
            id: dragArea
            anchors.fill: parent
            drag.target: draggableItem
            drag.mimeData: { "text/plain": "Hello from Draggable!", "application/x-item-id": "draggable1" }
            drag.supportedActions: Qt.CopyAction | Qt.MoveAction
            Drag.onDragFinished: (action) => { draggableItem.opacity = 1.0; if(action === Qt.MoveAction) draggableItem.visible = false; }
            Drag.onDragStarted: { draggableItem.opacity = 0.7; }
        }
    }

    // 드롭 영역
    DropArea {
        id: dropTarget
        anchors.right: parent.right
        anchors.bottom: parent.bottom
        anchors.margins: 20
        width: 150; height: 150

        Rectangle {
            id: dropVisual
            anchors.fill: parent
            color: parent.containsDrag ? "lightgreen" : "lightgray"
            border.color: parent.containsDrag ? "darkgreen" : "gray"
            Text {
                id: dropText
                anchors.centerIn: parent
                text: parent.containsDrag ? "Drop Here" : "Drop Area"
            }
        }

        // 가장 중요한 핸들러: 드래그 진입 시 수락 여부 결정
        onEntered: (drag) => {
            console.log("DropArea entered by drag source.");
            // 'text/plain' 데이터가 있고, 'Copy' 액션을 지원하면 수락
            if (drag.hasFormat("text/plain") && (drag.supportedActions & Qt.CopyAction)) {
                console.log("Accepting CopyAction.");
                drag.accept(Qt.CopyAction) // 명시적으로 복사 액션 수락
            } else if (drag.hasFormat("application/x-item-id") && (drag.supportedActions & Qt.MoveAction)) {
                console.log("Accepting MoveAction.");
                drag.accept(Qt.MoveAction) // 명시적으로 이동 액션 수락
            } else {
                console.log("Rejecting drag.");
                drag.accepted = false // 지원하지 않는 형식/액션이면 거절
            }
        }

        // 드롭 발생 시 처리
        onDropped: (drag) => {
            console.log("DropArea received drop! Action:", drag.dropAction);
            if (drag.hasText) {
                dropVisual.dropText.text = "Dropped:\n" + drag.text; // 드롭된 텍스트 표시
                dropVisual.color = "yellowgreen"
            }
            if (drag.hasFormat("application/x-item-id")){
                dropVisual.dropText.text = "Moved:\n" + drag.getData("application/x-item-id");
                dropVisual.color = "khaki"
            }
             // drag.dropAction (최종 액션)에 따라 추가 처리 가능
        }

        // 드래그 아이템이 영역을 벗어날 때 처리 (선택 사항)
        onExited: {
            console.log("Drag exited DropArea.");
            dropVisual.color = "lightgray" // 시각적 피드백 초기화
            dropVisual.dropText.text = "Drop Area"
        }
    }
}
```

## 참고 사항

*   `DropArea`는 드래그 앤 드롭의 수신 측 역할을 하며, **[`Drag` Attached Property](./Drag.md)는 송신 측 역할을 합니다.**
*   `onEntered` 핸들러에서 드롭을 수락(`drag.accept()` 또는 `drag.acceptProposedAction()`)하지 않으면 `onDropped` 시그널은 발생하지 않습니다.
*   `drag` 파라미터를 통해 드래그 소스가 제공하는 `mimeData`와 `supportedActions`를 확인하여 조건부로 드롭을 수락/거절하는 로직을 구현하는 것이 일반적입니다.
*   `containsDrag` 프로퍼티를 사용하여 드래그 중인 아이템이 영역 위에 있을 때 시각적 피드백(예: 배경색 변경)을 제공할 수 있습니다. 