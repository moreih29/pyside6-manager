# MultiPointTouchArea

**모듈:** `import QtQuick`

## 개요

`MultiPointTouchArea`는 터치스크린에서 발생하는 하나 이상의 터치 포인트(touch points)를 감지하고 해당 정보를 제공하는 보이지 않는 아이템입니다. 개별 터치 포인트의 시작, 이동, 종료 및 속성(위치, 압력 등)을 추적하여 복잡한 멀티터치 제스처를 직접 구현하는 데 사용됩니다.

`PinchArea`가 핀치 제스처에 특화된 편의 기능을 제공하는 반면, `MultiPointTouchArea`는 더 낮은 수준의 터치 이벤트 정보를 제공하여 개발자가 자유롭게 제스처를 정의하고 구현할 수 있도록 합니다.

## 주요 프로퍼티

| 이름              | 타입                       | 기본값 | 설명                                                                                         |
| :---------------- | :------------------------- | :----- | :------------------------------------------------------------------------------------------- |
| `enabled`         | `bool`                     | `true` | `MultiPointTouchArea`가 활성화되어 터치 이벤트를 받을지 여부.                                    |
| `touchPoints`     | `list<TouchPoint>`         | `[]`   | (읽기 전용) 현재 활성화된(화면에 닿아 있는) 터치 포인트 목록.                                  |
| `minimumTouchPoints` | `int`                   | 0      | 이벤트를 받기 시작하기 위해 필요한 최소 터치 포인트 수. 0이면 제한 없음.                       |
| `maximumTouchPoints` | `int`                   | 0      | 동시에 처리할 최대 터치 포인트 수. 0이면 제한 없음.                                           |
| `mouseEnabled`    | `bool`                     | `false`| 마우스 이벤트를 터치 이벤트로 시뮬레이션할지 여부 (테스트용).                                |
| `acceptedButtons` | `Qt::MouseButtons`         | `Qt::LeftButton` | `mouseEnabled`가 `true`일 때 터치 시뮬레이션에 사용할 마우스 버튼.                           |

### TouchPoint 객체 주요 속성 (`touchPoints` 리스트 내 객체)

| 이름           | 타입      | 설명                                                                    |
| :------------- | :-------- | :---------------------------------------------------------------------- |
| `pointId`      | `int`     | 각 터치 포인트를 고유하게 식별하는 ID.                                      |
| `startX`, `startY` | `real`  | 터치 포인트가 시작된 위치 (`MultiPointTouchArea` 기준).                 |
| `x`, `y`       | `real`    | 현재 터치 포인트의 위치 (`MultiPointTouchArea` 기준).                     |
| `previousX`, `previousY` | `real` | 이전 터치 이벤트에서의 위치 (`MultiPointTouchArea` 기준).                   |
| `pressure`     | `real`    | 터치 압력 (0.0 ~ 1.0). 하드웨어 지원 필요.                                |
| `velocity`     | `QVector2D` | 터치 포인트의 현재 속도 벡터.                                            |
| `pressed`      | `bool`    | 현재 터치 포인트가 눌린 상태인지 여부 (시작~종료 사이).                     |
| `area`         | `QSizeF`  | (일부 하드웨어) 터치 영역의 크기 추정치.                                  |

## 주요 시그널

| 이름              | 파라미터                   | 반환타입 | 설명                                                                 |
| :---------------- | :------------------------- | :------- | :------------------------------------------------------------------- |
| `touchUpdated`    | -                          | -        | 하나 이상의 활성 `touchPoints` 속성이 변경될 때마다 발생.           |
| `pressed`         | `list<TouchPoint> points`  | -        | 하나 이상의 새로운 터치 포인트가 눌렸을 때 발생 (시작). `points`는 새로 눌린 포인트 목록. |
| `updated`         | `list<TouchPoint> points`  | -        | 기존 터치 포인트의 속성(위치, 압력 등)이 변경되었을 때 발생. `points`는 변경된 포인트 목록. |
| `released`        | `list<TouchPoint> points`  | -        | 하나 이상의 터치 포인트가 화면에서 떼어졌을 때 발생 (종료). `points`는 떼어진 포인트 목록. |
| `canceled`        | `list<TouchPoint> points`  | -        | 시스템 등의 이유로 터치 이벤트가 예기치 않게 중단될 때 발생.         |
| `gestureStarted`  | `GestureEvent event`       | -        | 특정 제스처(플랫폼 종속적일 수 있음)가 시작될 때 발생 (고급 사용).   |

