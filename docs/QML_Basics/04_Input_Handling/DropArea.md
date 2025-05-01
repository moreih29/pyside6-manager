# DropArea

## 모듈 정보

```qml
import QtQuick
```

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
| `onContainsDragChanged` | - | - | `containsDrag` 프로퍼티 값이 변경될 때 발생. |

**DropEvent (drag 파라미터) 주요 속성 및 메소드:**

*   `accepted`: (bool) 드롭이 수락되었는지 여부 (`accept()` 메소드 호출 결과 반영, 읽기 전용).
*   `acceptedButtons`: (Qt.MouseButtons) 드롭을 시작한 마우스 버튼.
*   `dropAction`: (Qt.DropAction) 최종적으로 결정된 드롭 액션 (읽기 전용, `onDropped`에서 확인).
*   `proposedAction`: (Qt.DropAction) `DropArea`가 제안/수락한 드롭 액션. `onEntered`에서 설정 가능.
*   `supportedActions`: (Qt.DropActions) 드래그 소스가 지원하는 액션 목록 (읽기 전용).
*   `formats`: (list<string>) 드래그 소스가 제공하는 MIME 타입 목록 (읽기 전용).
*   `keys`: (list<string>) 드롭을 수락하기 위해 필요한 특정 키(MIME 타입 식별자 등). `DropArea`의 `keys` 프로퍼티와 관련 (고급). (읽기 전용)
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
import QtQuick.Window 2.15

