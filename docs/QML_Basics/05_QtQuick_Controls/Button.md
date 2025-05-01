# Button

**모듈:** `import QtQuick.Controls`

## 개요

`Button`은 사용자가 클릭하여 특정 동작(action)을 트리거할 수 있는 표준 푸시 버튼 컨트롤입니다. 텍스트 레이블, 아이콘 또는 둘 다를 표시할 수 있으며, 다양한 스타일을 지원합니다.

`Button`은 `AbstractButton`에서 상속받아 기본적인 버튼 동작(클릭 감지, 체크 상태 등)을 구현합니다.

## 기반 클래스

*   `AbstractButton`

## 주요 프로퍼티

| 이름        | 타입             | 기본값          | 설명                                                                                                        |
| :---------- | :--------------- | :-------------- | :---------------------------------------------------------------------------------------------------------- |
| `text`      | `string`         | ""            | 버튼에 표시될 텍스트 레이블.                                                                                |
| `icon.name` | `string`         | ""            | (테마 사용 시) 버튼에 표시될 아이콘의 이름 (예: "document-open"). 테마에서 아이콘을 찾아 표시.               |
| `icon.source`| `url`           | `undefined`     | 버튼에 표시될 아이콘 이미지 파일의 URL. `icon.name`보다 우선 순위가 높습니다.                                 |
| `icon.color`| `color`          | (스타일 의존)  | 아이콘의 색상.                                                                                            |
| `icon.width`, `icon.height` | `real` | (스타일 의존)  | 아이콘의 너비와 높이.                                                                                       |
| `checkable` | `bool`           | `false`         | 버튼이 체크 가능한 상태(토글 버튼)를 가질지 여부.                                                              |
| `checked`   | `bool`           | `false`         | 버튼의 현재 체크 상태. `checkable`이 `true`일 때 유효.                                                    |
| `autoExclusive`| `bool`        | `false`         | (주로 `RadioButton`, `ToolButton`에서 사용) 같은 부모를 가진 다른 `autoExclusive` 버튼 중 하나만 `checked` 상태가 되도록 할지 여부. |
| `down`      | `bool`           | `false`         | (읽기 전용) 버튼이 현재 눌린 상태인지 여부.                                                                  |
| `enabled`   | `bool`           | `true`          | 버튼이 활성화되어 사용자와 상호작용할 수 있는지 여부. 비활성화되면 보통 흐리게 표시됨.                        |
| `flat`      | `bool`           | `false`         | 버튼 배경을 평평하게 표시할지 여부 (테두리 등이 사라짐). 마우스를 올리면 나타나는 스타일도 있음.               |
| `highlighted`| `bool`          | `false`         | (읽기 전용) 버튼이 하이라이트 상태인지 여부 (예: 기본 버튼).                                                   |
| `display`   | `enum`           | `Button.TextBesideIcon` | 텍스트와 아이콘을 함께 표시할 때의 배치 방식 (`TextOnly`, `IconOnly`, `TextBesideIcon`, `TextUnderIcon`).      |
| `action`    | `Action`         | `null`          | 버튼과 연결될 `Action` 객체. `Action`의 속성(`text`, `icon`, `enabled`, `checked` 등)이 버튼에 자동으로 반영됨. |
| `hoverEnabled`| `bool`          | `true`          | 마우스 호버(hover) 효과를 사용할지 여부.                                                                    |
| `hovered`   | `bool`           | `false`         | (읽기 전용) 마우스 커서가 버튼 위에 있는지 여부.                                                              |
| `font`      | `font`           | (스타일 의존)  | 버튼 텍스트의 글꼴.                                                                                       |
| `background`| `Item`           | (스타일 의존)  | 버튼의 배경 아이템. 스타일 커스터마이징에 사용.                                                             |
| `contentItem`| `Item`          | (스타일 의존)  | 버튼의 내용(텍스트, 아이콘)을 담는 아이템. 스타일 커스터마이징에 사용.                                       |
| `indicator` | `Item`           | (스타일 의존)  | 버튼의 상태(예: 체크 상태)를 나타내는 인디케이터 아이템. 스타일 커스터마이징에 사용.                          |
| `focusPolicy`| `Qt::FocusPolicy`| `Qt::StrongFocus`| 버튼이 키보드 포커스를 받는 방식.                                                                             |
| `ToolTip.visible`, `ToolTip.text`, `ToolTip.delay` | `bool`, `string`, `int` | - | 버튼에 마우스를 올렸을 때 표시될 툴팁 설정.                                                                |

