# Item

`Item`은 Qt Quick의 모든 시각적 요소(Visual Item)의 가장 기본적인 기반 클래스입니다. 자체적으로는 화면에 아무것도 그리지 않지만, 다른 모든 시각적 요소들이 공통적으로 가지는 핵심적인 속성들과 기능들을 제공합니다.

## 모듈 정보

```qml
import QtQuick 2.15 // 또는 사용하는 Qt Quick 버전
```

## 개요

`Item`은 화면 상의 위치(`x`, `y`), 크기(`width`, `height`), 가시성(`visible`), 투명도(`opacity`) 등 기본적인 시각적 속성을 정의합니다. 또한, 자식 아이템들을 포함하고 관리(`children`, `data` 프로퍼티)하며, 키보드 포커스 처리(`focus`, `activeFocus`), 좌표 변환(`mapToItem`, `mapFromItem`), 상태 관리(`states`), 변형(`transform`) 등 다양한 기능을 위한 기반을 제공합니다.

`Rectangle`, `Text`, `Image` 등 화면에 실제로 무언가를 그리는 컴포넌트들은 모두 `Item`을 직간접적으로 상속받습니다. 따라서 `Item`의 프로퍼티와 시그널은 대부분의 다른 시각적 QML 타입에서도 사용할 수 있습니다.

## 기반 클래스

`QtObject`

## 주요 프로퍼티

| 이름             | 타입          | 기본값              | 설명                                                                                                  |
| :--------------- | :------------ | :------------------ | :---------------------------------------------------------------------------------------------------- |
| `x`, `y`         | `real`        | `0`                 | 부모 좌표계 기준 아이템의 좌상단 위치입니다.                                                                       |
| `width`, `height`| `real`        | `0`                 | 아이템의 너비와 높이입니다.                                                                               |
| `z`              | `real`        | `0`                 | Z-축 순서. 값이 높을수록 다른 아이템 위에 그려집니다. 동일 `z` 값에서는 나중에 선언된 아이템이 위에 그려집니다.                               |
| `visible`        | `bool`        | `true`              | 아이템의 가시성 여부입니다. `false`이면 화면에 그려지지 않고 입력 이벤트도 받지 않습니다.                                                    |
| `opacity`        | `real`        | `1.0`               | 아이템의 불투명도 (0.0: 완전 투명, 1.0: 완전 불투명).                                                               |
| `enabled`        | `bool`        | `true`              | 아이템의 활성화 여부. `false`이면 일반적으로 사용자 입력(예: 마우스 클릭)을 받지 않으며 시각적으로 비활성화 상태로 보일 수 있습니다.                               |
| `rotation`       | `real`        | `0`                 | 아이템의 회전 각도 (도 단위). `transform` 프로퍼티와 함께 사용될 수 있습니다.                                                     |
| `scale`          | `real`        | `1.0`               | 아이템의 크기 배율. `transform` 프로퍼티와 함께 사용될 수 있습니다.                                                          |
| `clip`           | `bool`        | `false`             | `true`이면 자식 아이템들이 이 아이템의 경계를 벗어나 그려지지 않도록 잘라냅니다(클리핑). 성능에 영향을 줄 수 있습니다.                                       |
| `focus`          | `bool`        | `false`             | 아이템이 키보드 포커스를 가질 수 있는지 여부. `true`로 설정하고 가시 상태여야 포커스를 받을 수 있습니다.                                           |
| `activeFocus`    | `readonly bool`| `false`             | 아이템이 현재 *실제로* 활성 키보드 포커스를 가지고 있는지 여부입니다.                                                               |
| `children`       | `readonly list<Item>` | `[]`            | 이 아이템의 직계 자식 아이템들의 리스트입니다.                                                                          |
| `data`           | `default list<Object>` | `[]`           | `Item`의 기본 프로퍼티. `Item { ... }` 내부에 선언된 객체(주로 자식 아이템)들이 이 리스트에 추가됩니다.                                        |
| `parent`         | `Item`        | (부모 아이템)        | 이 아이템의 부모 아이템에 대한 참조입니다.                                                                            |
| `states`         | `list<State>` | `[]`                | 아이템이 가질 수 있는 여러 상태(`State`) 객체들의 리스트입니다. 상태 기반 UI 변경에 사용됩니다.                                                |
| `state`          | `string`      | `""`              | 현재 아이템의 활성 상태 이름입니다. `states` 리스트에 정의된 `State` 객체의 `name` 프로퍼티 값 중 하나로 설정합니다.                                  |
| `transitions`    | `list<Transition>` | `[]`            | 상태 변경 시 적용될 애니메이션 효과(`Transition`) 객체들의 리스트입니다.                                                             |
| `transform`      | `list<Transform>` | `[]`            | 아이템에 적용될 변형(Transform: 이동, 회전, 크기 조절 등) 객체들의 리스트입니다.                                                        |
| `anchors`        | `QtObject`    | (앵커 객체)        | 다른 아이템과의 상대적인 위치 관계를 설정하는 앵커 라인(left, right, top, bottom, centerIn, fill 등)들을 관리하는 객체입니다.                            |
| `childrenRect`   | `readonly QtObject` | (자식 경계 객체)  | 모든 자식 아이템들을 포함하는 경계 사각형의 정보를 담고 있는 객체 (`x`, `y`, `width`, `height` 프로퍼티 가짐).                               |
| `implicitWidth`, `implicitHeight` | `real` | `0`           | 아이템의 내용(예: 텍스트, 이미지)에 기반한 자연스러운 크기입니다. 레이아웃 시스템에서 크기 계산에 사용될 수 있습니다.                                    |

