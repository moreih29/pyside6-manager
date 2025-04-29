# TextArea

**모듈:** `import QtQuick.Controls`

## 개요

`TextArea`는 사용자가 여러 줄의 텍스트를 입력하고 편집할 수 있는 컨트롤입니다. `TextField`와 유사한 기능을 제공하지만, 여러 줄 텍스트 처리, 자동 줄 바꿈(word wrap), 스크롤 기능 등이 추가되었습니다.

내부적으로 `TextEdit` 컴포넌트를 사용하여 텍스트 편집 기능을 구현하며, `Flickable`을 통해 스크롤 기능을 제공할 수 있습니다.

## 기반 클래스

*   `TextEdit` (간접적으로 `Item` 상속)

## 주요 프로퍼티

`TextField`와 많은 프로퍼티를 공유하며 (예: `text`, `placeholderText`, `color`, `font`, `readOnly`, `enabled`, `validator`, `inputMethodHints`, `selection` 관련 속성 등), `TextArea`에 특화된 주요 프로퍼티는 다음과 같습니다.

| 이름             | 타입        | 기본값                  | 설명                                                                                                                          |
| :--------------- | :---------- | :---------------------- | :---------------------------------------------------------------------------------------------------------------------------- |
| `wrapMode`       | `enum`      | `TextEdit.WrapAtWordBoundaryOrAnywhere` | 텍스트 줄 바꿈 방식 (`NoWrap`, `WordWrap`, `WrapAnywhere`, `WrapAtWordBoundaryOrAnywhere`).                                       |
| `textFormat`     | `enum`      | `TextEdit.PlainText`   | 입력 및 표시되는 텍스트 형식 (`PlainText`, `RichText`, `StyledText`, `AutoText`). `RichText`는 기본적인 HTML 서식 지원.             |
| `selectByKeyboard`| `bool`     | `true`                  | 키보드(Shift + 화살표 등)로 텍스트를 선택할 수 있는지 여부.                                                                       |
| `persistentSelection`| `bool` | `false`                 | 포커스를 잃어도 텍스트 선택 상태를 유지할지 여부.                                                                                |
| `background`     | `Item`      | (스타일 의존)          | `TextArea`의 배경 아이템. 스타일 커스터마이징에 사용.                                                                           |
| `focusPolicy`    | `Qt::FocusPolicy`| `Qt::StrongFocus`       | `TextArea`가 키보드 포커스를 받는 방식.                                                                                        |
| `up`, `down`, `left`, `right` | `Flickable` | -                       | (읽기 전용) 내부 `Flickable`의 관련 프로퍼티 접근자 (예: `up.atYBeginning`, `left.atXEnd`). 스크롤 상태 확인에 사용될 수 있음. |
| `ScrollBar.vertical`, `ScrollBar.horizontal` | `ScrollBar` | - | 내부 스크롤바 컴포넌트 (스타일에서 제공 시). `TextArea` 외부에서 스크롤바를 연결하거나 제어할 때 사용 가능.                      |
| `ToolTip.visible`, `ToolTip.text`, `ToolTip.delay` | `bool`, `string`, `int` | - | `TextArea`에 마우스를 올렸을 때 표시될 툴팁 설정.                                                                              |

## 주요 시그널

`TextField`와 유사한 시그널(`textChanged`, `textEdited`, `selectionChanged`, `cursorPositionChanged`)을 포함하며, 추가적으로 링크 관련 시그널 등이 있습니다.

| 이름            | 파라미터 | 반환타입 | 설명                                                                               |
| :-------------- | :------- | :------- | :--------------------------------------------------------------------------------- |
| `textChanged`   | -        | -        | `text` 프로퍼티 값이 변경될 때 발생.                                                 |
| `textEdited`    | -        | -        | 사용자의 편집 행위로 인해 `text` 값이 변경될 때 발생.                                |
| `linkActivated` | `string link` | -      | (`textFormat`이 `RichText` 등일 때) 사용자가 텍스트 내의 링크를 클릭했을 때 발생. |
| `linkHovered`   | `string link` | -      | (`textFormat`이 `RichText` 등일 때) 사용자가 텍스트 내의 링크 위에 마우스를 올렸을 때 발생. |

## 주요 메소드

`TextField`와 동일한 메소드(`clear`, `copy`, `cut`, `paste`, `selectAll`, `selectWord`, `deselect`, `insert`, `remove`, `positionToRectangle`, `positionAt`)를 대부분 지원합니다.

| 이름                | 파라미터 | 반환타입 | 설명                                                               |
| :------------------ | :------- | :------- | :----------------------------------------------------------------- |
| `append(string text)`| `string`| `void`  | 텍스트 끝에 문자열 추가.                                           |
| `clearSelection()`  | -        | `void`  | `deselect()`와 동일. 현재 텍스트 선택 해제.                         |
| `ensureVisible(int position)`| `int` | `void` | 지정된 문자 인덱스 위치가 보이도록 스크롤.                           |
| `getFormattedText(int start, int end)` | `int`, `int` | `string`| 지정된 범위의 텍스트를 현재 `textFormat`에 맞춰 서식 정보와 함께 반환. |

## 예제

```qml
import QtQuick
import QtQuick.Controls
import QtQuick.Layouts

Window {
    width: 400
    height: 300
    visible: true
    title: "TextArea Example"

    TextArea {
        id: textArea
        anchors.fill: parent
        anchors.margins: 10

        placeholderText: "Enter multiple lines of text here..."
        wrapMode: TextEdit.WordWrap // 단어 단위 줄 바꿈 활성화
        font.pointSize: 12

        // 내부 스크롤바 사용 (스타일에서 제공하는 경우)
        ScrollBar.vertical: ScrollBar {}

        // 프로그램적으로 텍스트 추가
        Component.onCompleted: {
            textArea.append("\nAppended text line.")
        }

        // 텍스트 변경 시 로그 출력
        onTextChanged: {
            // console.log("TextArea text changed. Length:", length)
        }

        // 선택 영역 변경 시 로그 출력
        onSelectionChanged: {
            // console.log("Selection changed:", selectionStart, "-", selectionEnd)
        }
    }
}
```

## 참고 사항

*   `TextArea`는 기본적으로 수직 스크롤을 지원하며, 필요에 따라 수평 스크롤도 가능합니다 (`wrapMode` 설정에 따라).
*   내장된 스크롤 기능 외에 `TextArea`를 `Flickable` 안에 직접 배치하여 사용할 수도 있습니다 (이 경우 `TextArea` 자체의 스크롤 기능은 비활성화하는 것이 좋음).
*   `textFormat`을 `RichText`로 설정하면 기본적인 HTML 태그 (`<b>`, `<i>`, `<font color=...>`, `<a href=...>` 등)를 사용하여 텍스트 서식을 지정하고 링크를 만들 수 있습니다.
*   성능: 매우 긴 텍스트를 다룰 때는 성능에 영향을 줄 수 있으므로 주의가 필요합니다.
*   한 줄 입력에는 `TextField`를 사용하는 것이 더 적합합니다. 