# Dialog

**모듈:** `import QtQuick.Controls`

## 개요

`Dialog`는 사용자 정의 가능한 내용을 담는 기본적인 팝업 대화상자 컨트롤입니다. 제목(`title`), 내용 영역(`contentItem`), 그리고 표준 버튼(`standardButtons`) 또는 사용자 정의 버튼(`footer`)을 포함할 수 있습니다.

`Dialog`는 모달(modal) 또는 비모달(non-modal) 형태로 표시될 수 있으며, 사용자에게 정보를 제공하거나 입력을 요구하는 간단한 상호작용에 사용됩니다. `Popup`을 기반으로 하므로 팝업 관련 프로퍼티(`opened`, `modal`, `dim` 등)를 상속받습니다.

## 기반 클래스

*   `Popup`

## 주요 프로퍼티

| 이름                | 타입                  | 기본값                      | 설명                                                                                                                                                            |
| :------------------ | :-------------------- | :-------------------------- | :-------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `title`             | `string`              | ""                        | 대화상자의 제목 표시줄에 표시될 텍스트.                                                                                                                             |
| `contentItem`       | `Item`                | `null`                      | 대화상자의 주 내용 영역을 구성하는 아이템. 여기에 `Text`, `TextField`, `ColumnLayout` 등 원하는 QML 요소들을 배치합니다.                                               |
| `standardButtons`   | `StandardButton flags`| `Dialog.NoButton`           | 대화상자 하단에 표시될 표준 버튼 조합 (`Dialog.Ok`, `Dialog.Cancel`, `Dialog.Yes`, `Dialog.No` 등). 여러 버튼은 `|` (파이프) 연산자로 조합합니다.                                      |
| `footer`            | `Item`                | `null`                      | 대화상자 하단 영역을 사용자 정의하는 아이템. `standardButtons` 대신 사용하거나 함께 사용하여 추가적인 버튼이나 컨트롤을 배치할 수 있습니다.                                   |
| `implicitContentWidth` | `real`             | (계산됨)                    | `contentItem`의 암시적(implicit) 너비. 대화상자 크기 계산에 사용됩니다.                                                                                             |
| `implicitContentHeight`| `real`             | (계산됨)                    | `contentItem`의 암시적(implicit) 높이. 대화상자 크기 계산에 사용됩니다.                                                                                             |
| `result`            | `int`                 | (읽기 전용)                 | 대화상자가 닫힐 때의 결과 코드. `standardButtons` 중 어떤 버튼이 클릭되었는지 나타냅니다 (`Dialog.Accepted`, `Dialog.Rejected`, 또는 클릭된 `StandardButton` 값). `reject()` 호출 시 `Dialog.Rejected`. |
| `opened`            | `bool`                | `false`                     | `Popup`에서 상속. `true`이면 대화상자가 열리고, `false`이면 닫힙니다. `open()` 및 `close()` 메서드로 제어합니다.                                                        |
| `modal`             | `bool`                | `true`                      | `Popup`에서 상속. `true`이면 모달 대화상자로 표시되어 뒤쪽 창과의 상호작용을 막습니다.                                                                               |
| `dim`               | `bool`                | `modal`과 동일             | `Popup`에서 상속. `true`이고 `modal`일 때 대화상자 뒤의 배경을 어둡게 표시할지 여부.                                                                                 |
| `closePolicy`       | `Popup.ClosePolicy`   | `Popup.CloseOnEscape`       | `Popup`에서 상속. 대화상자가 닫히는 조건 (`CloseOnEscape`, `CloseOnPressOutside`, `CloseOnPressOutsideParent` 등 조합 가능).                                        |

## 주요 시그널

| 이름         | 파라미터 | 설명                                                                                                     |
| :----------- | :------- | :------------------------------------------------------------------------------------------------------- |
| `accepted()` | -        | `standardButtons` 중 `AcceptRole`을 가진 버튼(Ok, Yes 등)이 클릭되거나 `accept()` 메서드가 호출되었을 때 발생합니다. |
| `rejected()` | -        | `standardButtons` 중 `RejectRole`을 가진 버튼(Cancel, No 등)이 클릭되거나 `reject()` 메서드가 호출되었을 때 발생합니다. |
| `applied()`  | -        | `standardButtons` 중 `ApplyRole`을 가진 버튼(Apply 등)이 클릭되었을 때 발생합니다. 대화상자는 닫히지 않습니다.          |
| `discarded()`| -        | 사용자가 `closePolicy`에 따라 대화상자를 닫았을 때 (예: Esc 키, 바깥 클릭) 발생합니다.                               |
| `opened()`   | -        | `Popup`에서 상속. `open()` 메서드가 호출되어 대화상자가 열렸을 때 발생합니다.                                |
| `closed()`   | -        | `Popup`에서 상속. 대화상자가 닫힐 때 발생합니다. `result` 프로퍼티를 확인하여 닫힌 이유를 알 수 있습니다.         |

