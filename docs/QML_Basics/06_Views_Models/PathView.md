# PathView

**모듈:** `import QtQuick`

## 개요

`PathView`는 모델(model)의 데이터를 특정 경로(path)를 따라 배치하고 표시하는 뷰(view) 컴포넌트입니다. `ListView`나 `GridView`가 항목들을 직선적인 행이나 열, 격자에 배치하는 것과 달리, `PathView`는 곡선, 원형 등 임의의 경로를 정의하고 그 경로 위에 델리게이트(delegate) 아이템들을 위치시킵니다.

회전 메뉴(Carousel), 커버 플로우(Cover Flow) 등 시각적으로 독특하고 동적인 인터페이스를 구현하는 데 사용됩니다. `PathView`는 경로 상의 현재 항목을 중심으로 다른 항목들의 크기, 투명도, 각도 등을 조절하여 3D 효과나 원근감을 표현할 수도 있습니다.

## 기반 클래스

*   `Item`

## 주요 프로퍼티

`ListView`, `GridView`와 일부 프로퍼티를 공유합니다 (`model`, `delegate`, `count`, `currentIndex`, `currentItem`, `cacheBuffer`).

`PathView`에 특화되거나 중요하게 사용되는 프로퍼티는 다음과 같습니다.

| 이름                 | 타입         | 기본값        | 설명                                                                                                                                                            |
| :------------------- | :----------- | :------------ | :-------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `path`               | `Path`       | `null`        | 델리게이트 아이템들이 배치될 경로를 정의하는 `Path` 객체. `PathLine`, `PathQuad`, `PathCubic`, `PathArc`, `PathSvg` 등을 사용하여 경로를 구성합니다.                                |
| `pathItemCount`      | `int`        | (model.count) | 경로 상에 동시에 표시될(생성될) 델리게이트 아이템의 최대 개수. 모델의 전체 항목 수(`count`)보다 작게 설정하여 성능을 최적화할 수 있습니다.                                |
| `preferredHighlightBegin` | `real`    | 0.5           | 경로 상에서 현재 항목(`currentItem`)이 위치할 선호 지점 (0.0: 경로 시작, 1.0: 경로 끝). 값이 0.5이면 경로의 중앙에 현재 항목이 오도록 합니다.                                       |
| `preferredHighlightEnd` | `real`      | 0.5           | `preferredHighlightBegin`과 동일한 목적이지만, 경로가 닫혀 있지 않을 때 끝 부분에서의 정렬을 위해 사용될 수 있습니다. 일반적으로 `preferredHighlightBegin`과 같은 값을 사용합니다. |
| `highlightRangeMode` | `enumeration`| `StrictlyEnforceRange` | `PathView.onPath`가 `true`인 델리게이트 아이템만 상호작용 가능하게 할지 여부 (`StrictlyEnforceRange`, `ApplyRange`).                                                                 |
| `movementEnded`      | `Signal`     |               | 사용자의 드래그 또는 플릭(flick) 동작으로 인한 뷰 이동이 멈췄을 때 발생하는 시그널.                                                                                       |
| `flickDeceleration`  | `real`       | (플랫폼 의존) | 사용자가 플릭했을 때 뷰가 감속하는 정도.                                                                                                                        |
| `snapMode`           | `enumeration`| `NoSnap`      | 뷰 이동이 멈출 때 가장 가까운 항목에 맞춰지는 방식 (`PathView.NoSnap`, `PathView.SnapToItem`).                                                                        |
| `interactive`        | `bool`       | `true`        | 사용자가 마우스나 터치로 뷰를 드래그하거나 플릭하여 이동시킬 수 있는지 여부.                                                                                             |
| `offset`             | `real`       | 0             | 경로 상의 모든 아이템에 적용될 오프셋 값 (픽셀 단위). 경로 자체를 이동시키는 효과.                                                                                   |
| `maximumFlickVelocity` | `real`    | (플랫폼 의존) | 플릭 동작으로 간주될 최대 속도.                                                                                                                                  |

