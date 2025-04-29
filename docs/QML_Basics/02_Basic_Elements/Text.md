# Text

`Text`는 화면에 텍스트를 표시하는 데 사용되는 기본적인 QML 컴포넌트입니다. 다양한 서식 옵션을 통해 텍스트의 모양과 레이아웃을 제어할 수 있습니다.

## 모듈 정보

```qml
import QtQuick 2.15 // 또는 사용하는 Qt Quick 버전
```

## 개요

`Text` 요소는 문자열(`text` 프로퍼티)을 화면에 렌더링합니다. 글꼴(`font` 그룹 프로퍼티), 색상(`color`), 정렬(`horizontalAlignment`, `verticalAlignment`), 줄 바꿈(`wrapMode`), 생략 부호(`elide`), 서식 있는 텍스트(`textFormat`) 등 다양한 프로퍼티를 통해 텍스트의 시각적 표현을 상세하게 설정할 수 있습니다.

## 기반 클래스

`Item`

## 주요 프로퍼티

| 이름                 | 타입                 | 기본값                       | 설명                                                                                                                                        |
| :------------------- | :------------------- | :--------------------------- | :---------------------------------------------------------------------------------------------------------------------------------------- |
| `text`               | `string`             | `""`                       | 표시할 텍스트 문자열입니다. HTML과 유사한 서식 태그를 포함할 수 있습니다 (`textFormat` 설정에 따라).                                                         |
| `font`               | `QtObject`           | (시스템 기본 글꼴)          | 텍스트 글꼴 속성을 관리하는 그룹 객체입니다. 하위 프로퍼티로 `family`, `pointSize`, `pixelSize`, `bold`, `italic`, `underline`, `strikeout` 등을 가집니다.                        |
| `color`              | `color`              | (시스템 기본 색상)          | 텍스트의 색상입니다.                                                                                                                          |
| `wrapMode`           | `enum`               | `Text.NoWrap`                | 텍스트 너비가 `width` 프로퍼티를 초과할 때 줄 바꿈 처리 방식을 지정합니다. (`NoWrap`, `WordWrap`, `WrapAnywhere`, `Wrap`)                                          |
| `elide`              | `enum`               | `Text.ElideNone`             | 텍스트가 지정된 너비나 높이에 맞지 않을 때 생략 부호(...)를 표시할 위치를 지정합니다. (`ElideNone`, `ElideLeft`, `ElideMiddle`, `ElideRight`)                                  |
| `horizontalAlignment`| `enum`               | `Text.AlignLeft`             | 가로 정렬 방식을 지정합니다. (`AlignLeft`, `AlignRight`, `AlignHCenter`, `AlignJustify`)                                                              |
| `verticalAlignment`  | `enum`               | `Text.AlignTop`              | 세로 정렬 방식을 지정합니다. (`AlignTop`, `AlignBottom`, `AlignVCenter`)                                                                       |
| `textFormat`         | `enum`               | `Text.PlainText`             | `text` 프로퍼티를 해석하는 방식을 지정합니다. (`PlainText`, `StyledText`, `RichText`, `AutoText` - 일부 HTML 태그 지원)                                                |
| `style`              | `enum`               | `Text.Normal`                | 텍스트 스타일을 지정합니다. (`Normal`, `Outline`, `Raised`, `Sunken`)                                                                       |
| `styleColor`         | `color`              | (시스템 기본 색상)          | `style`이 `Outline`, `Raised`, `Sunken`일 때 사용되는 보조 색상입니다.                                                                           |
| `lineHeight`         | `real`               | `0`                          | 줄 간격을 설정합니다. `0`이면 글꼴에 따른 기본값을 사용합니다. `lineHeightMode`로 동작 방식을 변경할 수 있습니다.                                                              |
| `lineHeightMode`     | `enum`               | `Text.ProportionalHeight`   | `lineHeight`가 적용되는 방식을 지정합니다. (`ProportionalHeight`, `FixedHeight`)                                                                |
| `maximumLineCount`   | `int`                | `0`                          | 표시할 최대 줄 수를 제한합니다. `0`이면 제한이 없습니다.                                                                                        |
| `contentWidth`, `contentHeight` | `readonly real` | (계산됨)                     | 현재 텍스트 내용의 실제 너비와 높이입니다. 레이아웃 계산 등에 유용하게 사용됩니다.                                                                               |
| `fontInfo`           | `readonly QtObject` | (글꼴 정보 객체)          | 현재 적용된 글꼴의 상세 정보(예: `pixelSize`)를 제공합니다.                                                                                      |

