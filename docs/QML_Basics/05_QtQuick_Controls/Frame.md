# Frame

## 모듈 정보

```qml
import QtQuick.Controls
```

## 개요

`Frame`은 다른 QML 아이템들을 시각적으로 그룹화하고 테두리(border) 및 배경(background)을 제공하는 컨테이너 컨트롤입니다. 주로 관련된 컨트롤들을 묶어 UI 구조를 명확하게 하거나 시각적인 구분을 위해 사용됩니다.

`Frame` 자체는 레이아웃 기능(예: 자식 자동 배치)을 제공하지 않으므로, 내부에 `ColumnLayout`, `RowLayout`, `GridLayout` 등을 배치하여 자식 아이템들의 레이아웃을 관리하는 것이 일반적입니다.

## 기반 클래스

*   `Control`

## 주요 프로퍼티

| 이름         | 타입   | 기본값         | 설명                                                                     |
| :----------- | :----- | :------------- | :----------------------------------------------------------------------- |
| `background` | `Item` | (스타일 의존) | 프레임의 배경 아이템. 테두리 및 배경 스타일링을 위해 접근 및 커스터마이징 가능. |
| `enabled`    | `bool` | `true`         | 프레임 및 내부 컨트롤들의 활성화 상태에 영향을 줄 수 있음 (스타일 의존).        |
| `focusPolicy`| `Qt::FocusPolicy`| `Qt.NoFocus`  | 프레임 자체의 포커스 정책 (기본적으로 포커스 받지 않음).                  |
| `font`       | `font` | (스타일 의존) | 프레임 내부에 배치될 컨트롤들의 기본 글꼴에 영향을 줄 수 있음 (상속).      |
| `ToolTip.visible`, `ToolTip.text`, `ToolTip.delay` | `bool`, `string`, `int` | - | 프레임에 마우스를 올렸을 때 표시될 툴팁 설정.                           |

## 예제

```qml
import QtQuick
import QtQuick.Controls
import QtQuick.Layouts

Window {
    width: 300
    height: 250
    visible: true
    title: "Frame Example"

    ColumnLayout { // 전체 레이아웃
        anchors.fill: parent
        anchors.margins: 10
        spacing: 10

        Frame {
            id: loginFrame
            Layout.fillWidth: true
            // Frame 자체는 레이아웃 기능이 없으므로 내부 레이아웃 사용
            ColumnLayout {
                anchors.fill: parent
                anchors.margins: 10 // Frame 내부 여백
                spacing: 5

                Label { text: "Login Information" }
                TextField {
                    Layout.fillWidth: true
                    placeholderText: "Username"
                }
                TextField {
                    Layout.fillWidth: true
                    placeholderText: "Password"
                    echoMode: TextInput.Password
                }
                Button {
                    text: "Login"
                    Layout.alignment: Qt.AlignRight
                }
            }
            // 프레임 배경 스타일링 (예시)
            background: Rectangle {
                border.color: "gray"
                border.width: 1
                radius: 4
            }
        }

        Frame {
            Layout.fillWidth: true
            enabled: false // 비활성화된 프레임
            RowLayout {
                anchors.fill: parent
                anchors.margins: 10
                Label { text: "Disabled Section" }
                CheckBox { text: "Option"; checked: true }
            }
        }
    }
}
```

## 참고 사항

*   `Frame`은 시각적 그룹화와 테두리/배경 제공이 주 목적이며, 레이아웃 관리는 내부에 배치된 레이아웃 컴포넌트(`ColumnLayout` 등)가 담당합니다.
*   `GroupBox`는 `Frame`과 유사하지만 `title` 프로퍼티를 통해 그룹 상자 제목을 표시할 수 있는 기능을 추가로 제공합니다.
*   `background` 프로퍼티를 통해 프레임의 배경(테두리 포함)을 커스터마이징할 수 있습니다. `Rectangle` 등을 사용하여 원하는 모양을 만들 수 있습니다.
*   `enabled` 프로퍼티를 `false`로 설정하면 프레임과 그 안에 포함된 모든 컨트롤들이 시각적으로 비활성화 상태로 표시될 수 있습니다 (스타일에 따라 다름). 

## 공식 문서 링크

*   [Frame QML Type ](https://doc.qt.io/qt-6/qml-qtquick-controls-frame.html) 