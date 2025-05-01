# ListView

**모듈:** `import QtQuick`

## 개요

`ListView`는 모델(model)의 데이터를 목록 형태로 표시하는 데 사용되는 가장 기본적인 뷰(view) 컴포넌트입니다. 항목들을 수직 또는 수평으로 나열하며, 각 항목의 시각적 표현은 델리게이트(delegate)를 통해 정의됩니다.

`ListView`는 내장된 `Flickable` 기능을 통해 스크롤을 지원하며, 화면에 보이는 영역의 항목들만 생성하고 관리하여 많은 수의 데이터를 효율적으로 처리할 수 있습니다.

## 기반 클래스

*   `Flickable` (스크롤 기능 제공)

## 주요 프로퍼티

| 이름                       | 타입            | 기본값               | 설명                                                                                                                                                                  |
| :------------------------- | :-------------- | :------------------- | :-------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `model`                    | `model`         | `null`               | 뷰에 표시할 데이터 모델. `ListModel`, JavaScript 배열/객체, 숫자(개수), C++ 모델 등을 사용할 수 있습니다.                                                                   |
| `delegate`                 | `Component`     | `null`               | 모델의 각 항목을 시각적으로 표현하는 QML 컴포넌트. 델리게이트 내에서는 `index`(항목 인덱스) 및 모델 데이터(예: `modelData`, 역할 이름)에 접근할 수 있습니다.                 |
| `orientation`              | `enumeration`   | `Qt.Vertical`        | 목록의 방향 (`ListView.Vertical` 또는 `ListView.Horizontal`).                                                                                                           |
| `count`                    | `int`           | (읽기 전용)          | 모델에 포함된 항목의 총 개수 (`model` 프로퍼티에서 파생됨).                                                                                                             |
| `currentIndex`             | `int`           | -1                   | 현재 선택된 항목의 인덱스. `-1`은 선택된 항목이 없음을 의미합니다.                                                                                                       |
| `currentItem`              | `Item`          | (읽기 전용)          | 현재 선택된 항목에 해당하는 델리게이트 아이템.                                                                                                                       |
| `spacing`                  | `real`          | 0                    | 각 델리게이트 아이템 사이의 간격 (픽셀 단위).                                                                                                                           |
| `header`                   | `Component`     | `null`               | 목록의 시작 부분(수직 목록의 경우 위쪽, 수평 목록의 경우 왼쪽)에 표시될 컴포넌트.                                                                                             |
| `headerItem`               | `Item`          | (읽기 전용)          | `header` 컴포넌트로부터 생성된 아이템 인스턴스.                                                                                                                        |
| `headerPositioning`        | `enumeration`   | (스타일 의존)        | 헤더의 위치 고정 방식 (`ListView.InlineHeader`, `ListView.OverlayHeader`, `ListView.PullBackHeader`). (Qt 5.4+)                                                              |
| `footer`                   | `Component`     | `null`               | 목록의 끝 부분(수직 목록의 경우 아래쪽, 수평 목록의 경우 오른쪽)에 표시될 컴포넌트.                                                                                             |
| `footerItem`               | `Item`          | (읽기 전용)          | `footer` 컴포넌트로부터 생성된 아이템 인스턴스.                                                                                                                        |
| `footerPositioning`        | `enumeration`   | (스타일 의존)        | 푸터의 위치 고정 방식 (`ListView.InlineFooter`, `ListView.OverlayFooter`, `ListView.PullBackFooter`). (Qt 5.4+)                                                              |
| `section`                  | `object`        | (읽기 전용)          | 목록 섹션 관련 프로퍼티 및 메서드를 포함하는 객체 (`section.property`, `section.criteria`, `section.delegate`, `section.labelPositioning`). 항목들을 특정 기준으로 그룹화하는 데 사용됩니다. | 
| `currentSection`           | `string`        | ""                 | 현재 뷰포트에서 가장 위에 보이는 섹션의 이름.                                                                                                                   |
| `snapMode`                 | `enumeration`   | `NoSnap`             | 스크롤이 멈출 때 델리게이트 경계에 맞춰지는 방식 (`ListView.NoSnap`, `ListView.SnapToItem`, `ListView.SnapOneItem`).                                                          |
| `highlight`                | `Component`     | `null`               | 현재 선택된 항목(`currentItem`)을 시각적으로 강조하는 컴포넌트.                                                                                                          |
| `highlightItem`            | `Item`          | (읽기 전용)          | `highlight` 컴포넌트로부터 생성된 아이템 인스턴스.                                                                                                                     |
| `highlightFollowsCurrentItem`| `bool`          | `true`               | `highlight`가 `currentIndex` 변경 시 즉시 이동할지 여부. `false`이면 사용자가 스크롤을 멈춘 후에 이동합니다.                                                                       |
| `highlightRangeMode`       | `enumeration`   | `StrictlyEnforceRange` | `highlight` 컴포넌트가 뷰 경계를 벗어나 표시될 수 있는지 여부 (`ListView.StrictlyEnforceRange`, `ListView.ApplyRange`).                                                        |
| `highlightMoveDuration`    | `int`           | (플랫폼 의존)        | `highlight`가 현재 항목으로 이동하는 데 걸리는 시간 (밀리초). `highlightMoveVelocity`와 함께 사용 불가.                                                                        |
| `highlightMoveVelocity`    | `real`          | (플랫폼 의존)        | `highlight`가 현재 항목으로 이동하는 속도 (픽셀/초). `highlightMoveDuration`과 함께 사용 불가.                                                                              |
| `highlightResizeDuration`  | `int`           | (플랫폼 의존)        | `highlight`가 크기를 변경하는 데 걸리는 시간 (밀리초).                                                                                                                  |
| `highlightResizeVelocity`  | `real`          | (플랫폼 의존)        | `highlight`가 크기를 변경하는 속도 (픽셀/초).                                                                                                                           |
| `preferredHighlightBegin`  | `real`          | 0                    | 하이라이트가 표시될 선호 시작 위치 (뷰포트 기준, 0.0 ~ 1.0). 수직 목록에서는 위쪽, 수평에서는 왼쪽.                                                                            |
| `preferredHighlightEnd`    | `real`          | 1                    | 하이라이트가 표시될 선호 끝 위치 (뷰포트 기준, 0.0 ~ 1.0). 수직 목록에서는 아래쪽, 수평에서는 오른쪽.                                                                             |
| `cacheBuffer`              | `real`          | (플랫폼 의존)        | 뷰포트 외부에서 미리 생성하고 캐시할 델리게이트의 양 (픽셀 단위). 스크롤 성능을 향상시킬 수 있지만 메모리 사용량이 증가합니다.                                                     |
| `reuseItems`               | `bool`          | `true` (Qt 6.0+)     | 화면 밖으로 나간 델리게이트 아이템을 재사용할지 여부. 성능 향상에 중요합니다.                                                                                                |
| `keyNavigationEnabled`     | `bool`          | `false`              | 키보드(화살표 키 등)를 사용하여 항목 간 이동을 활성화할지 여부.                                                                                                          |
| `keyNavigationWraps`       | `bool`          | `false`              | 키보드 네비게이션 시 목록의 끝에서 처음으로(또는 반대로) 순환할지 여부.                                                                                                     |
| `clip`                     | `bool`          | `false`              | `Flickable`에서 상속. `true`로 설정하면 뷰 경계 밖의 내용을 그리지 않습니다. 델리게이트가 뷰 크기를 벗어나는 경우 `true`로 설정하는 것이 일반적입니다.                           |
| `contentWidth`, `contentHeight`| `real`        | (읽기 전용)          | `Flickable`에서 상속. 내용의 전체 너비/높이.                                                                                                                            |
| `displayMarginBeginning`   | `real`          | 0                    | 뷰의 시작 부분(스크롤 시작 방향)에 추가할 외부 여백 (픽셀 단위). (Qt 5.3+)                                                                                                 |
| `displayMarginEnd`         | `real`          | 0                    | 뷰의 끝 부분(스크롤 끝 방향)에 추가할 외부 여백 (픽셀 단위). (Qt 5.3+)                                                                                                      |
| `layoutDirection`          | `enumeration`   | `Qt.LeftToRight`     | 레이아웃 방향 (`Qt.LeftToRight` 또는 `Qt.RightToLeft`). 수평 목록의 배치 순서에 영향을 줍니다.                                                                                    |
| `effectiveLayoutDirection` | `enumeration`   | (읽기 전용)          | 실제 적용되는 레이아웃 방향 (상위 Item에서 상속 가능).                                                                                                               |
| `verticalLayoutDirection`  | `enumeration`   | `ListView.TopToBottom` | 수직 스크롤 시 항목이 쌓이는 방향 (`ListView.TopToBottom` 또는 `ListView.BottomToTop`).                                                                                      |
| `add`, `remove`, `move`    | `Transition`    |                      | 항목 추가/제거/이동 시 적용될 트랜지션(애니메이션).                                                                                                               |
| `addDisplaced`, `removeDisplaced`, `moveDisplaced` | `Transition` |    | 다른 항목의 추가/제거/이동으로 인해 위치가 변경되는 항목에 적용될 트랜지션.                                                                                                 |
| `populate`                 | `Transition`    |                      | 뷰가 처음 표시될 때 항목에 적용될 트랜지션.                                                                                                                       |

