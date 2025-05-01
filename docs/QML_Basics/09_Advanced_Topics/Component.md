# Component

**모듈:** `import QtQml`

## 개요

`Component` 타입은 QML 컴포넌트 정의를 캡슐화합니다. 컴포넌트는 잘 정의된 인터페이스를 가진 재사용 가능하고 캡슐화된 QML 타입입니다.

일반적으로 컴포넌트는 별도의 `.qml` 파일로 정의됩니다. `Component` 타입을 사용하면 QML 문서 내에 인라인으로 컴포넌트를 정의할 수 있습니다. 이는 작은 컴포넌트를 한 파일 내에서 재사용하거나, 논리적으로 다른 QML 컴포넌트와 함께 속하는 컴포넌트를 정의할 때 유용할 수 있습니다.

`Component` 자체는 시각적인 표현을 가지지 않으며, 내부에 정의된 QML 타입들의 '설계도' 역할을 합니다. 컴포넌트 내부에 정의된 아이템은 `Loader`나 JavaScript 코드를 통해 명시적으로 인스턴스화될 때까지 로드되지 않습니다.

## 주요 프로퍼티

| 이름     | 타입        | 기본값 | 설명                                                                                                |
| :------- | :---------- | :----- | :-------------------------------------------------------------------------------------------------- |
| `progress` | `real`      | `1.0`  | (읽기 전용) 컴포넌트 로딩 진행률 (0.0 ~ 1.0). 주로 비동기 로딩이나 외부 URL에서 로드할 때 의미가 있습니다. |
| `status` | `enumeration`| `Ready`| (읽기 전용) 컴포넌트 로딩 상태 (`Component.Null`, `Component.Ready`, `Component.Loading`, `Component.Error`). |
| `url`    | `url`       | -      | (읽기 전용) 컴포넌트를 구성하는 데 사용된 URL (외부 `.qml` 파일을 `Qt.createComponent()` 등으로 로드한 경우). |

## 주요 메소드

| 이름             | 파라미터                                     | 반환타입   | 설명                                                                                                                                 |
| :--------------- | :------------------------------------------- | :--------- | :----------------------------------------------------------------------------------------------------------------------------------- |
| `createObject()` | `parent`: `QtObject`, `properties`: `object` | `object`   | **동기적으로** 컴포넌트의 인스턴스를 생성하고 반환합니다. `parent`는 생성될 객체의 부모, `properties`는 초기 프로퍼티 값의 맵입니다 (선택 사항). 객체 생성 실패 시 `null`을 반환합니다. UI 스레드를 차단할 수 있습니다. |
| `incubateObject()`| `parent`: `QtObject`, `properties`: `object`, `mode`: `enumeration` | `object` (Incubator) | **비동기적으로** 컴포넌트 인스턴스 생성을 시작하고 Incubator 객체를 반환합니다. `mode`는 `Qt.Synchronous` 또는 `Qt.Asynchronous`(기본값)를 지정할 수 있습니다. UI 스레드 차단을 피하기 위해 권장됩니다. Incubator의 `status`와 `object` 프로퍼티를 통해 생성 과정을 추적합니다. |
| `errorString()`  | -                                            | `string`   | 오류 발생 시, 오류에 대한 사람이 읽을 수 있는 설명을 반환합니다. 오류가 없으면 빈 문자열을 반환합니다.                                   |

## 첨부된 시그널 (Attached Signals)

`Component`는 모든 QML 객체에서 사용할 수 있는 두 가지 첨부된 시그널 핸들러를 제공합니다.

| 이름            | 설명                                                                  |
| :-------------- | :-------------------------------------------------------------------- |
| `Component.onCompleted` | 객체의 인스턴스화가 완료된 후 실행됩니다. 전체 QML 환경이 설정된 후 시작 스크립트를 실행하는 데 사용할 수 있습니다. |
| `Component.onDestruction` | 객체 파괴가 시작될 때 실행됩니다. `onCompleted`에서 수행한 작업을 되돌리는 데 사용할 수 있습니다.   |

## 주요 열거형 (Component.)

| 이름      | 설명                                                                 |
| :-------- | :------------------------------------------------------------------- |
| `Null`    | 컴포넌트에 대한 데이터가 없는 상태.                                     |
| `Ready`   | 컴포넌트가 로드되어 인스턴스를 생성할 수 있는 상태.                            |
| `Loading` | 컴포넌트가 현재 로딩 중인 상태.                                         |
| `Error`   | 컴포넌트 로딩 중 오류가 발생한 상태. `errorString()`으로 상세 확인 가능. |

## 예제

### 인라인 컴포넌트 정의 및 사용 (Loader)

```qml
import QtQuick
import QtQml // Component 타입을 직접 사용 시 필요
import QtQuick.Window // Window 사용을 위해 추가

Window { // Window로 감싸서 단독 실행 가능하게 함
    width: 150; height: 100
    visible: true
    title: "Inline Component Example"

    // 간단한 빨간 사각형 컴포넌트 정의
    Component {
        id: redSquare

        Rectangle {
            color: "red"
            width: 10
            height: 10
        }
    }

    // 정의된 컴포넌트를 Loader에서 사용
    Loader { x: 10; y: 10; sourceComponent: redSquare }
    Loader { x: 30; y: 10; sourceComponent: redSquare }
}
```

