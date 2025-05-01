# TableView

## 모듈 정보

```qml
import QtQuick
```

## 개요

`TableView`는 모델의 데이터를 행(row)과 열(column)으로 구성된 테이블(표) 형태로 표시하는 뷰 컴포넌트입니다. 모델은 테이블 구조(행/열)와 데이터를 제공해야 하며, `TableView`는 이 데이터를 효율적으로 표시하고 스크롤하는 기능을 담당합니다.

주로 여러 열을 가진 구조화된 데이터를 표시하는 데 사용됩니다.

**참고:** Qt 6의 `TableView`는 `QtQuick` 모듈에 있으며, 이전 버전이나 Qt Quick Controls의 `TableView`와는 다릅니다.

## 기반 클래스

*   `Flickable` (스크롤 기능 제공)

## 주요 프로퍼티

| 이름                      | 타입            | 기본값               | 설명                                                                                                                                                            |
| :------------------------ | :-------------- | :------------------- | :-------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `model`                   | `model`         | `null`               | 테이블에 표시할 데이터 모델. **주의:** 여러 열을 표시하려면 C++ `QAbstractItemModel` 또는 QML `TableModel`(`QtQml.Models`)을 사용해야 합니다. `ListModel`은 첫 번째 열만 채웁니다. |
| `delegate`                | `Component`     | `null`               | 각 **셀(cell)**을 시각적으로 표현하는 QML 컴포넌트. 컨텍스트 프로퍼티(`row`, `column`, `selected`, `current`, `modelData` 등)를 통해 셀 데이터 및 상태에 접근합니다.          |
| `columnSpacing`           | `real`          | 0                    | 열(column) 사이의 간격 (픽셀 단위).                                                                                                                             |
| `rowSpacing`              | `real`          | 0                    | 행(row) 사이의 간격 (픽셀 단위).                                                                                                                                |
| `columnWidthProvider`     | `var` (function)| `null`               | 각 열의 너비를 동적으로 계산하는 JavaScript 함수. `function(column)` 형태로 정의하며, 각 열 인덱스에 대한 너비를 반환해야 합니다.                                           |
| `rowHeightProvider`       | `var` (function)| `null`               | 각 행의 높이를 동적으로 계산하는 JavaScript 함수. `function(row)` 형태로 정의하며, 각 행 인덱스에 대한 높이를 반환해야 합니다.                                             |
| `rows`                    | `int`           | (읽기 전용)          | 모델의 행(row) 개수.                                                                                                                                            |
| `columns`                 | `int`           | (읽기 전용)          | 모델의 열(column) 개수.                                                                                                                                         |
| `currentRow`              | `int`           | -1                   | 현재 포커스된 행의 인덱스. (`keyNavigationEnabled` 또는 프로그래밍 방식)                                                                                                   |
| `currentColumn`           | `int`           | -1                   | 현재 포커스된 열의 인덱스. (`keyNavigationEnabled` 또는 프로그래밍 방식)                                                                                                   |
| `reuseItems`              | `bool`          | `true`               | 화면 밖으로 나간 델리게이트 아이템(셀)을 재사용할지 여부. 성능 향상에 중요합니다.                                                                                             |
| `alternatingRows`         | `bool`          | `false`              | 행 배경색을 번갈아 다르게 표시할지 여부. (델리게이트에서 직접 구현해야 할 수 있음)                                                                                              |
| `selectionModel`          | `ItemSelectionModel` | `null`            | (Qt 6.2+) 항목 선택 상태를 관리하는 모델. `selectionMode`와 함께 사용됩니다.                                                                                               |
| `selectionMode`           | `enumeration`   | `NoSelection`        | (Qt 6.6+) 항목 선택 모드 (`NoSelection`, `SingleSelection`, `MultiSelection`, `ExtendedSelection`, `ContiguousSelection`).                                                    |
| `selectionBehavior`       | `enumeration`   | `SelectItems`        | (Qt 6.4+) 선택 동작 방식 (`SelectItems`, `SelectRows`, `SelectColumns`).                                                                                              |
| `editTriggers`            | `enumeration`   | `NoEditTriggers`     | (Qt 6.5+) 셀 편집을 시작하는 조건 (`NoEditTriggers`, `SelectedClicked`, `EditKeyPressed`, `AnyKeyPressed`, `DoubleClicked`, `CurrentChanged`, `AllEditTriggers`). 편집을 위해서는 `TableView.editDelegate`도 필요합니다. | 
| `keyNavigationEnabled`    | `bool`          | `false`              | (Qt 6.4+) 키보드(화살표 키 등)를 사용하여 셀 간 이동을 활성화할지 여부.                                                                                                       |
| `pointerNavigationEnabled`| `bool`          | `true`               | (Qt 6.4+) 마우스/터치 포인터로 셀을 클릭/탭하여 `currentRow`, `currentColumn`을 변경할 수 있는지 여부.                                                                         |
| `resizableColumns`        | `bool`          | `false`              | (Qt 6.5+) 사용자가 열 너비를 조절할 수 있는지 여부 (구현은 외부 헤더 등에서 필요할 수 있음).                                                                                    |
| `resizableRows`           | `bool`          | `false`              | (Qt 6.5+) 사용자가 행 높이를 조절할 수 있는지 여부 (구현은 외부 헤더 등에서 필요할 수 있음).                                                                                     |
| `syncView`                | `TableView`     | `null`               | 다른 `TableView`와 스크롤 위치를 동기화할 뷰.                                                                                                                   |
| `syncDirection`           | `Qt::Orientations`| `Qt.Vertical | Qt.Horizontal` | `syncView`와 동기화할 방향.                                                                                                                                |
| `topRow`, `bottomRow`   | `int`           | (읽기 전용)          | 현재 뷰포트에 보이는 가장 위/아래 행의 인덱스.                                                                                                                   |
| `leftColumn`, `rightColumn`| `int`         | (읽기 전용)          | 현재 뷰포트에 보이는 가장 왼쪽/오른쪽 열의 인덱스.                                                                                                               |
| `animate`                 | `bool`          | `false`              | (Qt 6.4+) 뷰 위치 변경 시 애니메이션을 적용할지 여부.                                                                                                               |