## Path 객체

`path` 프로퍼티에는 `Path` 객체를 할당해야 합니다. `Path` 객체는 하나 이상의 경로 세그먼트(segment) 요소들로 구성됩니다.

*   **`PathLine { x, y }`**: 현재 지점에서 지정된 `(x, y)`까지 직선 경로를 추가합니다.
*   **`PathQuad { x, y, controlX, controlY }`**: 현재 지점에서 `(x, y)`까지 제어점 `(controlX, controlY)`를 사용하는 2차 베지어 곡선 경로를 추가합니다.
*   **`PathCubic { x, y, control1X, control1Y, control2X, control2Y }`**: 현재 지점에서 `(x, y)`까지 두 개의 제어점을 사용하는 3차 베지어 곡선 경로를 추가합니다.
*   **`PathArc { x, y, radiusX, radiusY, useLargeArc?, direction? }`**: 현재 지점에서 `(x, y)`까지 타원 호 경로를 추가합니다.
*   **`PathSvg { path }`**: SVG 경로 데이터 문자열(`path`)을 사용하여 복잡한 경로를 정의합니다.
*   **`PathMove { x, y }`**: 경로 그리기를 멈추고 새로운 `(x, y)` 지점으로 이동합니다 (경로 시작점 설정 등).

`Path` 객체는 `startX`, `startY` 프로퍼티를 통해 시작점을 명시적으로 지정할 수도 있습니다.

## 델리게이트 컨텍스트 프로퍼티

`PathView`의 델리게이트 내에서는 다음과 같은 추가적인 컨텍스트 프로퍼티를 사용할 수 있습니다.

| 이름             | 타입    | 설명                                                                                                                  |
| :--------------- | :------ | :-------------------------------------------------------------------------------------------------------------------- |
| `PathView.view`  | `PathView`| 부모 `PathView` 인스턴스에 접근.                                                                                        |
| `PathView.onPath`| `bool`  | 현재 델리게이트 아이템이 `pathItemCount`에 의해 실제로 경로 상에 배치되었는지 여부.                                               |
| `PathView.percentage`| `real` | 현재 델리게이트가 경로 상의 어느 지점에 위치하는지 백분율(0.0 ~ 1.0)로 나타냅니다. 경로의 시작 부분이 0.0, 끝 부분이 1.0입니다. |
| `PathView.position` | `real`| 현재 델리게이트가 경로 상의 어느 지점에 위치하는지를 픽셀 단위 거리로 나타냅니다.                                                   |
| `PathView.angle` | `real`  | 현재 델리게이트 위치에서의 경로 접선 각도 (도 단위). 아이템 회전에 사용할 수 있습니다.                                           |
| `PathView.elevation` | `real`| (실험적) 경로 상에서의 상대적인 고도. 3D 효과에 사용될 수 있습니다.                                                            |
| `PathView.progress` | `real`| (실험적) 경로 상에서의 진행률 (0.0 ~ 1.0). `percentage`와 유사하지만 애니메이션 등에 활용될 수 있습니다.                       |

## 예제 (원형 회전 메뉴)

