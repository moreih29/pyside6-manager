# ColumnLayout

## 모듈 정보

```qml
import QtQuick.Layouts
```

## 개요

`ColumnLayout`은 자식 아이템들을 세로(열) 방향으로 위에서 아래로 배치하는 레이아웃 컴포넌트입니다. `RowLayout`과 유사하게 동작하지만 배치 방향이 수직이라는 점이 다릅니다. `spacing` 프로퍼티를 통해 아이템 간의 수직 간격을 조절할 수 있습니다.

`ColumnLayout`은 자식 아이템들의 크기(특히 높이)와 `Layout`의 Attached Properties (`Layout.fillHeight`, `Layout.preferredHeight` 등)를 고려하여 각 아이템의 최종 크기와 위치를 결정합니다.

## 주요 프로퍼티

| 이름      | 타입    | 기본값 | 설명                                   |
| :-------- | :------ | :----- | :------------------------------------- |
| `spacing` | `real`  | 5      | 자식 아이템들 사이의 간격 (픽셀 단위). 기본값은 5입니다. |
| `layoutDirection` | `enum` | `Qt.LeftToRight` | (Layouts 1.1+) 아이템 배치 방향 (`Qt.LeftToRight` 또는 `Qt.RightToLeft`). 기본값은 `Qt.LeftToRight`입니다. *(ColumnLayout에서는 주로 시각적 정렬에 영향)* |
| `uniformCellSizes` | `bool` | `false` | (Layouts 6.6+) `true`이면 모든 셀(아이템)이 동일한 크기를 갖도록 강제합니다. 기본값은 `false`입니다. |

## Layout Attached Properties (자식 아이템에서 사용)

`ColumnLayout`의 자식 아이템들은 `Layout`의 Attached Properties를 사용하여 레이아웃 동작 방식을 상세하게 제어할 수 있습니다.

| 이름                  | 타입      | 기본값  | 설명                                                                  |
| :-------------------- | :-------- | :------ | :------------------------------------------------------------------- |
| `Layout.alignment`    | `Qt.Alignment` | `0`     | 아이템의 수평 정렬 방식 (`Qt.AlignLeft`, `Qt.AlignHCenter`, `Qt.AlignRight`). |
| `Layout.fillHeight`   | `bool`    | `false` | 아이템이 레이아웃의 할당된 높이를 채우도록 할지 여부. 기본값은 `false`입니다. |
| `Layout.fillWidth`    | `bool`    | `false` | 아이템이 레이아웃의 전체 너비를 채우도록 할지 여부.                     |
| `Layout.maximumHeight`| `real`    | -1      | 아이템의 최대 높이.                                                  |
| `Layout.maximumWidth` | `real`    | -1      | 아이템의 최대 너비.                                                  |
| `Layout.minimumHeight`| `real`    | 0       | 아이템의 최소 높이.                                                  |
| `Layout.minimumWidth` | `real`    | 0       | 아이템의 최소 너비.                                                  |
| `Layout.preferredHeight`| `real`  | -1      | 아이템이 선호하는 높이. `-1`이면 암시적 높이(`implicitHeight`) 사용. |
| `Layout.preferredWidth` | `real`  | -1      | 아이템이 선호하는 너비. `-1`이면 암시적 너비(`implicitWidth`) 사용.   |
| `Layout.margins`      | `real`    | 0       | 아이템 주위의 모든 여백. 개별 여백(`leftMargin` 등)을 설정하면 이 값은 무시됩니다. |
| `Layout.leftMargin`   | `real`    | 0       | 아이템 왼쪽 여백. |
| `Layout.rightMargin`  | `real`    | 0       | 아이템 오른쪽 여백. |
| `Layout.topMargin`    | `real`    | 0       | 아이템 위쪽 여백. |
| `Layout.bottomMargin` | `real`    | 0       | 아이템 아래쪽 여백. |
| `Layout.horizontalStretchFactor` | `int` | 0    | 레이아웃 내에서 아이템이 수평으로 늘어나는 비율. 0이면 늘어나지 않음. (ColumnLayout에서는 주로 0) |
| `Layout.verticalStretchFactor`   | `int` | 0    | 레이아웃 내에서 아이템이 수직으로 늘어나는 비율. 0이면 늘어나지 않음. |

## 예제

```qml
import QtQuick
import QtQuick.Layouts

Window {
    width: 200
    height: 300
    visible: true
    title: "ColumnLayout Example"

    ColumnLayout {
        anchors.fill: parent
        spacing: 10

        Rectangle {
            color: "lightblue"
            Layout.preferredHeight: 50
            Layout.fillWidth: true // ColumnLayout 너비 채우기
            Text {
                anchors.centerIn: parent
                text: "Item 1"
            }
        }

        Rectangle {
            color: "lightgreen"
            Layout.fillHeight: true // 남은 높이 채우기
            Layout.minimumHeight: 60 // 최소 높이
            Layout.preferredWidth: 150 // 선호 너비
            Layout.alignment: Qt.AlignHCenter // 수평 중앙 정렬
            Text {
                anchors.centerIn: parent
                text: "Item 2 (fills height)"
            }
        }

        Rectangle {
            color: "lightcoral"
            Layout.preferredHeight: 70
            Layout.preferredWidth: 100 // 선호 너비 지정
            Layout.alignment: Qt.AlignRight // 우측 정렬
            Text {
                anchors.centerIn: parent
                text: "Item 3"
            }
        }
    }
}
```

## 참고 사항

*   `ColumnLayout` 자체의 크기는 명시적으로 설정하거나 (`width`, `height`, `anchors`) 부모 레이아웃에 의해 결정됩니다.
*   `Layout.fillHeight`가 `true`인 아이템이 여러 개일 경우, 사용 가능한 공간은 해당 아이템들의 선호 높이(`Layout.preferredHeight`) 비율 또는 기본 비율에 따라 분배됩니다. (stretch factor가 설정되지 않았을 경우)
*   자식 아이템의 `implicitWidth`와 `implicitHeight`도 레이아웃 계산에 영향을 미칩니다.

## 공식 문서 링크

*   [Qt Quick ColumnLayout QML Type](https://doc.qt.io/qt-6/qml-qtquick-layouts-columnlayout.html) 