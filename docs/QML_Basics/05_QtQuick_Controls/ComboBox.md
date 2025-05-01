# ComboBox

**모듈:** `import QtQuick.Controls`

## 개요

`ComboBox`는 사용자가 미리 정의된 목록에서 하나의 항목을 선택할 수 있는 드롭다운 목록 컨트롤입니다. 현재 선택된 항목을 표시하며, 클릭하면 선택 가능한 항목들의 목록 팝업(popup)이 나타납니다.

목록에 표시될 데이터는 `model` 프로퍼티를 통해 제공하며, 리스트 모델(ListModel), 문자열 리스트(string list), 숫자(count) 등 다양한 형태의 모델을 사용할 수 있습니다.

## 주요 프로퍼티

| 이름             | 타입                   | 기본값          | 설명                                                                                                                                      |
| :--------------- | :--------------------- | :-------------- | :---------------------------------------------------------------------------------------------------------------------------------------- |
| `model`          | `any`                  | `null`          | 콤보박스 목록에 표시될 데이터를 제공하는 모델. `ListModel`, `QStringList`, `int` (0부터 count-1까지 인덱스), `ObjectModel` 등 사용 가능.             |
| `currentIndex`   | `int`                  | -1              | 현재 선택된 항목의 인덱스. 모델이 없거나 비어있으면 -1.                                                                                     |
| `currentText`    | `string`               | ""            | (읽기 전용) 현재 선택된 항목의 텍스트 표현. `displayText` 또는 모델의 `displayRole` (기본값) 사용.                                             |
| `displayText`    | `string`               | `currentText`   | 콤보박스 자체에 표시될 텍스트. 기본적으로 `currentText`를 사용하지만, 다른 텍스트를 표시하고 싶을 때 설정 가능.                                |
| `count`          | `int`                  | -               | (읽기 전용) 모델에 포함된 항목의 총 개수.                                                                                                 |
| `delegate`       | `Component`            | (스타일 의존)  | 드롭다운 목록의 각 항목을 렌더링하는 델리게이트 컴포넌트. 모델 데이터(`modelData`, `index` 등)에 접근 가능.                       |
| `indicator`      | `Item`                 | (스타일 의존)  | 드롭다운 목록이 있음을 나타내는 인디케이터 아이템 (보통 아래쪽 화살표). 스타일 커스터마이징에 사용.                                            |
| `popup`          | `Popup`                | (스타일 의존)  | 드롭다운 목록을 표시하는 팝업 컴포넌트. 스타일 커스터마이징 및 동작 제어에 사용.                                                             |
| `contentItem`    | `Item`                 | (스타일 의존)  | 콤보박스의 주 내용 영역(현재 선택된 항목 표시). 스타일 커스터마이징에 사용.                                                               |
| `background`     | `Item`                 | (스타일 의존)  | 콤보박스의 배경 아이템. 스타일 커스터마이징에 사용.                                                                                       |
| `editable`       | `bool`                 | `false`         | 사용자가 콤보박스에 직접 텍스트를 입력할 수 있는지 여부. `true`이면 내부적으로 `TextField`를 사용하며, 입력된 텍스트는 모델과 연동될 수 있음. |
| `editText`       | `string`               | `currentText`   | `editable`이 `true`일 때 편집 가능한 텍스트.                                                                                            |
| `validator`      | `Validator`            | `null`          | `editable`이 `true`일 때 입력 텍스트의 유효성 검사기.                                                                                     |
| `inputMethodHints`| `Qt::InputMethodHints`| `Qt.ImhNone`    | `editable`이 `true`일 때 가상 키보드 등에 제공할 입력 힌트.                                                                             |
| `flat`           | `bool`                 | `false`         | `editable`이 `true`일 때, 내부 `TextField`의 배경을 평평하게 표시할지 여부.                                                              |
| `enabled`        | `bool`                 | `true`          | 콤보박스가 활성화되어 사용자와 상호작용할 수 있는지 여부.                                                                                   |
| `down`           | `bool`                 | `false`         | (읽기 전용) 현재 팝업 목록이 열려 있는지 여부 (내부 `Popup`의 `opened`와 유사).                                                            |
| `hoverEnabled`   | `bool`                 | `true`          | 마우스 호버 효과를 사용할지 여부.                                                                                                         |
| `hovered`        | `bool`                 | `false`         | (읽기 전용) 마우스 커서가 콤보박스 위에 있는지 여부.                                                                                      |
| `font`           | `font`                 | (스타일 의존)  | 콤보박스 텍스트의 글꼴.                                                                                                                 |
| `focusPolicy`    | `Qt::FocusPolicy`      | `Qt.StrongFocus`| 콤보박스가 키보드 포커스를 받는 방식.                                                                                                     |
| `textRole`       | `string`               | "text"        | (`editable`이 `true`일 때) 모델에서 `editText`로 사용할 역할(role) 이름.                                                              |
| `valueRole`      | `string`               | "value"       | (`editable`이 `true`일 때, 내부 모델 사용 시) 모델에서 값으로 사용할 역할 이름.                                                           |
| `delegateRole`   | `string`               | ""            | (`editable`이 `true`일 때) 모델에서 델리게이트 컴포넌트로 사용할 역할 이름.                                                               |
| `ToolTip.visible`, `ToolTip.text`, `ToolTip.delay` | `bool`, `string`, `int` | - | 콤보박스에 마우스를 올렸을 때 표시될 툴팁 설정.                                                                                        |

