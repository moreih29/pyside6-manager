# Animation

## 모듈 정보

```qml
import QtQuick
```

## 개요

QML에서 **애니메이션(Animation)** 은 시간에 따라 아이템의 프로퍼티 값을 부드럽게 변경하여 시각적인 움직임이나 효과를 만드는 기본 메커니즘입니다. `State`/`Transition` 시스템과 함께 사용되어 상태 변화를 자연스럽게 표현하거나, 단독으로 사용하여 특정 조건에서 애니메이션을 실행할 수도 있습니다.

QML은 다양한 종류의 애니메이션 타입을 제공하며, 이들을 조합하여 복잡한 애니메이션 시퀀스를 구현할 수 있습니다.

`Animation` 타입 자체는 직접 사용할 수 없으며, 다른 모든 애니메이션 타입들의 기반 클래스 역할을 합니다.

## 기반 클래스

*   `Animation` (모든 애니메이션 타입의 추상 기반 클래스)

## 주요 애니메이션 타입

### 1. 프로퍼티 애니메이션 (`PropertyAnimation` 및 하위 클래스)

특정 프로퍼티의 값을 시작 값(`from`)에서 목표 값(`to`)까지 지정된 시간(`duration`) 동안 변경합니다.

*   **`PropertyAnimation`**: 모든 타입의 프로퍼티를 애니메이션할 수 있는 범용 애니메이션. 값 타입에 따라 내부적으로 적절한 인터폴레이터(interpolator)를 사용합니다.
*   **`NumberAnimation`**: 숫자(`real`, `int`) 타입 프로퍼티에 최적화됨.
*   **`ColorAnimation`**: 색상(`color`) 타입 프로퍼티에 최적화됨.
*   **`Vector3dAnimation`**: 3D 벡터(`vector3d`) 타입 프로퍼티에 최적화됨.
*   **`RotationAnimation`**: 아이템의 `rotation` 프로퍼티나 `Transform` 요소의 회전 관련 프로퍼티를 애니메이션합니다.
*   **`AnchorAnimation`**: `anchors` 변경을 애니메이션합니다.
*   **`ParentAnimation`**: 부모 변경(`parent`)을 애니메이션합니다.
*   **`PathAnimation`**: `Path`를 따라 아이템을 이동시킵니다.

**주요 프로퍼티 (PropertyAnimation 기준):**

| 이름         | 타입      | 기본값 | 설명                                                                                                                                 |
| :----------- | :-------- | :----- | :----------------------------------------------------------------------------------------------------------------------------------- |
| `target`     | `Object`  | `null` | 애니메이션을 적용할 대상 객체 (일반적으로 `Item`의 `id`). `Transition` 또는 `Behavior` 내에서는 자동으로 설정되는 경우가 많습니다.                    |
| `property`   | `string`  | ""   | 애니메이션을 적용할 대상 프로퍼티의 이름 (단일 프로퍼티).                                                                                 |
| `properties` | `string`  | ""   | 쉼표(`,`)로 구분하여 여러 프로퍼티 이름을 지정. 모든 프로퍼티에 동일한 `from`, `to`, `duration`, `easing`이 적용됩니다. (`property`와 동시 사용 불가) |
| `from`       | `variant` | (현재값)| 애니메이션 시작 값. 지정하지 않으면 애니메이션 시작 시점의 프로퍼티 현재 값이 사용됩니다.                                                        |
| `to`         | `variant` | (설정 필요)| 애니메이션 목표 값.                                                                                                                    |
| `duration`   | `int`     | 250    | 애니메이션 지속 시간 (밀리초 단위).                                                                                                    |
| `easing`     | `Easing`  | (선형)  | 애니메이션의 속도 변화 곡선. `Easing.Linear`, `Easing.InQuad`, `Easing.OutElastic`, `Easing.InOutBounce` 등 다양한 타입 제공 (`easing.type`, `easing.amplitude` 등 사용). |

### 2. 애니메이션 그룹 (`SequentialAnimation`, `ParallelAnimation`)

여러 애니메이션을 조합하여 복잡한 시퀀스를 만듭니다.

*   **`SequentialAnimation`**: 내부에 포함된 애니메이션들을 순서대로 하나씩 실행합니다.
*   **`ParallelAnimation`**: 내부에 포함된 애니메이션들을 동시에 실행합니다.

### 3. 스크립트 및 제어 애니메이션

애니메이션 흐름을 제어하거나 중간에 코드를 실행합니다.

