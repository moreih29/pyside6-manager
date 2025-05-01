# GridView

**모듈:** `import QtQuick`

## 개요

`GridView`는 모델(model)의 데이터를 2차원 그리드(격자) 형태로 표시하는 뷰(view) 컴포넌트입니다. `ListView`와 유사하게 모델과 델리게이트(delegate)를 사용하여 각 항목을 표시하지만, 항목들이 여러 행과 열에 걸쳐 배열됩니다.

사진 갤러리, 아이콘 목록 등 항목을 격자 형태로 보여주는 UI에 적합합니다. `GridView` 역시 `Flickable`을 기반으로 하여 스크롤 기능을 내장하고 있으며, 효율적인 항목 관리를 지원합니다.

## 기반 클래스

*   `Flickable` (스크롤 기능 제공)

## 주요 프로퍼티

`ListView`와 많은 프로퍼티를 공유합니다 (`model`, `delegate`, `count`, `currentIndex`, `currentItem`, `header`, `footer`, `section`, `highlight`, `cacheBuffer`, `reuseItems`, `clip`, 트랜지션(`add`, `remove`, `move` 등) 등). 자세한 내용은 `ListView` 문서를 참고하세요.

`GridView`에 특화되거나 중요하게 사용되는 프로퍼티는 다음과 같습니다.

| 이름                | 타입            | 기본값                   | 설명                                                                                                                                 |
| :------------------ | :-------------- | :----------------------- | :----------------------------------------------------------------------------------------------------------------------------------- |
| `cellWidth`         | `real`          | 0                        | 그리드의 각 셀(cell)의 너비. 모든 셀은 동일한 너비를 가집니다.                                                                              |
| `cellHeight`        | `real`          | 0                        | 그리드의 각 셀(cell)의 높이. 모든 셀은 동일한 높이를 가집니다.                                                                              |
| `flow`              | `enumeration`   | `GridView.FlowLeftToRight` | 항목이 배열되는 방향. `FlowLeftToRight` (왼쪽에서 오른쪽으로, 다음 행으로 이동), `FlowTopToBottom` (위에서 아래로, 다음 열로 이동).             |
| `layoutDirection`   | `enumeration`   | `Qt.LeftToRight`         | 레이아웃 방향 (`Qt.LeftToRight` 또는 `Qt.RightToLeft`). `flow`와 함께 사용되어 오른쪽에서 왼쪽으로 채우는 등의 배치를 가능하게 합니다.           |
| `snapMode`          | `enumeration`   | `NoSnap`                 | 스크롤이 멈출 때 셀 경계에 맞춰지는 방식 (`GridView.NoSnap`, `GridView.SnapToCell`).                                                         |

## 부착 프로퍼티 (Attached Properties)

델리게이트 아이템 내부에서 사용할 수 있습니다.

| 이름                 | 타입    | 설명                                                                         |
| :------------------- | :------ | :--------------------------------------------------------------------------- |
| `GridView.view`      | `GridView`| 부모 `GridView` 인스턴스.                                                     |
| `GridView.isCurrentItem` | `bool`  | 현재 델리게이트가 `GridView`의 `currentItem`인지 여부.                       |
| `GridView.delayRemove` | `bool`  | `true`로 설정하면, 항목이 모델에서 제거될 때 즉시 파괴되지 않고 `remove` 트랜지션이 완료된 후 파괴됩니다. |

## 부착 시그널 (Attached Signals)

델리게이트 아이템 내부에서 연결할 수 있습니다.

| 이름              | 설명                                             |
| :---------------- | :----------------------------------------------- |
| `GridView.onAdd`  | 항목이 뷰에 추가될 때 발생하는 트랜지션용 시그널.      |
| `GridView.onMove` | 항목이 뷰 내에서 이동할 때 발생하는 트랜지션용 시그널. |
| `GridView.onRemove`| 항목이 뷰에서 제거될 때 발생하는 트랜지션용 시그널.    |

## 주요 시그널

`ListView`와 동일한 주요 시그널을 공유합니다 (`currentIndexChanged`, `currentItemChanged`, `countChanged`, `movementStarted`, `movementEnded` 등).

추가적으로 다음 시그널이 유용하게 사용될 수 있습니다:

| 이름                   | 파라미터 | 설명                                                                 |
| :--------------------- | :------- | :------------------------------------------------------------------- |
| `clicked(int index)`   | `int`    | (Qt 6.2+) 사용자가 델리게이트를 클릭했을 때 발생합니다. 클릭된 인덱스가 전달됩니다. | 
| `pressAndHold(int index)`| `int`    | (Qt 6.2+) 사용자가 델리게이트를 길게 눌렀을 때 발생합니다.                 |

