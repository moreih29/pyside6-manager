# ColorDialog

**모듈:** `import QtQuick.Dialogs`

## 개요

`ColorDialog`는 사용자가 색상을 선택할 수 있는 표준 대화상자를 제공합니다. 이 대화상자는 일반적으로 시스템의 네이티브 색상 선택기 UI를 사용합니다.

사용자가 색상을 선택하고 'OK'를 누르면 선택된 색상 정보를 얻을 수 있습니다.

## 기반 클래스

*   `Dialog` (`QtQuick.Dialogs` 내부 구현)

## 주요 프로퍼티

| 이름           | 타입          | 기본값        | 설명                                                                        |
| :------------- | :------------ | :------------ | :-------------------------------------------------------------------------- |
| `title`        | `string`      | "Select Color"| 대화상자의 제목 표시줄 텍스트.                                                |
| `color`        | `color`       | `Qt.black`    | 현재 선택된 색상 또는 대화상자가 열릴 때 초기에 선택될 색상.                    |
| `currentColor` | `color`       | `color`       | 대화상자 UI 내에 '현재 색상'으로 표시될 수 있는 색상 (참고용).                  |
| `options`      | `enum flags`  | `0`           | 대화상자 옵션 플래그 (`ColorDialog.ShowAlphaChannel`, `ColorDialog.NoButtons`). |
| `visible`      | `bool`        | `false`       | 대화상자를 표시할지 여부. `open()` 및 `close()` 메서드로 제어됩니다.          |
| `modality`     | `Qt.WindowModality` | `Qt.WindowModal` | 대화상자의 모달(modal) 동작 방식.                                             |

## 주요 시그널

| 이름         | 파라미터 | 설명                                                            |
| :----------- | :------- | :-------------------------------------------------------------- |
| `accepted()` | -        | 사용자가 'OK' 또는 'Accept' 역할의 버튼을 클릭했을 때 발생합니다.      |
| `rejected()` | -        | 사용자가 'Cancel' 또는 'Reject' 역할의 버튼을 클릭했을 때 발생합니다. |
| `colorChanged`| `color`  | `color` 프로퍼티가 변경될 때 발생합니다 (사용자가 색상을 선택할 때). |
| `currentColorChanged`| `color` | `currentColor` 프로퍼티가 변경될 때 발생합니다.                   |
| `visibleChanged` | `bool`   | `visible` 프로퍼티가 변경될 때 발생합니다.                        |

## 주요 메소드

| 이름      | 파라미터 | 반환타입 | 설명                                            |
| :-------- | :------- | :------- | :---------------------------------------------- |
| `open()`  | -        | -        | 대화상자를 엽니다 (`visible = true`).           |
| `close()` | -        | -        | 대화상자를 닫습니다 (`visible = false`).        |

## 예제

```qml
import QtQuick
import QtQuick.Controls
import QtQuick.Layouts
import QtQuick.Dialogs

Window {
    width: 300; height: 200
    visible: true
    title: "ColorDialog Example"

    ColorDialog {
        id: colorDialog
        title: "Choose Background Color"
        color: displayRect.color // 현재 사각형 색상으로 초기화
        // currentColor: displayRect.color // 현재 색상 표시 (옵션)
        // options: ColorDialog.ShowAlphaChannel // 알파 채널 조절 옵션 활성화

        onAccepted: {
            console.log("Color selected:", colorDialog.color)
            displayRect.color = colorDialog.color // 선택된 색상 적용
        }
        onRejected: {
            console.log("Color selection cancelled.")
        }
    }

    ColumnLayout {
        anchors.centerIn: parent
        spacing: 15

        Rectangle {
            id: displayRect
            width: 100; height: 50
            color: "steelblue" // 초기 색상
            border.color: "black"
            Layout.alignment: Qt.AlignHCenter
        }

        Button {
            text: "Change Color"
            Layout.alignment: Qt.AlignHCenter
            onClicked: {
                colorDialog.open()
            }
        }
    }
}
```

## 참고 사항

*   `ColorDialog`는 `QtQuick.Dialogs` 모듈을 임포트해야 사용할 수 있습니다.
*   `open()` 메소드를 호출하여 대화상자를 표시합니다.
*   `color` 프로퍼티를 사용하여 대화상자가 열릴 때의 초기 색상을 설정하고, 사용자가 최종적으로 선택한 색상 값을 얻습니다.
*   `accepted()` 시그널 핸들러 내에서 `color` 프로퍼티 값을 사용하여 사용자가 선택한 색상을 애플리케이션에 적용할 수 있습니다.
*   `options` 프로퍼티에 `ColorDialog.ShowAlphaChannel` 플래그를 추가하면 사용자가 색상의 투명도(알파 값)까지 조절할 수 있는 UI가 제공될 수 있습니다 (시스템 지원 시).
*   대화상자의 실제 모양은 실행되는 운영체제의 네이티브 색상 선택기 UI를 따릅니다. 