*   **`ScriptAction`**: 애니메이션 시퀀스 중간에 JavaScript 코드를 실행합니다. `script` 프로퍼티에 실행할 코드를 작성합니다.
*   **`PauseAnimation`**: 지정된 `duration` 동안 애니메이션 실행을 일시 정지합니다.
*   **`PropertyAction`**: 애니메이션 시퀀스 중간에 프로퍼티 값을 즉시 변경합니다.

## Animation 기본 프로퍼티

모든 애니메이션 타입(`PropertyAnimation`, `SequentialAnimation` 등)은 `Animation` 기반 클래스로부터 다음 프로퍼티들을 상속받습니다.

| 이름            | 타입    | 기본값 | 설명                                                                                                                                 |
| :-------------- | :------ | :----- | :----------------------------------------------------------------------------------------------------------------------------------- |
| `running`       | `bool`  | `false`| 애니메이션이 현재 실행 중인지 여부. `true`로 설정하면 애니메이션을 시작하고, `false`로 설정하면 중지합니다. `start()` 및 `stop()` 메서드 사용 권장.       |
| `loops`         | `int`   | 1      | 애니메이션 반복 횟수. `Animation.Infinite`로 설정하면 무한 반복합니다.                                                                       |
| `paused`        | `bool`  | `false`| 애니메이션이 현재 일시 정지 상태인지 여부. `pause()` 및 `resume()` 메서드로 제어할 수도 있습니다.                                                  |
| `alwaysRunToEnd`| `bool`  | `false`| `true`로 설정하면 `stop()` 메서드가 호출되어도 애니메이션이 즉시 멈추지 않고 현재 루프의 끝까지 실행된 후 멈춥니다. `Transition` 내에서는 효과가 없습니다. |

## 사용 방법

애니메이션은 주로 다음과 같은 방식으로 사용됩니다.

1.  **`Transition` 내에서 사용**: 상태 변경 시 자동으로 실행됩니다. (Transition 문서 참고)
    ```qml
    Transition {
        NumberAnimation { properties: "x,y"; duration: 500 }
    }
    ```
2.  **`Behavior` 내에서 사용**: 특정 프로퍼티 값이 변경될 때마다 자동으로 실행됩니다. (Behavior 문서 참고)
    ```qml
    Behavior on x {
        NumberAnimation { duration: 200 }
    }
    ```
3.  **독립적인 애니메이션 객체로 사용**: `id`를 부여하고 `start()`, `stop()`, `pause()`, `resume()` 등의 메서드를 호출하여 직접 제어합니다. 특정 이벤트 핸들러(예: `onClicked`) 내에서 애니메이션을 시작할 때 유용합니다.
```qml
// Window를 사용하여 단독 실행 가능한 예제
import QtQuick
import QtQuick.Controls

Window {
    id: window
    width: 300; height: 150
    visible: true
    title: "Standalone Animation Example"

    Rectangle {
        id: rect
        width: 50; height: 50
        color: "blue"
        // 초기 위치
        x: 20; y: (parent.height - height) / 2

        // X축 이동 애니메이션 정의
        NumberAnimation {
            id: moveAnimation
            target: rect
            property: "x"
            to: window.width - rect.width - 20 // 오른쪽 끝으로 이동
            duration: 1000
            easing.type: Easing.InOutQuad
            // loops: Animation.Infinite // 무한 반복 예시
        }
    }

    // 애니메이션 제어 버튼
    Row {
        anchors.bottom: parent.bottom
        anchors.horizontalCenter: parent.horizontalCenter
        anchors.margins: 10
        spacing: 10

        Button {
            text: "Start"
            onClicked: moveAnimation.start()
        }
        Button {
            text: "Stop"
            onClicked: moveAnimation.stop()
        }
        Button {
            text: "Restart"
            onClicked: moveAnimation.restart() // 추가된 restart() 메소드 예시
        }
    }
}
```

## 주요 시그널 (`Animation` 기반)

| 이름         | 파라미터 | 설명                                                                                                                                        |
| :----------- | :------- | :------------------------------------------------------------------------------------------------------------------------------------------ |
| `started()`  | -        | 애니메이션이 시작될 때 발생합니다. (단, `Behavior`, `Transition`, 그룹 내 애니메이션에서는 발생하지 않음)                                                     |
| `stopped()`  | -        | 애니메이션이 (수동 중지 또는 완료로 인해) 멈췄을 때 발생합니다. (단, `Behavior`, `Transition`, 그룹 내 애니메이션에서는 발생하지 않음)                                |
| `finished()` | -        | 애니메이션이 자연스럽게 완료되었을 때 발생합니다 (`loops`가 `Infinite`가 아니고 `stop()`으로 중지되지 않은 경우). (단, `Behavior`, `Transition`, 그룹 내 애니메이션에서는 발생하지 않음) | 

