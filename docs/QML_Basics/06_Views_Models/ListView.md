# ListView

**모듈:** `import QtQuick`

## 개요

`ListView`는 모델(model)의 데이터를 목록 형태로 표시하는 데 사용되는 가장 기본적인 뷰(view) 컴포넌트입니다. 항목들을 수직 또는 수평으로 나열하며, 각 항목의 시각적 표현은 델리게이트(delegate)를 통해 정의됩니다.

`ListView`는 내장된 `Flickable` 기능을 통해 스크롤을 지원하며, 화면에 보이는 영역의 항목들만 생성하고 관리하여 많은 수의 데이터를 효율적으로 처리할 수 있습니다.

## 기반 클래스

*   `Flickable` (스크롤 기능 제공)

## 주요 프로퍼티

| 이름                | 타입            | 기본값          | 설명                                                                                                                                                              |
| :------------------ | :-------------- | :-------------- | :---------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `model`             | `any`           | `null`          | 뷰에 표시할 데이터 모델. `ListModel`, JavaScript 배열/객체, 숫자(개수), C++ 모델 등을 사용할 수 있습니다.                                                               |
| `delegate`          | `Component`     | `null`          | 모델의 각 항목을 시각적으로 표현하는 QML 컴포넌트. 델리게이트 내에서는 `index`(항목 인덱스) 및 모델 데이터(예: `modelData`, 역할 이름)에 접근할 수 있습니다.             |
| `orientation`       | `enumeration`   | `Qt.Vertical`   | 목록의 방향 (`ListView.Vertical` 또는 `ListView.Horizontal`).                                                                                                       |
| `count`             | `int`           | (읽기 전용)     | 모델에 포함된 항목의 총 개수 (`model` 프로퍼티에서 파생됨).                                                                                                         |
| `currentIndex`      | `int`           | -1              | 현재 선택된 항목의 인덱스. `-1`은 선택된 항목이 없음을 의미합니다.                                                                                                   |
| `currentItem`       | `Item`          | (읽기 전용)     | 현재 선택된 항목에 해당하는 델리게이트 아이템.                                                                                                                   |
| `spacing`           | `real`          | 0               | 각 델리게이트 아이템 사이의 간격 (픽셀 단위).                                                                                                                       |
| `header`            | `Component`     | `null`          | 목록의 시작 부분(수직 목록의 경우 위쪽, 수평 목록의 경우 왼쪽)에 표시될 컴포넌트.                                                                                         |
| `footer`            | `Component`     | `null`          | 목록의 끝 부분(수직 목록의 경우 아래쪽, 수평 목록의 경우 오른쪽)에 표시될 컴포넌트.                                                                                         |
| `section`           | `object`        | (읽기 전용)     | 목록 섹션 관련 프로퍼티 및 메서드를 포함하는 객체 (`section.property`, `section.criteria`, `section.delegate`, `section.labelPositioning`). 항목들을 특정 기준으로 그룹화하는 데 사용됩니다. |
| `snapMode`          | `enumeration`   | `NoSnap`        | 스크롤이 멈출 때 델리게이트 경계에 맞춰지는 방식 (`ListView.NoSnap`, `ListView.SnapToItem`, `ListView.SnapOneItem`).                                                      |
| `highlight`         | `Component`     | `null`          | 현재 선택된 항목(`currentItem`)을 시각적으로 강조하는 컴포넌트.                                                                                                      |
| `highlightRangeMode`| `enumeration`   | `StrictlyEnforceRange` | `highlight` 컴포넌트가 뷰 경계를 벗어나 표시될 수 있는지 여부 (`ListView.StrictlyEnforceRange`, `ListView.ApplyRange`).                                                    |
| `cacheBuffer`       | `real`          | (플랫폼 의존)   | 뷰포트 외부에서 미리 생성하고 캐시할 델리게이트의 양 (픽셀 단위). 스크롤 성능을 향상시킬 수 있지만 메모리 사용량이 증가합니다.                                                 |
| `reuseItems`        | `bool`          | `true` (Qt 6.0+) | (Qt 6.0 이상) 화면 밖으로 나간 델리게이트 아이템을 재사용할지 여부. 성능 향상에 중요합니다.                                                                            |
| `clip`              | `bool`          | `false`         | `Flickable`에서 상속. `true`로 설정하면 뷰 경계 밖의 내용을 그리지 않습니다. 델리게이트가 뷰 크기를 벗어나는 경우 `true`로 설정하는 것이 일반적입니다.                       |
| `contentWidth`      | `real`          | (읽기 전용)     | `Flickable`에서 상속. 내용의 전체 너비.                                                                                                                             |
| `contentHeight`     | `real`          | (읽기 전용)     | `Flickable`에서 상속. 내용의 전체 높이.                                                                                                                             |

## 주요 시그널