## 예제

```qml
import QtQuick

Window {
    width: 500
    height: 400
    visible: true
    title: "MultiPointTouchArea Example"

    MultiPointTouchArea {
        id: touchArea
        anchors.fill: parent
        minimumTouchPoints: 1 // 최소 1개 터치부터 감지
        maximumTouchPoints: 5 // 최대 5개 터치 동시 처리

        // 터치 포인트를 시각적으로 표시하기 위한 리피터
        Repeater {
            model: touchArea.touchPoints // 현재 활성 터치 포인트 목록 사용

            Rectangle {
                id: touchIndicator
                width: 40 * modelData.pressure + 20 // 압력에 따라 크기 변경 (지원 시)
                height: width
                radius: width / 2
                color: Qt.rgba(0.2, 0.5, 0.8, 0.7)
                border.color: "steelblue"
                // 터치 포인트 위치에 배치
                x: modelData.x - width / 2
                y: modelData.y - height / 2

                property point startPos: Qt.point(modelData.startX, modelData.startY)
                property int pointId: modelData.pointId

                Text {
                    anchors.centerIn: parent
                    color: "white"
                    text: touchIndicator.pointId + "\n(" + Math.round(parent.x) + ", " + Math.round(parent.y) + ")"
                    font.pointSize: 8
                }

                // 터치 시작 위치 표시 (선택 사항)
                Rectangle {
                    x: touchIndicator.startPos.x - touchIndicator.x - 5 // 상대 위치 계산
                    y: touchIndicator.startPos.y - touchIndicator.y - 5 // 상대 위치 계산
                    width: 10; height: 10
                    color: "transparent"
                    border.color: "red"
                }
            }
        }

        // 시그널 핸들러 예시
        onTouchUpdated: {
            // console.log("Touch Updated: Active points =", touchPoints.length)
            // 여기서 touchPoints 리스트를 분석하여 커스텀 제스처 로직 구현 가능
        }

        onPressed: (points) => {
            for (var i = 0; i < points.length; ++i) {
                console.log("Pressed point ID:", points[i].pointId, "at", points[i].x, points[i].y)
            }
        }

        onReleased: (points) => {
             for (var i = 0; i < points.length; ++i) {
                console.log("Released point ID:", points[i].pointId)
            }
        }
    }

    Text {
        anchors.bottom: parent.bottom
        anchors.horizontalCenter: parent.horizontalCenter
        anchors.bottomMargin: 10
        text: "Touch the screen with multiple fingers."
    }
}
```

## 참고 사항

*   `touchPoints` 프로퍼티는 현재 *활성* 상태인 터치 포인트의 목록만 포함합니다. 터치가 시작되거나 끝나는 순간의 정보는 `pressed`, `released` 시그널의 파라미터를 통해 얻는 것이 더 정확할 수 있습니다.
*   `onTouchUpdated` 시그널은 터치 포인트의 속성이 변경될 때마다 매우 빈번하게 발생할 수 있으므로, 성능에 민감한 로직은 주의해서 구현해야 합니다.
*   복잡한 제스처(예: 스와이프, 회전, 탭 등)를 직접 구현하려면 `touchPoints` 목록의 변화를 추적하고 상태를 관리하는 로직이 필요합니다.
*   `QtQuick.InputHandlers` 모듈의 `TapHandler`, `DragHandler`, `PinchHandler` 등을 사용하면 일반적인 제스처를 더 쉽게 구현할 수 있습니다. 