## 주요 메소드

`ListView`와 동일한 주요 메소드를 공유합니다 (`positionViewAtIndex`, `incrementCurrentIndex`, `decrementCurrentIndex`, `itemAt`, `indexAt` 등).

## 예제

```qml
import QtQuick
import QtQuick.Controls // For ScrollBar
import QtQml.Models // ListModel 임포트

Window {
    width: 350; height: 400
    visible: true
    title: "GridView Example"

    ListModel {
        id: colorModel
        ListElement { colorCode: "#FF5733"; name: "Red Orange" }
        ListElement { colorCode: "#FFC300"; name: "Yellow" }
        ListElement { colorCode: "#DAF7A6"; name: "Light Green" }
        ListElement { colorCode: "#33FFBD"; name: "Turquoise" }
        ListElement { colorCode: "#33A7FF"; name: "Light Blue" }
        ListElement { colorCode: "#9D33FF"; name: "Purple" }
        ListElement { colorCode: "#FF33F6"; name: "Pink" }
        // ... 추가 항목 ...
        ListElement { colorCode: "#808080"; name: "Gray" }
    }

    GridView {
        id: gridView
        anchors.fill: parent
        anchors.rightMargin: scrollBar.visible ? scrollBar.width : 0
        model: colorModel
        clip: true
        focus: true // 키보드 포커스 받도록
        keyNavigationEnabled: true // 키 네비게이션 활성화

        // 각 셀의 크기 지정
        cellWidth: 100
        cellHeight: 100

        // 각 셀(항목)을 표시할 델리게이트
        delegate: Rectangle {
            width: GridView.view.cellWidth - 10 // 셀 너비에서 여백 빼기
            height: GridView.view.cellHeight - 10 // 셀 높이에서 여백 빼기
            color: model.colorCode // 모델의 colorCode 역할 사용
            radius: 5
            border.color: GridView.isCurrentItem ? "blue" : "darkgray" // 현재 항목 테두리 강조
            border.width: GridView.isCurrentItem ? 2 : 1
            // 델리게이트 내에서 GridView.view로 GridView 인스턴스 접근 가능

            Text {
                anchors.centerIn: parent
                text: model.name // 모델의 name 역할 사용
                wrapMode: Text.WordWrap
                horizontalAlignment: Text.AlignHCenter
                width: parent.width - 10
            }

            MouseArea {
                anchors.fill: parent
                onClicked: {
                    gridView.currentIndex = index // 클릭 시 현재 인덱스 설정
                    console.log("Clicked color:", name)
                }
            }
        }

        // 현재 선택된 항목 강조 (크기를 약간 키우는 효과)
        highlight: Rectangle {
            width: GridView.view.cellWidth - 5
            height: GridView.view.cellHeight - 5
            color: "transparent"
            border.color: "darkgoldenrod"
            border.width: 3
            radius: 8
            // 하이라이트 이동 애니메이션
            Behavior on x { SpringAnimation { spring: 2; damping: 0.2 } }
            Behavior on y { SpringAnimation { spring: 2; damping: 0.2 } }
        }
        highlightFollowsCurrentItem: true

        // 스크롤바 추가
        ScrollBar.vertical: ScrollBar { id: scrollBar }
    }
}
```

## 참고 사항

*   `GridView`는 모든 셀이 동일한 크기(`cellWidth`, `cellHeight`)를 갖는다고 가정합니다. 가변 크기 그리드가 필요한 경우 다른 접근 방식(예: `Flow` 레이아웃과 `Repeater` 조합)을 고려해야 할 수 있습니다.
*   `flow` 프로퍼티를 통해 항목이 배열되는 주 방향(가로 우선 또는 세로 우선)을 제어할 수 있습니다.
*   델리게이트 내에서 `GridView.view`를 사용하여 `GridView` 인스턴스의 프로퍼티(예: `cellWidth`)에 접근할 수 있습니다.
*   `ListView`와 마찬가지로 `model`, `delegate`가 필수적이며, `highlight`를 사용하여 선택된 항목을 강조할 수 있습니다.
*   성능 최적화를 위해 델리게이트를 가볍게 유지하고 `cacheBuffer`, `reuseItems` (Qt 6.0+ 기본값 `true`) 프로퍼티를 활용하는 것이 좋습니다.

## 공식 문서 링크

* [GridView QML Type ](https://doc.qt.io/qt-6/qml-qtquick-gridview.html) 