## 부착 프로퍼티 (Attached Properties)

델리게이트 아이템 내부에서 사용할 수 있습니다.

| 이름                | 타입        | 설명                                                                         |
| :------------------ | :---------- | :--------------------------------------------------------------------------- |
| `TableView.view`    | `TableView` | 부모 `TableView` 인스턴스.                                                    |
| `TableView.editDelegate`| `Component` | 셀 편집 시 사용할 컴포넌트. `editTriggers`와 함께 사용됩니다.                  |

## 주요 시그널

| 이름                      | 파라미터                               | 설명                                                                               |
| :------------------------ | :------------------------------------- | :--------------------------------------------------------------------------------- |
| `clicked(row, column)`    | `int`, `int`                           | 사용자가 특정 셀을 클릭했을 때 발생합니다. (Qt 6.2+ `pointerNavigationEnabled` 영향 받을 수 있음) |
| `doubleClicked(row, column)`| `int`, `int`                           | 사용자가 특정 셀을 더블 클릭했을 때 발생합니다.                                           |
| `pressAndHold(row, column)`| `int`, `int`                          | 사용자가 특정 셀을 길게 눌렀을 때 발생합니다.                                         |
| `currentRowChanged`       |                                        | `currentRow` 프로퍼티가 변경될 때 발생합니다.                                        |
| `currentColumnChanged`    |                                        | `currentColumn` 프로퍼티가 변경될 때 발생합니다.                                     |
| `selectionChanged`        |                                        | (Qt 6.2+) `selectionModel`의 선택 상태가 변경될 때 발생합니다.                          |
| `layoutChanged`           |                                        | (Qt 6.5+) 테이블 레이아웃(예: 셀 크기)이 변경되었을 때 발생합니다.                     |
| `columnMoved`             | `int logicalIndex`, `int oldVisualIndex`, `int newVisualIndex` | (Qt 6.8+) 사용자에 의해 열 순서가 변경되었을 때 발생합니다.                             |
| `rowMoved`                | `int logicalIndex`, `int oldVisualIndex`, `int newVisualIndex`   | (Qt 6.8+) 사용자에 의해 행 순서가 변경되었을 때 발생합니다.                             |

