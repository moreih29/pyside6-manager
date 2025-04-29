# TableView

**모듈:** `import QtQuick.Controls`

## 개요

`TableView`는 모델의 데이터를 행(row)과 열(column)으로 구성된 테이블(표) 형태로 표시하는 컨트롤 기반 뷰입니다. `ListView`나 `GridView`와 달리, `TableView`는 각 열(column)을 명시적으로 정의하고, 열 헤더(header) 표시, 열 크기 조절, 행/열 정렬 등의 고급 테이블 기능을 제공합니다.

데이터베이스 결과, 설정 목록 등 구조화된 데이터를 표 형식으로 보여주는 데 매우 유용합니다.

**참고:** `TableView`는 `QtQuick.Controls` 모듈에 속하며, 기본적인 `QtQuick` 모듈의 `ListView`, `GridView`와는 다른 특징을 가집니다.

## 기반 클래스

*   `Control`

## 주요 프로퍼티

| 이름                | 타입            | 기본값        | 설명                                                                                                                               |
| :------------------ | :-------------- | :------------ | :--------------------------------------------------------------------------------------------------------------------------------- |
| `model`             | `any`           | `null`        | 테이블에 표시할 데이터 모델. `ListModel`, C++ 모델 (`QAbstractItemModel` 등)을 주로 사용합니다. 각 항목은 열에 해당하는 역할(role)을 가져야 합니다. |
| `selectionModel`    | `ItemSelectionModel` | `null`        | 항목 선택 상태를 관리하는 모델.                                                                                                      |
| `rows`              | `int`           | (읽기 전용)   | 모델의 행(row) 개수.                                                                                                                 |
| `columns`           | `int`           | (읽기 전용)   | 테이블에 정의된 열(column)의 개수.                                                                                                   |
| `currentRow`        | `int`           | -1            | 현재 선택된 행의 인덱스.                                                                                                             |
| `currentColumn`     | `int`           | -1            | 현재 선택된 열의 인덱스.                                                                                                             |
| `columnWidthProvider`| `function`      | `null`        | 각 열의 너비를 동적으로 계산하는 JavaScript 함수. `function(column)` 형태로 정의하며, 각 열 인덱스에 대한 너비를 반환해야 합니다.              |
| `rowHeightProvider` | `function`      | `null`        | 각 행의 높이를 동적으로 계산하는 JavaScript 함수. `function(row)` 형태로 정의하며, 각 행 인덱스에 대한 높이를 반환해야 합니다.                |
| `delegate`          | `Component`     | (스타일 의존) | 각 셀(cell)의 내용을 표시하는 델리게이트 컴포넌트. 컨텍스트 프로퍼티로 `model` (전체 모델), `modelData` (해당 셀 데이터), `row`, `column`, `selected`, `current` 등에 접근 가능. |
| `rowDelegate`       | `Component`     | (스타일 의존) | 각 행(row)의 배경 등을 표시하는 델리게이트 컴포넌트.                                                                                   |
| `columnHeaderVisible`| `bool`          | `true`        | 열 헤더를 표시할지 여부.                                                                                                             |
| `rowHeaderVisible`  | `bool`          | `false`       | 행 헤더를 표시할지 여부. (일반적으로 사용 빈도 낮음)                                                                                     |
| `sortIndicatorVisible` | `bool`        | `true`        | 정렬된 열 헤더에 정렬 방향 표시기(화살표)를 표시할지 여부.                                                                                 |
| `sortIndicatorColumn` | `int`         | -1            | 현재 정렬 기준이 되는 열의 인덱스.                                                                                                     |
| `sortIndicatorOrder`| `enumeration`   | `Qt.AscendingOrder` | 현재 정렬 순서 (`Qt.AscendingOrder` 또는 `Qt.DescendingOrder`).                                                                          |
| `alternatingRowColors`| `bool`         | `true`        | 행의 배경색을 번갈아 다르게 표시할지 여부.                                                                                               |
| `background`        | `Item`          | (스타일 의존) | 테이블 전체의 배경 아이템.                                                                                                             |
| `contentItem`       | `Item`          | (스타일 의존) | 테이블의 셀 내용을 담는 내부 아이템.                                                                                                    |
| `headerDelegate`    | `Component`     | (스타일 의존) | 열 헤더를 표시하는 델리게이트 컴포넌트.                                                                                                  |
| `horizontalScrollBarPolicy` | `ScrollBarPolicy`| `AsNeeded` | 수평 스크롤바 표시 정책. (`ScrollBar`와 동일)                                                                                            |
| `verticalScrollBarPolicy`   | `ScrollBarPolicy`| `AsNeeded` | 수직 스크롤바 표시 정책. (`ScrollBar`와 동일)                                                                                            |