## 주요 시그널

`AbstractButton`에서 상속받은 시그널들입니다.

| 이름         | 파라미터 | 반환타입 | 설명                                                                                                          |
| :----------- | :------- | :------- | :---------------------------------------------------------------------------------------------------------- |
| `clicked`    | -        | -        | 버튼이 클릭되었을 때(눌렀다 떼었을 때) 발생. 가장 일반적으로 사용되는 시그널.                                    |
| `pressed`    | -        | -        | 버튼이 눌렸을 때 발생.                                                                                      |
| `released`   | -        | -        | 버튼에서 마우스/터치가 떼어졌을 때 발생.                                                                       |
| `canceled`   | -        | -        | 버튼 누름이 취소되었을 때(예: 누른 상태로 버튼 밖으로 드래그 후 뗌) 발생.                                        |
| `toggled`    | `bool checked` | -        | 버튼의 `checked` 상태가 변경되었을 때 발생 (`checkable`이 `true`일 때). 파라미터는 새로운 `checked` 상태. |
| `doubleClicked`| -      | -        | 버튼이 더블클릭되었을 때 발생.                                                                               |

## 예제

```qml
import QtQuick
import QtQuick.Controls
import QtQuick.Layouts

Window {
    width: 400
    height: 200
    visible: true
    title: "Button Examples"

    ColumnLayout {
        anchors.centerIn: parent
        spacing: 10

        Button {
            text: "Click Me"
            icon.source: "qrc:/qt-project.org/imports/QtQuick/Controls/images/arrow-right.png" // 예시 아이콘 URL
            onClicked: {
                console.log("Button clicked!")
            }
            ToolTip.text: "This is a standard button."
            ToolTip.delay: 500 // 0.5초 후 툴팁 표시
        }

        Button {
            text: "Checkable Button"
            checkable: true
            icon.name: "edit-select-all" // 테마 아이콘 이름 사용 (테마 설정 필요)
            display: Button.TextUnderIcon
            onToggled: (checked) => {
                console.log("Checkable button toggled:", checked)
            }
        }

        Button {
            text: "Disabled Button"
            enabled: false
        }

        Button {
            text: "Flat Button"
            flat: true
        }

        // Action과 연결된 버튼
        Action {
            id: myAction
            text: "Action Button"
            icon.name: "document-save"
            shortcut: "Ctrl+S"
            onTriggered: {
                console.log("Action triggered!")
            }
        }
        Button {
            action: myAction // Action 연결
        }
    }
}
```

## 참고 사항

*   버튼의 모양과 느낌(Look and Feel)은 현재 적용된 스타일에 따라 크게 달라집니다. `qtquickcontrols2.conf` 파일을 통해 앱 전체 스타일을 설정하거나, 개별 컨트롤의 프로퍼티(`background`, `contentItem` 등)를 직접 수정하여 커스터마이징할 수 있습니다.
*   `Action` 컴포넌트와 연결하면 메뉴 항목, 툴바 버튼 등과 동일한 동작 및 상태(텍스트, 아이콘, 활성화 여부 등)를 공유할 수 있어 편리합니다.
*   `ToolButton`은 주로 툴바에 사용되는 좀 더 간결한 형태의 버튼입니다.
*   버튼 클릭 외에 누르고 있는 동안의 동작 등을 처리하려면 `pressed`, `released` 시그널을 사용할 수 있습니다. 

## 공식 문서 링크

*   [Button QML Type](https://doc.qt.io/qt-6/qml-qtquick-controls-button.html) 