## 부착 시그널 (Attached Signals)

델리게이트 아이템 내부에서 연결할 수 있습니다.

| 이름            | 설명                                                           |
| :-------------- | :------------------------------------------------------------- |
| `TableView.commit`| (editDelegate 내) 편집 내용을 모델에 커밋할 때 발생합니다.     |
| `TableView.pooled`| 델리게이트 아이템이 재사용 풀(pool)에 반환될 때 발생합니다.      |
| `TableView.reused`| 델리게이트 아이템이 재사용 풀에서 꺼내져 재사용될 때 발생합니다. |

## 주요 메소드

| 이름                         | 파라미터                                                    | 반환타입     | 설명                                                                                                                                              |
| :--------------------------- | :---------------------------------------------------------- | :----------- | :------------------------------------------------------------------------------------------------------------------------------------------------ |
| `cellAtPosition(x, y, includeSpacing?)` | `real`, `real`, `bool`                                        | `point`      | 지정된 좌표(`x`, `y`)에 해당하는 셀의 행/열 인덱스를 `point` 객체로 반환합니다.                                                                           |
| `itemAtCell(cell)`           | `point`                                                     | `Item`       | 지정된 셀(`point(column, row)`)에 현재 로드된 델리게이트 아이템을 반환합니다. 없으면 `null`.                                                               |
| `itemAtIndex(index)`       | `QModelIndex`                                               | `Item`       | (Qt 6.5+) 지정된 모델 인덱스에 해당하는 델리게이트 아이템을 반환합니다.                                                                               |
| `modelIndex(cell)`         | `point`                                                     | `QModelIndex`| (Qt 6.4+) 지정된 셀(`point(column, row)`)에 해당하는 모델 인덱스를 반환합니다.                                                                         |
| `columnWidth(column)`      | `int`                                                       | `real`       | (Qt 6.2+) 지정된 열의 현재 너비를 반환합니다. 로드되지 않았으면 -1.                                                                                   |
| `rowHeight(row)`           | `int`                                                       | `real`       | (Qt 6.2+) 지정된 행의 현재 높이를 반환합니다. 로드되지 않았으면 -1.                                                                                    |
| `setColumnWidth(column, size)`| `int`, `real`                                               | -            | 지정된 열의 명시적 너비를 설정합니다. (`columnWidthProvider`보다 우선순위 낮음). -1이면 리셋.                                                               |
| `setRowHeight(row, size)`    | `int`, `real`                                               | -            | 지정된 행의 명시적 높이를 설정합니다. (`rowHeightProvider`보다 우선순위 낮음). -1이면 리셋.                                                                    |
| `clearColumnWidths()`      | -                                                           | -            | `setColumnWidth`로 설정된 모든 명시적 너비를 제거합니다.                                                                                              |
| `clearRowHeights()`        | -                                                           | -            | `setRowHeight`로 설정된 모든 명시적 높이를 제거합니다.                                                                                                 |
| `positionViewAtCell(cell, mode, offset?, subRect?)`| `point`, `PositionMode`, `point`, `rect`                 | -            | 지정된 셀(`point(column, row)`)이 `mode`에 지정된 위치에 오도록 뷰를 스크롤합니다.                                                                           |
| `positionViewAtColumn(...)`  | `int`, `PositionMode`, `real`, `rect`                       | -            | 지정된 열이 특정 위치에 오도록 수평 스크롤합니다.                                                                                                       |
| `positionViewAtRow(...)`     | `int`, `PositionMode`, `real`, `rect`                       | -            | 지정된 행이 특정 위치에 오도록 수직 스크롤합니다.                                                                                                       |
| `positionViewAtIndex(...)` | `QModelIndex`, `PositionMode`, `point`, `rect`              | -            | (Qt 6.5+) 지정된 모델 인덱스가 특정 위치에 오도록 스크롤합니다.                                                                                          |
| `edit(modelIndex)`           | `QModelIndex`                                               | -            | (Qt 6.5+) 지정된 모델 인덱스의 셀 편집을 시작합니다. (`editDelegate` 필요)                                                                                  |
| `closeEditor()`            | -                                                           | -            | (Qt 6.5+) 현재 열려있는 셀 편집기를 닫습니다.                                                                                                       |
| `forceLayout()`              | -                                                           | -            | 테이블 레이아웃을 강제로 다시 계산합니다.                                                                                                                   |
| `moveColumn(source, destination)`| `int`, `int`                                            | -            | (Qt 6.8+) 열 순서를 변경합니다. 모델이 `Qt::ItemIsDragEnabled`, `Qt::ItemIsDropEnabled` 플래그를 지원해야 할 수 있습니다.                                             |
| `moveRow(source, destination)`| `int`, `int`                                             | -            | (Qt 6.8+) 행 순서를 변경합니다. 모델이 해당 플래그를 지원해야 할 수 있습니다.                                                                                |
| `clearColumnReordering()`    | -                                                           | -            | (Qt 6.8+) 열 순서 변경을 초기 상태로 되돌립니다.                                                                                                        |
| `clearRowReordering()`       | -                                                           | -            | (Qt 6.8+) 행 순서 변경을 초기 상태로 되돌립니다.                                                                                                          |

