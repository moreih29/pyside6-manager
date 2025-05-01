# ColorDialog

## 모듈 정보

```qml
import QtQuick.Dialogs
```

## 개요

`ColorDialog`는 사용자가 색상을 선택할 수 있는 표준 대화상자를 제공합니다. 이 대화상자는 일반적으로 시스템의 네이티브 색상 선택기 UI를 사용합니다. Qt 6.4부터 `QtQuick.Dialogs` 모듈에 포함되었습니다.

사용자가 색상을 선택하고 'OK'를 누르면 선택된 색상 정보를 `selectedColor` 프로퍼티를 통해 얻을 수 있습니다.

## 기반 클래스

*   `Dialog` (`QtQuick.Dialogs`)

## 주요 프로퍼티

`Dialog`의 프로퍼티 (`title`, `visible`, `modality`, `flags` 등)를 상속받습니다.

| 이름           | 타입          | 기본값        | 설명                                                                                                                                   |
| :------------- | :------------ | :------------ | :------------------------------------------------------------------------------------------------------------------------------------- |
| `selectedColor`| `color`       | `Qt.black`    | 현재 선택된 색상 또는 대화상자가 열릴 때 초기에 선택될 색상.                                                                                    |
| `options`      | `enum flags`  | `0`           | 대화상자 옵션 플래그 (`ShowAlphaChannel`, `NoButtons`, `NoEyeDropperButton` (Qt 6.6+), `DontUseNativeDialog`). 플래그를 `|` 연산자로 조합하여 사용합니다. | 

## 주요 시그널

`Dialog`의 시그널 (`accepted()`, `rejected()`, `visibleChanged` 등)을 상속받습니다.

| 이름            | 파라미터    | 설명                                                            |
| :-------------- | :---------- | :-------------------------------------------------------------- |
| `accepted()`    | -           | 사용자가 'OK' 또는 'Accept' 역할의 버튼을 클릭했을 때 발생합니다.      |
| `rejected()`    | -           | 사용자가 'Cancel' 또는 'Reject' 역할의 버튼을 클릭했을 때 발생합니다. |
| `selectedColorChanged` | `color`    | `selectedColor` 프로퍼티가 변경될 때 발생합니다.                  |

## 주요 메소드

`Dialog`의 메소드 (`open()`, `close()`)를 상속받습니다.

| 이름      | 파라미터 | 반환타입 | 설명                                            |
| :-------- | :------- | :------- | :---------------------------------------------- |
| `open()`  | -        | -        | 대화상자를 엽니다 (`visible = true`).           |
| `close()` | -        | -        | 대화상자를 닫습니다 (`visible = false`).        |

## 예제

```qml
import QtQuick
import QtQuick.Controls // Button, Rectangle 사용
import QtQuick.Layouts // ColumnLayout 사용
import QtQuick.Dialogs // ColorDialog 사용

Window {
    width: 300; height: 200
    visible: true
    title: "ColorDialog Example (Qt 6.4+)"

    ColorDialog {
        id: colorDialog
        title: "Choose Background Color"
        // 'color'/'currentColor' 대신 'selectedColor' 사용
        selectedColor: displayRect.color // 현재 사각형 색상으로 초기화

        // options: ColorDialog.ShowAlphaChannel // 알파 채널 조절 옵션 활성화

        onAccepted: {
            // accepted 시그널에서 selectedColor 프로퍼티로 선택된 색상 접근
            console.log("Color selected:", colorDialog.selectedColor)
            displayRect.color = colorDialog.selectedColor // 선택된 색상을 Rectangle에 적용
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
                // 대화상자 열기 전에 현재 색상으로 selectedColor 업데이트
                colorDialog.selectedColor = displayRect.color
                colorDialog.open()
            }
        }
    }
}
```

## 참고 사항

*   `ColorDialog`는 `QtQuick.Dialogs` 모듈을 임포트해야 사용할 수 있습니다 (Qt 6.4 이상).
*   `open()` 메소드를 호출하여 대화상자를 표시합니다.
*   `selectedColor` 프로퍼티를 사용하여 대화상자가 열릴 때의 초기 색상을 설정하고, 사용자가 최종적으로 선택한 색상 값을 얻습니다.
*   `accepted()` 시그널 핸들러 내에서 `selectedColor` 프로퍼티 값을 사용하여 사용자가 선택한 색상을 애플리케이션에 적용할 수 있습니다.
*   `options` 프로퍼티에 `ColorDialog.ShowAlphaChannel` 플래그를 추가하면 사용자가 색상의 투명도(알파 값)까지 조절할 수 있는 UI가 제공될 수 있습니다 (시스템 지원 시).
*   대화상자의 실제 모양은 실행되는 운영체제의 네이티브 색상 선택기 UI를 따릅니다.

## 공식 문서 링크

* [ColorDialog QML Type | Qt Quick Dialogs 6.9](https://doc.qt.io/qt-6/qml-qtquick-dialogs-colordialog.html) 