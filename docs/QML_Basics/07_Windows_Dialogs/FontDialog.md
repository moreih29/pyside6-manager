# FontDialog

**모듈:** `import QtQuick.Dialogs`

## 개요

`FontDialog`는 사용자가 시스템에 설치된 글꼴과 관련 속성(크기, 스타일 등)을 선택할 수 있는 표준 대화상자를 제공합니다. 이 대화상자는 일반적으로 시스템의 네이티브 글꼴 선택기 UI를 사용합니다.

사용자가 글꼴을 선택하고 'OK'를 누르면 선택된 글꼴 정보를 얻을 수 있습니다.

## 기반 클래스

*   `Dialog` (`QtQuick.Dialogs` 내부 구현)

## 주요 프로퍼티

| 이름           | 타입         | 기본값        | 설명                                                                                               |
| :------------- | :----------- | :------------ | :------------------------------------------------------------------------------------------------- |
| `title`        | `string`     | "Select Font"| 대화상자의 제목 표시줄 텍스트.                                                                       |
| `font`         | `font`       | (시스템 기본값)| 현재 선택된 글꼴 또는 대화상자가 열릴 때 초기에 선택될 글꼴. `font` 타입 객체 (`font.family`, `font.pointSize`, `font.bold` 등). |
| `currentFont`  | `font`       | `font`        | 대화상자 UI 내에 '현재 글꼴'로 표시될 수 있는 글꼴 (참고용).                                           |
| `options`      | `enum flags` | `0`           | 대화상자 옵션 플래그 (`FontDialog.NoButtons`, `FontDialog.MonospacedFonts`).                                |
| `visible`      | `bool`       | `false`       | 대화상자를 표시할지 여부. `open()` 및 `close()` 메서드로 제어됩니다.                                  |
| `modality`     | `Qt.WindowModality` | `Qt.WindowModal` | 대화상자의 모달(modal) 동작 방식.                                                                    |

## 주요 시그널

| 이름         | 파라미터 | 설명                                                                     |
| :----------- | :------- | :----------------------------------------------------------------------- |
| `accepted()` | -        | 사용자가 'OK' 또는 'Accept' 역할의 버튼을 클릭했을 때 발생합니다.               |
| `rejected()` | -        | 사용자가 'Cancel' 또는 'Reject' 역할의 버튼을 클릭했을 때 발생합니다.          |
| `fontChanged`| `font`   | `font` 프로퍼티가 변경될 때 발생합니다 (사용자가 글꼴 속성을 변경할 때).      |
| `currentFontChanged`| `font` | `currentFont` 프로퍼티가 변경될 때 발생합니다.                            |
| `visibleChanged` | `bool`   | `visible` 프로퍼티가 변경될 때 발생합니다.                                 |

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
    width: 400; height: 250
    visible: true
    title: "FontDialog Example"

    FontDialog {
        id: fontDialog
        title: "Choose Text Font"
        font: displayLabel.font // 현재 라벨의 폰트로 초기화

        onAccepted: {
            console.log("Font selected:", fontDialog.font.family, fontDialog.font.pointSize)
            displayLabel.font = fontDialog.font // 선택된 폰트 적용
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
            font.family: "Arial"
            font.pointSize: 14
            font.bold: false
            Layout.alignment: Qt.AlignHCenter
        }

        Button {
            text: "Change Font"
            Layout.alignment: Qt.AlignHCenter
            onClicked: {
                fontDialog.open()
            }
        }
    }
}
```

## 참고 사항

*   `FontDialog`는 `QtQuick.Dialogs` 모듈을 임포트해야 사용할 수 있습니다.
*   `open()` 메소드를 호출하여 대화상자를 표시합니다.
*   `font` 프로퍼티는 QML의 `font` 타입 객체입니다. 이를 사용하여 대화상자의 초기 글꼴을 설정하고, 사용자가 최종적으로 선택한 글꼴 정보(`font.family`, `font.pointSize`, `font.bold`, `font.italic` 등)를 얻을 수 있습니다.
*   `accepted()` 시그널 핸들러 내에서 `font` 프로퍼티 값을 사용하여 사용자가 선택한 글꼴을 애플리케이션의 텍스트 요소에 적용할 수 있습니다.
*   `options` 프로퍼티에 `FontDialog.MonospacedFonts` 플래그를 추가하면 고정폭 글꼴만 표시하도록 제한할 수 있습니다 (시스템 지원 시).
*   대화상자의 실제 모양은 실행되는 운영체제의 네이티브 글꼴 선택기 UI를 따릅니다. 