## 예제 (TableModel, DelegateChooser, HeaderView 사용)

```qml
import QtQuick
import QtQuick.Controls // HeaderView, CheckBox, SpinBox, TextField 등 사용
import Qt.labs.qmlmodels // TableModel 사용

Window {
    width: 550; height: 400
    visible: true
    title: "Advanced TableView Example"

    // 데이터 모델 정의
    TableModel {
        id: fruitModel

        // 컬럼 정의 (표시될 데이터의 키를 지정)
        TableModelColumn { display: "available" } // boolean
        TableModelColumn { display: "fruitType" } // string
        TableModelColumn { display: "quantity" }  // number
        TableModelColumn { display: "price" }     // number

        // 초기 데이터 행
        rows: [
            { "available": true, "fruitType": "Apple", "quantity": 5, "price": 1.50 },
            { "available": false, "fruitType": "Banana", "quantity": 8, "price": 0.75 },
            { "available": true, "fruitType": "Orange", "quantity": 3, "price": 2.10 },
            { "available": true, "fruitType": "Pear", "quantity": 10, "price": 1.80 },
            { "available": false, "fruitType": "Grape", "quantity": 50, "price": 0.05 }
        ]
    }

    // 수평 헤더 뷰
    HorizontalHeaderView {
        id: headerView
        syncView: tableView // TableView와 동기화
        anchors.left: parent.left
        anchors.top: parent.top
        anchors.right: parent.right
        height: 30
        model: ["Available", "Type", "Qty", "Price ($)"] // 헤더 텍스트
    }

    // 테이블 뷰
    TableView {
        id: tableView
        anchors.top: headerView.bottom
                anchors.left: parent.left
                anchors.right: parent.right
        anchors.bottom: parent.bottom
        clip: true // 경계 밖 내용 자르기

        model: fruitModel

        // 컬럼 너비 제공 함수
        columnWidthProvider: function(column) {
            if (column === 0) return 80;  // Available 컬럼 너비
            if (column === 1) return 150; // Type 컬럼 너비
            if (column === 2) return 100; // Qty 컬럼 너비
            return 100;                   // Price 컬럼 너비 (나머지)
        }

        // 키보드 네비게이션 활성화 (Qt 6.4+)
        keyNavigationEnabled: true

        // 선택 모드 설정 (Qt 6.6+) 및 동작 방식 (Qt 6.4+)
        selectionMode: TableView.ExtendedSelection // 다중 선택 가능 (Ctrl/Shift 사용)
        selectionBehavior: TableView.SelectRows // 행 단위 선택

        // 다른 셀 타입 표시를 위한 DelegateChooser 사용
        delegate: DelegateChooser {
            // DelegateChoice 내부에서 배경색/선택색 처리
            DelegateChoice {
                column: 0
                delegate: Item { // CheckBox를 직접 배치하는 대신 Item으로 감싸서 배경 추가
                    implicitWidth: 80 // columnWidthProvider와 일치시키거나 필요에 따라 조정
                    implicitHeight: 35 // 필요에 따라 조정

                    Rectangle { // 배경 및 선택 색상
                        anchors.fill: parent
                        color: tableView.selectionModel && tableView.selectionModel.isRowSelected(row, index) ? "lightblue" : (row % 2 === 0 ? "whitesmoke" : "white")
                        border.color: "lightgray"
                    }

                    CheckBox {
                anchors.centerIn: parent
                        checked: model.display // 'available' 역할 데이터 바인딩
                        onClicked: {
                            // 모델 데이터 직접 업데이트 (setData 사용 권장될 수 있음)
                            var modifiableRow = fruitModel.getRow(row);
                            modifiableRow.available = checked;
                            fruitModel.setRow(row, modifiableRow);
                            // 또는 model.display = checked; (단방향 쓰기 가능 시)
                        }
                    }
                }
            }

            // 2번 컬럼 (Quantity) - SpinBox 사용
            DelegateChoice {
                column: 2
                delegate: Item { // SpinBox를 직접 배치하는 대신 Item으로 감싸서 배경 추가
                    implicitWidth: 100
                    implicitHeight: 35

                    Rectangle { // 배경 및 선택 색상
                        anchors.fill: parent
                        color: tableView.selectionModel && tableView.selectionModel.isRowSelected(row, index) ? "lightblue" : (row % 2 === 0 ? "whitesmoke" : "white")
                        border.color: "lightgray"
                    }

                    SpinBox {
                anchors.fill: parent
                        value: model.display // 'quantity' 역할 데이터 바인딩
                        editable: true
                        // SpinBox 배경을 투명하게 만들어 Item의 배경이 보이도록 함 (스타일에 따라 조정 필요)
                        background: Rectangle { color: "transparent" }
                        onValueModified: {
                            var modifiableRow = fruitModel.getRow(row);
                            modifiableRow.quantity = value;
                            fruitModel.setRow(row, modifiableRow);
                            // 또는 model.display = value;
                        }
                    }
                }
            }

            // 나머지 컬럼 (기본) - Label 사용
            DelegateChoice {
                delegate: Item { // Label을 직접 배치하는 대신 Item으로 감싸서 배경 추가
                    implicitWidth: column === 1 ? 150 : 100 // Type or Price
                    implicitHeight: 35

                    Rectangle { // 배경 및 선택 색상
                        anchors.fill: parent
                        color: tableView.selectionModel && tableView.selectionModel.isRowSelected(row, index) ? "lightblue" : (row % 2 === 0 ? "whitesmoke" : "white")
                        border.color: "lightgray"
                    }

                    Label {
                        id: defaultLabel
                        text: model.display // 'fruitType' 또는 'price' 역할 데이터
                        anchors.verticalCenter: parent.verticalCenter
                        anchors.left: parent.left
                        anchors.leftMargin: 8
                        rightPadding: 8 // 오른쪽 여백 추가
                        elide: Text.ElideRight // 내용이 길면 생략 부호(...) 표시
                        // Price 컬럼은 소수점 2자리까지 표시
                        Component.onCompleted: {
                            if (column === 3) {
                                // model.display가 숫자인지 확인 후 변환
                                var price = parseFloat(model.display);
                                if (!isNaN(price)) {
                                    defaultLabel.text = price.toFixed(2);
                                }
                            }
                        }
                    }
                }
            }
        } // End DelegateChooser

    } // End TableView
}
```

