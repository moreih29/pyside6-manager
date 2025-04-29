# QML 프로퍼티와 바인딩 (Properties and Bindings)

QML에서 프로퍼티(Property)는 객체의 상태나 속성을 나타내는 값이며, 프로퍼티 바인딩(Property Binding)은 이러한 프로퍼티 값들을 서로 동적으로 연결하는 강력하고 핵심적인 메커니즘입니다.

## 개요

모든 QML 객체는 프로퍼티를 가질 수 있습니다. 이는 객체의 모양(예: `width`, `height`, `color`), 동작 방식, 또는 내부 상태를 정의합니다. QML의 가장 큰 특징 중 하나는 **프로퍼티 바인딩** 기능으로, 한 프로퍼티의 값을 다른 프로퍼티 값이나 JavaScript 표현식에 기반하여 자동으로 업데이트되도록 설정할 수 있습니다.

## 상세 설명

### 프로퍼티 선언

QML 컴포넌트 내에서 새로운 프로퍼티를 선언할 때는 `property` 키워드를 사용합니다.

```qml
property <타입> <이름>: <초기값 또는 바인딩 표현식>
property <타입> <이름> // 초기값 생략 시 기본값 사용
readonly property <타입> <이름>: <값> // 읽기 전용 프로퍼티
```

*   **`<타입>`**: 프로퍼티의 데이터 타입 ([기본 데이터 타입](./DataTypes.md) 참조). `int`, `string`, `bool`, `color`, `Item`, `list<string>` 등.
*   **`<이름>`**: 프로퍼티의 이름 (소문자로 시작하는 camelCase 권장).
*   **`<초기값 또는 바인딩 표현식>`**: 프로퍼티의 초기값을 설정하거나, 다른 프로퍼티에 기반한 JavaScript 표현식을 사용하여 바인딩을 설정합니다.
*   **`readonly property`**: 선언 시 할당된 값에서 변경할 수 없는 읽기 전용 프로퍼티를 만듭니다.

### 프로퍼티 접근

QML 객체의 프로퍼티에 접근할 때는 객체의 `id`나 다른 참조 방법을 통해 점(`.`) 표기법을 사용합니다.

```qml
myObject.propertyName
parent.width
root.message
```

### 프로퍼티 바인딩 (Property Binding)

프로퍼티 바인딩은 콜론(`:`) 뒤에 값 대신 JavaScript 표현식을 사용하여 설정합니다. 이 표현식이 참조하는 다른 프로퍼티의 값이 변경되면, 바인딩된 프로퍼티의 값도 **자동으로 다시 계산되어 업데이트**됩니다.

```qml
Rectangle {
    id: rect1
    width: 200
    height: 100
}

Rectangle {
    id: rect2
    width: rect1.width / 2  // rect1의 너비가 바뀌면 rect2의 너비도 자동 변경
    height: rect1.height * 1.5 // rect1의 높이가 바뀌면 rect2의 높이도 자동 변경
    color: width > 150 ? "red" : "blue" // 너비에 따라 색상이 자동 변경
    opacity: enabled ? 1.0 : 0.5 // enabled 프로퍼티 값에 따라 투명도 자동 변경
}
```

*   **자동 업데이트**: 바인딩은 의존하는 프로퍼티(예: `rect1.width`)가 변경될 때마다 자동으로 재평가됩니다.
*   **JavaScript 표현식**: 단순 참조뿐만 아니라 연산자, 함수 호출 등 다양한 JavaScript 표현식을 사용할 수 있습니다.
*   **바인딩 깨기**: 일단 바인딩이 설정된 프로퍼티에 JavaScript 코드(예: 시그널 핸들러 내)에서 정적인 값을 할당하면, 해당 바인딩은 깨지고 더 이상 자동으로 업데이트되지 않습니다.

### 프로퍼티 별칭 (Property Alias)

내부 컴포넌트의 프로퍼티를 외부에서 더 쉽게 접근할 수 있도록 별칭(alias)을 만들 수 있습니다.

```qml
// MyCustomButton.qml
Item {
    property alias text: buttonLabel.text // 내부 Text 요소의 text 프로퍼티를 외부에 text로 노출
    
    FluButton { // 예시 Fluent UI 버튼
        // ...
        FluText { 
            id: buttonLabel
            text: "Default Text"
        }
    }
}

// 사용하는 곳
MyCustomButton {
    text: "Click Me" // 별칭을 통해 내부 Text 요소의 text 설정
}
```

### 기본 프로퍼티 (Default Property)

컴포넌트는 하나의 프로퍼티를 '기본(default)' 프로퍼티로 지정할 수 있습니다. 이렇게 하면 해당 컴포넌트 태그 내부에 직접 작성된 자식 요소들이 자동으로 이 기본 프로퍼티(주로 `list` 타입)에 할당됩니다.

```qml
// Container.qml
Item {
    default property alias content: column.data // column의 data 프로퍼티를 기본 프로퍼티 'content'로 지정
    
    Column { 
        id: column 
        // 자식들이 여기에 추가됨
    }
}

// 사용하는 곳
Container {
    // 아래 요소들은 자동으로 Container의 'content' (즉, column.data)에 추가됨
    Rectangle { color: "red"; width: 50; height: 50 }
    Text { text: "Hello" }
}
```
`Item`의 기본 프로퍼티는 `data`, `Row`, `Column` 등 레이아웃의 기본 프로퍼티도 `data`입니다.

## 예제

```qml
import QtQuick 2.15

Rectangle {
    id: root
    width: 300; height: 200
    color: "lightgray"

    property int padding: 10
    readonly property bool allowResize: true
    property alias childText: label.text

    Rectangle {
        id: innerRect
        // 프로퍼티 바인딩 사용
        x: root.padding 
        y: root.padding
        width: root.width - root.padding * 2
        height: root.height / 3
        color: root.activeFocus ? "lightblue" : "white"
        radius: 5
        visible: root.allowResize // readonly 프로퍼티 참조
    }

    Text {
        id: label
        text: "Initial Text" // childText 별칭을 통해 외부에서 변경 가능
        anchors.bottom: parent.bottom
        anchors.left: parent.left
        anchors.leftMargin: root.padding
        anchors.bottomMargin: root.padding
        // 프로퍼티 바인딩 사용
        font.pixelSize: Math.min(root.width, root.height) / 10 
    }

    MouseArea {
        anchors.fill: parent
        onClicked: {
            // JavaScript에서 프로퍼티 값 변경 (바인딩 깨짐 발생 가능)
            root.color = "lightyellow" // 'color' 프로퍼티의 바인딩이 있다면 깨짐
            label.text = "Clicked!" // 'childText' 별칭을 통해 접근하는 것과 동일
        }
    }
}
```

## 참고 사항

*   **성능**: 매우 복잡하거나 연쇄적인 프로퍼티 바인딩은 성능에 영향을 줄 수 있습니다. 성능 최적화가 필요한 경우 바인딩 대신 시그널 핸들러에서 값을 명시적으로 업데이트하는 것을 고려할 수 있습니다.
*   **디버깅**: `console.log()`나 QML 디버거를 사용하여 프로퍼티 값의 변화와 바인딩 동작을 추적할 수 있습니다.
*   **바인딩 루프**: 프로퍼티 A가 B에 바인딩되고, B가 다시 A에 바인딩되는 등 순환 참조가 발생하면 바인딩 루프 경고가 발생하며 예기치 않게 동작할 수 있습니다. 