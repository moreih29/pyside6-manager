# State

## 모듈 정보

```qml
import QtQuick
```

## 개요

`State` 요소는 QML `Item`이 가질 수 있는 특정 상태를 정의하는 데 사용됩니다. 아이템은 여러 개의 상태를 가질 수 있으며, 각 상태는 아이템의 특정 프로퍼티 값이나 구성을 나타냅니다.

예를 들어, 버튼은 'normal', 'pressed', 'hovered' 상태를 가질 수 있으며, 각 상태마다 다른 배경색이나 크기를 가질 수 있습니다. 상태는 아이템의 `states` 리스트 프로퍼티 내에 정의되며, `state` 프로퍼티를 변경하여 현재 활성화된 상태를 전환합니다.

## 사용 방법

`State` 요소는 `Item`의 `states` 프로퍼티 내에 리스트 형태로 정의됩니다. 각 `State`는 `name` 프로퍼티를 통해 고유한 이름을 가집니다. 기본 상태(아이템이 처음 로드될 때의 상태)는 `state` 프로퍼티의 초기값(기본값: `""`)으로 정의되거나, `State`의 `when` 프로퍼티를 통해 조건부로 활성화될 수 있습니다.

```qml
import QtQuick

// Window를 최상위 요소로 사용하여 단독 실행 가능하게 함
Window {
    width: 200; height: 150 // 내용 표시에 충분한 크기
    visible: true
    title: "State Example"

    Item {
        id: container
        anchors.fill: parent // Window 크기에 맞춤

        // 상태 리스트 정의
        states: [
            State {
                name: "state1" // 상태 이름
                // 이 상태일 때 변경될 프로퍼티 정의
                PropertyChanges { target: rect; color: "lightblue" }
                PropertyChanges { target: label; text: "State 1 Active" }
            },
            State {
                name: "state2"
                PropertyChanges { target: rect; color: "lightgreen" }
                PropertyChanges { target: label; text: "State 2 Active" }
            },
            // 조건부 상태 (when 프로퍼티 사용)
            State {
                name: "hovered"
                when: mouseArea.containsMouse // 마우스가 위에 있을 때 자동으로 활성화
                PropertyChanges { target: rect; border.color: "red"; border.width: 2 }
            }
        ]

        // 초기 상태 설정 (선택 사항, 기본값 "")
        // state: "state1"

        Rectangle {
            id: rect
            width: 180; height: 80 // 크기 조정
            anchors.centerIn: parent
            color: "gray" // 기본 상태의 색상
            border.color: "transparent"
            radius: 4
        }

        Text {
            id: label
            anchors.centerIn: rect // Rectangle 중앙에 배치
            text: "Default State"
        }

        MouseArea {
            id: mouseArea
            anchors.fill: rect // Rectangle 영역만 반응하도록 수정
            hoverEnabled: true // when 조건 사용 위해 hover 활성화
            onClicked: {
                // 클릭 시 상태 전환 (hovered 상태는 when 조건에 의해 관리됨)
                if (container.state === "state1") {
                    container.state = "state2"
                } else {
                    container.state = "state1"
                }
            }
        }
    }
}
```

## 주요 프로퍼티 (`State` 요소의 프로퍼티)

| 이름           | 타입    | 기본값 | 설명                                                                                                                                 |
| :------------- | :------ | :----- | :----------------------------------------------------------------------------------------------------------------------------------- |
| `name`         | `string`| ""   | 상태의 고유한 이름. `Item`의 `state` 프로퍼티에서 이 이름을 사용하여 상태를 전환합니다.                                                  |
| `when`         | `bool`  | `false`| 이 상태가 활성화될 조건. 이 값이 `true`가 되면 `Item`의 `state` 프로퍼티가 자동으로 이 상태의 `name`으로 설정됩니다. 조건부 상태 정의에 사용됩니다. |
| `extend`       | `string`| ""   | (고급) 다른 상태를 상속받을 때 사용. 상속받는 상태의 `PropertyChanges` 등을 포함합니다.                                                  |
| `changes`      | `list<Change>` | `[]` | (기본 프로퍼티) 이 상태에 적용될 변경 사항(`PropertyChanges`, `StateChangeScript`, `ParentChange` 등) 목록. `extend`된 상태의 변경 사항 위에 적용됩니다. |

## 관련 요소

*   **`PropertyChanges`**: 특정 상태가 활성화될 때 대상 객체(`target`)의 프로퍼티 값을 어떻게 변경할지 정의합니다.
    *   `target`: 프로퍼티를 변경할 대상 아이템 (`id` 사용).
    *   `프로퍼티 이름`: 변경할 프로퍼티의 이름과 목표 값을 지정합니다 (예: `color: "red"`, `width: 200`).
    *   `explicit`: (고급) `true`로 설정하면 해당 프로퍼티가 이 `PropertyChanges`에서 명시적으로 설정되었음을 나타냅니다. 상태 복원 동작에 영향을 줄 수 있습니다.
    *   `restoreEntryValues`: (고급) 상태에서 나갈 때 프로퍼티 값을 이전 상태의 값으로 복원할지 여부를 제어합니다.

*   **`StateChangeScript`**: 상태가 활성화되거나 비활성화될 때 JavaScript 코드를 실행합니다.
    *   `script`: 실행할 JavaScript 코드 블록.
    *   `name`: (선택 사항) 스크립트의 이름.

*   **`ParentChange`**: 상태 변경 시 아이템의 부모를 변경합니다.
    *   `target`: 부모를 변경할 대상 아이템.
    *   `parent`: 새로운 부모 아이템.
    *   `x`, `y`, `width`, `height`: 새로운 부모 좌표계에서의 위치 및 크기.

*   **`AnchorChanges`**: 상태 변경 시 아이템의 앵커(`anchors`)를 변경합니다.
    *   `target`: 앵커를 변경할 대상 아이템.
    *   앵커 프로퍼티 (`anchors.left`, `anchors.right`, `anchors.fill` 등): 새로운 앵커 설정을 지정합니다.

## 참고 사항

*   상태는 `Item` (또는 그 하위 클래스)의 `states` 프로퍼티 내에 정의됩니다.
*   `Item`의 `state` 프로퍼티 값을 변경하여 상태를 전환합니다. 기본 상태는 `state`가 `""` (빈 문자열)인 상태입니다.
*   `PropertyChanges`를 사용하여 특정 상태일 때 아이템들의 프로퍼티 값을 지정합니다. 대상 아이템은 `target` 프로퍼티에 `id`로 지정합니다.
*   `when` 프로퍼티를 사용하면 특정 조건(예: 마우스 호버, 포커스)에 따라 상태가 자동으로 변경되도록 할 수 있습니다. `when` 조건이 만족되지 않으면 `state`는 이전 상태 또는 기본 상태(`""`)로 돌아갑니다.
*   상태 변경 시 애니메이션 효과를 주려면 `Transition` 요소를 사용합니다. `State` 자체는 프로퍼티 값을 즉시 변경합니다.
*   복잡한 상태 관리나 상태 변경 시 특정 로직 실행이 필요할 경우 `StateChangeScript`를 사용할 수 있습니다.
*   `ParentChange`나 `AnchorChanges`를 사용하면 상태에 따라 아이템의 부모나 레이아웃을 동적으로 변경할 수 있습니다.
*   [State QML Type ](https://doc.qt.io/qt-6/qml-qtquick-state.html) 