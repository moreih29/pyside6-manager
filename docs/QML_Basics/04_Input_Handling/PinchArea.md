# PinchArea

**모듈:** `import QtQuick`

## 개요

`PinchArea`는 터치스크린에서 두 손가락을 이용한 핀치(pinch) 제스처(오므리기/벌리기)를 감지하고 처리하는 보이지 않는 아이템입니다. 주로 이미지 확대/축소, 지도 줌 레벨 변경 등과 같이 스케일(scale)이나 회전(rotation)을 조작하는 인터페이스에 사용됩니다.

`MouseArea`와 유사하게 다른 시각적 아이템 위에 배치되어 해당 영역에서 발생하는 핀치 이벤트를 처리합니다.

## 주요 프로퍼티

| 이름        | 타입         | 기본값 | 설명                                                                                                        |
| :---------- | :----------- | :----- | :---------------------------------------------------------------------------------------------------------- |
| `enabled`   | `bool`       | `true` | `PinchArea`가 활성화되어 핀치 제스처를 받을지 여부.                                                            |
| `pinch.target` | `Item`    | `null` | 핀치 제스처가 적용될 대상 아이템. 지정하지 않으면 `PinchArea`의 부모 아이템이 대상이 됩니다.                     |
| `pinch.active` | `bool`    | `false`| (읽기 전용) 현재 핀치 제스처가 진행 중인지 여부.                                                               |
| `pinch.scale`| `real`    | 1.0    | (읽기 전용) 핀치 제스처 시작 시점 대비 현재 스케일 비율. 오므리면 1.0보다 작아지고, 벌리면 1.0보다 커집니다.      |
| `pinch.previousScale`| `real` | 1.0  | (읽기 전용) 이전 `pinchUpdated` 시그널에서의 `pinch.scale` 값.                                                 |
| `pinch.rotation`| `real`   | 0.0    | (읽기 전용) 핀치 제스처 시작 시점 대비 현재 회전 각도 (도 단위). 시계 방향 회전이 양수 값입니다.                |
| `pinch.previousRotation`| `real` | 0.0 | (읽기 전용) 이전 `pinchUpdated` 시그널에서의 `pinch.rotation` 값.                                              |
| `pinch.center` | `QPointF` | -      | (읽기 전용) 현재 두 터치 지점의 중심 좌표 (`PinchArea` 기준).                                                  |
| `pinch.startCenter` | `QPointF` | -    | (읽기 전용) 핀치 제스처가 시작될 때의 두 터치 지점 중심 좌표 (`PinchArea` 기준).                                 |
| `minimumScale`, `maximumScale` | `real` | 0, infinity | `pinch.scale`의 최소/최대 허용 값. 제스처 중 이 범위를 넘어도 값은 계속 계산되지만, 제스처 종료 시 이 범위로 제한될 수 있음. |
| `minimumRotation`, `maximumRotation` | `real` | -360, 360 | `pinch.rotation`의 최소/최대 허용 값.                                                                       |
| `acceptedButtons` | `Qt.MouseButtons` | `Qt.LeftButton` | (주로 테스트용) 마우스로 핀치 제스처를 시뮬레이션할 때 사용할 버튼 (Ctrl + 마우스 버튼 조합).                 |

## 주요 시그널

| 이름            | 파라미터            | 반환타입 | 설명                                                 |
| :-------------- | :------------------ | :------- | :--------------------------------------------------- |
| `pinchStarted`  | `PinchEvent pinch`  | -        | 핀치 제스처가 시작될 때 발생.                      |
| `pinchUpdated`  | `PinchEvent pinch`  | -        | 핀치 제스처 중 스케일, 회전 또는 중심이 변경될 때 발생. |
| `pinchFinished` | `PinchEvent pinch`  | -        | 핀치 제스처가 종료될 때 발생.                      |

**PinchEvent 파라미터:** `pinchStarted`, `pinchUpdated`, `pinchFinished` 시그널 핸들러 내에서 위 프로퍼티 테이블의 `pinch.*` 속성들에 접근할 수 있습니다 (예: `pinch.scale`, `pinch.rotation`).

## 예제

```qml
import QtQuick

Window {
    width: 400
    height: 400
    visible: true
    title: "PinchArea Example"

    Rectangle {
        id: targetRect
        width: 100
        height: 100
        color: "lightblue"
        anchors.centerIn: parent
        // 핀치 제스처의 기준점을 중앙으로 설정
        transformOrigin: Item.Center

        Text {
            anchors.centerIn: parent
            text: "Pinch Me!"
        }
    }

    PinchArea {
        anchors.fill: parent // Window 전체 영역에서 핀치 감지

        // pinch.target을 명시적으로 설정 (기본값은 parent이므로 여기선 생략 가능)
        // pinch.target: targetRect

        property real currentScale: 1.0
        property real currentRotation: 0.0

        onPinchStarted: {
            console.log("Pinch started")
            // 제스처 시작 시점의 스케일/회전을 저장할 필요는 없음 (pinch.scale/rotation이 상대값이므로)
        }

        onPinchUpdated: (pinch) => {
            // 이전 상태에서 변화량만큼 스케일/회전 적용
            currentScale += pinch.scale - pinch.previousScale
            currentRotation += pinch.rotation - pinch.previousRotation

            // 스케일 제한 (옵션)
            currentScale = Math.max(0.5, Math.min(currentScale, 3.0))

            // 대상 아이템에 적용
            targetRect.scale = currentScale
            targetRect.rotation = currentRotation

            console.log("Pinch updated: scale=", pinch.scale.toFixed(2),
                        "rotation=", pinch.rotation.toFixed(2),
                        "center=", pinch.center.x.toFixed(0), pinch.center.y.toFixed(0))
        }

        onPinchFinished: (pinch) => {
            // 제스처 종료 시 최종 상태 업데이트 (onPinchUpdated에서 이미 처리됨)
            console.log("Pinch finished")
            // 필요하다면 여기서 최종 스케일/회전 값 정리
            // targetRect.scale = pinch.scale; // 이렇게 하면 제스처 동안의 누적이 아닌 최종 상대값만 반영됨
            // targetRect.rotation = pinch.rotation;
        }
    }
}
```

## 참고 사항

*   `PinchArea`는 두 개 이상의 터치 포인트가 감지될 때 활성화됩니다.
*   `onPinchUpdated` 핸들러에서 `pinch.scale`과 `pinch.rotation`은 제스처 *시작* 시점 기준의 *상대적인* 값입니다. 따라서 일반적으로 이전 상태 값(`pinch.previousScale`, `pinch.previousRotation`)과의 차이를 계산하여 현재 아이템의 스케일/회전에 누적 적용합니다.
*   핀치 제스처의 중심(`pinch.center`)을 변형의 기준점(`transformOrigin`)으로 사용하면 사용자가 핀치하는 지점을 중심으로 확대/축소/회전하는 효과를 만들 수 있습니다 (예제에서는 `Item.Center` 사용).
*   `MultiPointTouchArea`는 더 일반적인 멀티 터치 이벤트를 처리하며, `PinchArea`는 핀치 제스처에 특화된 편의 기능을 제공합니다.
*   마우스 시뮬레이션: Ctrl 키를 누른 상태에서 왼쪽 마우스 버튼으로 드래그하면 스케일 변경, 오른쪽 마우스 버튼으로 드래그하면 회전을 시뮬레이션할 수 있습니다. 