## 부착 프로퍼티 (Attached Properties)

델리게이트 아이템 내부에서 사용할 수 있습니다.

| 이름                 | 타입    | 설명                                                                         |
| :------------------- | :------ | :--------------------------------------------------------------------------- |
| `ListView.view`      | `ListView`| 부모 `ListView` 인스턴스.                                                     |
| `ListView.isCurrentItem` | `bool`  | 현재 델리게이트가 `ListView`의 `currentItem`인지 여부.                       |
| `ListView.delayRemove` | `bool`  | `true`로 설정하면, 항목이 모델에서 제거될 때 즉시 파괴되지 않고 `remove` 트랜지션이 완료된 후 파괴됩니다. |

## 부착 시그널 (Attached Signals)

델리게이트 아이템 내부에서 연결할 수 있습니다.

| 이름              | 설명                                             |
| :---------------- | :----------------------------------------------- |
| `ListView.onAdd`  | 항목이 뷰에 추가될 때 발생하는 트랜지션용 시그널.      |
| `ListView.onMove` | 항목이 뷰 내에서 이동할 때 발생하는 트랜지션용 시그널. |
| `ListView.onRemove`| 항목이 뷰에서 제거될 때 발생하는 트랜지션용 시그널.    |

## 주요 시그널

| 이름                   | 파라미터 | 설명                                                                 |
| :--------------------- | :------- | :------------------------------------------------------------------- |
| `currentIndexChanged`  |          | `currentIndex` 프로퍼티가 변경될 때 발생합니다.                      |
| `currentItemChanged`   |          | `currentItem` 프로퍼티가 변경될 때 발생합니다.                     |
| `countChanged`         |          | `count` 프로퍼티가 변경될 때 발생합니다.                               |
| `clicked(int index)`   | `int`    | (Qt 6.2+) 사용자가 델리게이트를 클릭했을 때 발생합니다. 클릭된 인덱스가 전달됩니다. | 
| `pressAndHold(int index)`| `int`    | (Qt 6.2+) 사용자가 델리게이트를 길게 눌렀을 때 발생합니다.                 |
| `movementStarted`      |          | `Flickable`에서 상속. 스크롤(이동)이 시작될 때 발생합니다.             |
| `movementEnded`        |          | `Flickable`에서 상속. 스크롤(이동)이 끝났을 때 발생합니다.               |

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
import QtQml.Models // ListModel 임포트

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
        // ... 추가 항목
    }

    ListView {
        id: listView
        anchors.fill: parent
        anchors.rightMargin: scrollBar.visible ? scrollBar.width : 0 // 스크롤바 공간
        model: myModel
        spacing: 5
        clip: true // 내용 잘라내기 활성화
        keyNavigationEnabled: true // 키보드 네비게이션 활성화
        focus: true // 키보드 포커스 받도록 설정

        // 각 항목을 표시할 델리게이트 정의
        delegate: Rectangle {
            width: ListView.view.width // 부모 ListView 접근
            height: 50
            color: model.color // 모델의 color 역할 사용
            border.color: ListView.isCurrentItem ? "blue" : "gray" // 현재 항목 테두리 강조
            border.width: ListView.isCurrentItem ? 2 : 1

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

        // 현재 선택된 항목 강조 (별도 컴포넌트 사용)
        highlight: Rectangle {
            width: listView.width; height: 50
            color: "yellow"
            opacity: 0.3 // 반투명으로 기존 내용 보이게
            border.color: "darkgoldenrod"
            border.width: 2
            // 하이라이트 이동 애니메이션
            Behavior on y { SpringAnimation { spring: 2; damping: 0.2 } }
        }
        highlightFollowsCurrentItem: true // 즉시 따라오도록

        // 항목 추가/제거 시 페이드 애니메이션
        add: Transition {
            NumberAnimation { property: "opacity"; from: 0; to: 1.0; duration: 300 }
        }
        remove: Transition {
            // 제거 시 delayRemove 사용 예시 (델리게이트에 ListView.delayRemove = true 필요)
            // NumberAnimation { property: "opacity"; from: 1.0; to: 0; duration: 300 }
        }

        // 스크롤바 추가 (QtQuick.Controls 필요)
        ScrollBar.vertical: ScrollBar { id: scrollBar }
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
*   스크롤 성능 최적화를 위해 `cacheBuffer` 값을 조절하거나, Qt 6.0 이상에서는 `reuseItems: true` (기본값)를 활용하는 것이 중요합니다. `reuseItems` 사용 시 델리게이트 내부 상태 관리에 주의해야 할 수 있습니다.
*   내장된 스크롤 기능 외에 `ScrollBar`나 `ScrollIndicator`를 명시적으로 추가하여 사용자에게 스크롤 상태를 보여주고 제어할 수 있게 할 수 있습니다. 
*   `add`, `remove`, `move` 등의 프로퍼티에 `Transition`을 할당하여 항목 변경 시 애니메이션 효과를 줄 수 있습니다.

## 공식 문서 링크

* [ListView QML Type ](https://doc.qt.io/qt-6/qml-qtquick-listview.html) 