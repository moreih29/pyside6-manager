# RowLayout

**모듈:** `import QtQuick.Layouts`

## 개요

`RowLayout`은 자식 아이템들을 가로(행) 방향으로 나란히 배치하는 레이아웃 컴포넌트입니다. 아이템들은 왼쪽에서 오른쪽으로 순서대로 배치되며, `spacing` 프로퍼티를 통해 아이템 간의 간격을 조절할 수 있습니다.

`RowLayout`은 자식 아이템들의 크기(특히 너비)와 `Layout`의 Attached Properties (`Layout.fillWidth`, `Layout.preferredWidth` 등)를 고려하여 각 아이템의 최종 크기와 위치를 결정합니다.

## 주요 프로퍼티

| 이름      | 타입    | 기본값 | 설명                                     |
| :-------- | :------ | :----- | :--------------------------------------- |
| `spacing` | `real`  | 5      | 자식 아이템들 사이의 간격 (픽셀 단위).  |
| `layoutDirection` | `enum` | `Qt.LeftToRight` | 아이템 배치 방향 (`Qt.LeftToRight` 또는 `Qt.RightToLeft`). |

## Layout Attached Properties (자식 아이템에서 사용)

`RowLayout`의 자식 아이템들은 `Layout`의 Attached Properties를 사용하여 레이아웃 동작 방식을 상세하게 제어할 수 있습니다.

| 이름                  | 타입      | 기본값  | 설명                                                                 |
| :-------------------- | :-------- | :------ | :------------------------------------------------------------------- |
| `Layout.alignment`    | `Qt.Alignment` | `0`     | 아이템의 수직 정렬 방식 (`Qt.AlignTop`, `Qt.AlignVCenter`, `Qt.AlignBottom`). |
| `Layout.fillHeight`   | `bool`    | `false` | 아이템이 레이아웃의 전체 높이를 채우도록 할지 여부.                     |
| `Layout.fillWidth`    | `bool`    | `true`  | 아이템이 레이아웃의 할당된 너비를 채우도록 할지 여부.                   |
| `Layout.maximumHeight`| `real`    | -1      | 아이템의 최대 높이.                                                  |
| `Layout.maximumWidth` | `real`    | -1      | 아이템의 최대 너비.                                                  |
| `Layout.minimumHeight`| `real`    | 0       | 아이템의 최소 높이.                                                  |
| `Layout.minimumWidth` | `real`    | 0       | 아이템의 최소 너비.                                                  |
| `Layout.preferredHeight`| `real`  | -1      | 아이템이 선호하는 높이. `-1`이면 암시적 높이(`implicitHeight`) 사용. |
| `Layout.preferredWidth` | `real`  | -1      | 아이템이 선호하는 너비. `-1`이면 암시적 너비(`implicitWidth`) 사용.   |

## 예제

```qml
import QtQuick
import QtQuick.Layouts

Window {
    width: 300
    height: 100
    visible: true
    title: "RowLayout Example"

    RowLayout {
        anchors.fill: parent
        spacing: 10

        Rectangle {
            color: "lightblue"
            Layout.preferredWidth: 50
            Layout.fillHeight: true // RowLayout 높이 채우기
            Text {
                anchors.centerIn: parent
                text: "Item 1"
            }
        }

        Rectangle {
            color: "lightgreen"
            Layout.fillWidth: true // 남은 너비 채우기
            Layout.minimumWidth: 60 // 최소 너비
            Layout.preferredHeight: 50 // 선호 높이
            Layout.alignment: Qt.AlignVCenter // 수직 중앙 정렬
            Text {
                anchors.centerIn: parent
                text: "Item 2 (fills width)"
            }
        }

        Rectangle {
            color: "lightcoral"
            Layout.preferredWidth: 70
            Layout.preferredHeight: 70 // 선호 높이 지정
            Layout.alignment: Qt.AlignBottom // 하단 정렬
            Text {
                anchors.centerIn: parent
                text: "Item 3"
            }
        }
    }
}
```

## 참고 사항

*   `RowLayout` 자체의 크기는 명시적으로 설정하거나 (`width`, `height`, `anchors`) 부모 레이아웃에 의해 결정됩니다.
*   `Layout.fillWidth`가 `true`인 아이템이 여러 개일 경우, 사용 가능한 공간은 해당 아이템들의 선호 너비(`Layout.preferredWidth`) 비율 또는 기본 비율에 따라 분배됩니다.
*   자식 아이템의 `implicitWidth`와 `implicitHeight`도 레이아웃 계산에 영향을 미칩니다. 