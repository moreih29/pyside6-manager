# Switch

**모듈:** `import QtQuick.Controls`

## 개요

`Switch`는 두 가지 상태(보통 on/off 또는 true/false) 사이를 전환(토글)하는 데 사용되는 컨트롤입니다. 사용자는 스위치의 핸들을 클릭하거나 드래그하여 상태를 변경할 수 있습니다.

`CheckBox`와 유사하게 boolean 상태(`checked`)를 관리하지만, 시각적으로 스위치 형태를 가지며 모바일 인터페이스 등에서 자주 사용됩니다. `Switch`도 `AbstractButton`을 기반으로 합니다.

## 기반 클래스

*   `AbstractButton`

## 주요 프로퍼티

`AbstractButton`의 프로퍼티를 상속하며, `Switch`에 관련된 주요 프로퍼티는 다음과 같습니다.

| 이름         | 타입   | 기본값         | 설명                                                                                                  |
| :----------- | :----- | :------------- | :---------------------------------------------------------------------------------------------------- |
| `checked`    | `bool` | `false`        | 스위치의 현재 상태 (`true`: on, `false`: off). `checkable`은 항상 `true`로 간주됨.                         |
| `text`       | `string`| ""           | 스위치 옆에 표시될 수 있는 텍스트 레이블 (스타일에 따라 지원 여부 및 위치가 다름).                           |
| `position`   | `real` | (`checked` 기반)| (읽기 전용) 핸들의 시각적 위치 (0.0: off, 1.0: on). 애니메이션 등에 사용될 수 있음.                     |
| `visualPosition`| `real`| (`position` 기반)| (읽기 전용) 드래그 중일 때를 포함한 핸들의 현재 시각적 위치 (0.0 ~ 1.0).                                  |
| `pressed`    | `bool` | `false`        | (읽기 전용) 사용자가 스위치 핸들을 현재 누르고(드래그 중) 있는지 여부.                                  |
| `indicator`  | `Item` | (스타일 의존) | 스위치의 핸들(움직이는 부분) 아이템. 스타일 커스터마이징에 사용.                                          |
| `background` | `Item` | (스타일 의존) | 스위치의 배경(트랙) 아이템. 스타일 커스터마이징에 사용.                                                  |
| `contentItem`| `Item` | (스타일 의존) | 스위치의 내용(텍스트 레이블 등)을 담는 아이템 (스타일이 지원하는 경우). 스타일 커스터마이징에 사용.          |
| `enabled`    | `bool` | `true`         | 스위치가 활성화되어 사용자와 상호작용할 수 있는지 여부.                                                  |
| `hoverEnabled`|`bool` | `true`         | 마우스 호버 효과를 사용할지 여부.                                                                     |
| `hovered`    | `bool` | `false`        | (읽기 전용) 마우스 커서가 스위치 위에 있는지 여부.                                                     |
| `focusPolicy`| `Qt::FocusPolicy`| `Qt::StrongFocus`| 스위치가 키보드 포커스를 받는 방식.                                                                   |
| `ToolTip.visible`, `ToolTip.text`, `ToolTip.delay` | `bool`, `string`, `int` | - | 스위치에 마우스를 올렸을 때 표시될 툴팁 설정.                                                           |

## 주요 시그널

`AbstractButton`에서 상속받은 시그널들을 주로 사용합니다.

| 이름      | 파라미터 | 반환타입 | 설명                                                        |
| :-------- | :------- | :------- | :---------------------------------------------------------- |
| `clicked` | -        | -        | 스위치가 클릭되었을 때 발생. 클릭 시 `checked` 상태가 토글됨. |
| `toggled` | -        | -        | `checked` 상태가 변경되었을 때 발생.                         |

## 예제

```qml
import QtQuick
import QtQuick.Controls
import QtQuick.Layouts

Window {
    width: 300
    height: 200
    visible: true
    title: "Switch Example"

    ColumnLayout {
        anchors.centerIn: parent
        spacing: 15

        Switch {
            id: wifiSwitch
            text: "Wi-Fi" // 일부 스타일은 text 표시 지원
            checked: false // 초기 상태: off
            // onCheckedChanged는 AbstractButton에 정의된 시그널이 아님
            // 상태 변경 감지는 onClicked 또는 onToggled 사용
            onToggled: {
                statusLabel.text = checked ? "Wi-Fi is ON" : "Wi-Fi is OFF"
                console.log("Wi-Fi Switch toggled:", checked)
            }
        }

        Switch {
            id: bluetoothSwitch
            text: "Bluetooth"
            checked: true // 초기 상태: on
        }

        Switch {
            text: "Disabled Switch"
            enabled: false
            checked: true
        }

        Label {
            id: statusLabel
            text: wifiSwitch.checked ? "Wi-Fi is ON" : "Wi-Fi is OFF"
            Layout.alignment: Qt.AlignCenter
            font.bold: true
        }
    }
}
```

## 참고 사항

*   `Switch`는 `CheckBox`와 기능적으로 유사하지만, 시각적인 표현 방식과 사용자 경험(UX)에서 차이가 있습니다. 보통 설정 화면 등에서 on/off 상태를 명확히 보여줄 때 사용됩니다.
*   `checked` 프로퍼티를 통해 스위치의 상태를 확인하고 변경할 수 있습니다.
*   `toggled` 시그널은 `checked` 상태가 변경될 때마다 발생합니다.
*   `position` 프로퍼티(0.0 또는 1.0)는 스위치 상태 전환 애니메이션을 구현할 때 유용하게 사용될 수 있습니다.
*   스타일링은 `indicator`, `background` 등의 프로퍼티나 Qt Quick Controls 스타일 시스템을 통해 가능합니다. 

## 공식 문서 링크

*   [Switch QML Type ](https://doc.qt.io/qt-6/qml-qtquick-controls-switch.html) 