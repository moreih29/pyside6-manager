# `FpsItem.py` 문서

이 파일은 QML에서 현재 화면의 초당 프레임 수(FPS)를 계산하고 표시하는 컴포넌트를 정의합니다.

## `FpsItem` 클래스

`QQuickPaintedItem`을 상속받아 QML에 그려지는 아이템이지만, 실제로는 화면에 아무것도 그리지 않고 FPS 계산 로직만 수행합니다. (Paint 메서드가 구현되어 있지 않음)

**주요 기능:**

*   `QTimer`를 사용하여 1초 간격으로 프레임 수를 계산합니다.
*   윈도우의 `afterRendering` 시그널에 연결하여 매 프레임 렌더링이 끝날 때마다 내부 프레임 카운트(`_frameCount`)를 증가시킵니다.
*   1초마다 타이머의 `timeout` 시그널이 발생하면, 그동안 누적된 프레임 카운트를 `fps` 속성에 저장하고 프레임 카운트를 0으로 리셋합니다.

**속성:**

*   `fps`: 계산된 초당 프레임 수. QML에서 읽기 전용으로 사용할 수 있으며, 값이 변경될 때 `fpsChanged` 시그널이 발생합니다.

**시그널:**

*   `fpsChanged`: `fps` 속성 값이 업데이트될 때 발생합니다.

**메서드:**

*   `__init__(self)`: 클래스 생성자. 타이머를 설정하고 윈도우 변경 및 타이머 시그널에 대한 연결을 설정합니다.
*   `frameCountIncrease(self)`: 내부 프레임 카운트를 1 증가시킵니다. `window().afterRendering` 시그널에 의해 호출됩니다.
*   `onWindowChanged(self)`: 아이템이 속한 윈도우가 변경될 때 호출됩니다. 새 윈도우의 `afterRendering` 시그널에 `frameCountIncrease` 메서드를 연결합니다.
*   `onTimeout(self)`: 1초마다 타이머에 의해 호출됩니다. 현재 프레임 카운트를 `fps` 속성에 설정하고 카운트를 초기화합니다.

**사용 예 (QML):**

```qml
import example 1.0

Item {
    FpsItem {
        id: fpsCounter
    }

    Text {
        text: "FPS: " + fpsCounter.fps
    }
}
``` 