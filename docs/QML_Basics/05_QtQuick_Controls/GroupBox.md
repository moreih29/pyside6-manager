# GroupBox

**모듈:** `import QtQuick.Controls`

## 개요

`GroupBox`는 `Frame`과 유사하게 다른 QML 아이템들을 시각적으로 그룹화하고 테두리와 배경을 제공하는 컨테이너 컨트롤입니다. `Frame`과의 주요 차이점은 `title` 프로퍼티를 통해 그룹 상자의 제목을 표시할 수 있다는 것입니다.

주로 설정 창이나 폼(form) 등에서 관련된 컨트롤들을 논리적인 그룹으로 묶고 제목을 부여하여 UI 구조를 명확하게 표현하는 데 사용됩니다.

## 기반 클래스

*   `Frame`

## 주요 프로퍼티

`Frame`의 프로퍼티를 모두 상속하며 (`background`, `enabled`, `font` 등), `GroupBox`에 추가된 주요 프로퍼티는 다음과 같습니다.

| 이름        | 타입    | 기본값       | 설명                                                                                             |
| :---------- | :------ | :----------- | :----------------------------------------------------------------------------------------------- |
| `title`     | `string`| ""         | 그룹 상자의 상단 테두리에 표시될 제목 텍스트.                                                     |
| `label`     | `Label` | (스타일 의존)| (읽기 전용) 제목(`title`)을 표시하는 데 사용되는 내부 `Label` 컴포넌트. 글꼴, 색상 등 세부 스타일 조정 가능. |

## 예제

```qml
import QtQuick
import QtQuick.Controls
import QtQuick.Layouts

Window {
    width: 350
    height: 300
    visible: true
    title: "GroupBox Example"

    ColumnLayout {
        anchors.fill: parent
        anchors.margins: 10
        spacing: 10

        GroupBox {
            title: "User Profile"
            Layout.fillWidth: true

            // GroupBox 내부에 레이아웃 배치
            GridLayout {
                anchors.fill: parent
                anchors.margins: 5 // GroupBox 내부 여백
                columns: 2

                Label { text: "Name:" }
                TextField { Layout.fillWidth: true; placeholderText: "Enter name" }

                Label { text: "Age:" }
                SpinBox { Layout.fillWidth: true; from: 0; to: 120 }

                Label { text: "Receive Newsletter:" }
                Switch { checked: true }
            }
        }

        GroupBox {
            title: "Options"
            Layout.fillWidth: true
            // 제목 Label 스타일 변경 예시
            label: Label {
                text: parent.title // GroupBox의 title 사용
                font.bold: true
                color: "darkblue"
            }

            RowLayout {
                 anchors.fill: parent
                 anchors.margins: 5
                 CheckBox { text: "Enable Feature X" }
                 CheckBox { text: "Enable Feature Y" }
            }
        }
    }
}
```

## 참고 사항

*   `GroupBox`는 시각적 그룹화와 제목 표시가 주 목적이며, 레이아웃 관리는 `Frame`과 마찬가지로 내부에 배치된 레이아웃 컴포넌트가 담당합니다.
*   `title` 프로퍼티에 문자열을 설정하여 그룹 상자의 제목을 지정합니다.
*   `label` 프로퍼티를 통해 내부적으로 사용되는 `Label` 컴포넌트에 접근하여 제목의 글꼴, 색상 등 세부적인 스타일을 조정할 수 있습니다.
*   배경 및 테두리 스타일링은 상속받은 `Frame`의 `background` 프로퍼티를 통해 가능합니다.
*   단순히 테두리만 필요한 그룹화에는 `Frame`을 사용하는 것이 더 적합할 수 있습니다. 