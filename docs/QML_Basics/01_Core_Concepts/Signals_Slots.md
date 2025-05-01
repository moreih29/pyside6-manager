# QML 시그널과 핸들러 (Signals and Handlers)

## 개요

QML에서 시그널(Signal)은 객체가 특정 이벤트 발생(예: 버튼 클릭, 프로퍼티 변경)을 외부에 알리는 메커니즘이며, 시그널 핸들러(Signal Handler)는 이러한 시그널에 반응하여 특정 코드를 실행하는 방법입니다. 이는 Qt의 시그널-슬롯 메커니즘과 유사하게 동작하며, QML의 이벤트 기반 프로그래밍 모델의 핵심입니다.

QML 객체는 특정 상황이 발생했을 때 시그널을 방출(emit)할 수 있습니다. 예를 들어, `Button`은 클릭될 때 `clicked()` 시그널을 방출하고, 프로퍼티는 값이 변경될 때 `<propertyName>Changed()` 시그널을 방출합니다. 다른 객체들은 이러한 시그널에 연결된 핸들러를 정의하여 시그널 발생 시 원하는 동작(예: 함수 호출, 프로퍼티 변경)을 수행할 수 있습니다.

## 상세 설명

### 시그널 (Signals)

*   **내장 시그널**: 대부분의 QML 컴포넌트는 특정 사용자 상호작용이나 상태 변경에 대응하는 내장 시그널을 가지고 있습니다. (예: `MouseArea`의 `clicked()`, `TextInput`의 `textChanged()`, 모든 프로퍼티의 `<propertyName>Changed()`)
*   **사용자 정의 시그널**: `signal` 키워드를 사용하여 컴포넌트 내에서 사용자 정의 시그널을 선언할 수 있습니다.

    ```qml
    signal <이름>[([<타입1> <파라미터1>, <타입2> <파라미터2>, ...])]
    ```
    *   **`<이름>`**: 시그널 이름 (소문자 camelCase 권장).
    *   **`[파라미터 목록]`**: 시그널과 함께 전달할 데이터의 타입과 이름을 괄호 안에 정의할 수 있습니다 (선택 사항).

    ```qml
    Item {
        signal buttonActivated(string buttonName, int clickCount)
        signal simpleEvent // 파라미터 없는 시그널
        
        MouseArea {
            anchors.fill: parent
            onClicked: {
                // 시그널 발생시키기 (JavaScript에서 호출)
                parent.buttonActivated("MainButton", 1) 
                parent.simpleEvent()
            }
        }
    }
    ```
*   **시그널 방출(Emit)**:
    *   프로퍼티 변경 시그널(`Changed`)은 프로퍼티 값이 변경될 때 자동으로 방출됩니다.
    *   다른 내장 시그널(예: `clicked`)은 해당 이벤트(클릭) 발생 시 자동으로 방출됩니다.
    *   사용자 정의 시그널은 일반적으로 JavaScript 코드 내에서 시그널 이름 뒤에 괄호(`()`)를 붙여 함수처럼 호출하여 방출합니다.

### 시그널 핸들러 (Signal Handlers)

시그널에 반응하는 코드를 작성하는 가장 일반적인 방법은 `on<SignalName>` 형태의 핸들러를 사용하는 것입니다. 시그널 이름의 첫 글자를 대문자로 바꾼 이름 앞에 `on`을 붙입니다.

```qml
Button {
    id: myButton
    text: "Click Me"
    
    // clicked() 시그널에 대한 핸들러
    onClicked: {
        console.log("Button was clicked!")
        // 다른 동작 수행...
    }
}

Rectangle {
    id: myRect
    width: 100
    color: "red"
    
    // width 프로퍼티의 widthChanged() 시그널에 대한 핸들러
    onWidthChanged: {
        console.log("Width changed to:", width)
    }
    
    // height 프로퍼티의 heightChanged() 시그널에 대한 핸들러
    onHeightChanged: {
        console.log("Height changed!") // 시그널 자체에 파라미터가 없으므로 핸들러도 없음
    }
}

MyComponent { // 위에서 정의한 사용자 정의 시그널을 가진 컴포넌트라고 가정
    id: myComp
    
    // buttonActivated(string buttonName, int clickCount) 시그널 핸들러
    onButtonActivated: (buttonName, clickCount) => { // 파라미터 수신
        console.log("Button activated:", buttonName, "Count:", clickCount)
    }
    
    // simpleEvent() 시그널 핸들러
    onSimpleEvent: {
        console.log("Simple event occurred!")
    }
}
```