### 첨부된 시그널 사용

```qml
import QtQuick
import QtQuick.Window

Window { // 예시 실행을 위해 Window 사용
    width: 200; height: 100
    visible: true
    title: "Attached Signals Example"

    Rectangle {
        width: 50; height: 50
        color: "lightgreen"
        Component.onCompleted: console.log("Rectangle Completed!")
        Component.onDestruction: console.log("Rectangle Destruction!")
    }
}
```

### 동적 생성 (JavaScript 및 비동기 Incubator)

```qml
import QtQuick
import QtQuick.Controls // Button 사용 예시
import QtQml
import QtQuick.Window // Window 사용을 위해 추가

Window { // Window로 감싸서 단독 실행 가능하게 함
    width: 300; height: 250
    visible: true
    title: "Dynamic Creation Example"
    id: windowRoot // Window 자체를 참조하기 위한 id

    // 재사용 가능한 버튼 컴포넌트 정의
    Component {
        id: myButtonComponent

        Rectangle {
            id: buttonRoot
            width: 100; height: 30
            color: "lightblue"
            border.color: "steelblue"
            radius: 5
            property alias buttonText: buttonLabel.text
            signal clicked

            Text { id: buttonLabel; anchors.centerIn: parent; text: "Click" }
            MouseArea { anchors.fill: parent; onClicked: buttonRoot.clicked() }
        }
    }

    Button {
        id: createButton
        anchors.top: parent.top; anchors.horizontalCenter: parent.horizontalCenter; anchors.margins: 10
        text: "Create Button Dynamically"
        onClicked: {
            // incubator를 사용한 비동기 생성
            // 부모를 windowRoot (Window)로 지정
            const incubator = myButtonComponent.incubateObject(windowRoot, { "buttonText": "Dynamic Btn" });

            if (incubator.status !== Component.Ready) {
                // 즉시 준비되지 않은 경우 (비동기 진행)
                console.log("Incubation started...");
                incubator.onStatusChanged = function(status) {
                    console.log("Incubator status:", status);
                    if (status === Component.Ready) {
                        const newButton = incubator.object;
                        console.log("Object created asynchronously:", newButton);
                        if (newButton) { // 생성 성공 확인
                            // 생성된 객체 배치 및 설정 (Window의 자식이므로 Window 내 좌표 사용)
                            newButton.y = createButton.y + createButton.height + 10;
                            newButton.anchors.horizontalCenter = parent.horizontalCenter; // 버튼과 같은 수평 중앙 정렬
                            newButton.clicked.connect(function() { console.log("Dynamic button clicked!") });
                        } else {
                            console.error("Failed to create object asynchronously.");
                        }
                    } else if (status === Component.Error) {
                         console.error("Error during incubation:", myButtonComponent.errorString());
                    }
                }
            } else {
                // 즉시 준비된 경우 (동기 완료)
                const newButton = incubator.object;
                console.log("Object created synchronously:", newButton);
                 if (newButton) {
                    newButton.y = createButton.y + createButton.height + 10;
                    newButton.anchors.horizontalCenter = parent.horizontalCenter;
                    newButton.clicked.connect(function() { console.log("Dynamic button clicked!") });
                } else {
                     console.error("Failed to create object synchronously.");
                }
            }
        }
    }
}
```

## 참고 사항

*   `Component`는 내부에 단일 루트 아이템을 가져야 합니다.
*   인라인 `Component`는 이름을 지정할 수 없으므로 프로퍼티 타입이나 타입 어노테이션에 사용할 수 없습니다. 이런 경우 별도의 `.qml` 파일을 사용하는 것이 좋습니다.
*   `createObject()`는 UI 끊김을 유발할 수 있으므로, 가능하면 `incubateObject()`를 사용한 비동기 생성을 권장합니다.
*   `Loader` 요소는 `Component`를 선언적으로 사용하여 동적 로딩을 구현하는 편리한 방법입니다.
*   `Qt.createComponent()` 함수를 사용하여 JavaScript에서 동적으로 `Component` 객체를 생성할 수도 있습니다.
*   동적으로 생성된 객체는 `destroy()` 메소드를 사용하여 명시적으로 제거할 수 있으며, 부모가 설정되지 않은 경우 가비지 컬렉터에 의해 파괴되지 않도록 참조를 유지해야 합니다.
*   **생성 컨텍스트 (Creation Context)**: `Component`의 생성 컨텍스트는 해당 `Component`가 선언된 컨텍스트에 해당합니다. 이 컨텍스트는 컴포넌트가 `Loader`나 `ListView` 같은 객체에 의해 인스턴스화될 때 부모 컨텍스트로 사용됩니다. 이를 통해 인스턴스화된 객체는 자신이 생성된 컴포넌트의 컨텍스트 내의 ID와 프로퍼티에 접근할 수 있습니다.

## 공식 문서 링크

* [Component QML Type | Qt Qml 6.9](https://doc.qt.io/qt-6/qml-qtqml-component.html) 