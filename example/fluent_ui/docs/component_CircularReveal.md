# `CircularReveal.py` 문서

이 파일은 QML에서 원형 노출(Circular Reveal) 애니메이션 효과를 구현하는 컴포넌트를 정의합니다.

## `CircularReveal` 클래스

`QQuickPaintedItem`을 상속받아 QML 화면에 그려지는 아이템으로 작동합니다.

**주요 기능:**

*   지정된 대상(`target` 속성) 아이템의 이미지를 캡처합니다.
*   캡처한 이미지를 배경으로 사용하여, 지정된 중심점(`center`)에서 시작하여 반지름(`radius`)이 점차 커지는 원형 클리핑 마스크 애니메이션을 통해 내용을 서서히 드러내는 효과를 구현합니다.
*   `QPropertyAnimation`을 사용하여 반지름 변경 애니메이션을 제어합니다.

**속성:**

*   `radius`: 원형 클리핑 마스크의 현재 반지름. 애니메이션을 통해 값이 변경됩니다.
*   `target`: 원형 노출 효과를 적용할 대상 QML 아이템.

**시그널:**

*   `radiusChanged`: `radius` 속성이 변경될 때 발생합니다.
*   `imageChanged`: 대상 아이템의 이미지를 성공적으로 캡처했을 때 발생합니다.
*   `animationFinished`: 반지름 애니메이션이 완료되었을 때 발생합니다.
*   `targetChanged`: `target` 속성이 변경될 때 발생합니다.

**메서드 (Slots):**

*   `start(self, w: int, h: int, center: QPoint, radius: int)`: 애니메이션을 시작합니다. 대상 아이템의 크기(`w`, `h`), 애니메이션 중심점(`center`), 최종 반지름(`radius`)을 인자로 받습니다. 이 메서드는 대상 아이템의 이미지를 비동기적으로 캡처(`grabToImage`)하고, 캡처가 완료되면 `handleGrabResult` 슬롯을 호출합니다.
*   `handleGrabResult(self)`: 이미지 캡처가 완료되었을 때 호출됩니다. 캡처된 이미지를 내부 `_source`에 저장하고, 아이템을 보이게 설정한 후 반지름 애니메이션(`_anim`)을 시작합니다.
*   `onAnimaFinish(self)`: 애니메이션이 완료되었을 때 호출됩니다. 아이템을 다시 보이지 않게 설정하고 `animationFinished` 시그널을 발생시킵니다.

**기타 메서드:**

*   `paint(self, painter: QPainter)`: `QQuickPaintedItem`의 메서드를 오버라이드하여 실제 그리기 작업을 수행합니다. 캡처된 이미지를 그리고, 계산된 원형 경로를 사용하여 클리핑 마스크 효과를 적용합니다.
*   `release(self)`: 애니메이션 객체와 이미지 데이터 등 리소스를 해제합니다. 