```qml
import QtQuick

Window {
    width: 400; height: 400
    visible: true
    title: "PathView Example (Circular Menu)"

    ListModel {
        id: menuModel
        ListElement { name: "Item 1"; color: "red" }
        ListElement { name: "Item 2"; color: "orange" }
        ListElement { name: "Item 3"; color: "yellow" }
        ListElement { name: "Item 4"; color: "green" }
        ListElement { name: "Item 5"; color: "blue" }
        ListElement { name: "Item 6"; color: "indigo" }
        ListElement { name: "Item 7"; color: "violet" }
    }

    PathView {
        id: pathView
        anchors.fill: parent
        model: menuModel
        pathItemCount: 5 // 경로 상에 동시에 5개 아이템만 표시 (성능 최적화)
        preferredHighlightBegin: 0.5 // 현재 아이템이 경로 중앙(0.5)에 오도록
        preferredHighlightEnd: 0.5

        // 원형 경로 정의
        path: Path {
            startX: pathView.width / 2
            startY: pathView.height / 2 - 120 // 원의 중심에서 위쪽으로 시작

            // 원형 경로 (타원 호 사용, 시작점과 끝점을 같게)
            PathArc {
                x: pathView.width / 2
                y: pathView.height / 2 - 120
                radiusX: 120 // 원의 반지름 X
                radiusY: 120 // 원의 반지름 Y
                useLargeArc: true // 큰 호 사용 (360도 원)
            }
        }

        // 각 항목을 표시할 델리게이트
        delegate: Rectangle {
            id: delegateRect
            width: 60; height: 60
            radius: 30
            color: model.color
            border.color: "white"
            border.width: 2

            // 경로 상에 있을 때만 보이도록 함
            visible: PathView.onPath

            // 델리게이트 아이템의 위치와 크기, 투명도를 경로 상 위치에 따라 조절
            transform: [ // 배열을 사용하여 여러 변형 적용
                // 1. 원점에 대한 오프셋 (아이템 중심이 경로에 오도록)
                Translate { x: -width / 2; y: -height / 2 },

                // 2. 크기 조절 (중앙에 가까울수록 크게)
                Scale {
                    // preferredHighlightBegin (0.5) 에서의 거리를 계산
                    property real distance: Math.abs(PathView.view.pathPercent - 0.5)
                    // 거리가 0에 가까울수록(중앙) 1.0, 멀어질수록 0.5까지 작아짐
                    xScale: 1.0 - distance * 1.0 // 0.5 * 2 = 1.0
                    yScale: 1.0 - distance * 1.0
                    origin.x: delegateRect.width / 2
                    origin.y: delegateRect.height / 2
                },

                // 3. 회전 (경로 각도에 따라 아이템 방향 조절 - 옵션)
                /* Rotate { */
                /*     angle: PathView.angle */
                /*     origin.x: delegateRect.width / 2 */
                /*     origin.y: delegateRect.height / 2 */
                /* } */
            ]

            // 투명도 조절 (중앙에 가까울수록 불투명하게)
            opacity: 1.0 - Math.abs(PathView.view.pathPercent - 0.5) * 1.5 // 0.5 * 1.5 = 0.75

            Text {
                anchors.centerIn: parent
                text: model.name
                color: "white"
                font.bold: true
            }
        }
    }
}
```

## 참고 사항

*   `PathView`의 핵심은 `path` 프로퍼티에 `Path` 객체를 정의하는 것입니다. 다양한 경로 세그먼트를 조합하여 원하는 모양의 경로를 만들 수 있습니다.
*   델리게이트는 `PathView`의 컨텍스트 프로퍼티(`PathView.percentage`, `PathView.angle` 등)를 활용하여 경로 상의 위치에 따라 동적으로 모양, 크기, 회전, 투명도 등을 변경할 수 있습니다. 이는 시각적으로 흥미로운 효과를 만드는 데 중요합니다.
*   `pathItemCount` 프로퍼티는 성능 최적화에 중요합니다. 모델에 항목이 많더라도 실제로 경로 상에 동시에 렌더링될 아이템 수를 제한할 수 있습니다.
*   `preferredHighlightBegin/End` 프로퍼티는 현재 선택된 아이템이 경로 상의 어느 지점에 위치할지를 결정합니다.
*   `PathView`는 내장된 플릭(flick) 및 드래그 스크롤 기능을 제공하며, `snapMode`를 통해 스크롤이 멈출 때 항목에 맞춰지도록 할 수 있습니다.
*   복잡한 경로 정의는 SVG 경로 데이터(`PathSvg`)를 사용하는 것이 더 편리할 수 있습니다. 