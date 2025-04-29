# SpinBox

**모듈:** `import QtQuick.Controls`

## 개요

`SpinBox`는 사용자가 특정 범위 내의 숫자 값을 선택하거나 편집할 수 있도록 하는 컨트롤입니다. 일반적으로 텍스트 필드와 값 증가/감소를 위한 위/아래 버튼으로 구성됩니다. 사용자는 버튼을 클릭하거나, 텍스트 필드에 직접 숫자를 입력하거나, 마우스 휠 또는 키보드 화살표 키를 사용하여 값을 조절할 수 있습니다.

정수(`value`) 또는 실수(`value`) 값을 다룰 수 있으며, 값의 범위(`from`, `to`)와 증가/감소 단위(`stepSize`)를 지정할 수 있습니다.

## 기반 클래스

*   `Control` (내부적으로 `Range` 모델과 `TextField`를 조합하여 사용)

## 주요 프로퍼티

| 이름             | 타입             | 기본값          | 설명                                                                                                                                  |
| :--------------- | :--------------- | :-------------- | :------------------------------------------------------------------------------------------------------------------------------------ |
| `value`          | `real` or `int`  | 0               | 스핀박스의 현재 값. `from`과 `to` 사이의 값입니다. `decimals` > 0 이면 `real`, 아니면 `int`로 취급될 수 있음.                                |
| `from`           | `real` or `int`  | 0               | 스핀박스가 나타내는 값의 최소 범위.                                                                                                     |
| `to`             | `real` or `int`  | 99              | 스핀박스가 나타내는 값의 최대 범위.                                                                                                     |
| `stepSize`       | `real` or `int`  | 1               | 위/아래 버튼 클릭, 휠 스크롤, 화살표 키 입력 시 값이 변경되는 단위.                                                                         |
| `decimals`       | `int`            | 0               | 실수 값을 표시할 때 사용할 소수점 이하 자릿수. `value`가 `real` 타입처럼 동작하게 함.                                                        |
| `textFromValue`  | `function`       | (기본 형식 지정) | `value`를 텍스트 필드에 표시될 문자열로 변환하는 함수. 기본적으로 로케일 설정과 `decimals`를 고려하여 변환. 사용자 정의 형식 지정에 사용.         |
| `valueFromText`  | `function`       | (기본 파싱)    | 텍스트 필드에 입력된 문자열을 숫자 `value`로 변환하는 함수. 기본적으로 로케일 설정을 고려하여 파싱. 사용자 정의 파싱 규칙 적용에 사용.           |
| `validator`      | `Validator`      | (내부 생성)    | 텍스트 필드 입력 유효성 검사기. 기본적으로 `DoubleValidator` 또는 `IntValidator`가 `from`, `to`, `decimals`에 맞춰 내부적으로 생성되어 사용됨. |
| `editable`       | `bool`           | `false`         | 사용자가 텍스트 필드에 직접 값을 입력할 수 있는지 여부. `true`이면 편집 가능.                                                               |
| `inputMethodHints`| `Qt::InputMethodHints`| `Qt.ImhDigitsOnly` | `editable`이 `true`일 때 가상 키보드 등에 제공할 입력 힌트.                                                                              |
| `up.indicator`, `up.pressed`, `up.enabled` | `Item`, `bool` | -             | 위쪽(값 증가) 버튼의 인디케이터 아이템 및 상태 프로퍼티.                                                                                 |
| `down.indicator`, `down.pressed`, `down.enabled` | `Item`, `bool` | -           | 아래쪽(값 감소) 버튼의 인디케이터 아이템 및 상태 프로퍼티.                                                                               |
| `contentItem`    | `Item`           | (내부 `TextField`)| 텍스트 필드 부분 아이템. 스타일 커스터마이징에 사용.                                                                                    |
| `background`     | `Item`           | (스타일 의존)  | 스핀박스 전체의 배경 아이템. 스타일 커스터마이징에 사용.                                                                                  |
| `wrap`           | `bool`           | `false`         | 값이 `to`에서 증가하거나 `from`에서 감소할 때 반대쪽 끝 값으로 순환할지 여부.                                                                |
| `enabled`        | `bool`           | `true`          | 스핀박스가 활성화되어 사용자와 상호작용할 수 있는지 여부.                                                                                 |
| `font`           | `font`           | (스타일 의존)  | 텍스트 필드의 글꼴.                                                                                                                 |
| `focusPolicy`    | `Qt::FocusPolicy`| `Qt.StrongFocus`| 스핀박스가 키보드 포커스를 받는 방식.                                                                                                   |
| `wheelEnabled`   | `bool`           | `false`         | 마우스 휠 스크롤로 값을 변경할 수 있는지 여부.                                                                                          |
| `ToolTip.visible`, `ToolTip.text`, `ToolTip.delay` | `bool`, `string`, `int` | - | 스핀박스에 마우스를 올렸을 때 표시될 툴팁 설정.                                                                                         |

