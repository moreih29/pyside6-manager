# MessageDialog

**모듈:** `import QtQuick.Dialogs` (Qt 6.3+)

## 개요

`MessageDialog`는 사용자에게 간단한 메시지(정보, 경고, 질문 등)를 표시하고 표준 버튼(Ok, Cancel, Yes, No 등)을 통해 응답을 받는 데 사용되는 편리한 표준 대화상자입니다. Qt 6.3부터 `QtQuick.Dialogs` 모듈에 포함되었습니다.

운영체제의 표준 메시지 상자 모양과 비슷하게 표시되는 경우가 많습니다. 주 텍스트(`text`), 정보 텍스트(`informativeText`), 상세 텍스트(`detailedText`)를 사용하여 메시지를 전달할 수 있습니다.

## 기반 클래스

*   `Dialog` (`QtQuick.Dialogs`)

## 주요 프로퍼티

`Dialog`의 프로퍼티 (`title`, `visible`, `modality`, `flags` 등)를 상속받습니다.

| 이름                | 타입                  | 기본값                      | 설명                                                                                                                                                              |
| :------------------ | :-------------------- | :-------------------------- | :-------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `text`              | `string`              | ""                        | 대화상자에 표시될 주 메시지 텍스트.                                                                                                                               |
| `informativeText`   | `string`              | ""                        | 주 메시지(`text`) 아래에 더 자세한 정보를 제공하기 위해 표시될 추가 텍스트.                                                                                           |
| `detailedText`      | `string`              | ""                        | 사용자가 "Show Details..." 버튼(자동으로 생성될 수 있음)을 클릭했을 때 확장되어 보이는 상세 텍스트.                                                                |
| `buttons`           | `flags`               | `MessageDialog.NoButton`    | 대화상자 하단에 표시될 버튼 조합. `MessageDialog.Ok`, `MessageDialog.Cancel`, `MessageDialog.Yes`, `MessageDialog.No`, `MessageDialog.Save` 등 다양한 플래그를 `|` 연산자로 조합합니다. |

## 주요 시그널

`Dialog`의 시그널 (`accepted()`, `rejected()`, `visibleChanged` 등)을 상속받습니다.

| 이름            | 파라미터                                          | 설명                                                                                                                                 |
| :-------------- | :------------------------------------------------ | :----------------------------------------------------------------------------------------------------------------------------------- |
| `accepted()`    | -                                                 | `AcceptRole` 또는 `YesRole`을 가진 버튼(Ok, Yes, Save 등)이 클릭되었을 때 발생합니다.                                                     |
| `rejected()`    | -                                                 | `RejectRole` 또는 `NoRole`을 가진 버튼(Cancel, No, Abort 등)이 클릭되었을 때 발생합니다.                                                      |
| `buttonClicked` | `StandardButton button`, `ButtonRole role`        | 어떤 버튼이든 클릭되었을 때 발생합니다. `button` 파라미터는 클릭된 버튼 종류(`MessageDialog.Ok` 등), `role`은 버튼의 역할(`AcceptRole`, `RejectRole` 등)을 나타냅니다. | 

## 주요 메소드

`Dialog`의 메소드 (`open()`, `close()`)를 상속받습니다.

| 이름      | 파라미터 | 반환타입 | 설명                                            |
| :-------- | :------- | :------- | :---------------------------------------------- |
| `open()`  | -        | -        | 대화상자를 엽니다 (`visible = true`).           |
| `close()` | -        | -        | 대화상자를 닫습니다 (`visible = false`).        |

## 예제

