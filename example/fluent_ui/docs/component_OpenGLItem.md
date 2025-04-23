# `OpenGLItem.py` 문서

이 파일은 QML 내에서 사용자 정의 OpenGL 렌더링을 수행하는 컴포넌트를 정의합니다.

## `OpenGLItem` 클래스

`QQuickFramebufferObject`를 상속받아 QML 아이템으로 작동하며, 자체적인 Framebuffer Object(FBO)에 OpenGL 명령을 사용하여 렌더링합니다.

**주요 기능:**

*   QML 아이템 영역 내에 OpenGL 컨텍스트를 설정하고 렌더링을 수행합니다.
*   내부 `FBORenderer` 클래스를 사용하여 실제 OpenGL 렌더링 로직을 구현합니다.
*   간단한 시간 기반 애니메이션 값(`t` 속성)을 제공하여 셰이더에서 활용할 수 있도록 합니다.

**속성:**

*   `t`: 시간에 따라 변경되는 부동 소수점 값. `tChanged` 시그널과 함께 QML에서 접근 가능하며, 셰이더 파라미터 등으로 사용될 수 있습니다.

**시그널:**

*   `tChanged`: `t` 속성 값이 변경될 때 발생합니다.

**내부 클래스: `FBORenderer`**

`QQuickFramebufferObject.Renderer`와 `QOpenGLFunctions`를 상속받아 실제 렌더링 작업을 담당합니다.

*   **주요 역할:**
    *   OpenGL 함수 초기화 (`initializeOpenGLFunctions`).
    *   Vertex 및 Fragment 셰이더를 컴파일하고 링크하여 셰이더 프로그램(`program`) 생성.
    *   렌더링 대상이 될 Framebuffer Object(`__openGLFb`) 생성 (`createFramebufferObject` 메서드).
    *   매 프레임 렌더링 로직 수행 (`render` 메서드):
        *   화면 지우기 (`glClear`).
        *   셰이더 프로그램 바인딩 및 속성/유니폼 설정 (정점 데이터, `t` 값 등).
        *   OpenGL 그리기 명령 실행 (`glDrawArrays`).
        *   블렌딩 설정 (`glEnable(GL_BLEND)`, `glBlendFunc`).

*   **셰이더 코드:**
    *   **Vertex Shader:** 정점 위치를 그대로 전달하고, 좌표(`coords`)를 Fragment 셰이더로 넘깁니다.
    *   **Fragment Shader:** `coords`와 `t` 유니폼 값을 사용하여 색상을 계산합니다. 예제 코드는 시간에 따라 변화하는 패턴을 그립니다 (`smoothstep`, `floor` 함수 사용).

**메서드:**

*   `createRenderer(self)`: `QQuickFramebufferObject`의 가상 함수를 구현하여 `FBORenderer` 인스턴스를 생성하고 반환합니다.
*   `timerEvent(self, event)`: 주기적으로 `update()`를 호출하여 화면을 다시 그리도록 요청합니다. (1ms 간격 타이머)

**사용 예 (QML):**

```qml
import example 1.0

OpenGLItem {
    id: glItem
    width: 200
    height: 200
    // t 속성은 시간에 따라 자동으로 변경됨
    // 예를 들어 t 값에 따라 다른 효과를 주거나 QML 애니메이션과 연동 가능
    NumberAnimation on t {
        from: 0
        to: 1
        duration: 2000
        loops: Animation.Infinite
    }
}
``` 