Window {
    width: 450
    height: 350
    visible: true
    title: "Robust DropArea Example - Revised Drag Source"

    Column {
        anchors.centerIn: parent
        spacing: 20

        Rectangle {
            id: draggableItem
            width: 100; height: 80
            color: dragHandler.active ? "steelblue" : "lightblue"
            border.color: "gray"

            Drag.mimeData: {
                "text/plain": "Text data from source (via DragHandler)",
                "application/x-mydata": { "value": 42, "label": "Custom Data (via DragHandler)" }
            }
            Drag.supportedActions: Qt.CopyAction | Qt.MoveAction

            Text { anchors.centerIn: parent; text: "Drag Me" }

            DragHandler {
                id: dragHandler
                target: draggableItem

                onGrabChanged: (transition, point) => {
                    if (transition === PointerDevice.GrabExclusive) {
                        draggableItem.opacity = 0.7;
                        draggableItem.z = 1;
                        console.log("[DragHandler] Grab acquired (Drag likely started).");
                        draggableItem.Drag.active = true;
                    } else if (transition === PointerDevice.UngrabExclusive || transition === PointerDevice.CancelGrabExclusive) {
                        var finalAction = Qt.IgnoreAction;
                        console.log("[DragHandler] Grab released/canceled (Drag finished). Guessed Action:", finalAction);
                        draggableItem.opacity = 1.0;
                        draggableItem.z = 0;
                        draggableItem.Drag.active = false;

                        if (finalAction === Qt.MoveAction) {
                            draggableItem.visible = false;
                            console.log("[DragHandler] Original item hidden due to MoveAction.");
                        }
                    }
                }
            }
        }

        DropArea {
            id: dropAreaTarget
            width: 200; height: 150

            property string statusText: "Drop Area"
            property color areaColor: "lightgray"
            property bool itemDropped: false
            property int lastAcceptedAction: Qt.IgnoreAction

            Rectangle {
                id: dropVisualRect
                anchors.fill: parent
                color: dropAreaTarget.containsDrag ? "palegreen" : dropAreaTarget.areaColor
                border.color: dropAreaTarget.containsDrag ? "darkgreen" : "gray"
                border.width: 2
                radius: 5

                Text {
                    anchors.centerIn: parent
                    horizontalAlignment: Text.AlignHCenter
                    text: dropAreaTarget.containsDrag ? "Release to Drop" : dropAreaTarget.statusText
                }
            }

            onEntered: (drag) => {
                console.log("[DropArea] Entered. Formats:", drag.formats, "Supported Actions:", drag.supportedActions);
                dropAreaTarget.itemDropped = false;
                dropAreaTarget.lastAcceptedAction = Qt.IgnoreAction;

                var formatsList = drag.formats;

                if (formatsList.indexOf("text/plain") !== -1 && (drag.supportedActions & Qt.CopyAction)) {
                    console.log("[DropArea] Accepting CopyAction for text/plain.");
                    dropAreaTarget.lastAcceptedAction = Qt.CopyAction;
                    drag.accept(Qt.CopyAction);
                }
                else if (formatsList.indexOf("application/x-mydata") !== -1 && (drag.supportedActions & Qt.MoveAction)) {
                    console.log("[DropArea] Accepting MoveAction for application/x-mydata.");
                    dropAreaTarget.lastAcceptedAction = Qt.MoveAction;
                    drag.accept(Qt.MoveAction);
                }
                else {
                    console.log("[DropArea] Rejecting drag (unsupported format or action).");
                }
            }

            onDropped: (drag) => {
                console.log("[DropArea] Dropped. Final Action:", drag.action);
                dropAreaTarget.itemDropped = true;

                if (drag.action === Qt.CopyAction && drag.formats.indexOf("text/plain") !== -1) {
                    dropAreaTarget.statusText = "Copied:\n" + drag.text;
                    dropAreaTarget.areaColor = "lightyellow";
                    console.log("[DropArea] Processed dropped text:", drag.text);
                }
                else if (drag.action === Qt.MoveAction && drag.formats.indexOf("application/x-mydata") !== -1) {
                    var sourceItem = drag.source;
                    if (sourceItem && sourceItem.Drag && sourceItem.Drag.mimeData) {
                        var customData = sourceItem.Drag.mimeData["application/x-mydata"];
                        if (customData) {
                            dropAreaTarget.statusText = "Moved:\nLabel: " + customData.label + "\nValue: " + customData.value;
                            dropAreaTarget.areaColor = "lightpink";
                            console.log("[DropArea] Processed dropped custom data:", JSON.stringify(customData));
                        } else {
                            dropAreaTarget.statusText = "Move Error!\n(Custom Data Missing)";
                            dropAreaTarget.areaColor = "orangered";
                            console.warn("[DropArea] Could not retrieve custom data for MoveAction (mimeData invalid?).");
                        }
                    } else {
                        dropAreaTarget.statusText = "Move Error!\n(Source Invalid?)";
                        dropAreaTarget.areaColor = "orangered";
                        console.warn("[DropArea] Could not retrieve source item or its mimeData for MoveAction.");
                    }
                }
                else {
                    dropAreaTarget.statusText = "Drop Error!";
                    dropAreaTarget.areaColor = "orangered";
                    console.warn("[DropArea] Drop occurred but action/data mismatch. Final Action:", drag.action, "Formats:", drag.formats);
                }
            }

            onExited: {
                console.log("[DropArea] Exited.");
                dropAreaTarget.lastAcceptedAction = Qt.IgnoreAction;
            }

            onContainsDragChanged: {
                console.log("[DropArea] containsDrag changed to:", containsDrag);
            }
        }
    }
}
```

## 참고 사항

*   `DropArea`는 드래그 앤 드롭의 수신 측 역할을 하며, **[`Drag` Attached Property](./Drag.md)는 송신 측 역할을 합니다.**
*   `onEntered` 핸들러에서 드롭을 수락(`drag.accept()` 또는 `drag.acceptProposedAction()`)하지 않으면 `onDropped` 시그널은 발생하지 않습니다.
*   `drag` 파라미터를 통해 드래그 소스가 제공하는 `mimeData`와 `supportedActions`를 확인하여 조건부로 드롭을 수락/거절하는 로직을 구현하는 것이 일반적입니다.
*   `containsDrag` 프로퍼티를 사용하여 드래그 중인 아이템이 영역 위에 있을 때 시각적 피드백(예: 배경색 변경)을 제공할 수 있습니다.

## 공식 문서 링크

*   [Qt Quick DropArea QML Type](https://doc.qt.io/qt-6/qml-qtquick-droparea.html) 