```qml
import QtQuick
import QtQuick.Controls // Button 사용
import QtQuick.Layouts // Flow 사용
import QtQuick.Dialogs // MessageDialog 사용

Window {
    width: 400; height: 200
    visible: true
    title: "MessageDialog Example (Qt 6.3+)"

    // 정보 메시지 대화상자
    MessageDialog {
        id: infoDialog
        title: "Information"
        text: "Operation completed successfully."
        // icon 프로퍼티는 Qt 6.3+ MessageDialog에 없음
        buttons: MessageDialog.Ok // 'standardButtons' 대신 'buttons' 사용

        onAccepted: {
            console.log("Info dialog accepted (OK clicked).")
        }
    }

    // 질문 메시지 대화상자
    MessageDialog {
        id: questionDialog
        title: "Confirmation"
        text: "Are you sure you want to quit?"
        informativeText: "All unsaved changes will be lost."
        // icon 프로퍼티 없음
        buttons: MessageDialog.Yes | MessageDialog.No // 여러 버튼 조합

        // Yes 버튼 클릭 시 (AcceptRole 또는 YesRole)
        onAccepted: {
            console.log("User chose Yes.")
            Qt.quit() // 애플리케이션 종료
        }

        // No 버튼 클릭 시 (RejectRole 또는 NoRole)
        onRejected: {
            console.log("User chose No.")
            // 아무것도 하지 않음
        }

        // 또는 buttonClicked 시그널 사용
        // onButtonClicked: (button, role) => {
        //     if (button === MessageDialog.Yes) {
        //         console.log("Yes button clicked (via buttonClicked)")
        //         Qt.quit()
        //     } else if (button === MessageDialog.No) {
        //         console.log("No button clicked (via buttonClicked)")
        //     }
        // }
    }

    // 경고 메시지 대화상자 (상세 텍스트 포함)
    MessageDialog {
        id: warningDialog
        title: "Warning"
        text: "An error occurred while processing the file."
        // icon 프로퍼티 없음
        detailedText: "Details:\n- File not found\n- Permission denied"
        buttons: MessageDialog.Ok
    }

    // 메인 창 내용
    Flow { // 버튼 배치를 위해 Flow 사용 (Layouts도 가능)
        anchors.centerIn: parent
        spacing: 10

        Button {
            text: "Show Info"
            onClicked: infoDialog.open()
        }
        Button {
            text: "Show Question"
            onClicked: questionDialog.open()
        }
        Button {
            text: "Show Warning"
            onClicked: warningDialog.open()
        }
    }
}
```

## 참고 사항

*   `MessageDialog`는 `QtQuick.Dialogs` 모듈을 임포트해야 사용할 수 있습니다 (Qt 6.3 이상).
*   다른 대화상자처럼 `id`를 부여하고 `open()` 메소드를 호출하여 표시합니다.
*   `text` (주 메시지), `informativeText` (추가 정보), `detailedText` (상세 정보)를 사용하여 다양한 수준의 정보를 전달할 수 있습니다.
*   Qt 6.3 이후 버전의 `MessageDialog`에는 `icon` 프로퍼티가 없습니다. 아이콘 표시는 플랫폼에 따라 다를 수 있습니다.
*   `buttons` 프로퍼티에 `MessageDialog.Ok`, `MessageDialog.Cancel` 등 원하는 버튼 플래그를 `|` (bitwise OR) 연산자로 조합하여 설정합니다.
*   사용자가 클릭한 버튼의 역할(AcceptRole, RejectRole 등)에 따라 `accepted()` 또는 `rejected()` 시그널이 발생합니다. `buttonClicked` 시그널을 사용하여 클릭된 특정 버튼 종류(`MessageDialog.Ok` 등)와 역할(`AcceptRole` 등)을 직접 확인할 수도 있습니다.
*   사용자 정의 UI 요소가 필요한 복잡한 대화상자는 `QtQuick.Controls`의 `Dialog`를 사용하는 것이 더 적합합니다.
*   `MessageDialog`의 모양은 실행되는 운영체제의 표준 메시지 상자를 따르는 경우가 많아 플랫폼 간에 다르게 보일 수 있습니다.

## 공식 문서 링크

* [MessageDialog QML Type | Qt Quick Dialogs 6.9](https://doc.qt.io/qt-6/qml-qtquick-dialogs-messagedialog.html) 