## 주요 메소드

| 이름      | 파라미터 | 반환타입 | 설명                                                                 |
| :-------- | :------- | :------- | :------------------------------------------------------------------- |
| `open()`  | -        | -        | `Popup`에서 상속. 대화상자를 엽니다 (`opened = true`).                 |
| `close()` | -        | -        | `Popup`에서 상속. 대화상자를 닫습니다 (`opened = false`).              |
| `accept()`| -        | -        | 프로그램적으로 '수락' 동작을 실행합니다 (`accepted` 시그널 발생, `result = Dialog.Accepted`). |
| `reject()`| -        | -        | 프로그램적으로 '거절' 동작을 실행합니다 (`rejected` 시그널 발생, `result = Dialog.Rejected`). |

## 예제

```qml
import QtQuick
import QtQuick.Controls
import QtQuick.Layouts

Window {
    width: 400; height: 300
    visible: true
    title: "Dialog Example"

    // 사용자 정보 입력을 위한 Dialog 정의
    Dialog {
        id: userInfoDialog
        title: "Enter User Information"
        standardButtons: Dialog.Ok | Dialog.Cancel // OK와 Cancel 버튼 표시
        modal: true // 모달로 표시
        width: 300

        // 대화상자 내용 영역
        contentItem: ColumnLayout {
            spacing: 10
            Label { text: "Please enter your name:" }
            TextField { id: nameInput; placeholderText: "Name" }
            Label { text: "Please enter your age:" }
            SpinBox { id: ageInput; from: 0; to: 120 }
        }

        // OK 버튼 클릭 시 처리
        onAccepted: {
            console.log("Dialog Accepted!")
            console.log("Name:", nameInput.text, "Age:", ageInput.value)
            resultLabel.text = "Entered: Name=" + nameInput.text + ", Age=" + ageInput.value
        }

        // Cancel 버튼 클릭 시 처리
        onRejected: {
            console.log("Dialog Rejected!")
            resultLabel.text = "Input cancelled."
        }

        // Dialog가 닫힐 때 입력 필드 초기화 (선택 사항)
        onClosed: {
             nameInput.text = ""
             ageInput.value = 0
        }
    }

    // 메인 창 내용
    ColumnLayout {
        anchors.centerIn: parent
        spacing: 15

        Label {
            id: resultLabel
            text: "Dialog result will be shown here."
            Layout.alignment: Qt.AlignHCenter
        }

        Button {
            text: "Show User Info Dialog"
            Layout.alignment: Qt.AlignHCenter
            onClicked: {
                userInfoDialog.open() // Dialog 열기
            }
        }
    }
}
```

## 참고 사항

*   `Dialog`는 `id`를 부여하고 `open()` 메소드를 호출하여 표시합니다.
*   `contentItem` 프로퍼티에 대화상자의 주 내용을 구성하는 QML 아이템을 배치합니다. 레이아웃(`ColumnLayout` 등)을 사용하여 여러 컨트롤을 배치하는 것이 일반적입니다.
*   `standardButtons` 프로퍼티를 사용하여 OK, Cancel, Yes, No 등 미리 정의된 버튼들을 쉽게 추가할 수 있습니다. 각 버튼의 역할(`AcceptRole`, `RejectRole` 등)에 따라 `accepted()`, `rejected()` 시그널이 발생합니다.
*   `footer` 프로퍼티를 사용하여 표준 버튼 대신 또는 추가로 사용자 정의 버튼이나 다른 컨트롤들을 하단에 배치할 수 있습니다.
*   `result` 프로퍼티와 `closed()` 시그널을 통해 대화상자가 어떻게 닫혔는지 (예: OK 클릭, Cancel 클릭, Esc 키 등) 확인할 수 있습니다.
*   `modal: true`로 설정하면 대화상자가 열려 있는 동안 부모 창과의 상호작용이 차단됩니다.
*   간단한 메시지만 표시하는 경우 `MessageDialog` (`QtQuick.Dialogs`)가 더 편리할 수 있습니다. 

## 공식 문서 링크

* [Dialog QML Type ](https://doc.qt.io/qt-6/qml-qtquick-controls-dialog.html) 