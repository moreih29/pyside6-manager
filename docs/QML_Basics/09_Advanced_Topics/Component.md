# Component

**모듈:** `import QtQml` (주로 사용되지만, 기본적인 `QtQuick` 환경에서도 내장 요소로 사용 가능)

## 개요

`Component` 요소는 QML 코드 블록을 캡슐화하여 재사용 가능한 컴포넌트를 정의하는 데 사용됩니다. 이렇게 정의된 컴포넌트는 필요할 때마다 인스턴스화하여 사용할 수 있습니다.

주요 목적은 코드의 모듈화, 재사용성 증대, 그리고 동적 객체 생성을 위한 템플릿 제공입니다. `Component` 자체는 시각적인 표현을 가지지 않으며, 내부에 정의된 QML 코드의 '설계도' 또는 '팩토리' 역할을 합니다.

## 사용 방법

`Component` 요소 내부에는 인스턴스화될 QML 아이템(일반적으로 단일 루트 아이템)을 정의합니다.

```qml
import QtQuick
import QtQml // Component를 명시적으로 사용 시

Item {
    width: 300; height: 200

    // 재사용 가능한 버튼 컴포넌트 정의
    Component {
        id: myButtonComponent

        Rectangle {
            id: buttonRoot
            width: 100; height: 30
            color: "lightblue"
            border.color: "steelblue"
            radius: 5

            // 컴포넌트 외부에서 설정할 수 있는 프로퍼티 (alias 사용)
            property alias buttonText: buttonLabel.text
            property alias buttonColor: buttonRoot.color
            signal clicked // 컴포넌트에서 발생시킬 시그널 정의

            Text {
                id: buttonLabel
                anchors.centerIn: parent
                text: "Click Me"
            }

            MouseArea {
                anchors.fill: parent
                onClicked: buttonRoot.clicked() // 내부 시그널 발생
            }
        }
    }

    // 정의된 컴포넌트를 사용하여 인스턴스 생성 (Loader 사용 예시)
    Loader {
        id: buttonLoader1
        anchors.top: parent.top; anchors.left: parent.left; anchors.margins: 10
        sourceComponent: myButtonComponent

        // 로드 완료 후 프로퍼티 설정 및 시그널 연결
        onLoaded: {
            item.buttonText = "Button 1"
            item.clicked.connect(function() { console.log("Button 1 clicked!") })
        }
    }

    // JavaScript에서 동적으로 인스턴스 생성 예시
    Button {
        anchors.top: buttonLoader1.bottom; anchors.left: parent.left; anchors.margins: 10
        text: "Create Button 2"
        onClicked: {
            var component = myButtonComponent;
            var incubator = component.incubateObject(parent); // 비동기 생성 시작

            if (incubator.status !== Component.Ready) {
                // 로딩이 즉시 완료되지 않은 경우 (비동기)
                incubator.onStatusChanged = function(status) {
                    if (status === Component.Ready) {
                        var newButton = incubator.object; // 생성된 객체 가져오기
                        newButton.parent = parent; // 부모 설정 (주의: 좌표계 및 레이아웃 고려 필요)
                        newButton.x = 10;
                        newButton.y = 150;
                        newButton.buttonText = "Button 2";
                        newButton.buttonColor = "lightgreen";
                        newButton.clicked.connect(function() { console.log("Button 2 clicked!") });
                    }
                };
            } else {
                // 로딩이 즉시 완료된 경우 (동기)
                var newButton = incubator.object;
                newButton.parent = parent;
                newButton.x = 10;
                newButton.y = 150;
                newButton.buttonText = "Button 2";
                newButton.buttonColor = "lightgreen";
                newButton.clicked.connect(function() { console.log("Button 2 clicked!") });
            }
        }
    }
}
```

## 주요 프로퍼티