## 주요 시그널

| 이름              | 파라미터 | 반환타입 | 설명                                                                                        |
| :---------------- | :------- | :------- | :------------------------------------------------------------------------------------------ |
| `activated`       | `int index` | -        | 사용자가 목록에서 항목을 선택(활성화)했을 때 발생. 파라미터는 선택된 항목의 인덱스.             |
| `currentIndexChanged`| -      | -        | `currentIndex` 프로퍼티 값이 변경되었을 때 발생.                                               |
| `currentTextChanged` | -      | -        | `currentText` 프로퍼티 값이 변경되었을 때 발생.                                                |
| `accepted`        | -        | -        | (`editable`이 `true`일 때) 사용자가 Enter/Return 키로 편집을 완료했을 때 발생.                 |
| `rejected`        | -        | -        | (`editable`이 `true`일 때) 사용자가 Esc 키로 편집을 취소했을 때 발생.                          |
| `textEdited`      | -        | -        | (`editable`이 `true`일 때) 사용자의 편집 행위로 `editText`가 변경될 때 발생.                   |

## 주요 메소드

| 이름              | 파라미터 | 반환타입 | 설명                                              |
| :---------------- | :------- | :------- | :------------------------------------------------ |
| `textAt(int index)`| `int`  | `string` | 지정된 인덱스에 해당하는 항목의 텍스트를 반환.      |
| `find(string text, Qt::MatchFlags flags)`| `string`, `enum`| `int`| 지정된 텍스트와 일치하는 첫 번째 항목의 인덱스를 반환. |
| `incrementCurrentIndex()` | - | `void` | `currentIndex`를 1 증가시킴.                   |
| `decrementCurrentIndex()` | - | `void` | `currentIndex`를 1 감소시킴.                   |
| `showPopup()`     | -        | `void`   | 드롭다운 목록 팝업을 염.                        |
| `hidePopup()`     | -        | `void`   | 드롭다운 목록 팝업을 닫음.                      |

## 예제

