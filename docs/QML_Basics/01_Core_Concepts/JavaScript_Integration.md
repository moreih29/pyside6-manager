# QML 내 JavaScript 통합 (JavaScript Integration)

## 개요

QML은 선언적인 UI 정의 언어이지만, 동적인 동작과 로직 처리를 위해 JavaScript를 언어의 핵심 부분으로 통합하여 사용합니다. JavaScript 코드는 QML 내 여러 곳에서 자연스럽게 사용될 수 있습니다.

JavaScript는 QML에서 다음과 같은 주요 목적으로 활용됩니다:

*   **프로퍼티 바인딩**: 복잡한 계산이나 조건 로직을 포함하는 동적인 프로퍼티 값 설정.
*   **시그널 핸들러**: 이벤트 발생 시 실행될 절차적 코드 작성.
*   **사용자 정의 함수**: 재사용 가능한 로직을 컴포넌트 내에 함수로 정의.
*   **독립적인 로직 구현**: UI와 분리된 로직을 별도의 `.js` 파일로 작성하고 QML에서 임포트하여 사용.

QML 환경에서 사용되는 JavaScript는 표준 ECMAScript 사양을 따르며, 몇 가지 QML 환경에 특화된 기능(QML 객체 접근 등)이 추가됩니다.

## 상세 설명

### 프로퍼티 바인딩 내 JavaScript

프로퍼티 바인딩 표현식은 기본적으로 JavaScript 표현식입니다. 산술 연산, 삼항 연산자, `Math` 객체 함수 등을 자유롭게 사용할 수 있습니다.

```qml
Rectangle {
    width: parent.width / 2
    height: Math.max(100, parent.height * 0.8) // Math 객체 사용
    color: isError ? "red" : "green" // 삼항 연산자
    opacity: 1.0 - (sliderValue / 100) // 산술 연산
}
```

### 시그널 핸들러 내 JavaScript

`on<SignalName>` 형태의 시그널 핸들러 블록 내부에는 여러 줄의 JavaScript 코드를 작성하여 이벤트 발생 시 실행될 로직을 구현합니다.

```qml
Button {
    onClicked: {
        var currentTime = new Date();
        console.log("Button clicked at:", currentTime.toLocaleTimeString());
        if (someCondition) {
            performAction(); // 아래 정의된 함수 호출
        } else {
            resetState();
        }
    }
}
```

### 사용자 정의 JavaScript 함수

QML 컴포넌트 내부에 `function` 키워드를 사용하여 사용자 정의 JavaScript 함수를 정의할 수 있습니다. 이렇게 정의된 함수는 해당 컴포넌트 내부 또는 외부에서 호출될 수 있습니다.

```qml
Item {
    id: calculator
    property int valueA: 5
    property int valueB: 10
    
    // 사용자 정의 함수
    function add(a, b) {
        return a + b;
    }
    
    function calculate() {
        var result = add(valueA, valueB); // 내부 함수 호출
        console.log("Calculation result:", result);
        return result;
    }
    
    Component.onCompleted: {
        calculate(); // 컴포넌트 생성 완료 시 함수 호출
    }
}
```

### 외부 JavaScript 파일 임포트 (`.js`)

공통적으로 사용되거나 복잡한 로직은 별도의 `.js` 파일로 분리하고 QML에서 임포트하여 사용할 수 있습니다. `.js` 파일은 전역 범위에 함수나 변수를 정의해야 하며, `import` 시 `as` 키워드로 네임스페이스를 지정해야 합니다.

**`utils.js`:**
```javascript
// utils.js

// .pragma library // QML에서 상태 공유를 위해 필요할 수 있음

function formatMessage(name) {
    return "Hello, " + name + "!";
}

var defaultTimeout = 500;
```

**`MyComponent.qml`:**
```qml
import QtQuick 2.15
import "utils.js" as Utils // .js 파일 임포트 및 네임스페이스 지정

Item {
    property string userName: "QML"
    
    Button {
        text: "Show Message"
        onClicked: {
            var message = Utils.formatMessage(userName); // 임포트한 함수 사용
            console.log(message);
            console.log("Default timeout:", Utils.defaultTimeout); // 임포트한 변수 사용
        }
    }
}
```
*   **`.pragma library`**: `.js` 파일 최상단에 이 주석을 추가하면, 해당 스크립트는 모든 QML 인스턴스에서 상태를 공유하는 공유 라이브러리로 취급됩니다. 상태 공유가 필요 없다면 생략할 수 있습니다.

### QML 객체 접근

JavaScript 코드 내에서는 `id`를 통해 다른 QML 객체에 접근하고, 그 객체의 프로퍼티를 읽거나 쓰거나, 메소드를 호출할 수 있습니다.

```qml
Item {
    id: root
    width: 200
    
    Text {
        id: label
        text: "Initial"
    }
    
    function updateLabel(newText) {
        label.text = newText; // ID로 다른 객체의 프로퍼티 변경
        label.font.bold = true;
        
        if (label.text.length > 10) {
            root.width = label.contentWidth + 20; // ID로 다른 객체의 프로퍼티 읽기
        }
    }
}
```

## 예제

```qml
import QtQuick 2.15
import "helpers.js" as Helpers // 외부 JS 파일 임포트

Rectangle {
    id: mainArea
    width: 300; height: 200
    color: "lightsteelblue"

    property int clickCount: 0
    property bool isValid: textInput.acceptableInput
    
    // JS 함수 정의
    function logState() {
        console.log("Click Count:", clickCount, "Is Valid:", isValid);
    }
    
    // 프로퍼티 바인딩 내 JS 표현식
    border.color: isValid ? "green" : "red"
    border.width: isValid ? 1 : 2

    TextInput {
        id: textInput
        anchors.centerIn: parent
        text: "Enter text"
        validator: IntValidator { bottom: 0; top: 100; } // 예: 0-100 정수만 유효
        
        // 시그널 핸들러 내 JS 코드
        onAccepted: {
            clickCount++; // 프로퍼티 직접 수정
            var formatted = Helpers.formatInput(textInput.text); // 외부 JS 함수 호출
            console.log("Accepted:", formatted);
            logState(); // 내부 JS 함수 호출
        }
    }
}
```

**`helpers.js`:**
```javascript
// helpers.js
.pragma library

function formatInput(text) {
    // 예시: 입력값 앞뒤 공백 제거 및 대문자화
    return text.trim().toUpperCase();
}
```

## 참고 사항

*   **성능**: JavaScript 코드는 QML의 메인 UI 스레드에서 실행됩니다. 시간이 오래 걸리는 복잡한 계산이나 블로킹 I/O 작업은 UI 반응성을 저하시킬 수 있으므로 `WorkerScript` 사용을 고려해야 합니다.
*   **스코프**: JavaScript 코드 내에서 변수 스코프 규칙을 잘 이해해야 합니다. QML 컴포넌트 내에 정의된 함수나 변수는 해당 컴포넌트 인스턴스에 속합니다.
*   **디버깅**: `console.log()`, `console.warn()`, `console.error()` 등을 사용하여 JavaScript 코드 실행을 디버깅할 수 있습니다. Qt Creator는 QML/JS 디버깅 기능도 제공합니다.
*   **QML 환경 제약**: 브라우저 환경의 JavaScript와 달리 `window`, `document` 등 DOM 관련 객체는 사용할 수 없습니다. 