| 이름         | 타입        | 기본값 | 설명                                                                                                |
| :----------- | :---------- | :----- | :-------------------------------------------------------------------------------------------------- |
| `id`         | `identifier`| -      | `Component` 요소를 참조하기 위한 고유 식별자입니다.                                                    |
| `progress`   | `real`      | `1.0`  | (읽기 전용) 컴포넌트 로딩 진행률 (0.0 ~ 1.0). 비동기 로딩 시 유용합니다. 주로 외부 파일 로딩 시 의미가 있습니다. |
| `status`     | `enumeration`| `Ready`| (읽기 전용) 컴포넌트의 현재 상태 (`Null`, `Ready`, `Loading`, `Error`).                                |
| `url`        | `url`       | -      | 컴포넌트 정의가 포함된 외부 QML 파일의 URL. `Component` 요소 내부에 직접 정의하는 대신 외부 파일을 사용할 때 지정합니다. |

## 주요 메소드

| 이름             | 파라미터                                     | 반환타입        | 설명                                                                                                                                 |
| :--------------- | :------------------------------------------- | :-------------- | :----------------------------------------------------------------------------------------------------------------------------------- |
| `createObject()` | `parent`: `Item`, `properties`: `variantMap` | `object`        | **동기적으로** 컴포넌트의 인스턴스를 생성합니다. `parent`는 생성될 객체의 부모 아이템, `properties`는 생성 시 설정할 초기 프로퍼티 값의 맵입니다. **UI 스레드를 차단할 수 있으므로 주의해야 합니다.** |
| `incubateObject()`| `parent`: `Item`, `properties`: `variantMap`, `mode`: `enumeration` | `Component.Incubator` | **비동기적으로** 컴포넌트 인스턴스 생성을 시작합니다. `mode`는 `Asynchronous` (기본값) 또는 `Synchronous`를 지정할 수 있습니다. UI 스레드 차단을 피하기 위해 권장되는 방식입니다. 반환된 `Incubator` 객체의 `status`와 `object`를 통해 생성 과정을 추적하고 결과를 얻습니다. |

## 주요 열거형 (Component.)

| 이름          | 설명                                                                                                 |
| :------------ | :--------------------------------------------------------------------------------------------------- |
| `Null`        | 컴포넌트가 유효하지 않거나 설정되지 않은 상태.                                                           |
| `Ready`       | 컴포넌트가 로드되었고 인스턴스를 생성할 준비가 된 상태.                                                    |
| `Loading`     | 컴포넌트가 현재 로딩 중인 상태 (주로 외부 `url` 사용 시).                                                |
| `Error`       | 컴포넌트 로딩 중 오류가 발생한 상태.                                                                      |
| `Asynchronous`| `incubateObject` 메소드의 모드. 비동기적으로 인스턴스를 생성합니다. (기본값 및 권장)                        |
| `Synchronous` | `incubateObject` 메소드의 모드. 동기적으로 인스턴스를 생성 시도합니다. (결국 `createObject`와 유사해짐) |

## 참고 사항

*   `Component` 내부에 정의된 아이템의 `id`는 컴포넌트 내부에서만 유효합니다. 외부에서 접근하려면 `property alias`를 사용해야 합니다.
*   컴포넌트의 루트 아이템은 일반적으로 하나여야 합니다.
*   `createObject()`는 간단하지만 복잡하거나 큰 컴포넌트의 경우 UI 끊김을 유발할 수 있습니다. 가능하면 `incubateObject()`를 사용한 비동기 생성을 고려하세요.
*   `Loader` 요소는 `Component`를 보다 선언적으로 사용하여 동적 로딩을 구현하는 편리한 방법입니다.
*   QML 파일 자체도 하나의 암묵적인 컴포넌트로 간주될 수 있습니다. 예를 들어 `Loader`의 `source` 프로퍼티에 파일 경로를 지정하는 것은 해당 파일의 루트 아이템을 컴포넌트로 취급하여 로드하는 것과 같습니다. 