## 주요 시그널

| 이름                     | 파라미터 | 반환타입 | 설명                                                                   |
| :----------------------- | :------- | :------- | :--------------------------------------------------------------------- |
| `<propertyName>Changed`  | -        | -        | 해당 프로퍼티(`x`, `y`, `width`, `height`, `visible`, `opacity` 등) 값이 변경될 때 발생합니다. |
| `focusChanged`           | -        | -        | `focus` 프로퍼티 값이 변경될 때 발생합니다.                                               |
| `activeFocusChanged`     | -        | -        | `activeFocus` 프로퍼티 값이 변경될 때 발생합니다.                                          |
| `parentChanged`          | -        | -        | `parent` 프로퍼티 값이 변경될 때 발생합니다.                                              |
| `stateChanged`           | -        | -        | `state` 프로퍼티 값이 변경될 때 발생합니다.                                               |
| `childrenRectChanged`    | -        | -        | `childrenRect` 프로퍼티 값이 변경될 때 발생합니다.                                         |

## 주요 메소드

| 이름             | 파라미터                      | 반환타입 | 설명                                                                                                                               |
| :--------------- | :---------------------------- | :------- | :--------------------------------------------------------------------------------------------------------------------------------- |
| `mapToItem`      | `item: Item`, `point: QPointF` | `QPointF`| 이 아이템 좌표계의 점(`point`)을 다른 `item`의 좌표계로 변환합니다. `mapToItem(null, ...)`은 씬(Scene) 좌표계로 변환합니다.                                       |
| `mapFromItem`    | `item: Item`, `point: QPointF` | `QPointF`| 다른 `item` 좌표계의 점(`point`)을 이 아이템의 좌표계로 변환합니다. `mapFromItem(null, ...)`은 씬 좌표계의 점을 이 아이템 좌표계로 변환합니다.                             |
| `forceActiveFocus()`| -                             | `void`   | 아이템이 `focus: true`이고 `visible: true`일 때, 해당 아이템에 강제로 키보드 포커스를 설정하려고 시도합니다.                                                               |

## 예제

```qml
import QtQuick 2.15
import QtQuick.Window 2.15 // Window 사용을 위해 추가

Window { // 예제를 감싸는 Window 추가
    width: 300
    height: 200
    visible: true // Window를 보이게 설정
    title: "Item Example"

    Item { // 기존 루트 Item (이제 Window의 자식)
        id: rootItem
        anchors.fill: parent // Window를 채우도록 변경
        focus: true // 루트 아이템이 포커스를 받을 수 있도록 설정

        Item { // 첫 번째 자식 Item
            id: childItem1
            x: 10; y: 10
            width: 100; height: 50
            // 이 Item은 아무것도 그리지 않음. 영역만 차지.

            Rectangle { // childItem1의 자식
                anchors.fill: parent // 부모(childItem1)를 채움
                color: "lightblue"
            }
        }

        Item { // 두 번째 자식 Item
            id: childItem2
            // anchors를 이용한 위치 지정
            anchors.top: childItem1.bottom
            anchors.topMargin: 10
            anchors.left: parent.left // 여기서 parent는 rootItem을 의미
            anchors.leftMargin: 10
            width: 150; height: 80
            rotation: 10 // 회전
            scale: 0.8   // 크기 축소
            opacity: 0.7 // 반투명
            clip: true   // 자식 클리핑 활성화
            focus: true  // 포커스 가능

            Rectangle { // childItem2의 자식
                anchors.fill: parent
                color: childItem2.activeFocus ? "orange" : "lightgreen" // 활성 포커스 상태에 따라 색 변경
                border.color: "black"
            }

            Text { // childItem2의 다른 자식
                text: "Clipped Text"
                anchors.centerIn: parent
                x: 20 // 클리핑 때문에 일부만 보일 수 있음
            }

            // childItem2의 activeFocus 변경 시그널 핸들러
            onActiveFocusChanged: {
                console.log("childItem2 activeFocus:", activeFocus)
            }
        }

        // Keys 이벤트 핸들러는 포커스를 가진 Item에서 처리하는 것이 일반적이므로,
        // rootItem 또는 childItem2 내부에 두는 것이 더 명확할 수 있습니다.
        // 여기서는 Window 레벨이 아닌 rootItem에 유지합니다.
        Keys.onPressed: (event) => { // 루트 아이템에서 키 이벤트 처리
            if (event.key === Qt.Key_Tab) {
                // Tab 키를 누르면 childItem2에 포커스 강제 설정 시도
                childItem2.forceActiveFocus()
                event.accepted = true // 이벤트 처리 완료
            }
        }
    }
}
```

## 참고 사항

*   **추상적 개념**: `Item` 자체는 시각적 표현이 없으므로, 화면에 무언가를 표시하려면 `Rectangle`, `Text`, `Image` 등 `Item`을 상속받은 구체적인 컴포넌트를 사용해야 합니다.
*   **기본 컨테이너**: `Item`은 다른 아이템들을 그룹화하고 배치하기 위한 기본적인 컨테이너로 자주 사용됩니다.
*   **성능**: 불필요한 `Item` 중첩은 성능에 영향을 줄 수 있습니다. 가능한 플랫한 구조를 유지하는 것이 좋습니다.

## 공식 문서 링크

*   [Qt Quick Item QML Type](https://doc.qt.io/qt-6/qml-qtquick-item.html) 