**`font` 객체 하위 프로퍼티 (주요 항목):**

| 이름        | 타입      | 기본값           | 설명                                               |
| :---------- | :-------- | :--------------- | :----------------------------------------------- |
| `family`    | `string`  | (시스템 기본)  | 글꼴 이름 (예: "Arial", "Times New Roman")           |
| `pointSize` | `real`    | (시스템 기본)  | 포인트 단위 글꼴 크기입니다.                         |
| `pixelSize` | `int`     | (시스템 기본)  | 픽셀 단위 글꼴 크기입니다. `pointSize`와 동시에 설정하지 않습니다. |
| `bold`      | `bool`    | `false`          | 굵게 표시 여부입니다.                             |
| `italic`    | `bool`    | `false`          | 이탤릭체 표시 여부입니다.                         |
| `underline` | `bool`    | `false`          | 밑줄 표시 여부입니다.                             |
| `strikeout` | `bool`    | `false`          | 취소선 표시 여부입니다.                           |

## 주요 시그널

| 이름            | 파라미터        | 반환타입 | 설명                                                                                              | 
| :-------------- | :-------------- | :------- | :------------------------------------------------------------------------------------------------ | 
| `textChanged`   | -               | -        | `text` 프로퍼티 값이 변경될 때 발생합니다.                                                              |
| `linkActivated` | `link: string`  | -        | `textFormat`이 `RichText` 또는 `StyledText`일 때, 텍스트 내의 링크(`<a href=...>` 태그)가 클릭되면 발생합니다. | `link` 파라미터는 클릭된 링크의 URL입니다. |
| `linkHovered`   | `link: string`  | -        | `textFormat`이 `RichText` 또는 `StyledText`일 때, 텍스트 내의 링크 위에 마우스 커서가 올라가면 발생합니다.       |

## 예제

```qml
import QtQuick 2.15
import QtQuick.Layouts 1.15

ColumnLayout {
    spacing: 10

    // 기본 텍스트
    Text {
        text: "Hello, QML Text!"
    }

    // 글꼴 및 색상 변경
    Text {
        text: "Styled Text"
        font.family: "Arial"
        font.pointSize: 16
        font.bold: true
        color: "darkblue"
    }

    // 여러 줄 텍스트 및 줄 바꿈
    Text {
        width: 150 // 너비 제한 필요
        text: "This is a longer text that needs to wrap around."
        wrapMode: Text.WordWrap // 단어 단위 줄 바꿈
        horizontalAlignment: Text.AlignHCenter // 가운데 정렬
    }

    // 텍스트 생략
    Text {
        width: 100
        text: "Very long text that will be elided."
        elide: Text.ElideRight // 오른쪽 생략
    }

    // 서식 있는 텍스트 (StyledText)
    Text {
        textFormat: Text.StyledText
        text: "<b>Bold</b>, <i>Italic</i>, <font color='red'>Red</font>, and <a href='https://example.com'>Link</a>."
        
        // 링크 클릭 시그널 핸들러
        onLinkActivated: (link) => {
            console.log("Link activated:", link)
            // Qt.openUrlExternally(link) // 외부 브라우저로 열기 (Qt 가져오기 필요)
        }
    }
}
```

## 참고 사항

*   **크기**: `Text` 요소의 `width`와 `height`는 기본적으로 텍스트 내용에 따라 결정됩니다(`implicitWidth`, `implicitHeight`). 하지만 레이아웃이나 `wrapMode`, `elide` 등을 올바르게 사용하려면 `width`를 명시적으로 설정해야 하는 경우가 많습니다.
*   **성능**: 복잡한 서식 있는 텍스트(`RichText`, `StyledText`)는 일반 텍스트(`PlainText`)보다 렌더링 성능이 떨어질 수 있습니다. 꼭 필요한 경우에만 사용하는 것이 좋습니다.
*   **글꼴 로딩**: 사용자 정의 글꼴을 사용하려면 애플리케이션에 해당 글꼴 파일을 포함시키고 로드해야 할 수 있습니다.
*   **국제화**: 사용자에게 보여지는 텍스트에는 `qsTr()` 함수를 사용하여 국제화를 지원하는 것이 좋습니다. (예: `text: qsTr("Settings")`) 