*참고: `running`, `paused`, `alwaysRunToEnd` 프로퍼티 변경 시 관련 시그널(`runningChanged` 등)도 발생합니다.*

## 주요 메소드 (`Animation` 기반)

| 이름        | 파라미터 | 반환타입 | 설명                                                         |
| :---------- | :------- | :------- | :----------------------------------------------------------- |
| `start()`   | -        | -        | 애니메이션을 시작합니다.                                       |
| `stop()`    | -        | -        | 애니메이션을 중지합니다. `alwaysRunToEnd` 설정에 따라 동작이 달라질 수 있습니다. |
| `pause()`   | -        | -        | 애니메이션을 일시 정지합니다.                                    |
| `resume()`  | -        | -        | 일시 정지된 애니메이션을 재개합니다.                             |
| `restart()` | -        | -        | 애니메이션을 처음부터 다시 시작합니다 (`stop()` 후 `start()`와 유사).  |
| `complete()`| -        | -        | 애니메이션을 즉시 완료 상태로 이동시키고 중지합니다.                   |

## Easing Curves (이징 곡선)

`easing` 프로퍼티는 애니메이션의 속도 변화를 제어하여 더 자연스럽고 보기 좋은 움직임을 만듭니다. `easing.type`에 다양한 값을 설정할 수 있습니다.

*   **Linear**: `Easing.Linear` (일정한 속도, 기본값)
*   **Quadratic**: `Easing.InQuad`, `Easing.OutQuad`, `Easing.InOutQuad`
*   **Cubic**: `Easing.InCubic`, `Easing.OutCubic`, `Easing.InOutCubic`
*   **Quartic**: `Easing.InQuart`, `Easing.OutQuart`, `Easing.InOutQuart`
*   **Quintic**: `Easing.InQuint`, `Easing.OutQuint`, `Easing.InOutQuint`
*   **Sine**: `Easing.InSine`, `Easing.OutSine`, `Easing.InOutSine`
*   **Exponential**: `Easing.InExpo`, `Easing.OutExpo`, `Easing.InOutExpo`
*   **Circular**: `Easing.InCirc`, `Easing.OutCirc`, `Easing.InOutCirc`
*   **Elastic**: `Easing.InElastic`, `Easing.OutElastic`, `Easing.InOutElastic` (추가 프로퍼티: `easing.amplitude`, `easing.period`)
*   **Back**: `Easing.InBack`, `Easing.OutBack`, `Easing.InOutBack` (추가 프로퍼티: `easing.overshoot`)
*   **Bounce**: `Easing.InBounce`, `Easing.OutBounce`, `Easing.InOutBounce` (추가 프로퍼티: `easing.amplitude`, `easing.bounces`)

## 참고 사항

*   애니메이션은 QML UI에 동적인 느낌을 주는 핵심 요소입니다. 적절하게 사용하면 사용자 경험을 크게 향상시킬 수 있습니다.
*   애니메이션 성능은 대상 프로퍼티, 애니메이션 복잡성, 대상 아이템 수 등에 영향을 받습니다. 특히 많은 아이템에 복잡한 애니메이션을 동시에 적용할 때는 성능 테스트가 필요할 수 있습니다.
*   `PropertyAnimation`은 대부분의 경우에 충분하지만, 특정 타입(`number`, `color` 등)에 최적화된 애니메이션 타입을 사용하면 가독성과 잠재적 성능 이점을 얻을 수 있습니다.
*   `SequentialAnimation`과 `ParallelAnimation`을 사용하여 여러 애니메이션을 효과적으로 조합할 수 있습니다.
*   `Easing` 곡선을 적절히 활용하면 애니메이션을 훨씬 더 자연스럽고 보기 좋게 만들 수 있습니다.

## 공식 문서 링크

* [Animation QML Type ](https://doc.qt.io/qt-6/qml-qtquick-animation.html)
* [PropertyAnimation QML Type ](https://doc.qt.io/qt-6/qml-qtquick-propertyanimation.html) (가장 일반적인 애니메이션 타입)
* [Easing QML Type ](https://doc.qt.io/qt-6/qml-qtquick-easing.html) (이징 곡선 상세) 