# TextField

**모듈:** `import QtQuick.Controls`

## 개요

`TextField`는 사용자가 한 줄의 텍스트를 입력하고 편집할 수 있는 컨트롤입니다. 텍스트 입력, 유효성 검사, 플레이스홀더 텍스트 표시, 에코 모드(비밀번호 입력 등) 등의 기능을 제공합니다.

`TextField`는 기본적인 텍스트 편집 기능을 제공하며, 스타일링을 통해 모양을 변경할 수 있습니다.

## 기반 클래스

*   `TextInput` (간접적으로 `Item` 상속)

## 주요 프로퍼티

| 이름                | 타입                 | 기본값             | 설명                                                                                                                               |
| :------------------ | :------------------- | :----------------- | :--------------------------------------------------------------------------------------------------------------------------------- |
| `text`              | `string`             | ""               | 현재 입력 필드에 표시되고 편집되는 텍스트.                                                                                           |
| `placeholderText`   | `string`             | ""               | 입력 필드가 비어 있고 포커스가 없을 때 표시되는 안내 문구.                                                                             |
| `placeholderTextColor`| `color`            | (스타일 의존)     | `placeholderText`의 색상.                                                                                                          |
| `color`             | `color`              | (스타일 의존)     | 입력된 텍스트의 색상.                                                                                                                |
| `selectedTextColor` | `color`              | (스타일 의존)     | 선택된 텍스트의 색상.                                                                                                              |
| `selectionColor`    | `color`              | (스타일 의존)     | 선택된 텍스트의 배경 색상.                                                                                                         |
| `font`              | `font`               | (스타일 의존)     | 텍스트의 글꼴.                                                                                                                     |
| `readOnly`          | `bool`               | `false`            | 사용자가 텍스트를 편집할 수 없도록 설정. `true`이면 읽기 전용.                                                                          |
| `enabled`           | `bool`               | `true`             | `TextField`가 활성화되어 사용자와 상호작용할 수 있는지 여부. 비활성화되면 보통 흐리게 표시됨.                                               |
| `validator`         | `Validator`          | `null`             | 입력되는 텍스트의 유효성을 검사하는 `Validator` 객체 (예: `IntValidator`, `DoubleValidator`, `RegExpValidator`). 유효하지 않으면 입력이 거부될 수 있음. |
| `inputMask`         | `string`             | ""               | 사용자 입력을 특정 형식으로 제한하는 마스크 문자열 (예: 전화번호, 날짜 형식).                                                            |
| `inputMethodHints`  | `Qt::InputMethodHints` | `Qt.ImhNone`       | 가상 키보드나 입력기에 입력 모드 힌트를 제공 (예: `Qt.ImhDigitsOnly`, `Qt.ImhEmailCharacters`, `Qt.ImhSensitiveData`).                      |
| `echoMode`          | `enum`               | `TextInput.Normal` | 입력된 문자를 표시하는 방식 (`Normal`, `Password`, `NoEcho`, `PasswordEchoOnEdit`). 비밀번호 입력 등에 사용.                             |
| `passwordCharacter` | `string`             | "•" (불릿 문자) | `echoMode`가 `Password` 또는 `PasswordEchoOnEdit`일 때 표시될 문자.                                                                  |
| `passwordMaskDelay` | `int`                | 0                  | `echoMode`가 `PasswordEchoOnEdit`일 때, 입력된 문자가 `passwordCharacter`로 바뀌기 전까지 표시되는 시간 (밀리초). 0이면 즉시 변경.         |
| `maximumLength`     | `int`                | -1                 | 입력 가능한 최대 문자 수. -1이면 제한 없음.                                                                                          |
| `selectByMouse`     | `bool`               | `true`             | 마우스 드래그로 텍스트를 선택할 수 있는지 여부.                                                                                      |
| `persistentSelection`| `bool`            | `false`            | `TextField`가 포커스를 잃어도 텍스트 선택 상태를 유지할지 여부.                                                                        |
| `length`            | `int`                | -                  | (읽기 전용) 현재 `text`의 문자 수.                                                                                                 |
| `cursorPosition`    | `int`                | -                  | 현재 텍스트 커서의 위치 (문자 인덱스).                                                                                               |
| `selectionStart`, `selectionEnd` | `int`    | -                  | 현재 선택된 텍스트의 시작 및 끝 인덱스.                                                                                              |
| `selectedText`      | `string`             | -                  | (읽기 전용) 현재 선택된 텍스트.                                                                                                      |
| `acceptableInput`   | `bool`               | -                  | (읽기 전용) 현재 `text`가 `validator` 또는 `inputMask`에 의해 유효한 상태인지 여부.                                                    |
| `inputMethodComposing`| `bool`             | -                 | (읽기 전용) 현재 입력기(IME)가 조합 중인지 여부.                                                                                    |
| `hoverEnabled`      | `bool`               | `true`             | 마우스 호버 효과를 사용할지 여부.                                                                                                    |
| `hovered`           | `bool`               | `false`            | (읽기 전용) 마우스 커서가 `TextField` 위에 있는지 여부.                                                                              |
| `background`        | `Item`               | (스타일 의존)     | `TextField`의 배경 아이템. 스타일 커스터마이징에 사용.                                                                              |
| `focusPolicy`       | `Qt::FocusPolicy`    | `Qt::StrongFocus`  | `TextField`가 키보드 포커스를 받는 방식.                                                                                           |
| `ToolTip.visible`, `ToolTip.text`, `ToolTip.delay` | `bool`, `string`, `int` | - | `TextField`에 마우스를 올렸을 때 표시될 툴팁 설정.                                                                                 |

