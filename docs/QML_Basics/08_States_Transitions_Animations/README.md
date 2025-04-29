# 08_States_Transitions_Animations: 동적인 UI 상태 변화 및 시각 효과

이 카테고리에서는 QML 애플리케이션에 동적인 움직임과 시각적인 피드백을 추가하는 데 사용되는 상태(State), 전환(Transition), 애니메이션(Animation) 관련 개념과 컴포넌트들을 다룹니다.

정적인 UI에서 벗어나 사용자의 행동이나 애플리케이션의 상태 변화에 따라 부드럽고 자연스럽게 변화하는 인터페이스를 구현하는 데 필수적인 요소들입니다.

## 주요 컴포넌트 및 개념

이 섹션에서는 상태, 전환, 애니메이션과 관련된 주요 요소들을 설명합니다.

*   **상태 (States)**:
    *   **[State](./State.md)**: QML 아이템이 가질 수 있는 특정 **시각적 또는 논리적 상태**를 정의합니다. 각 상태는 아이템 프로퍼티의 목표 값(`PropertyChanges`)이나 상태 진입/종료 시 실행될 스크립트(`StateChangeScript`)를 포함할 수 있습니다. 아이템의 `state` 프로퍼티를 변경하여 상태를 전환합니다.
    *   `states` 프로퍼티: `Item`의 프로퍼티로, 해당 아이템이 가질 수 있는 `State` 객체들의 리스트를 담습니다.
    *   `state` 프로퍼티: `Item`의 프로퍼티로, 현재 활성화된 상태의 이름을 나타냅니다. 이 값을 변경하여 아이템의 상태를 전환합니다.
    *   `PropertyChanges`: 특정 상태에서 변경될 프로퍼티와 그 목표 값을 지정합니다.
    *   `StateChangeScript`: 상태가 변경될 때 실행될 JavaScript 코드를 정의합니다.
    *   `when` 프로퍼티 (`State` 내부): 특정 조건이 참일 때 해당 상태가 자동으로 활성화되도록 합니다.
*   **전환 (Transitions)**:
    *   **[Transition](./Transition.md)**: 아이템의 상태(`state`)가 특정 값(`from`)에서 다른 값(`to`)으로 **변경될 때 적용될 애니메이션이나 스크립트**를 정의합니다. 상태 변경 시 프로퍼티 값이 부드럽게 변하는 효과를 만듭니다. `Item`의 `transitions` 프로퍼티에 리스트 형태로 포함됩니다.
    *   `from`, `to` 프로퍼티: 전환이 적용될 시작 상태(`from`)와 목표 상태(`to`)를 지정합니다. 와일드카드(`"*"`)를 사용하여 모든 상태 변화에 적용할 수도 있습니다.
    *   애니메이션 요소 (`NumberAnimation`, `ColorAnimation`, `PropertyAnimation` 등): 전환 과정 동안 프로퍼티 값이 어떻게 변할지를 정의합니다.
    *   `SequentialAnimation`, `ParallelAnimation`: 여러 애니메이션을 순차적 또는 병렬적으로 실행합니다.
    *   `ScriptAction`: 전환 중에 JavaScript 코드를 실행합니다.
*   **애니메이션 (Animations)**:
    *   **[Animation](./Animation.md)**: QML에서 프로퍼티 값을 **시간에 따라 부드럽게 변경하는 기본 메커니즘**입니다. 상태 전환(`Transition`), 프로퍼티 변경 감지(`Behavior`), 또는 독립적인 애니메이션 객체로 사용될 수 있습니다.
    *   `PropertyAnimation` (및 하위 타입): 특정 프로퍼티를 대상으로 하는 가장 일반적인 애니메이션 (`NumberAnimation`, `ColorAnimation`, `RotationAnimation` 등).
    *   `SequentialAnimation`, `ParallelAnimation`: 여러 애니메이션을 조합하여 복잡한 애니메이션 시퀀스를 만듭니다.
    *   `PauseAnimation`: 애니메이션 시퀀스 중간에 지연 시간을 추가합니다.
    *   `ScriptAction`: 애니메이션 도중 JavaScript 코드를 실행합니다.
    *   `easing` 프로퍼티: 애니메이션의 속도 변화 곡선(예: `Easing.InOutQuad`)을 제어하여 자연스러운 움직임을 만듭니다.
*   **동작 (Behaviors)**:
    *   **[Behavior](./Behavior.md)**: 특정 프로퍼티의 값이 **(상태 변경과 무관하게) 직접 변경될 때마다** 자동으로 적용될 애니메이션을 지정합니다. `on` 프로퍼티에 대상 프로퍼티 이름을 명시합니다. 레이아웃 변경 등에 따른 위치/크기 변화에 부드러운 효과를 줄 때 유용합니다.

## 핵심 원리

1.  **상태 정의**: 아이템이 가질 수 있는 여러 시각적 또는 논리적 상태를 `State` 요소로 정의합니다. (`states` 리스트 내)
2.  **상태 변경**: 아이템의 `state` 프로퍼티 값을 변경하여 원하는 상태로 전환합니다.
3.  **전환 정의**: `transitions` 리스트에 상태 변경(`from` -> `to`) 시 적용될 애니메이션(`PropertyAnimation` 등)을 `Transition` 요소로 정의하여 부드러운 시각적 변화를 만듭니다.
4.  **애니메이션 적용**: 상태가 변경되면 해당 `Transition`에 정의된 애니메이션이 자동으로 실행됩니다.
5.  **Behavior 활용**: 상태 변경과 별개로, 특정 프로퍼티 값이 코드나 바인딩에 의해 직접 변경될 때마다 항상 애니메이션 효과를 주고 싶다면 `Behavior on <propertyName>`를 사용합니다.

이 카테고리의 문서들을 통해 QML 애플리케이션에 생동감을 불어넣는 상태 관리, 전환 효과, 다양한 애니메이션 기법을 익힐 수 있습니다. 