# BusyIndicator

**모듈:** `import QtQuick.Controls`

## 개요

`BusyIndicator`는 애플리케이션이 현재 작업을 수행 중이거나 데이터를 로드하는 등 사용자가 기다려야 하는 상태임을 시각적으로 나타내는 컨트롤입니다. 일반적으로 회전하는 원이나 애니메이션 형태로 표시되어 작업이 멈추지 않고 진행 중임을 알려줍니다.

`ProgressBar`와 달리, `BusyIndicator`는 구체적인 진행률을 표시하지 않고 단순히 '바쁨' 상태만을 나타냅니다.

## 기반 클래스

*   `Control`

## 주요 프로퍼티

| 이름          | 타입    | 기본값        | 설명                                                                                                       |
| :------------ | :------ | :------------ | :--------------------------------------------------------------------------------------------------------- |
| `running`     | `bool`  | `true`        | 인디케이터 애니메이션의 실행 여부를 제어합니다. `true`이면 애니메이션이 실행되고, `false`이면 멈추고 숨겨질 수 있습니다. |
| `background`  | `Item`  | (스타일 의존) | 인디케이터의 배경 아이템. 일반적으로 사용되지 않거나 투명합니다.                                                   |
| `contentItem` | `Item`  | (스타일 의존) | 실제 애니메이션되는 시각적 요소 (예: 회전하는 이미지, 도형 등)를 담는 아이템. 스타일링의 핵심 부분입니다.                |
| `enabled`     | `bool`  | `true`        | 컨트롤의 활성화 상태.                                                                                        |
| `focusPolicy` | `FocusPolicy`| `Qt.NoFocus`  | 기본적으로 포커스를 받지 않습니다.                                                                           |
| `hoverEnabled`| `bool`  | `false`       | 마우스 호버 효과 활성화 여부.                                                                                |

## 주요 시그널

`BusyIndicator`는 주로 상태 변경을 알리는 시그널은 없지만, 상속받은 `Control`의 일반적인 시그널을 가집니다.

## 예제

```qml
import QtQuick
import QtQuick.Controls
import QtQuick.Layouts

Window {
    width: 300
    height: 200
    visible: true
    title: "BusyIndicator Example"

    ColumnLayout {
        anchors.centerIn: parent
        spacing: 20

        // 기본 BusyIndicator
        BusyIndicator {
            id: indicator1
            Layout.alignment: Qt.AlignHCenter
            running: true // 기본값은 true
        }

        // 실행 상태를 제어하는 예제
        BusyIndicator {
            id: indicator2
            Layout.alignment: Qt.AlignHCenter
            running: startStopSwitch.checked // 스위치 상태에 따라 실행/정지
        }

        Switch {
            id: startStopSwitch
            Layout.alignment: Qt.AlignHCenter
            text: indicator2.running ? "Running" : "Stopped"
            checked: true // 초기 상태는 실행 중
        }

        Button {
            Layout.alignment: Qt.AlignHCenter
            text: "Toggle Indicator 1"
            onClicked: {
                indicator1.running = !indicator1.running
            }
        }
    }
}
```

## 참고 사항

*   `BusyIndicator`의 핵심 프로퍼티는 `running`입니다. 이 값을 `true`로 설정하면 인디케이터가 보이고 애니메이션이 실행되며, `false`로 설정하면 애니메이션이 멈추고 일반적으로 사라집니다 (스타일에 따라 다름).
*   애플리케이션이 백그라운드 작업을 수행하거나 데이터를 로딩하는 동안 `running`을 `true`로 설정하고, 작업이 완료되면 `false`로 설정하는 방식으로 사용합니다.
*   `BusyIndicator`는 시각적인 피드백만 제공하며, 사용자 입력을 막거나 하지는 않습니다. 만약 작업 중 사용자 입력을 막으려면 `BusyIndicator`와 함께 다른 방법 (예: `Overlay`나 입력 비활성화)을 사용해야 할 수 있습니다.
*   `contentItem`을 커스터마이징하여 인디케이터의 모양과 애니메이션을 완전히 변경할 수 있습니다. 기본 스타일은 플랫폼이나 적용된 스타일에 따라 다르게 보일 수 있습니다.
*   `ProgressBar`는 구체적인 진행률을 표시할 수 있을 때 사용하고, `BusyIndicator`는 진행률을 알 수 없거나 단순히 작업 중임을 알릴 때 사용합니다. 