## 주요 시그널

`TextInput`에서 상속받거나 `TextField` 자체에서 제공하는 시그널들입니다.

| 이름               | 파라미터 | 반환타입 | 설명                                                                      |
| :----------------- | :------- | :------- | :------------------------------------------------------------------------ |
| `textChanged`      | -        | -        | `text` 프로퍼티 값이 변경될 때 발생.                                        |
| `textEdited`       | -        | -        | 사용자의 편집 행위로 인해 `text` 값이 변경될 때 발생 (프로그래밍 방식 변경 제외). |
| `accepted`         | -        | -        | 사용자가 Enter 또는 Return 키를 눌러 입력 완료를 나타낼 때 발생.           |
| `editingFinished`  | -        | -        | 사용자가 Enter/Return 키를 누르거나 포커스를 잃어 편집이 종료될 때 발생.    |
| `cursorPositionChanged`| -   | -        | `cursorPosition` 값이 변경될 때 발생.                                   |
| `selectionChanged` | -        | -        | `selectionStart` 또는 `selectionEnd` 값이 변경될 때 발생.                 |

## 주요 메소드

`TextInput`에서 상속받은 메소드들입니다.

| 이름                  | 파라미터                   | 반환타입   | 설명                                                                     |
| :-------------------- | :------------------------- | :--------- | :----------------------------------------------------------------------- |
| `clear()`             | -                          | `void`     | `text`를 비움.                                                           |
| `copy()`              | -                          | `void`     | 선택된 텍스트를 클립보드로 복사.                                           |
| `cut()`               | -                          | `void`     | 선택된 텍스트를 잘라내어 클립보드로 이동.                                    |
| `paste()`             | -                          | `void`     | 클립보드의 내용을 현재 커서 위치에 붙여넣기.                               |
| `selectAll()`         | -                          | `void`     | 모든 텍스트를 선택.                                                      |
| `selectWord()`        | -                          | `void`     | 현재 커서 위치의 단어를 선택.                                            |
| `deselect()`          | -                          | `void`     | 현재 텍스트 선택을 해제.                                                 |
| `insert(int position, string text)` | `int`, `string`| `void`    | 지정된 위치에 텍스트 삽입.                                               |
| `remove(int start, int end)` | `int`, `int`     | `void`     | 지정된 범위의 텍스트 제거.                                               |
| `positionToRectangle(int pos)` | `int`         | `QRectF`   | 지정된 문자 인덱스 위치에 해당하는 사각형 영역 반환 (문자 위치 계산용).      |
| `positionAt(int x, int y)` | `int`, `int`   | `int`      | 지정된 좌표(x, y)에 가장 가까운 문자 인덱스 반환.                          |

## 예제

```qml
import QtQuick
import QtQuick.Controls
import QtQuick.Layouts

Window {
    width: 300
    height: 300
    visible: true
    title: "TextField Examples"

    ColumnLayout {
        anchors.fill: parent
        anchors.margins: 10
        spacing: 10

        TextField {
            id: simpleField
            Layout.fillWidth: true
            placeholderText: "Enter some text..."
            onTextChanged: console.log("SimpleField text changed:", text)
            onAccepted: console.log("SimpleField accepted:", text)
        }

        TextField {
            Layout.fillWidth: true
            placeholderText: "Password"
            echoMode: TextInput.Password // 비밀번호 모드
            ToolTip.text: "Enter your password (echo mode)"
        }

        TextField {
            Layout.fillWidth: true
            placeholderText: "Read Only Text"
            text: "You cannot edit this."
            readOnly: true
        }

        TextField {
            id: validatedField
            Layout.fillWidth: true
            placeholderText: "Enter numbers only (IntValidator)"
            // 0부터 100까지의 정수만 입력 허용
            validator: IntValidator { bottom: 0; top: 100; }
            // 유효하지 않은 입력 시 배경색 변경
            background: Rectangle {
                color: validatedField.acceptableInput ? "white" : "mistyrose"
                border.color: "gray"
            }
            onEditingFinished: {
                console.log("ValidatedField editing finished. Acceptable:", acceptableInput)
            }
        }

        TextField {
            Layout.fillWidth: true
            placeholderText: "Input Mask (Phone)"
            // 입력 마스크 적용 (미국 전화번호 형식 예시)
            inputMask: "(999) 999-9999;_"
        }

        Button {
            text: "Select All in Simple Field"
            Layout.alignment: Qt.AlignHCenter
            onClicked: simpleField.selectAll()
        }
    }
}
```

## 참고 사항

*   여러 줄 텍스트 입력에는 `TextArea` 컨트롤을 사용합니다.
*   `validator`나 `inputMask`를 사용하여 사용자 입력 형식을 제한하고 유효성을 검사할 수 있습니다.
*   `echoMode`를 사용하여 비밀번호와 같이 민감한 정보 입력을 처리할 수 있습니다.
*   스타일링은 `background` 프로퍼티나 Qt Quick Controls 스타일 시스템을 통해 가능합니다.
*   `accepted` 시그널은 사용자가 Enter/Return 키로 입력을 '완료'했을 때 발생하며, `editingFinished`는 포커스를 잃었을 때도 발생합니다. 