## 참고 사항

*   **모델 요구사항:** `TableView`에 여러 열을 표시하려면 **C++ `QAbstractItemModel`** 또는 **QML `TableModel`**(`Qt.labs.qmlmodels` 모듈)을 사용해야 합니다. `ListModel`을 사용하면 데이터는 첫 번째 열에만 표시됩니다. 예제는 `Qt.labs.qmlmodels.TableModel`을 사용합니다.
*   **모듈 임포트:** `TableView`는 `QtQuick`에, `TableModel`은 `Qt.labs.qmlmodels`에 있습니다. 예제처럼 헤더나 다양한 컨트롤(`CheckBox`, `SpinBox` 등)을 사용하려면 `QtQuick.Controls`도 임포트해야 합니다.
*   **델리게이트 (`delegate`):** 각 **셀**의 내용을 그립니다.
    *   `DelegateChooser`를 사용하면 컬럼별로 다른 시각적 표현(델리게이트)을 쉽게 적용할 수 있습니다.
    *   델리게이트 내에서는 `model.display` (기본 표시 역할 데이터), `row`, `column`, `index` (모델 인덱스), `current` 등의 컨텍스트 프로퍼티에 접근할 수 있습니다.
    *   모델 데이터를 수정하려면 `model.setData()` 또는 `TableModel`의 `setRow()` 같은 메소드를 사용해야 할 수 있습니다. (단순히 `model.display = newValue` 방식은 모델과 역할 설정에 따라 동작하지 않을 수 있습니다.)
    *   선택된 셀/행의 스타일 변경 시: `TableView`의 직접적인 델리게이트 컨텍스트가 아니므로 `selected` 프로퍼티를 직접 사용할 수 없습니다. 대신 각 `DelegateChoice` 내에서 배경 `Rectangle`의 `color` 등을 바인딩할 때 `tableView.selectionModel.isRowSelected(row, index)` 와 같이 `TableView`의 `selectionModel`을 통해 현재 행/셀의 선택 상태를 확인해야 합니다.
