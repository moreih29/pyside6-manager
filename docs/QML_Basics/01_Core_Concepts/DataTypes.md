# QML 기본 데이터 타입 (Basic Data Types)

QML은 UI 요소를 선언적으로 정의하기 위한 언어이며, 다양한 종류의 데이터를 다루기 위한 기본적인 데이터 타입들을 제공합니다. 프로퍼티(속성)를 정의하거나 함수 파라미터, 시그널 파라미터 등으로 이 타입들을 사용합니다.

## 개요

QML의 기본 데이터 타입은 크게 **기본 타입(Primitive Types)**과 **객체 타입(Object Types)**으로 나눌 수 있습니다. 기본 타입은 숫자, 문자열, 불리언 등을 나타내며, 객체 타입은 더 복잡한 구조나 QML 컴포넌트 자체를 나타냅니다. 또한, 목록이나 임의의 타입을 저장할 수 있는 가변 타입도 제공됩니다.

## 상세 설명

### 기본 타입 (Primitive Types)

*   **`int`**: 정수형 숫자 (예: `10`, `-5`, `0`)
*   **`real`**: 부동 소수점 실수형 숫자 (예: `3.14`, `-0.5`, `1.0`)
*   **`string`**: 문자열 (예: `"Hello, QML!"`, `'Single Quotes'`, `qsTr("Translated")`)
    *   따옴표(`"` 또는 `'`)로 감싸며, 국제화를 위해 `qsTr()` 함수를 사용할 수 있습니다.
*   **`bool`**: 불리언 값 (논리값) - `true` 또는 `false`
*   **`color`**: 색상 값. 다양한 형식으로 표현 가능합니다:
    *   색상 이름: `"red"`, `"blue"`, `"transparent"` 등 (SVG 색상 이름 표준)
    *   16진수 RGB: `"#FF0000"` (빨강)
    *   16진수 ARGB: `"#80FF0000"` (반투명 빨강 - Alpha=80)
    *   `Qt.rgba(r, g, b, a)` 함수: 각 채널 값을 0.0 ~ 1.0 사이로 지정. (예: `Qt.rgba(1, 0, 0, 0.5)`)
    *   `Qt.hsla(h, s, l, a)` 함수: HSL 색상 모델 사용.
*   **`url`**: URL(Uniform Resource Locator) 값. 주로 이미지 소스, QML 파일 경로 등에 사용됩니다.
    *   문자열 형태로 지정: `"image.png"`, `"qrc:/icons/app.ico"`, `"https://example.com/logo.png"`
    *   `Qt.resolvedUrl(relativePath)` 함수: 현재 QML 파일 기준 상대 경로를 해석하여 URL 객체 반환.
*   **`enum`**: 열거형 타입. 특정 컴포넌트나 모듈에서 미리 정의된 상수 값들의 집합입니다.
    *   `Component.AlignHCenter`, `Text.AlignRight`, `FluWindowType.SingleTask` 등
    *   타입 이름과 점(`.`)을 사용하여 값에 접근합니다.

### 객체 타입 (Object Types)

*   **QML 컴포넌트 타입**: `Item`, `Rectangle`, `Button`, `FluWindow` 등 QML에서 정의된 시각적/비시각적 컴포넌트 자체를 타입으로 사용합니다.
    *   다른 객체의 프로퍼티 타입으로 사용될 수 있습니다 (예: `property Item customHeader`).
    *   리스트(`list<Item>`) 형태로도 사용됩니다.
*   **`QtObject`**: 모든 QML 객체의 기본이 되는 타입. 시각적 표현이 없는 데이터 모델이나 유틸리티 객체 정의에 사용됩니다.
*   **JavaScript 객체**: `{ key1: value1, key2: value2 }` 형태로 JavaScript 객체를 직접 정의하여 사용할 수 있습니다. `var` 타입 프로퍼티에 할당하거나 시그널 파라미터로 전달하는 데 주로 사용됩니다.
*   **Qt C++ 타입**: Qt C++ 클래스를 QML에 등록하여 사용할 수 있습니다. (고급 주제)

### 목록 및 가변 타입

*   **`list<Type>`**: 특정 타입(`Type`)의 값들을 순서대로 담는 리스트(배열)입니다.
    *   `property list<string> names: ["Alice", "Bob"]`
    *   `property list<Item> buttons`
    *   `property list<QtObject> dataModels`
    *   리스트 요소는 대괄호(`[]`) 안에 쉼표(`,`)로 구분하여 정의합니다.
*   **`var`**: 어떤 타입의 값이든 저장할 수 있는 가변 타입입니다. JavaScript의 변수와 유사하게 동작합니다.
    *   유연하지만, 타입 검사가 컴파일 타임에 이루어지지 않아 오류 발생 가능성이 높고 성능상 불리할 수 있습니다.
    *   JavaScript 객체나 동적으로 타입이 결정되는 경우에 주로 사용됩니다.

## 예제

```qml
import QtQuick 2.15

Item {
    id: root
    width: 400
    height: 300

    // 기본 타입 프로퍼티 선언
    property int count: 0
    property real scaleFactor: 1.5
    property string message: "Initial Message"
    property bool enabled: true
    property color backgroundColor: "#F0F0F0"
    property url iconSource: Qt.resolvedUrl("icons/default.png")

    // 객체 타입 프로퍼티
    property Item headerItem: null
    property FluButton mainButton: null

    // 목록 및 가변 타입 프로퍼티
    property list<string> users: ["Admin", "Guest"]
    property list<real> values: [1.2, 3.4, 5.6]
    property var dynamicData: ({ name: "Example", value: 10 }) // JS 객체

    Component.onCompleted: {
        console.log("Count:", count)
        console.log("Scale:", scaleFactor)
        console.log("Message:", message)
        console.log("Enabled:", enabled)
        console.log("Background Color:", backgroundColor)
        console.log("Icon Source:", iconSource)
        console.log("Users:", users[0]) // 리스트 요소 접근
        console.log("Dynamic Data Name:", dynamicData.name) // JS 객체 속성 접근
        
        // var 타입 변경
        dynamicData = "Now it's a string!"
        console.log("Dynamic Data Changed:", dynamicData)
    }
    
    Rectangle {
        anchors.fill: parent
        color: root.backgroundColor // color 프로퍼티 사용
        border.color: Qt.rgba(0, 0, 0, 0.2) // Qt.rgba() 함수 사용
        visible: root.enabled // bool 프로퍼티 사용
    }
}
```

## 참고 사항

*   **타입 변환**: QML은 특정 상황에서 자동으로 타입 변환을 시도합니다 (예: `string`을 `int`나 `real`로). 하지만 명시적으로 타입을 맞추는 것이 안전합니다.
*   **`var` 타입 주의**: `var`는 편리하지만, 코드 가독성을 해치고 예기치 않은 오류를 발생시킬 수 있습니다. 가능한 구체적인 타입을 사용하는 것이 좋습니다.
*   **기본값**: 프로퍼티 선언 시 초기값을 지정하지 않으면 타입별 기본값(숫자 0, `false`, 빈 문자열, `null` 등)이 할당됩니다. 