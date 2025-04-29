# RadioButton

**모듈:** `import QtQuick.Controls`

## 개요

`RadioButton`은 여러 옵션 중에서 단 하나만 선택할 수 있는 버튼 컨트롤입니다. 일반적으로 여러 개의 `RadioButton`을 그룹으로 묶어 사용하며, 그룹 내에서는 한 번에 하나의 버튼만 선택(checked)될 수 있습니다.

`RadioButton`은 `AbstractButton`에서 상속받으며, `CheckBox`와 유사하게 텍스트 레이블과 선택 상태를 나타내는 인디케이터(일반적으로 원형)를 가집니다. `autoExclusive` 프로퍼티가 기본적으로 `true`로 설정되어 그룹 내 배타적 선택 동작을 구현합니다.

## 기반 클래스

*   `AbstractButton`

## 주요 프로퍼티

`AbstractButton` (특히 `Button`, `CheckBox`)의 프로퍼티 대부분을 상속하며, `RadioButton`에 특화된 주요 프로퍼티는 다음과 같습니다.

| 이름          | 타입   | 기본값         | 설명                                                                                             |
| :------------ | :----- | :------------- | :----------------------------------------------------------------------------------------------- |
| `text`        | `string`| ""           | 라디오 버튼 옆에 표시될 텍스트 레이블.                                                            |
| `checked`     | `bool` | `false`        | 라디오 버튼의 현재 선택(체크) 상태.                                                               |
| `autoExclusive`| `bool`| `true`         | 같은 부모를 가진 다른 `autoExclusive` 라디오 버튼 중 하나만 `checked` 상태가 되도록 강제.          |
| `indicator`   | `Item` | (스타일 의존) | 선택 상태를 시각적으로 나타내는 인디케이터 아이템 (보통 원형). 스타일 커스터마이징에 사용.        |
| `contentItem` | `Item` | (스타일 의존) | 라디오 버튼의 내용(텍스트 레이블)을 담는 아이템. 스타일 커스터마이징에 사용.                     |
| `background`  | `Item` | (스타일 의존) | 라디오 버튼의 배경 아이템 (보통 투명). 스타일 커스터마이징에 사용.                               |
| `font`        | `font` | (스타일 의존) | 텍스트 레이블의 글꼴.                                                                             |
| `enabled`     | `bool` | `true`         | 라디오 버튼이 활성화되어 사용자와 상호작용할 수 있는지 여부.                                       |
| `hoverEnabled`| `bool` | `true`         | 마우스 호버 효과를 사용할지 여부.                                                                |
| `hovered`     | `bool` | `false`        | (읽기 전용) 마우스 커서가 라디오 버튼 위에 있는지 여부.                                            |
| `focusPolicy` | `Qt::FocusPolicy`| `Qt::StrongFocus`| 라디오 버튼이 키보드 포커스를 받는 방식.                                                            |
| `ToolTip.visible`, `ToolTip.text`, `ToolTip.delay` | `bool`, `string`, `int` | - | 라디오 버튼에 마우스를 올렸을 때 표시될 툴팁 설정.                                                 |

## 주요 시그널

`AbstractButton`에서 상속받은 시그널들을 주로 사용합니다.

| 이름      | 파라미터 | 반환타입 | 설명                                                                   |
| :-------- | :------- | :------- | :--------------------------------------------------------------------- |
| `clicked` | -        | -        | 라디오 버튼이 클릭되었을 때 발생. 클릭 시 `checked` 상태가 보통 변경됨. |
| `toggled` | -        | -        | `checked` 상태가 변경되었을 때 발생.                                    |

## 예제

`RadioButton`은 보통 `ButtonGroup` (Qt Quick 모듈) 또는 레이아웃 컨테이너(`ColumnLayout`, `RowLayout` 등)와 함께 사용하여 그룹화합니다. `autoExclusive`가 `true`이면 같은 부모 아이템 내에서 자동으로 그룹화됩니다.

```qml
import QtQuick
import QtQuick.Controls
import QtQuick.Layouts

Window {
    width: 300
    height: 200
    visible: true
    title: "RadioButton Example"

    ColumnLayout {
        anchors.centerIn: parent
        spacing: 10

        Label { text: "Choose an option:" }

        // 방법 1: 같은 부모(ColumnLayout)를 이용한 자동 그룹화
        RadioButton {
            id: optionA
            text: "Option A"
            checked: true // 초기 선택값
            onClicked: console.log("Option A selected")
        }
        RadioButton {
            id: optionB
            text: "Option B"
            onClicked: console.log("Option B selected")
        }
        RadioButton {
            id: optionC
            text: "Option C (Disabled)"
            enabled: false
        }

        // 선택된 항목 확인 버튼 (예시)
        Button {
            text: "Show Selection"
            Layout.topMargin: 10
            onClicked: {
                if (optionA.checked) console.log("Current selection: A")
                else if (optionB.checked) console.log("Current selection: B")
                // optionC는 disabled이므로 checked는 항상 false
            }
        }
    }

    /* // 방법 2: ButtonGroup 사용 (Qt Quick 모듈 필요)
    ButtonGroup {
        id: radioGroup
        // autoExclusive: true // ButtonGroup 자체는 이 속성 없음
    }
    ColumnLayout {
        ...
        RadioButton { text: "Option X"; ButtonGroup.group: radioGroup }
        RadioButton { text: "Option Y"; ButtonGroup.group: radioGroup; checked: true }
        RadioButton { text: "Option Z"; ButtonGroup.group: radioGroup }
        Button {
            text: "Show Selection"
            onClicked: {
                 if(radioGroup.checkedButton) {
                      console.log("Current selection:", radioGroup.checkedButton.text)
                 }
            }
        }
    }
    */
}
```

## 참고 사항

*   `autoExclusive`가 `true` (기본값)인 `RadioButton`들은 같은 시각적 부모(parent) 아이템 내에서 자동으로 하나의 그룹으로 묶여 동작합니다. 즉, 하나를 선택하면 같은 부모 아래 다른 라디오 버튼은 자동으로 선택 해제됩니다.
*   명시적으로 그룹을 관리하거나 다른 부모를 가진 라디오 버튼들을 묶으려면 `ButtonGroup` (Qt Quick 모듈)을 사용할 수 있습니다. 이 경우 각 `RadioButton`의 `ButtonGroup.group` Attached Property를 해당 `ButtonGroup`의 `id`로 설정합니다.
*   `CheckBox`와 달리 `RadioButton`은 일반적으로 선택 해제가 아닌 다른 옵션 선택을 통해 상태가 변경됩니다.
*   스타일링은 `indicator`, `contentItem`, `background` 프로퍼티나 Qt Quick Controls 스타일 시스템을 통해 가능합니다. 