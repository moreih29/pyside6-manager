# Label

**모듈:** `import QtQuick.Controls`

## 개요

`Label`은 텍스트를 표시하기 위한 컨트롤입니다. 기본적인 `Text` 요소와 유사하지만, `QtQuick.Controls` 스타일 시스템과 통합되어 일관된 모양과 느낌을 제공하고, 접근성(Accessibility) 및 니모닉(mnemonic) 지원과 같은 추가 기능을 제공합니다.

다른 컨트롤(예: `TextField`, `ComboBox`)과 연관 지어 해당 컨트롤에 대한 설명을 제공하는 용도로 자주 사용됩니다 (`labelFor` 프로퍼티 사용).

## 기반 클래스

*   `Text` (간접적으로 `Item` 상속)

## 주요 프로퍼티

`Text` 요소의 프로퍼티 대부분을 상속하며 (예: `text`, `font`, `color`, `wrapMode`, `elide` 등), `Label`에 특화된 주요 프로퍼티는 다음과 같습니다.

| 이름         | 타입    | 기본값         | 설명                                                                                                                              |
| :----------- | :------ | :------------- | :-------------------------------------------------------------------------------------------------------------------------------- |
| `text`       | `string`| ""           | 레이블에 표시될 텍스트. HTML 부분 집합 및 니모닉 문자(&)를 포함할 수 있음 (`textFormat` 설정에 따라).                                      |
| `textFormat` | `enum`  | `Text.AutoText`| 텍스트 형식 (`PlainText`, `StyledText`, `RichText`, `AutoText`). `StyledText`는 니모닉(&)을 지원. `RichText`는 간단한 HTML 태그 지원.           |
| `font`       | `font`  | (스타일 의존) | 레이블 텍스트의 글꼴.                                                                                                              |
| `color`      | `color` | (스타일 의존) | 레이블 텍스트의 색상.                                                                                                              |
| `enabled`    | `bool`  | `true`         | 레이블이 활성화 상태인지 여부. `false`이면 보통 흐리게 표시됨.                                                                       |
| `elide`      | `enum`  | `Text.ElideNone`| 텍스트가 레이블 너비를 초과할 때 생략(...) 처리 방식 (`ElideLeft`, `ElideMiddle`, `ElideRight`).                                                |
| `wrapMode`   | `enum`  | `Text.NoWrap`  | 텍스트 줄 바꿈 방식 (`NoWrap`, `WordWrap`, `WrapAnywhere`, `WrapAtWordBoundaryOrAnywhere`).                                                  |
| `labelFor`   | `Item`  | `null`         | 이 레이블이 설명하는 대상 컨트롤(예: `TextField`). 설정하면 니모닉(&) 사용 시 해당 컨트롤로 포커스를 이동시키고, 접근성 정보에 사용됨. |
| `background` | `Item`  | `null`         | 레이블의 배경 아이템. 스타일 커스터마이징에 사용 (기본적으로 배경 없음).                                                              |
| `focusPolicy`| `Qt::FocusPolicy`| `Qt.NoFocus`  | 레이블이 키보드 포커스를 받는 방식 (기본적으로 받지 않음).                                                                           |
| `hoverEnabled`|`bool` | `false`        | 마우스 호버 효과를 사용할지 여부 (기본적으로 비활성).                                                                              |
| `hovered`    | `bool` | `false`        | (읽기 전용) 마우스 커서가 레이블 위에 있는지 여부 (`hoverEnabled`가 `true`일 때).                                                 |
| `ToolTip.visible`, `ToolTip.text`, `ToolTip.delay` | `bool`, `string`, `int` | - | 레이블에 마우스를 올렸을 때 표시될 툴팁 설정.                                                                     |

## 주요 시그널

`Text` 요소에서 상속받은 시그널을 포함합니다.

| 이름            | 파라미터 | 반환타입 | 설명                                                                               |
| :-------------- | :------- | :------- | :--------------------------------------------------------------------------------- |
| `textChanged`   | -        | -        | `text` 프로퍼티 값이 변경되었을 때 발생.                                                 |
| `linkActivated` | `string link` | -      | (`textFormat`이 `RichText` 등일 때) 사용자가 텍스트 내의 링크를 클릭했을 때 발생. |
| `linkHovered`   | `string link` | -      | (`textFormat`이 `RichText` 등일 때) 사용자가 텍스트 내의 링크 위에 마우스를 올렸을 때 발생. |

## 예제

```qml
import QtQuick
import QtQuick.Controls
import QtQuick.Layouts

Window {
    width: 300
    height: 200
    visible: true
    title: "Label Example"

    GridLayout {
        anchors.fill: parent
        anchors.margins: 10
        columns: 2

        // 기본 Label
        Label { text: "Username:" }
        TextField { Layout.fillWidth: true }

        // 니모닉(&)을 사용한 Label
        // Alt+E 누르면 연결된 TextField로 포커스 이동 (labelFor 지원 시)
        Label {
            text: "Email:" // 니모닉(&) 제거
            // labelFor: emailField // labelFor 속성 사용 불가 시 제거
            Layout.alignment: Qt.AlignRight | Qt.AlignVCenter // 오른쪽 정렬
        }
        TextField {
            id: emailField
            Layout.fillWidth: true
            placeholderText: "Enter email address"
        }

        // 여러 줄 Label
        Label {
            text: "Description (long text that might wrap or elide):
            This label demonstrates text wrapping and eliding features."
            wrapMode: Text.WordWrap // 단어 단위 줄 바꿈
            // elide: Text.ElideRight // 필요하면 생략(...) 처리
            Layout.columnSpan: 2 // 2열 차지
            Layout.fillWidth: true
        }

        // RichText Label
        Label {
            text: "Visit <a href='http://qt.io'>Qt Website</a> for <b>more</b> info."
            textFormat: Text.RichText
            onLinkActivated: (link) => Qt.openUrlExternally(link) // 링크 열기
            Layout.columnSpan: 2
        }
    }
}
```

## 참고 사항

*   `Label`은 `Text` 요소보다 컨트롤 스타일 시스템과의 통합, 접근성 지원(`labelFor`), 니모닉 지원(`&` 문자) 등에서 이점을 가집니다.
*   `labelFor` 프로퍼티를 사용하여 레이블과 입력 컨트롤을 연결하면 사용자 경험(특히 키보드 네비게이션 및 스크린 리더 사용 시)을 향상시킬 수 있습니다. `text`에 `&` 문자를 사용하여 니모닉(단축키 Alt+문자)을 정의하면 해당 컨트롤로 바로 포커스를 이동시킬 수 있습니다.
*   `textFormat` 프로퍼티를 통해 텍스트를 일반 텍스트, 스타일 텍스트(니모닉 지원), 또는 리치 텍스트(HTML 부분 집합 지원)로 해석하도록 설정할 수 있습니다.
*   텍스트가 영역을 벗어날 경우 `wrapMode`와 `elide` 프로퍼티를 사용하여 줄 바꿈 또는 생략 처리를 제어할 수 있습니다. 

## 공식 문서 링크

*   [Label QML Type ](https://doc.qt.io/qt-6/qml-qtquick-controls-label.html) 