# SplitView

**모듈:** `import QtQuick.Controls`

## 개요

`SplitView`는 두 개 이상의 아이템을 포함하며, 아이템들 사이에 크기를 조절할 수 있는 핸들(handle) 또는 분할선(splitter)을 제공하는 컨테이너 컨트롤입니다. 사용자는 이 핸들을 드래그하여 각 아이템이 차지하는 공간의 비율을 동적으로 변경할 수 있습니다.

`SplitView`는 수평 또는 수직 방향으로 아이템들을 배치할 수 있으며, 파일 탐색기나 IDE와 같이 여러 뷰를 동시에 보여주고 사용자가 레이아웃을 조절할 수 있도록 하는 인터페이스에 유용합니다.

## 주요 프로퍼티

| 이름            | 타입                | 기본값             | 설명                                                                                                                             |
| :-------------- | :------------------ | :----------------- | :------------------------------------------------------------------------------------------------------------------------------- |
| `orientation`   | `Qt::Orientation`   | `Qt.Horizontal`    | 아이템 배치 및 분할 방향 (`Qt.Horizontal`: 좌우 배치, 수직 분할선 / `Qt.Vertical`: 상하 배치, 수평 분할선).                               |
| `handleDelegate`| `Component`         | (스타일 의존)     | 분할 핸들(사용자가 드래그하는 부분)의 시각적 표현을 정의하는 컴포넌트.                                                                    |
| `resizing`      | `bool`              | `false`            | (읽기 전용) 현재 사용자가 핸들을 드래그하여 크기를 조절 중인지 여부.                                                                     |

## Attached Properties (자식 아이템에서 사용)

`SplitView`의 자식 아이템들은 `SplitView`의 Attached Properties를 사용하여 레이아웃 동작 방식을 제어할 수 있습니다.

| 이름                   | 타입   | 기본값 | 설명                                                                                                     |
| :--------------------- | :----- | :----- | :------------------------------------------------------------------------------------------------------- |
| `SplitView.fillWidth`  | `bool` | `true` | (`orientation`이 `Qt.Vertical`일 때) 아이템이 `SplitView`의 전체 너비를 채우도록 할지 여부.                        |
| `SplitView.fillHeight` | `bool` | `true` | (`orientation`이 `Qt.Horizontal`일 때) 아이템이 `SplitView`의 전체 높이를 채우도록 할지 여부.                      |
| `SplitView.maximumWidth`| `real`| -1     | (`orientation`이 `Qt.Horizontal`일 때) 아이템의 최대 너비. -1이면 제한 없음. 핸들 드래그 시 이 값 이상으로 커지지 않음. |
| `SplitView.maximumHeight`|`real`| -1     | (`orientation`이 `Qt.Vertical`일 때) 아이템의 최대 높이. -1이면 제한 없음.                                            |
| `SplitView.minimumWidth`| `real`| 0      | (`orientation`이 `Qt.Horizontal`일 때) 아이템의 최소 너비. 핸들 드래그 시 이 값 이하로 작아지지 않음.                 |
| `SplitView.minimumHeight`|`real`| 0      | (`orientation`이 `Qt.Vertical`일 때) 아이템의 최소 높이.                                                              |

## 주요 메소드

| 이름                     | 파라미터                   | 반환타입 | 설명                                                              | 
| :----------------------- | :------------------------- | :------- | :---------------------------------------------------------------- |
| `itemAt(index)`          | `int index`                | `Item`   | 지정된 인덱스에 있는 아이템을 반환.                                 | 
| `addItem(item)`          | `Item item`                | `void`   | `SplitView`에 아이템을 동적으로 추가.                            | 
| `removeItem(item)`       | `Item item`                | `void`   | `SplitView`에서 아이템을 동적으로 제거.                            | 
| `insertItem(index, item)`| `int index`, `Item item`   | `void`   | 지정된 인덱스에 아이템을 동적으로 삽입.                           | 
| `moveItem(from, to)`     | `int from`, `int to`       | `void`   | 아이템의 순서를 동적으로 변경.                                     | 
| `count`                  | -                          | `int`    | (프로퍼티) `SplitView`에 포함된 아이템의 수.                      | 
| `setSizes(list<real> sizes)` | `list<real>` sizes (옵션) | `void`   | 각 아이템의 크기를 프로그래밍 방식으로 설정. `sizes` 리스트는 비율이나 절대값을 포함할 수 있음 (Qt 문서 참조). | 

## 예제

```qml
import QtQuick
import QtQuick.Controls

Window {
    width: 600
    height: 400
    visible: true
    title: "SplitView Example"

    SplitView {
        id: splitView
        anchors.fill: parent
        orientation: Qt.Horizontal // 좌우 분할 (기본값)

        // 첫 번째 아이템 (왼쪽)
        Rectangle {
            id: leftPane
            color: "lightblue"
            width: 200 // 초기 너비 (비율에 따라 조절됨)
            SplitView.minimumWidth: 100 // 최소 너비
            SplitView.maximumWidth: 400 // 최대 너비
            // SplitView.fillHeight: true // 기본값

            Text {
                anchors.centerIn: parent
                text: "Left Pane\nWidth: " + Math.round(leftPane.width)
            }
        }

        // 두 번째 아이템 (오른쪽)
        SplitView { // 중첩 SplitView 가능
            id: rightSplit
            orientation: Qt.Vertical // 상하 분할

            Rectangle {
                id: topRightPane
                color: "lightgreen"
                height: 150 // 초기 높이
                SplitView.minimumHeight: 50
                // SplitView.fillWidth: true // 기본값

                Text {
                    anchors.centerIn: parent
                    text: "Top Right Pane\nHeight: " + Math.round(topRightPane.height)
                }
            }

            Rectangle {
                id: bottomRightPane
                color: "lightcoral"
                 // 남은 높이 차지

                Text {
                    anchors.centerIn: parent
                    text: "Bottom Right Pane\nHeight: " + Math.round(bottomRightPane.height)
                }
            }
        }

        // 커스텀 핸들 델리게이트 (선택 사항)
        handleDelegate: Rectangle {
            width: orientation === Qt.Horizontal ? 10 : undefined
            height: orientation === Qt.Vertical ? 10 : undefined
            color: splitView.resizing ? "steelblue" : "gray"
            border.color: "darkgray"

            MouseArea { // 핸들 드래그를 위한 영역
                anchors.fill: parent
                cursorShape: splitView.orientation === Qt.Horizontal ? Qt.SplitHCursor : Qt.SplitVCursor
            }
        }
    }
}
```

## 참고 사항

*   `SplitView`의 자식 아이템들은 `Item` 기반의 어떤 컴포넌트든 될 수 있습니다 (예: `Rectangle`, `Flickable`, 다른 `SplitView` 등).
*   각 자식 아이템의 초기 크기(`width` 또는 `height`)는 `SplitView` 내에서의 상대적인 비율을 결정하는 데 영향을 줄 수 있지만, 사용자가 핸들을 조작하면 변경됩니다.
*   `SplitView` Attached Properties (`minimumWidth/Height`, `maximumWidth/Height`)를 사용하여 각 아이템의 크기 조절 범위를 제한할 수 있습니다.
*   `handleDelegate`를 커스터마이징하여 분할 핸들의 모양과 느낌을 변경할 수 있습니다. 