## 주요 시그널

| 이름                 | 파라미터      | 설명                                                               |
| :------------------- | :------------ | :----------------------------------------------------------------- |
| `clicked(row, column)` | `int`, `int` | 사용자가 특정 셀을 클릭했을 때 발생합니다.                             |
| `doubleClicked(row, column)`| `int`, `int` | 사용자가 특정 셀을 더블 클릭했을 때 발생합니다.                        |
| `pressAndHold(row, column)`| `int`, `int` | 사용자가 특정 셀을 길게 눌렀을 때 발생합니다.                         |
| `currentCellChanged` |               | `currentRow` 또는 `currentColumn`이 변경될 때 발생합니다.               |
| `selectionChanged`   |               | `selectionModel`의 선택 상태가 변경될 때 발생합니다.                    |
| `columnWidthsChanged`|               | 열 너비가 변경될 때 발생합니다.                                        |
| `sortIndicatorChanged`|              | 정렬 관련 프로퍼티(`sortIndicatorColumn`, `sortIndicatorOrder`)가 변경될 때 발생합니다. |

## 주요 메소드

| 이름                      | 파라미터 | 반환타입 | 설명                                                               |
| :------------------------ | :------- | :------- | :----------------------------------------------------------------- |
| `addColumn(column)`       | `TableViewColumn` | -        | 테이블에 `TableViewColumn` 객체를 추가합니다.                           |
| `removeColumn(index)`     | `int`    | -        | 지정된 인덱스의 열을 제거합니다.                                     |
| `selectRow(row)`          | `int`    | -        | 지정된 행을 선택합니다.                                            |
| `selectColumn(column)`    | `int`    | -        | 지정된 열을 선택합니다.                                            |
| `selectAll()`             | -        | -        | 모든 항목을 선택합니다.                                              |
| `clearSelection()`        | -        | -        | 모든 선택을 해제합니다.                                            |
| `resizeColumnsToContents()`| -       | -        | 모든 열의 너비를 내용에 맞게 조절합니다. (주의: 성능 영향 가능성) |

## TableViewColumn

`TableView`의 각 열은 `TableViewColumn` 객체로 정의됩니다. 이 객체는 `TableView` 내부에 선언됩니다.

**주요 프로퍼티:**

| 이름          | 타입     | 기본값        | 설명                                                                           |
| :------------ | :------- | :------------ | :----------------------------------------------------------------------------- |
| `role`        | `string` | ""          | 이 열에 표시할 모델 데이터의 역할(role) 이름.                                     |
| `title`       | `string` | ""          | 열 헤더에 표시될 제목.                                                           |
| `width`       | `real`   | 100           | 열의 너비 (픽셀 단위).                                                           |
| `resizable`   | `bool`   | `true`        | 사용자가 열 너비를 조절할 수 있는지 여부.                                        |
| `movable`     | `bool`   | `true`        | 사용자가 열의 순서를 변경(이동)할 수 있는지 여부.                                   |
| `delegate`    | `Component`| `null`        | 이 열에 대한 특정 셀 델리게이트. 설정하지 않으면 `TableView`의 기본 `delegate` 사용. |
| `header`      | `Component`| `null`        | 이 열에 대한 특정 헤더 델리게이트. 설정하지 않으면 `TableView`의 기본 `headerDelegate` 사용. |
| `visible`     | `bool`   | `true`        | 열을 화면에 표시할지 여부.                                                       |
| `alignment`   | `enumeration`| `Qt.AlignLeft` | 셀 내용의 수평 정렬 (`Qt.AlignLeft`, `Qt.AlignRight`, `Qt.AlignHCenter`).           |
| `elideMode`   | `enumeration`| `Text.ElideRight` | 셀 내용이 너비보다 길 때 생략(...) 처리 방식 (`Text.ElideNone`, `Text.ElideLeft`, `Text.ElideRight`, `Text.ElideMiddle`). |

## 예제

