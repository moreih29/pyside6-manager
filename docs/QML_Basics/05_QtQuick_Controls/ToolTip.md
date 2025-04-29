# ToolTip

**모듈:** `import QtQuick.Controls`

## 개요

`ToolTip`은 특정 컨트롤이나 아이템 위에 마우스 커서를 잠시 올려놓았을 때 나타나는 작은 도움말 텍스트 상자입니다. 사용자에게 해당 컨트롤의 기능이나 추가 정보를 간략하게 제공하는 데 사용됩니다.

`ToolTip`은 일반적으로 독립적인 컴포넌트로 사용되기보다는 다른 컨트롤의 **부착 프로퍼티(attached property)** 인 `ToolTip.text`, `ToolTip.delay`, `ToolTip.visible` 등을 통해 사용됩니다.

## 기반 클래스

*   `Popup` (ToolTip 자체를 아이템으로 선언할 경우)

## 주요 부착 프로퍼티 (Attached Properties)

`ToolTip` 기능은 대부분 다른 컨트롤에 부착하여 사용합니다. 주요 부착 프로퍼티는 다음과 같습니다.

| 이름             | 타입    | 기본값        | 설명                                                                                                 |
| :--------------- | :------ | :------------ | :--------------------------------------------------------------------------------------------------- |
| `ToolTip.text`   | `string`| ""          | 툴팁으로 표시될 텍스트 내용. 이 프로퍼티에 값이 설정되면 해당 컨트롤에 마우스를 올렸을 때 툴팁이 나타납니다. |
| `ToolTip.delay`  | `int`   | (스타일 의존) | 마우스 커서를 올린 후 툴팁이 나타나기까지의 지연 시간 (밀리초 단위).                                  |
| `ToolTip.timeout`| `int`   | (스타일 의존) | 툴팁이 자동으로 사라지기까지의 시간 (밀리초 단위). -1이면 자동으로 사라지지 않습니다.                      |
| `ToolTip.visible`| `bool`  | `false`       | 툴팁을 강제로 표시하거나 숨길 때 사용합니다. 일반적으로는 직접 제어하지 않습니다.                         |

## ToolTip 아이템 프로퍼티 (아이템으로 직접 사용할 경우)

`ToolTip`을 `Popup`처럼 독립적인 아이템으로 선언하여 사용할 수도 있지만, 일반적이지는 않습니다. 이때는 `Popup`의 프로퍼티 (`x`, `y`, `opened`, `background` 등)와 함께 `text`, `delay`, `timeout` 프로퍼티를 직접 사용합니다.

## 예제

```qml
import QtQuick
import QtQuick.Controls
import QtQuick.Layouts

Window {
    width: 400
    height: 200
    visible: true
    title: "ToolTip Example"

    Flow {
        anchors.fill: parent
        anchors.margins: 20
        spacing: 10

        Button {
            text: "Hover Me (Default)"
            // 가장 기본적인 사용법: ToolTip.text 설정
            ToolTip.text: "This is a default tooltip."
            ToolTip.delay: 500 // 500ms 지연
        }

        CheckBox {
            text: "Option with Tooltip"
            ToolTip.text: "Check this option to enable feature X."
        }

        TextField {
            placeholderText: "Enter username"
            ToolTip.text: "<i>Username</i> must be at least <b>3</b> characters long."
            // ToolTip.text는 Rich Text 일부 지원
        }

        Slider {
            ToolTip.text: "Adjust the volume level."
            ToolTip.delay: 100 // 더 빠르게 표시
        }

        Switch {
            text: "Toggle Setting"
            ToolTip.text: "Turn this setting on or off."
            ToolTip.timeout: 3000 // 3초 후 자동으로 사라짐
        }

        Rectangle {
            width: 100; height: 50
            color: "lightgray"
            border.color: "gray"
            // 컨트롤이 아닌 일반 Item에도 ToolTip 사용 가능
            ToolTip.text: "This is a Rectangle."

            MouseArea {
                anchors.fill: parent
                hoverEnabled: true // ToolTip을 위해 hover 활성화 필요
            }
        }
    }
}
```

## 참고 사항

*   가장 일반적인 `ToolTip` 사용법은 대상 컨트롤에 `ToolTip.text` 부착 프로퍼티를 설정하는 것입니다.
*   `ToolTip.delay`를 사용하여 툴팁이 나타나는 시간을 조절할 수 있습니다.
*   `ToolTip.timeout`을 사용하여 툴팁이 자동으로 사라지는 시간을 설정할 수 있습니다.
*   `ToolTip.text`는 기본적인 서식(rich text subset)을 지원하여 굵게(`<b>`), 기울임꼴(`<i>`) 등을 사용할 수 있습니다.
*   컨트롤이 아닌 일반 `Item` (예: `Rectangle`)에 툴팁을 사용하려면 내부에 `hoverEnabled`가 `true`인 `MouseArea`가 있어야 합니다. 컨트롤들은 대부분 내부적으로 호버 감지를 처리합니다.
*   `ToolTip`의 시각적 스타일(배경, 글꼴 등)은 현재 적용된 `QtQuick.Controls` 스타일에 따라 결정되며, 필요시 사용자 정의 스타일을 통해 변경할 수 있습니다. 