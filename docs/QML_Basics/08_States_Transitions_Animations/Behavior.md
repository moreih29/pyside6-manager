# Behavior

**모듈:** `import QtQuick`

## 개요

`Behavior` 요소는 특정 프로퍼티의 값이 변경될 때마다 자동으로 애니메이션을 적용하는 간편한 방법을 제공합니다. `Transition`이 상태 변경 시 애니메이션을 정의하는 반면, `Behavior`는 개별 프로퍼티의 일반적인 변경에 대한 반응으로 애니메이션을 실행합니다.

이를 통해 명시적인 상태나 트랜지션 정의 없이도 UI 요소의 움직임이나 변화를 부드럽게 만들 수 있습니다.

## 사용 방법

`Behavior`는 애니메이션을 적용하려는 프로퍼티와 같은 레벨에 선언하며, `on` 프로퍼티에 대상 프로퍼티의 이름을 지정합니다. `Behavior` 내부에는 하나 이상의 `Animation` 요소를 정의하여 해당 프로퍼티 변경 시 실행될 애니메이션을 지정합니다.

```qml
import QtQuick

Item {
    width: 300; height: 200

    Rectangle {
        id: rect
        width: 50; height: 50
        color: "red"
        x: 0; y: 0

        // x 프로퍼티 값이 변경될 때마다 NumberAnimation을 300ms 동안 실행
        Behavior on x {
            NumberAnimation { duration: 300; easing.type: Easing.OutQuad }
        }

        // opacity 프로퍼티 값이 변경될 때마다 NumberAnimation을 500ms 동안 실행
        Behavior on opacity {
            NumberAnimation { duration: 500 }
        }
    }

    // 버튼을 누르면 사각형의 x 좌표와 투명도 변경
    MouseArea {
        anchors.fill: parent
        onClicked: {
            rect.x = (rect.x === 0) ? 150 : 0 // x 값 변경 (애니메이션 적용됨)
            rect.opacity = (rect.opacity === 1.0) ? 0.5 : 1.0 // opacity 값 변경 (애니메이션 적용됨)
        }
    }
}
```

위 예제에서 사각형(`rect`)의 `x` 프로퍼티가 변경될 때마다 (`onClicked` 핸들러 등에서), `Behavior on x` 내부에 정의된 `NumberAnimation`이 자동으로 실행되어 300ms 동안 부드럽게 이동합니다. 마찬가지로 `opacity` 프로퍼티가 변경될 때도 관련 `Behavior`의 애니메이션이 실행됩니다.

## 주요 프로퍼티

| 이름      | 타입        | 기본값 | 설명                                                                   |
| :-------- | :---------- | :----- | :--------------------------------------------------------------------- |
| `on`      | `property`  | -      | **(필수)** 애니메이션을 적용할 대상 프로퍼티. 프로퍼티의 이름을 직접 명시합니다. |
| `enabled` | `bool`      | `true` | `false`로 설정하면 이 `Behavior`가 비활성화되어 프로퍼티 변경 시 애니메이션이 실행되지 않습니다. |
| `animation`| `Animation` | `null` | 적용할 애니메이션 객체. `Behavior` 내부에 직접 애니메이션을 정의하는 대신 기존 애니메이션 객체를 참조할 때 사용합니다. |

## 애니메이션 지정

`Behavior` 내부에는 하나 이상의 `Animation` 파생 객체를 포함할 수 있습니다.

*   **단일 애니메이션**: 가장 일반적인 경우입니다. 프로퍼티 타입에 맞는 애니메이션(예: `NumberAnimation`, `ColorAnimation`)을 하나 정의합니다.
*   **여러 애니메이션 (그룹 사용)**: `SequentialAnimation`이나 `ParallelAnimation`을 사용하여 여러 효과를 조합할 수 있습니다. (흔하지 않음)
*   **애니메이션 타입 생략**: 특정 `Animation` 타입을 명시하지 않으면 QML이 프로퍼티 타입에 따라 적절한 기본 애니메이션(주로 `PropertyAnimation`)을 자동으로 선택합니다. 이 경우 `duration`이나 `easing` 같은 공통 애니메이션 속성만 지정할 수 있습니다.

    ```qml
    // NumberAnimation을 명시하지 않고 공통 속성만 지정
    Behavior on width {
        // QML이 자동으로 적절한 애니메이션(PropertyAnimation 또는 NumberAnimation)을 생성
        duration: 500
        easing.type: Easing.InOutSine
    }
    ```

## 참고 사항

*   `Behavior`는 특정 프로퍼티의 모든 변경에 대해 애니메이션을 적용하고자 할 때 매우 유용합니다. 예를 들어, 레이아웃 변경에 따라 요소의 위치나 크기가 바뀔 때 부드러운 전환 효과를 줄 수 있습니다.
*   상태 기반의 복잡한 전환 로직에는 `State`와 `Transition`을 사용하는 것이 더 적합할 수 있습니다.
*   `Behavior` 내부의 애니메이션은 `target`이나 `property`/`properties`를 명시할 필요가 없습니다. `Behavior`가 적용되는 대상 객체와 `on` 프로퍼티를 통해 자동으로 설정됩니다.
*   `enabled` 프로퍼티를 사용하여 특정 조건에서 `Behavior`를 동적으로 활성화하거나 비활성화할 수 있습니다. 