```qml
import QtQuick
import QtQuick.Controls
import QtQuick.Layouts

Window {
    width: 300
    height: 250
    visible: true
    title: "ComboBox Example"

    ColumnLayout {
        anchors.centerIn: parent
        spacing: 15

        Label { text: "Simple List Model:" }
        ComboBox {
            id: simpleCombo
            Layout.fillWidth: true
            model: ["First Item", "Second Item", "Third Item"]
            currentIndex: 1 // 초기 선택: "Second Item"

            onActivated: (index) => {
                console.log("Simple Combo Activated: index=", index, ", text=", textAt(index))
            }
        }

        Label { text: "ListModel with Roles:" }
        ComboBox {
            id: listModelCombo
            Layout.fillWidth: true
            textRole: "name" // 모델의 'name' 역할을 표시 텍스트(currentText)로 사용하도록 명시
            model: ListModel {
                ListElement { name: "Apple"; color: "red" }
                ListElement { name: "Banana"; color: "yellow" }
                ListElement { name: "Orange"; color: "orange" }
            }
            // 현재 선택된 아이템의 색상을 저장할 프로퍼티 추가
            property color currentItemColor: model[currentIndex] ? model[currentIndex].color : "transparent"

            // 커스텀 델리게이트 사용 예시
            delegate: ItemDelegate {
                width: listModelCombo.width
                contentItem: RowLayout {
                    Rectangle { 
                        width: 16; height: 16
                        color: model.color // 모델 데이터 접근
                        radius: 8
                        Layout.alignment: Qt.AlignVCenter
                    }
                    Label {
                        text: model.name // 모델 데이터 접근
                        font: listModelCombo.font
                        elide: Text.ElideRight
                        Layout.fillWidth: true
                    }
                }
                highlighted: listModelCombo.currentIndex === index // 현재 선택된 항목 강조
            }

            // ComboBox 자체에 표시될 내용 (currentText 대신)
            contentItem: RowLayout {
                 Rectangle { 
                    width: 16; height: 16
                    // currentItemColor 프로퍼티에 바인딩
                    color: listModelCombo.currentItemColor
                    radius: 8
                    Layout.alignment: Qt.AlignVCenter
                }
                Label {
                    text: listModelCombo.currentText // 현재 선택된 텍스트
                    font: listModelCombo.font
                    elide: Text.ElideRight
                    Layout.fillWidth: true
                }
            }

            onCurrentIndexChanged: {
                console.log("ListModel Combo Index Changed:", currentIndex)
                // 인덱스 변경 시 currentItemColor 업데이트
                currentItemColor = model[currentIndex] ? model[currentIndex].color : "transparent"
            }
        }

        Label { text: "Editable ComboBox:" }
        ComboBox {
            Layout.fillWidth: true
            editable: true
            model: ["Option 1", "Option 2", "Option 3"]
            onAccepted: {
                console.log("Editable Combo Accepted:", editText)
                // 모델에 없는 텍스트가 입력되면 모델에 추가할 수도 있음
                if (find(editText) === -1) {
                    // model.append({text: editText}) // ListModel인 경우
                     model.push(editText) // JavaScript 배열 모델인 경우
                     currentIndex = count - 1 // 새로 추가된 항목 선택
                }
            }
        }
    }
}
```

## 참고 사항

*   `model` 프로퍼티에는 다양한 데이터 소스를 사용할 수 있습니다. 모델의 각 항목이 어떻게 텍스트로 표시될지는 모델의 역할(role)과 `textRole` 프로퍼티에 따라 결정됩니다.
*   `delegate`를 사용하여 드롭다운 목록의 각 항목 표시 방식을 자유롭게 커스터마이징할 수 있습니다. 델리게이트 내에서는 `modelData` (ListModel 사용 시 역할 이름), `model.<roleName>`, `index` 등의 속성을 사용할 수 있습니다.
*   `editable`을 `true`로 설정하면 사용자가 목록에 없는 값을 직접 입력할 수 있습니다. `onAccepted` 시그널을 처리하여 입력된 값을 모델에 추가하는 등의 로직을 구현할 수 있습니다.
*   팝업(`popup`)의 모양이나 동작을 변경하려면 `popup` 프로퍼티에 접근하여 커스터마이징할 수 있습니다. 

## 공식 문서 링크

*   [ComboBox QML Type ](https://doc.qt.io/qt-6/qml-qtquick-controls-combobox.html) 