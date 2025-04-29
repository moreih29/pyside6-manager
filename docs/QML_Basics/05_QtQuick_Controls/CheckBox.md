# CheckBox

**모듈:** `import QtQuick.Controls`

## 개요

`CheckBox`는 사용자가 선택하거나 선택 해제할 수 있는 옵션을 나타내는 컨트롤입니다. 일반적으로 텍스트 레이블과 함께 표시되며, 체크 상태를 나타내는 시각적 인디케이터(indicator)를 가집니다.

`CheckBox`는 `AbstractButton`에서 상속받아 `checkable` 프로퍼티가 기본적으로 `true`이며, `checked` 프로퍼티를 통해 상태를 확인하거나 변경할 수 있습니다. `tristate` 프로퍼티를 사용하면 '부분 선택됨(partially checked)' 상태를 추가로 가질 수 있습니다.

## 기반 클래스

*   `AbstractButton`

## 주요 프로퍼티

`AbstractButton` (특히 `Button`)의 프로퍼티 대부분을 상속하며, `CheckBox`에 특화된 주요 프로퍼티는 다음과 같습니다.

| 이름        | 타입   | 기본값             | 설명                                                                                               |
| :---------- | :----- | :----------------- | :------------------------------------------------------------------------------------------------- |
| `text`      | `string`| ""               | 체크박스 옆에 표시될 텍스트 레이블.                                                                   |
| `checked`   | `bool` | `false`            | 체크박스의 현재 체크 상태 (`true`: 체크됨, `false`: 체크 안됨). `checkState`가 `Qt.PartiallyChecked`일 때는 읽기 전용으로 동작할 수 있음. |
| `tristate`  | `bool` | `false`            | 세 가지 상태(`Checked`, `Unchecked`, `PartiallyChecked`)를 사용할지 여부.                              |
| `checkState`| `enum` | `Qt.Unchecked`     | 체크박스의 현재 상태 (`Qt.Checked`, `Qt.Unchecked`, `Qt.PartiallyChecked`). `tristate`가 `false`이면 `PartiallyChecked`는 사용되지 않음. |
| `indicator` | `Item` | (스타일 의존)     | 체크 상태를 시각적으로 나타내는 인디케이터 아이템. 스타일 커스터마이징에 사용.                            |
| `contentItem`| `Item`| (스타일 의존)     | 체크박스의 내용(텍스트 레이블)을 담는 아이템. 스타일 커스터마이징에 사용.                              |
| `background`| `Item`| (스타일 의존)     | 체크박스의 배경 아이템 (보통 투명). 스타일 커스터마이징에 사용.                                      |
| `font`      | `font` | (스타일 의존)     | 텍스트 레이블의 글꼴.                                                                                |
| `enabled`   | `bool` | `true`             | 체크박스가 활성화되어 사용자와 상호작용할 수 있는지 여부.                                              |
| `hoverEnabled`|`bool`| `true`             | 마우스 호버 효과를 사용할지 여부.                                                                    |
| `hovered`   | `bool` | `false`            | (읽기 전용) 마우스 커서가 체크박스 위에 있는지 여부.                                                   |
| `focusPolicy`| `Qt::FocusPolicy`| `Qt::StrongFocus` | 체크박스가 키보드 포커스를 받는 방식.                                                              |
| `ToolTip.visible`, `ToolTip.text`, `ToolTip.delay` | `bool`, `string`, `int` | - | 체크박스에 마우스를 올렸을 때 표시될 툴팁 설정.                                                        |

## 주요 시그널

`AbstractButton`에서 상속받은 시그널 외에 `checkState` 변경 시그널이 있습니다.

| 이름              | 파라미터 | 반환타입 | 설명                                                                                    |
| :---------------- | :------- | :------- | :-------------------------------------------------------------------------------------- |
| `clicked`         | -        | -        | 체크박스가 클릭되었을 때 발생.                                                           |
| `pressed`         | -        | -        | 체크박스가 눌렸을 때 발생.                                                               |
| `released`        | -        | -        | 체크박스에서 마우스/터치가 떼어졌을 때 발생.                                                |
| `toggled`         | -        | -        | `checked` 상태가 변경되었을 때 발생 (사용자 클릭 또는 프로그래밍 방식). `checked`는 인수로 전달되지 않음. |
| `checkStateChanged`| -       | -        | `checkState` 프로퍼티 값이 변경되었을 때 발생.                                             |

## 예제

```qml
import QtQuick
import QtQuick.Controls
import QtQuick.Layouts

Window {
    width: 300
    height: 200
    visible: true
    title: "CheckBox Examples"

    ColumnLayout {
        anchors.verticalCenter: parent.verticalCenter
        anchors.left: parent.left
        anchors.right: parent.right
        anchors.margins: 10
        spacing: 10

        CheckBox {
            id: option1
            text: "Enable Option 1"
            checked: true // 초기에 체크된 상태
            onCheckedChanged: { // checked 프로퍼티 변경 시 핸들러
                console.log("Option 1 checked:", checked)
            }
        }

        CheckBox {
            id: option2
            text: "Enable Option 2"
            // onToggled: console.log("Option 2 toggled") // toggled 시그널 사용 가능
        }

        CheckBox {
            id: option3
            text: "Three-State Option"
            tristate: true // 세 가지 상태 활성화
            checkState: Qt.PartiallyChecked // 초기 상태: 부분 선택됨
            onCheckStateChanged: {
                console.log("Option 3 state changed:", checkState)
                // Qt.Unchecked = 0, Qt.PartiallyChecked = 1, Qt.Checked = 2
                // 클릭 시 상태 순환: Unchecked -> Checked -> (tristate ? PartiallyChecked -> Unchecked : Unchecked)
            }
            // 부분 선택 상태일 때 checked 프로퍼티는 어떻게 되는지 확인
            Component.onCompleted: console.log("Option 3 initial checked:", checked) // 부분 선택 시 false일 수 있음
        }

        CheckBox {
            text: "Disabled CheckBox"
            enabled: false
            checked: true
        }
    }
}
```

## 참고 사항

*   `checked` 프로퍼티는 `true`/`false`만 나타내지만, `checkState` 프로퍼티는 `tristate`가 `true`일 때 `Qt.PartiallyChecked` 상태까지 포함하여 더 정확한 상태를 나타냅니다.
*   사용자가 체크박스를 클릭하면 상태가 순환합니다. `tristate`가 `false`이면 `Unchecked` <-> `Checked`, `tristate`가 `true`이면 `Unchecked` -> `Checked` -> `PartiallyChecked` -> `Unchecked` 순서로 변경될 수 있습니다 (스타일에 따라 순서가 다를 수 있음).
*   여러 옵션 중 하나만 선택하게 하려면 `RadioButton`을 사용하고 `ButtonGroup`으로 묶는 것을 고려하십시오.
*   `indicator`, `contentItem`, `background` 프로퍼티를 통해 체크박스의 시각적 요소를 커스터마이징할 수 있습니다. 