```qml
import QtQuick
import QtQuick.Controls
import QtQuick.Layouts

Window {
    width: 500; height: 300
    visible: true
    title: "TableView Example"

    ListModel {
        id: contactModel
        ListElement { name: "Alice"; phone: "555-1234"; email: "alice@example.com" }
        ListElement { name: "Bob"; phone: "555-5678"; email: "bob@example.com" }
        ListElement { name: "Charlie"; phone: "555-9876"; email: "charlie@example.com" }
        ListElement { name: "David"; phone: "555-4321"; email: "david@example.com" }
    }

    TableView {
        id: tableView
        anchors.fill: parent
        model: contactModel
        alternatingRowColors: true
        clip: true // 내용 잘라내기

        // 열 정의
        TableViewColumn {
            role: "name" // 모델의 'name' 역할과 연결
            title: "Name"   // 헤더 제목
            width: 150
        }
        TableViewColumn {
            role: "phone"
            title: "Phone Number"
            width: 120
            resizable: false // 크기 조절 불가
        }
        TableViewColumn {
            role: "email"
            title: "Email Address"
            width: 200
            // 이 열만 오른쪽 정렬
            alignment: Qt.AlignRight
        }

        // 기본 셀 델리게이트 (모든 열에 적용됨)
        delegate: Rectangle {
            implicitWidth: 100 // 기본 너비
            implicitHeight: 30 // 기본 높이
            color: model.row % 2 === 0 ? (tableView.alternatingRowColors ? "whitesmoke" : "white") : "white"

            Text {
                text: modelData // 해당 셀의 데이터 (role에 따라 자동으로 가져옴)
                anchors.verticalCenter: parent.verticalCenter
                anchors.left: parent.left
                anchors.right: parent.right
                anchors.leftMargin: 5
                anchors.rightMargin: 5
                elide: parent.TableView.view.getColumn(model.column).elideMode // 열의 elideMode 사용
                horizontalAlignment: parent.TableView.view.getColumn(model.column).alignment // 열의 alignment 사용
            }
        }

        // 행 배경 델리게이트 (선택 시 배경 변경 예시)
        rowDelegate: Rectangle {
            height: 30
            color: model.selected ? "lightblue" : "transparent"
        }

        // 열 헤더 델리게이트 (클릭 시 정렬 기능 예시)
        headerDelegate: Rectangle {
            height: 35
            color: "lightgray"
            border.color: "gray"

            Text {
                text: modelData // TableViewColumn의 title
                anchors.centerIn: parent
                font.bold: true
            }
            Image {
                source: "qrc:/qt-project.org/imports/QtQuick/Controls/images/sortindicator-arrow-down.png" // 예시 아이콘
                anchors.right: parent.right
                anchors.verticalCenter: parent.verticalCenter
                anchors.rightMargin: 5
                visible: tableView.sortIndicatorColumn === model.column && tableView.sortIndicatorVisible
                rotation: tableView.sortIndicatorOrder === Qt.AscendingOrder ? 0 : 180
            }
            MouseArea {
                anchors.fill: parent
                onClicked: {
                    // 헤더 클릭 시 정렬 (간단 예시: 실제 정렬은 모델에서 처리 필요)
                    if (tableView.sortIndicatorColumn === model.column) {
                        tableView.sortIndicatorOrder = (tableView.sortIndicatorOrder === Qt.AscendingOrder ? Qt.DescendingOrder : Qt.AscendingOrder)
                    } else {
                        tableView.sortIndicatorColumn = model.column
                        tableView.sortIndicatorOrder = Qt.AscendingOrder
                    }
                    // 실제 데이터 정렬 로직 호출 필요
                    // 예: cppSortModel.sort(model.column, tableView.sortIndicatorOrder)
                    console.log("Sort by column:", model.column, "Order:", tableView.sortIndicatorOrder)
                }
            }
        }
    }
}
```

## 참고 사항

*   `TableView`를 사용하려면 `model`과 함께 하나 이상의 `TableViewColumn`을 정의해야 합니다.
*   `TableViewColumn`의 `role` 프로퍼티는 모델 데이터의 역할 이름과 일치해야 해당 열에 데이터가 표시됩니다.
*   `delegate`는 각 **셀**의 내용을 그리는 역할을 합니다. 델리게이트 내에서는 `modelData` (해당 셀의 값), `row`, `column` 인덱스 등에 접근할 수 있습니다. `model`은 전체 모델 객체에 접근합니다.
*   `rowDelegate`는 행 전체의 배경 등을 꾸미는 데 사용됩니다.
*   `headerDelegate`는 열 헤더의 모양과 동작(예: 클릭 시 정렬)을 정의합니다. 실제 데이터 정렬은 모델 수준(C++ 모델의 `sort()` 함수 등)에서 구현해야 하는 경우가 많습니다.
*   `columnWidthProvider`와 `rowHeightProvider`를 사용하여 내용에 따라 동적으로 크기를 조절할 수 있지만, 성능에 영향을 줄 수 있으므로 주의해야 합니다.
*   `QtQuick.Controls`의 다른 컴포넌트들과 마찬가지로 스타일링이 가능하며, `background`, `contentItem`, `delegate`, `rowDelegate`, `headerDelegate` 등을 커스터마이징할 수 있습니다. 