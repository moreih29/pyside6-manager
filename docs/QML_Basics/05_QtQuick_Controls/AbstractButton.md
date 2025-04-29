# AbstractButton

**모듈:** `import QtQuick.Controls`

## 개요

`AbstractButton`은 QML에서 다양한 종류의 버튼 컨트롤(`Button`, `CheckBox`, `RadioButton`, `Switch`, `ToolButton` 등)의 **추상 기반 클래스**입니다. 이 클래스는 직접 인스턴스화하여 사용하는 것이 아니라, 버튼과 유사한 컨트롤들이 공통적으로 가지는 프로퍼티, 시그널, 메서드를 정의하는 역할을 합니다.

`AbstractButton`을 이해하면 파생된 여러 버튼 컨트롤들의 공통적인 동작 방식과 상호작용 모델을 파악하는 데 도움이 됩니다.

## 기반 클래스

*   `Control`

## 주요 프로퍼티 (파생 클래스에서 상속)

`AbstractButton`은 다음과 같은 버튼 관련 핵심 프로퍼티들을 정의하며, 이들은 파생된 구체적인 버튼 클래스들에서 사용됩니다.

| 이름             | 타입        | 기본값        | 설명                                                                                                                                         |
| :--------------- | :---------- | :------------ | :------------------------------------------------------------------------------------------------------------------------------------------- |
| `text`           | `string`    | ""          | 버튼에 표시될 텍스트. 파생 클래스에 따라 이 텍스트가 표시되는 방식이 다릅니다.                                                                    |
| `checkable`      | `bool`      | `false`       | 버튼이 체크 가능한 상태를 가질 수 있는지 여부 (`CheckBox`, `RadioButton`, `ToolButton` 등에서 주로 `true`).                                                 |
| `checked`        | `bool`      | `false`       | 버튼의 현재 체크 상태 (`checkable`이 `true`일 때 유효). `CheckBox`, `RadioButton`, `Switch` 등에서 중요한 상태값입니다.                               |
| `autoExclusive`  | `bool`      | `false`       | (`checkable`이 `true`일 때) 같은 부모 아이템 내에서 이 프로퍼티가 `true`인 다른 버튼들과 배타적인 관계를 가지는지 여부 (`RadioButton`에서 주로 `true`).          |
| `down`           | `bool`      | (읽기 전용)   | 사용자가 버튼을 현재 누르고 있는 상태인지 여부.                                                                                                  |
| `pressed`        | `bool`      | (읽기 전용)   | `down`과 유사하지만, 버튼 영역 내에서 눌렀다가 떼는 동작까지 포함할 수 있는 상태.                                                                  |
| `action`         | `Action`    | `null`        | 버튼과 연결될 `Action` 객체. `Action`의 프로퍼티(text, icon, enabled 등)를 버튼에 자동으로 반영하고, `Action`의 `triggered` 시그널을 버튼 클릭과 연결할 수 있습니다. |
| `icon`           |             |               | 버튼에 표시될 아이콘 관련 프로퍼티 그룹 (`icon.source`, `icon.name`, `icon.color` 등).                                                            |
| `display`        | `DisplayMode`| `IconOnly` (ToolButton), `TextBesideIcon` (Button) | 아이콘과 텍스트를 함께 표시하는 방식 (`TextOnly`, `IconOnly`, `TextBesideIcon`, `TextUnderIcon`).                                                 |
| `indicator`      | `Item`      | (스타일 의존) | 체크 상태 등을 시각적으로 나타내는 인디케이터 아이템 (`CheckBox`, `RadioButton`, `Switch` 등에서 사용).                                                |
| `contentItem`    | `Item`      | (스타일 의존) | 버튼의 주 내용(텍스트, 아이콘 등)을 담는 아이템. 스타일링에 사용됩니다.                                                                           |
| `background`     | `Item`      | (스타일 의존) | 버튼의 배경 아이템. 스타일링에 사용됩니다.                                                                                                       |
| `enabled`        | `bool`      | `true`        | 컨트롤(버튼)의 활성화 상태. `Control`에서 상속.                                                                                              |
| `focusPolicy`    | `FocusPolicy`| `Qt.StrongFocus` | 버튼이 키보드 포커스를 받는 방식. `Control`에서 상속.                                                                                        |
| `hoverEnabled`   | `bool`      | `true`        | 마우스 호버 효과 활성화 여부. `Control`에서 상속.                                                                                            |
| `hovered`        | `bool`      | (읽기 전용)   | 마우스 커서가 버튼 위에 있는지 여부. `Control`에서 상속.                                                                                       |

## 주요 시그널 (파생 클래스에서 상속)

| 이름             | 파라미터 | 설명                                                                                                 |
| :--------------- | :------- | :--------------------------------------------------------------------------------------------------- |
| `clicked`        |          | 사용자가 버튼을 클릭했을 때 (눌렀다가 뗄 때) 발생합니다. 가장 일반적으로 사용되는 시그널입니다.                   |
| `pressed`        |          | 사용자가 버튼을 누르기 시작했을 때 발생합니다.                                                                 |
| `released`       |          | 사용자가 버튼에서 손을 뗄 때 발생합니다.                                                                       |
| `canceled`       |          | 버튼 누름 동작이 취소되었을 때 (예: 누른 상태에서 버튼 밖으로 포인터를 이동한 후 뗄 때) 발생합니다.                 |
| `toggled`        | `bool checked` | `checked` 상태가 변경될 때 발생합니다 (`checkable`이 `true`일 때). 새로운 `checked` 상태가 파라미터로 전달됩니다. |
| `pressAndHold`   |          | 사용자가 버튼을 일정 시간 이상 누르고 있을 때 발생합니다.                                                            |
| `doubleClicked`  |          | 사용자가 버튼을 빠르게 두 번 클릭했을 때 발생합니다.                                                               |

## 주요 메서드 (파생 클래스에서 상속)

| 이름       | 설명                                                                     |
| :--------- | :----------------------------------------------------------------------- |
| `toggle()` | (`checkable`이 `true`일 때) `checked` 상태를 반전시킵니다.                     |
| `click()`  | 프로그램적으로 버튼 클릭 동작을 발생시킵니다 (`clicked` 시그널 방출).          |

## 참고 사항

*   `AbstractButton` 자체를 QML 코드에서 직접 사용할 수는 없습니다. 이 문서는 `Button`, `CheckBox`, `RadioButton`, `Switch`, `ToolButton` 등 파생된 컨트롤들의 공통적인 기반을 설명하기 위한 것입니다.
*   각 파생 컨트롤은 `AbstractButton`의 프로퍼티와 시그널을 상속받아 사용하며, 필요에 따라 특정 프로퍼티의 기본값을 변경하거나 새로운 기능을 추가합니다.
*   예를 들어, `Button`은 주로 `clicked` 시그널을 사용하고, `CheckBox`나 `Switch`는 `toggled` 시그널과 `checked` 프로퍼티를 중요하게 사용합니다.
*   `action` 프로퍼티를 사용하면 UI의 액션 로직을 분리하여 관리하기 용이합니다. 