| 이름                   | 파라미터 | 설명                                                                 |
| :--------------------- | :------- | :------------------------------------------------------------------- |
| `currentIndexChanged`  |          | `currentIndex` 프로퍼티가 변경될 때 발생합니다.                      |
| `currentItemChanged`   |          | `currentItem` 프로퍼티가 변경될 때 발생합니다.                     |
| `countChanged`         |          | `count` 프로퍼티가 변경될 때 발생합니다.                               |
| `clicked(index)`       | `int`    | (Qt 6.2+) 사용자가 델리게이트를 클릭했을 때 발생합니다. 클릭된 인덱스가 전달됩니다. |
| `pressAndHold(index)`  | `int`    | (Qt 6.2+) 사용자가 델리게이트를 길게 눌렀을 때 발생합니다.                 |
| `movementStarted`      |          | `Flickable`에서 상속. 스크롤(이동)이 시작될 때 발생합니다.             |
| `movementEnded`        |          | `Flickable`에서 상속. 스크롤(이동)이 끝났을 때 발생합니다.               |
| `add`                  |          | 뷰에 델리게이트가 추가될 때의 트랜지션(transition)을 정의하는 시그널. |
| `remove`               |          | 뷰에서 델리게이트가 제거될 때의 트랜지션(transition)을 정의하는 시그널. |
| `move`                 |          | 뷰 내에서 델리게이트가 이동할 때의 트랜지션(transition)을 정의하는 시그널. |

## 주요 메소드

| 이름                             | 파라미터                     | 반환타입 | 설명                                                                                           |
| :------------------------------- | :--------------------------- | :------- | :--------------------------------------------------------------------------------------------- |
| `positionViewAtIndex(index, mode)`| `int`, `PositionMode`        | -        | 지정된 인덱스의 항목이 보이도록 뷰를 스크롤합니다. `mode`는 정렬 방식 (`Beginning`, `Center`, `End`, `Visible`, `Contain`)을 지정합니다. |
| `incrementCurrentIndex()`        | -                            | -        | `currentIndex`를 1 증가시킵니다.                                                               |
| `decrementCurrentIndex()`        | -                            | -        | `currentIndex`를 1 감소시킵니다.                                                               |
| `itemAt(x, y)`                   | `real`, `real`               | `Item`   | 지정된 좌표(`x`, `y`)에 있는 델리게이트 아이템을 반환합니다. 없으면 `null`을 반환합니다.              |
| `indexAt(x, y)`                  | `real`, `real`               | `int`    | 지정된 좌표(`x`, `y`)에 있는 델리게이트의 인덱스를 반환합니다. 없으면 `-1`을 반환합니다.             |

## 예제

```qml
import QtQuick
import QtQuick.Controls // For ScrollBar

Window {
    width: 300; height: 400
    visible: true
    title: "ListView Example"

    ListModel {
        id: myModel
        ListElement { name: "Alice"; age: 30; color: "lightblue" }
        ListElement { name: "Bob"; age: 25; color: "lightgreen" }
        ListElement { name: "Charlie"; age: 35; color: "lightcoral" }
        ListElement { name: "David"; age: 28; color: "lightgoldenrodyellow" }
        ListElement { name: "Eve"; age: 22; color: "lightpink" }
        ListElement { name: "Frank"; age: 40; color: "lightsalmon" }
        ListElement { name: "Grace"; age: 31; color: "lightseagreen" }
        ListElement { name: "Henry"; age: 29; color: "lightskyblue" }
    }

    ListView {
        id: listView
        anchors.fill: parent
        anchors.rightMargin: scrollBar.width // 스크롤바 공간
        model: myModel
        spacing: 5
        clip: true // 내용 잘라내기 활성화

        // 각 항목을 표시할 델리게이트 정의
        delegate: Rectangle {
            width: listView.width
            height: 50
            color: model.color // 모델의 color 역할 사용
            border.color: "gray"

            Text {
                anchors.centerIn: parent
                // 모델의 name과 age 역할 사용
                text: name + " (Age: " + age + ") - Index: " + index
            }

            MouseArea {
                anchors.fill: parent
                onClicked: {
                    // 클릭 시 해당 항목을 현재 항목으로 설정
                    listView.currentIndex = index
                    console.log("Clicked item:", name, "at index:", index)
                }
            }
        }

        // 현재 선택된 항목 강조
        highlight: Rectangle {
            width: listView.width; height: 50
            color: "yellow"
            opacity: 0.5
            border.color: "darkgoldenrod"
            border.width: 2
            // 하이라이트 이동 애니메이션
            Behavior on y { SpringAnimation { spring: 2; damping: 0.2 } }
        }

        // 스크롤바 추가 (QtQuick.Controls 필요)
        ScrollBar.vertical: ScrollBar { }
    }
}
```

## 참고 사항

*   `ListView`의 성능은 델리게이트의 복잡성에 크게 영향을 받습니다. 델리게이트는 가능한 한 가볍게 유지하는 것이 좋습니다.
*   `model` 프로퍼티에 데이터를 제공해야 뷰에 내용이 표시됩니다.
*   `delegate`는 모델의 각 항목을 어떻게 그릴지 정의하는 필수 요소입니다. 델리게이트 내에서는 `index`와 모델 역할(role) 이름 (또는 `modelData` 등)을 사용하여 데이터에 접근합니다.
*   `orientation`을 `ListView.Horizontal`로 설정하면 항목들이 가로로 나열됩니다.
*   `header`, `footer`, `section` 프로퍼티를 사용하여 목록에 추가적인 구조와 정보를 제공할 수 있습니다.
*   `highlight` 컴포넌트를 사용하여 현재 선택된 항목을 시각적으로 강조할 수 있습니다.
*   스크롤 성능 최적화를 위해 `cacheBuffer` 값을 조절하거나, Qt 6 이상에서는 `reuseItems` 프로퍼티를 활용할 수 있습니다.
*   내장된 스크롤 기능 외에 `ScrollBar`나 `ScrollIndicator`를 명시적으로 추가하여 사용자에게 스크롤 상태를 보여주고 제어할 수 있게 할 수 있습니다. 