*   **헤더 (`HorizontalHeaderView` / `VerticalHeaderView`):** `TableView` 자체에는 헤더 기능이 없습니다. `QtQuick.Controls`의 헤더 뷰 컴포넌트를 `TableView`의 `syncView` 프로퍼티와 연결하여 사용해야 합니다.
*   **성능:** 많은 데이터를 다룰 때는 `reuseItems: true`(기본값)를 유지하고, `columnWidthProvider`/`rowHeightProvider`를 효율적으로 구현하며, 델리게이트를 가볍게 만드는 것이 중요합니다.
*   **편집:** 셀 내용을 직접 편집하게 하려면 `editTriggers` 프로퍼티 설정과 `TableView.editDelegate` 정의가 필요합니다. 예제에서는 `CheckBox`나 `SpinBox`를 사용하여 간접적으로 편집하는 방식을 보여줍니다.
*   **선택 및 네비게이션:** `selectionMode`, `selectionBehavior` (Qt 6.4+)로 선택 방식을 제어하고, `keyNavigationEnabled` (Qt 6.4+)로 키보드 이동을 활성화할 수 있습니다.
*   **정렬/필터링:** 일반적으로 모델 수준(예: C++ `QSortFilterProxyModel`)에서 구현합니다.
*   **시그널 핸들링:** `currentRowChanged`, `clicked`와 같은 `TableView` 시그널은 `onSignalName:` 형태의 핸들러로 직접 연결할 수 없습니다. 예제 하단에 주석으로 표시된 것처럼 `Connections` 요소를 사용하거나 `Component.onCompleted` 등에서 JavaScript의 `connect()` 메소드를 사용해야 합니다.

## 공식 문서 링크

* [TableView QML Type ](https://doc.qt.io/qt-6/qml-qtquick-tableview.html)
* [TableModel QML Type | Qt 6.9](https://doc.qt.io/qt-6/qml-qtqml-models-tablemodel.html) 