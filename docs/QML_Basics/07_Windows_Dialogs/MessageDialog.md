# MessageDialog

**모듈:** `import QtQuick.Dialogs`

## 개요

`MessageDialog`는 사용자에게 간단한 메시지(정보, 경고, 질문 등)를 표시하고 표준 버튼(OK, Cancel, Yes, No 등)을 통해 응답을 받는 데 사용되는 편리한 표준 대화상자입니다.

`Dialog` (`QtQuick.Controls`)보다 사용법이 간단하며, 운영체제의 표준 메시지 상자 모양과 비슷하게 표시되는 경우가 많습니다. 아이콘(`icon`)과 상세 텍스트(`informativeText`)를 추가할 수도 있습니다.

## 기반 클래스

*   `Dialog` (`QtQuick.Dialogs` 내부 구현, `QtQuick.Controls`의 `Dialog`와는 다름)

## 주요 프로퍼티

| 이름                | 타입                  | 기본값                      | 설명                                                                                                                                                              |
| :------------------ | :-------------------- | :-------------------------- | :-------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `title`             | `string`              | ""                        | 대화상자의 제목 표시줄 텍스트.                                                                                                                                  |
| `text`              | `string`              | ""                        | 대화상자에 표시될 주 메시지 텍스트.                                                                                                                               |
| `informativeText`   | `string`              | ""                        | 주 메시지(`text`) 아래에 더 자세한 정보를 제공하기 위해 표시될 추가 텍스트.                                                                                           |
| `detailedText`      | `string`              | ""                        | 사용자가 "Show Details..." 버튼(자동으로 생성될 수 있음)을 클릭했을 때 확장되어 보이는 상세 텍스트.                                                                |
| `icon`              | `enumeration`         | `StandardIcon.NoIcon`       | 메시지 옆에 표시될 표준 아이콘 (`NoIcon`, `Information`, `Warning`, `Critical`, `Question`).                                                                        |
| `standardButtons`   | `StandardButton flags`| `StandardButton.Ok`         | 대화상자 하단에 표시될 표준 버튼 조합 (`Ok`, `Cancel`, `Yes`, `No`, `Abort`, `Retry`, `Ignore` 등). `QtQuick.Controls`의 `Dialog`와 동일한 플래그 사용.                         |
| `result`            | `StandardButton`      | (읽기 전용)                 | 대화상자가 닫힐 때 클릭된 표준 버튼 값 (`Ok`, `Cancel`, `Yes`, `No` 등).                                                                                             |
| `visible`           | `bool`                | `false`                     | 대화상자를 표시할지 여부. `open()` 및 `close()` 메서드로 제어됩니다.                                                                                                  |
| `modality`        | `Qt.WindowModality` | `Qt.WindowModal`      | 대화상자의 모달(modal) 동작 방식. 기본적으로 부모 창에 대한 모달(`WindowModal`)입니다.                                                                                |

## 주요 시그널

| 이름         | 파라미터         | 설명                                                                                                                         |
| :----------- | :--------------- | :------------------------------------------------------------------------------------------------------------------------- |
| `accepted()` | -                | `AcceptRole`을 가진 버튼(Ok, Yes 등)이 클릭되었을 때 발생합니다.                                                               |
| `rejected()` | -                | `RejectRole`을 가진 버튼(Cancel, No 등)이 클릭되었을 때 발생합니다.                                                              |
| `helpRequested()` | -             | `HelpRole`을 가진 버튼(Help)이 클릭되었을 때 발생합니다.                                                                       |
| `clickedButton` | `AbstractButton button` | (내부적) 특정 버튼이 클릭되었을 때 발생. `result` 확인이 더 일반적입니다.                                                |
| `visibleChanged` | `bool visible` | `visible` 프로퍼티가 변경될 때 발생합니다.                                                                                   |

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
    width: 400; height: 200
    visible: true
    title: "MessageDialog Example"

    // 정보 메시지 대화상자
    MessageDialog {
        id: infoDialog
        title: "Information"
        text: "Operation completed successfully."
        icon: StandardIcon.Information // 정보 아이콘
        standardButtons: StandardButton.Ok // OK 버튼만 표시
    }

    // 질문 메시지 대화상자
    MessageDialog {
        id: questionDialog
        title: "Confirmation"
        text: "Are you sure you want to quit?"
        informativeText: "All unsaved changes will be lost."
        icon: StandardIcon.Question // 질문 아이콘
        standardButtons: StandardButton.Yes | StandardButton.No // Yes, No 버튼 표시

        // Yes 버튼 클릭 시 처리
        onAccepted: {
            console.log("User chose Yes (result code: " + result + ")")
            Qt.quit() // 애플리케이션 종료
        }

        // No 버튼 클릭 시 처리
        onRejected: {
            console.log("User chose No (result code: " + result + ")")
            // 아무것도 하지 않음
        }
    }

    // 경고 메시지 대화상자 (상세 텍스트 포함)
    MessageDialog {
        id: warningDialog
        title: "Warning"
        text: "An error occurred while processing the file."
        icon: StandardIcon.Warning // 경고 아이콘
        detailedText: "Details:\n- File not found\n- Permission denied"
        standardButtons: StandardButton.Ok
    }

    // 메인 창 내용
    Flow {
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

*   `MessageDialog`는 `QtQuick.Dialogs` 모듈을 임포트해야 사용할 수 있습니다.
*   다른 대화상자처럼 `id`를 부여하고 `open()` 메소드를 호출하여 표시합니다.
*   `text` (주 메시지), `informativeText` (추가 정보), `detailedText` (상세 정보)를 사용하여 다양한 수준의 정보를 전달할 수 있습니다.
*   `icon` 프로퍼티에 `StandardIcon` 열거형 값을 설정하여 메시지 유형에 맞는 표준 아이콘을 표시할 수 있습니다.
*   `standardButtons` 프로퍼티에 원하는 표준 버튼 조합을 설정합니다. 사용자가 클릭한 버튼은 `result` 프로퍼티나 `accepted()`, `rejected()` 등의 시그널을 통해 확인할 수 있습니다.
*   사용자 정의 UI 요소가 필요한 복잡한 대화상자는 `QtQuick.Controls`의 `Dialog`를 사용하는 것이 더 적합합니다.
*   `MessageDialog`의 모양은 실행되는 운영체제의 표준 메시지 상자를 따르는 경우가 많아 플랫폼 간에 다르게 보일 수 있습니다. 