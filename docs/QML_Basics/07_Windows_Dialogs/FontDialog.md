# FontDialog

## 모듈 정보

```qml
import QtQuick.Dialogs
```

## 개요

`FontDialog`는 사용자가 시스템에 설치된 글꼴과 관련 속성(크기, 스타일 등)을 선택할 수 있는 표준 대화상자를 제공합니다. 이 대화상자는 일반적으로 시스템의 네이티브 글꼴 선택기 UI를 사용합니다. Qt 6.2부터 `QtQuick.Dialogs` 모듈에 포함되었습니다.

사용자가 글꼴을 선택하고 'OK'를 누르면 선택된 글꼴 정보를 `selectedFont` 프로퍼티를 통해 얻을 수 있습니다.

## 기반 클래스

*   `Dialog` (`QtQuick.Dialogs`)

## 주요 프로퍼티

`Dialog`의 프로퍼티 (`title`, `visible`, `modality`, `flags` 등)를 상속받습니다.

| 이름           | 타입         | 기본값        | 설명                                                                                                                                                   |
| :------------- | :----------- | :------------ | :----------------------------------------------------------------------------------------------------------------------------------------------------- |
| `selectedFont` | `font`       | (시스템 기본값)| 현재 선택된 글꼴 또는 대화상자가 열릴 때 초기에 선택될 글꼴. `font` 타입 객체 (`selectedFont.family`, `selectedFont.pointSize`, `selectedFont.bold` 등). |
| `options`      | `enum flags` | `0`           | 대화상자 옵션 플래그 (`ScalableFonts`, `NonScalableFonts`, `MonospacedFonts`, `ProportionalFonts`, `NoButtons`, `DontUseNativeDialog`). 플래그를 `|` 연산자로 조합. | 

## 주요 시그널

`Dialog`의 시그널 (`accepted()`, `rejected()`, `visibleChanged` 등)을 상속받습니다.

| 이름                 | 파라미터   | 설명                                                            |
| :------------------- | :--------- | :-------------------------------------------------------------- |
| `accepted()`         | -          | 사용자가 'OK' 또는 'Accept' 역할의 버튼을 클릭했을 때 발생합니다.      |
| `rejected()`         | -          | 사용자가 'Cancel' 또는 'Reject' 역할의 버튼을 클릭했을 때 발생합니다. |
| `selectedFontChanged`| `font`     | `selectedFont` 프로퍼티가 변경될 때 발생합니다.                   |

## 주요 메소드

`Dialog`의 메소드 (`open()`, `close()`)를 상속받습니다.

| 이름      | 파라미터 | 반환타입 | 설명                                            |
| :-------- | :------- | :------- | :---------------------------------------------- |
| `open()`  | -        | -        | 대화상자를 엽니다 (`visible = true`).           |
| `close()` | -        | -        | 대화상자를 닫습니다 (`visible = false`).        |

## 예제

```qml
import QtQuick
import QtQuick.Controls // Button, Label 사용
import QtQuick.Layouts // ColumnLayout 사용
import QtQuick.Dialogs // FontDialog 사용

Window {
    width: 400; height: 250
    visible: true
    title: "FontDialog Example (Qt 6.2+)"

    FontDialog {
        id: fontDialog
        title: "Choose Text Font"
        // 'font'/'currentFont' 대신 'selectedFont' 사용
        // selectedFont 프로퍼티는 font 타입 객체
        // 초기 폰트는 대화상자 열기 전에 설정하는 것이 좋음
        // selectedFont.family: displayLabel.font.family // 이런 방식 대신 아래 onClicked 참고

        onAccepted: {
            // accepted 시그널에서 selectedFont 프로퍼티로 선택된 font 객체 접근
            console.log("Font selected - Family:", fontDialog.selectedFont.family,
                        "Size:", fontDialog.selectedFont.pointSize,
                        "Bold:", fontDialog.selectedFont.bold,
                        "Italic:", fontDialog.selectedFont.italic)
            // 선택된 font 객체를 Label의 font 프로퍼티에 직접 할당
            displayLabel.font = fontDialog.selectedFont
        }
        onRejected: {
            console.log("Font selection cancelled.")
        }
    }

    ColumnLayout {
        anchors.centerIn: parent
        spacing: 15

        Label {
            id: displayLabel
            text: "Sample Text"
            // 초기 폰트 설정
            font.family: "Arial"
            font.pointSize: 14
            font.bold: false
            Layout.alignment: Qt.AlignHCenter
        }

        Button {
            text: "Change Font"
            Layout.alignment: Qt.AlignHCenter
            onClicked: {
                // 대화상자 열기 전에 현재 폰트로 selectedFont 설정
                fontDialog.selectedFont = displayLabel.font
                fontDialog.open()
            }
        }
    }
}
```

## 참고 사항

*   `FontDialog`는 `QtQuick.Dialogs` 모듈을 임포트해야 사용할 수 있습니다 (Qt 6.2 이상).
*   `open()` 메소드를 호출하여 대화상자를 표시합니다.
*   `selectedFont` 프로퍼티는 QML의 `font` 타입 객체입니다. 이를 사용하여 대화상자의 초기 글꼴을 설정하고, 사용자가 최종적으로 선택한 글꼴 정보(`selectedFont.family`, `selectedFont.pointSize`, `selectedFont.bold` 등)를 얻을 수 있습니다.
*   `accepted()` 시그널 핸들러 내에서 `selectedFont` 프로퍼티 값을 사용하여 사용자가 선택한 글꼴을 애플리케이션의 텍스트 요소에 적용할 수 있습니다.
*   `options` 프로퍼티에 `FontDialog.MonospacedFonts` 플래그를 추가하면 고정폭 글꼴만 표시하도록 제한할 수 있습니다 (시스템 지원 시).
*   대화상자의 실제 모양은 실행되는 운영체제의 네이티브 글꼴 선택기 UI를 따릅니다.

## 공식 문서 링크

* [FontDialog QML Type | Qt Quick Dialogs 6.9](https://doc.qt.io/qt-6/qml-qtquick-dialogs-fontdialog.html) 