*   **핸들러 이름**: `on` + 시그널 이름(첫 글자 대문자).
*   **파라미터**: 시그널이 파라미터를 가지고 있다면, 핸들러에서 해당 파라미터를 받아 사용할 수 있습니다. 파라미터 이름은 시그널 정의와 일치할 필요는 없지만, 순서는 중요합니다.
*   **실행 코드**: 핸들러 블록(`{}`) 안에는 JavaScript 코드를 작성하여 원하는 동작을 구현합니다.

### `Connections` 요소

다른 객체(현재 컴포넌트의 자식이 아니거나 직접 참조하기 어려운 객체)의 시그널을 처리해야 할 때는 `Connections` 요소를 사용합니다.

```qml
import QtQuick 2.15

Item {
    id: root
    width: 200; height: 100
    
    Timer {
        id: myTimer
        interval: 1000; running: true; repeat: true
    }
    
    // myTimer 객체의 triggered 시그널을 처리하기 위해 Connections 사용
    Connections {
        target: myTimer // 시그널을 발생시키는 대상 객체 지정
        
        // onTriggered 핸들러 정의
        onTriggered: {
            console.log("Timer ticked!")
        }
        
        // 다른 시그널 핸들러도 추가 가능
        // onRunningChanged: { ... }
    }
}
```
*   `target` 프로퍼티에 시그널을 발생시키는 객체의 `id`를 지정합니다.
*   `Connections` 요소 내부에 `on<SignalName>` 핸들러를 정의하여 대상 객체의 시그널을 처리합니다.

## 예제

```qml
import QtQuick 2.15
import QtQuick.Controls 2.15

Item {
    id: root
    width: 300; height: 200

    // 사용자 정의 시그널 선언
    signal messageRequested(string requestType)

    Column {
        anchors.centerIn: parent
        spacing: 10

        Button {
            id: helloButton
            text: "Say Hello"
            // 내장 clicked() 시그널 핸들러
            onClicked: {
                statusLabel.text = "Hello Button Clicked!"
                // 사용자 정의 시그널 방출
                root.messageRequested("greeting")
            }
        }

        Button {
            id: byeButton
            text: "Say Bye"
            onClicked: {
                statusLabel.text = "Bye Button Clicked!"
                root.messageRequested("farewell")
            }
        }
        
        Label {
            id: statusLabel
            text: "Status: Idle"
        }
    }
    
    // root의 messageRequested 시그널 핸들러
    onMessageRequested: (requestType) => {
        console.log("Message requested type:", requestType)
        if (requestType === "greeting") {
            statusLabel.text += " (Greeting sent)"
        }
    }
}
```

## 참고 사항

*   **시그널 vs. 함수**: 시그널은 특정 이벤트 발생을 알리는 것이 목적이며, 함수는 특정 작업을 수행하는 것이 목적입니다. 시그널은 직접적인 반환값을 가지지 않습니다.
*   **자동 연결**: `on<SignalName>` 핸들러는 QML 엔진에 의해 자동으로 해당 시그널에 연결됩니다.
*   **네이밍 컨벤션**: 시그널 이름은 소문자 camelCase, 핸들러 이름은 `on` + 대문자 CamelCase 형태를 따르는 것이 일반적입니다.
*   **성능**: 시그널과 핸들러는 QML의 효율적인 이벤트 처리 방식이지만, 매우 빈번하게 발생하는 시그널(예: 마우스 이동 중 계속 발생)에 복잡한 핸들러 로직을 연결하면 성능에 영향을 줄 수 있습니다. 