## 주요 시그널

| 이름            | 파라미터 | 반환타입 | 설명                                                        |
| :-------------- | :------- | :------- | :---------------------------------------------------------- |
| `valueChanged`  | -        | -        | `value` 프로퍼티 값이 변경되었을 때 발생.                    |
| `valueModified` | -        | -        | 사용자의 조작(버튼 클릭, 휠, 키보드, 편집 완료)으로 `value`가 변경되었을 때 발생. |

## 주요 메소드

| 이름        | 파라미터 | 반환타입 | 설명                                 |
| :---------- | :------- | :------- | :----------------------------------- |
| `increase()`| -        | `void`   | `value`를 `stepSize`만큼 증가시킴.  |
| `decrease()`| -        | `void`   | `value`를 `stepSize`만큼 감소시킴.  |

## 예제

```qml
import QtQuick
import QtQuick.Controls
import QtQuick.Layouts

Window {
    width: 300
    height: 250
    visible: true
    title: "SpinBox Example"

    ColumnLayout {
        anchors.centerIn: parent
        spacing: 15

        Label { text: "Integer SpinBox (0-10):" }
        SpinBox {
            id: intSpinBox
            Layout.fillWidth: true
            from: 0
            to: 10
            value: 5 // 초기값
            stepSize: 1
            editable: true // 직접 편집 가능
            wheelEnabled: true // 휠 사용 가능

            onValueChanged: console.log("Int SpinBox value changed:", value)
            onValueModified: console.log("Int SpinBox value modified by user.")
        }

        Label { text: "Real SpinBox (0.0-5.0, step 0.5):" }
        SpinBox {
            id: realSpinBox
            Layout.fillWidth: true
            from: 0.0
            to: 5.0
            value: 2.5
            stepSize: 0.5
            decimals: 1 // 소수점 1자리까지
            // editable: false // 편집 불가 (기본값)

            // 사용자 정의 텍스트 형식 (예: "Value: X.X")
            textFromValue: (value, locale) => {
                return "Value: " + Number(value).toLocaleLocaleString(locale, 'f', decimals)
            }
            // 사용자 정의 값 파싱 (textFromValue와 매칭 필요)
            valueFromText: (text, locale) => {
                // "Value: " 부분 제거 후 숫자 파싱
                var numStr = text.substring(7)
                return Number.fromLocaleString(locale, numStr)
            }
        }

        Label { text: "Wrap SpinBox (1-3):" }
        SpinBox {
            Layout.fillWidth: true
            from: 1
            to: 3
            value: 1
            wrap: true // 값 순환 활성화
        }
    }
}
```

## 참고 사항

*   정수 값 범위에는 `from`, `to`, `stepSize`에 정수를 사용하고 `decimals`를 0(기본값)으로 둡니다.
*   실수 값 범위에는 `from`, `to`, `stepSize`에 실수를 사용하고, `decimals`를 원하는 소수점 자릿수로 설정합니다.
*   `textFromValue`와 `valueFromText` 함수를 사용하여 값과 텍스트 필드 표시 간의 변환 로직을 커스터마이징할 수 있습니다 (예: 단위 추가, 특정 형식 지정).
*   `editable` 프로퍼티로 사용자의 직접 텍스트 입력을 허용하거나 막을 수 있습니다.
*   `validator` 프로퍼티는 일반적으로 직접 설정할 필요가 없으며, `SpinBox`가 내부적으로 관리합니다. 커스텀 유효성 검사가 필요하다면 `valueFromText`를 사용하는 것이 더 일반적입니다.
*   `wheelEnabled`를 `true`로 설정하면 마우스 휠로 값을 편리하게 조절할 수 있습니다. 