# GridLayout

**모듈:** `import QtQuick.Layouts`

## 개요

`GridLayout`은 자식 아이템들을 2차원 격자(Grid) 형태로 배치하는 레이아웃 컴포넌트입니다. 아이템들은 지정된 행(row)과 열(column)에 위치하며, 여러 행이나 열에 걸쳐 확장될 수도 있습니다 (`Layout.rowSpan`, `Layout.columnSpan`).

아이템 배치는 `flow`, `layoutDirection` 프로퍼티를 통해 제어할 수 있으며, 행과 열 사이의 간격은 각각 `rowSpacing`과 `columnSpacing`으로 설정합니다.

## 주요 프로퍼티

| 이름             | 타입    | 기본값           | 설명                                                                                                  |
| :--------------- | :------ | :--------------- | :---------------------------------------------------------------------------------------------------- |
| `rows`           | `int`   | 0                | 그리드의 행 수. 0이면 아이템 수에 따라 자동으로 결정됨.                                                 |
| `columns`        | `int`   | 0                | 그리드의 열 수. 0이면 아이템 수에 따라 자동으로 결정됨.                                                 |
| `rowSpacing`     | `real`  | 5                | 행들 사이의 간격 (픽셀 단위).                                                                        |
| `columnSpacing`  | `real`  | 5                | 열들 사이의 간격 (픽셀 단위).                                                                        |
| `flow`           | `enum`  | `GridLayout.LeftToRight` | 아이템 배치 순서 (`LeftToRight`, `TopToBottom`). `RightToLeft`, `BottomToTop` 등도 가능 (layoutDirection과 조합). |
| `layoutDirection`| `enum`  | `Qt.LeftToRight` | 레이아웃 방향 (`Qt.LeftToRight` 또는 `Qt.RightToLeft`). `flow`와 함께 아이템 배치 순서에 영향을 줌.          |

## Layout Attached Properties (자식 아이템에서 사용)

`GridLayout`의 자식 아이템들은 `Layout`의 Attached Properties를 사용하여 위치, 크기, 확장 등을 제어합니다.

| 이름                   | 타입      | 기본값  | 설명                                                                     |
| :--------------------- | :-------- | :------ | :----------------------------------------------------------------------- |
| `Layout.row`           | `int`     | -1      | 아이템이 위치할 행 인덱스. `-1`이면 `flow`에 따라 자동 배치.               |
| `Layout.column`        | `int`     | -1      | 아이템이 위치할 열 인덱스. `-1`이면 `flow`에 따라 자동 배치.               |
| `Layout.rowSpan`       | `int`     | 1       | 아이템이 차지할 행의 수.                                                 |
| `Layout.columnSpan`    | `int`     | 1       | 아이템이 차지할 열의 수.                                                 |
| `Layout.alignment`     | `Qt.Alignment` | `0`     | 셀 내에서 아이템의 정렬 방식 (`Qt.AlignLeft`, `Qt.AlignTop`, `Qt.AlignCenter` 등). |
| `Layout.fillHeight`    | `bool`    | `false` | 아이템이 할당된 셀의 전체 높이를 채우도록 할지 여부.                         |
| `Layout.fillWidth`     | `bool`    | `false` | 아이템이 할당된 셀의 전체 너비를 채우도록 할지 여부.                         |
| `Layout.maximumHeight` | `real`    | -1      | 아이템의 최대 높이.                                                      |
| `Layout.maximumWidth`  | `real`    | -1      | 아이템의 최대 너비.                                                      |
| `Layout.minimumHeight` | `real`    | 0       | 아이템의 최소 높이.                                                      |
| `Layout.minimumWidth`  | `real`    | 0       | 아이템의 최소 너비.                                                      |
| `Layout.preferredHeight`| `real`   | -1      | 아이템이 선호하는 높이. `-1`이면 암시적 높이(`implicitHeight`) 사용.     |
| `Layout.preferredWidth` | `real`   | -1      | 아이템이 선호하는 너비. `-1`이면 암시적 너비(`implicitWidth`) 사용.       |

## 예제

```qml
import QtQuick
import QtQuick.Layouts

Window {
    width: 400
    height: 200
    visible: true
    title: "GridLayout Example"

    GridLayout {
        anchors.fill: parent
        columns: 3 // 3열 그리드
        rowSpacing: 5
        columnSpacing: 10

        // 아이템들은 flow(기본 LeftToRight)에 따라 배치됨
        Rectangle { color: "red"; Layout.fillWidth: true; height: 50; Text { anchors.centerIn: parent; text: "Item 1"} }
        Rectangle { color: "green"; Layout.fillWidth: true; height: 50; Text { anchors.centerIn: parent; text: "Item 2"} }
        Rectangle { color: "blue"; Layout.fillWidth: true; height: 50; Text { anchors.centerIn: parent; text: "Item 3"} }

        // 특정 위치 지정 및 확장
        Rectangle {
            color: "yellow"
            Layout.row: 1
            Layout.column: 0
            Layout.columnSpan: 2 // 2열 차지
            Layout.fillWidth: true
            Layout.preferredHeight: 60
            Text { anchors.centerIn: parent; text: "Item 4 (spans 2 columns)"}
        }

        Rectangle {
            color: "cyan"
            Layout.row: 1 // Item 4와 같은 행
            Layout.column: 2 // 마지막 열
            Layout.fillWidth: true
            Layout.fillHeight: true // 이 셀의 높이 채우기
            Layout.alignment: Qt.AlignCenter // 셀 중앙 정렬
            Text { anchors.centerIn: parent; text: "Item 5"}
        }

        Rectangle {
            color: "magenta"
            Layout.row: 2
            Layout.column: 0
            Layout.columnSpan: 3 // 3열 모두 차지
            Layout.fillWidth: true
            Layout.preferredHeight: 40
            Text { anchors.centerIn: parent; text: "Item 6 (spans 3 columns)"}
        }
    }
}
```

## 참고 사항

*   `rows` 또는 `columns` 중 하나만 지정하면 나머지는 아이템 수에 맞춰 자동으로 계산됩니다.
*   `Layout.row`와 `Layout.column`을 명시적으로 지정하지 않으면 `flow`와 `layoutDirection`에 따라 순서대로 빈 셀에 배치됩니다.
*   `rowSpan`이나 `columnSpan`을 사용할 때 셀이 겹치지 않도록 주의해야 합니다. 