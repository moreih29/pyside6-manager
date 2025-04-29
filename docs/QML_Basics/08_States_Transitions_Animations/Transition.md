# Transition

**모듈:** `import QtQuick`

## 개요

`Transition` 요소는 QML `Item`의 상태(`state`)가 변경될 때 적용될 애니메이션이나 스크립트를 정의하는 데 사용됩니다. `State`만 사용하면 상태 변경 시 프로퍼티 값이 즉시 변경되지만, `Transition`을 사용하면 프로퍼티 값이 부드럽게 변경되는 시각적 효과를 줄 수 있습니다.

`Transition`은 `Item`의 `transitions` 리스트 프로퍼티 내에 정의되며, 각 `Transition`은 특정 상태 변경(예: 상태 'A'에서 상태 'B'로 변경)에 대응합니다.

## 사용 방법

`Transition` 요소는 `Item`의 `transitions` 프로퍼티 내에 리스트 형태로 정의됩니다. 각 `Transition`은 어떤 상태 변화(`from`, `to`)에 적용될지와 어떤 애니메이션(`NumberAnimation`, `SequentialAnimation` 등) 또는 스크립트(`ScriptAction`)를 실행할지를 지정합니다.

```qml
import QtQuick

Item {
    id: container
    width: 200; height: 100

    states: [
        State {
            name: "expanded"
            PropertyChanges { target: rect; width: 180; height: 80; color: "lightblue" }
        },
        State {
            name: "collapsed"
            PropertyChanges { target: rect; width: 100; height: 40; color: "lightcoral" }
        }
    ]

    // 초기 상태
    state: "collapsed"

    // 상태 전환 애니메이션 정의
    transitions: [
        Transition {
            // 모든 상태("*", 와일드카드)에서 "expanded" 상태로 변경될 때
            from: "*"
            to: "expanded"
            // 여러 애니메이션을 병렬로 실행
            ParallelAnimation {
                NumberAnimation { target: rect; properties: "width, height"; duration: 300; easing.type: Easing.InOutQuad }
                ColorAnimation { target: rect; property: "color"; duration: 300 }
            }
        },
        Transition {
            // "expanded" 상태에서 "collapsed" 상태로 변경될 때
            from: "expanded"
            to: "collapsed"
            // 순차 애니메이션 예시 (폭/높이 먼저 줄이고, 색상 변경)
            SequentialAnimation {
                NumberAnimation { target: rect; properties: "width, height"; duration: 250; easing.type: Easing.OutQuad }
                ColorAnimation { target: rect; property: "color"; duration: 100 }
            }
        },
        Transition {
            // 기본 상태("")에서 "collapsed" 상태로 변경될 때 (초기화 등)
            from: ""
            to: "collapsed"
            // 여기서는 애니메이션 없이 즉시 변경 (정의하지 않으면 기본값)
        }
    ]

    Rectangle {
        id: rect
        // 위치는 고정 (여기서는 중앙 정렬)
        anchors.centerIn: parent
        // 초기 크기 및 색상 (collapsed 상태와 동일하게 설정)
        width: 100; height: 40
        color: "lightcoral"
        radius: 5
    }

    MouseArea {
        anchors.fill: parent
        onClicked: {
            // 클릭 시 상태 토글
            container.state = (container.state === "collapsed" ? "expanded" : "collapsed")
        }
    }
}
```

## 주요 프로퍼티 (`Transition` 요소의 프로퍼티)

| 이름        | 타입            | 기본값 | 설명                                                                                                                                 |
| :---------- | :-------------- | :----- | :----------------------------------------------------------------------------------------------------------------------------------- |
| `from`      | `string`        | `"*"` | 이 전환이 적용될 시작 상태의 이름. 와일드카드(`"*"`)는 모든 상태를 의미합니다. 기본 상태는 빈 문자열(`""`)로 표현됩니다.                               |
| `to`        | `string`        | `"*"` | 이 전환이 적용될 목표 상태의 이름. 와일드카드(`"*"`)는 모든 상태를 의미합니다.                                                              |
| `reversible`| `bool`          | `false`| `true`로 설정하면, `to` 상태에서 `from` 상태로 돌아갈 때 이 전환에 정의된 애니메이션이 반대 방향으로 자동으로 적용됩니다. 양방향 전환을 간단하게 정의할 때 유용합니다. |
| `animations`| `list<Animation>`| `[]`   | (읽기 전용) 이 전환에 포함된 애니메이션 객체들의 리스트.                                                                               |

## 포함될 수 있는 요소

`Transition` 내부에는 다음과 같은 요소들을 배치하여 전환 동작을 정의합니다.

*   **애니메이션 요소**: 상태 변경 시 프로퍼티 값을 부드럽게 변경합니다.
    *   `PropertyAnimation`, `NumberAnimation`, `ColorAnimation`, `RotationAnimation`, `ScaleAnimation`, `Vector3dAnimation` 등
*   **애니메이션 그룹**: 여러 애니메이션을 조합합니다.
    *   `SequentialAnimation`: 포함된 애니메이션들을 순서대로 실행합니다.
    *   `ParallelAnimation`: 포함된 애니메이션들을 동시에 실행합니다.
*   **스크립트 액션**: 전환 도중 JavaScript 코드를 실행합니다.
    *   `ScriptAction`: `script` 프로퍼티에 실행할 코드를 작성합니다.
*   **애니메이션 제어**: 애니메이션 흐름을 제어합니다.
    *   `PauseAnimation`: 지정된 시간(`duration`) 동안 애니메이션을 일시 정지합니다.

## 참고 사항

*   `Transition`은 `Item`의 `transitions` 리스트 프로퍼티 내에 정의됩니다.
*   `from`과 `to` 프로퍼티를 사용하여 어떤 상태 변화에 이 전환을 적용할지 지정합니다. 와일드카드(`"*"`)를 사용하면 더 일반적인 전환을 정의할 수 있습니다.
*   가장 구체적인 `from`/`to` 조합을 가진 `Transition`이 우선적으로 적용됩니다 (예: `from: "stateA", to: "stateB"` 가 `from: "*", to: "stateB"` 보다 우선).
*   `Transition` 내부에는 하나 이상의 애니메이션 요소(`NumberAnimation`, `ParallelAnimation` 등)나 `ScriptAction`을 배치하여 전환 효과를 구현합니다.
*   애니메이션 요소 내에서는 `target`, `properties` (또는 `property`), `duration`, `easing` 등의 프로퍼티를 설정하여 애니메이션 대상과 방식을 지정합니다.
*   `reversible: true`를 설정하면 반대 방향 상태 전환(예: `stateB` -> `stateA`)에 대한 `Transition`을 별도로 정의할 필요 없이, 정의된 애니메이션이 자동으로 역방향으로 실행됩니다.
*   `Transition`이 정의되지 않은 상태 변경은 즉시 발생합니다 (애니메이션 없음). 