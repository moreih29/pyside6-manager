# Flickable

## 모듈 정보

```qml
import QtQuick
```

## 개요

`Flickable`은 자식 아이템이 자신의 영역보다 클 경우, 사용자가 마우스 드래그나 터치스크린에서의 플릭(flick) 제스처를 통해 내용을 스크롤하거나 이동시킬 수 있도록 하는 컨테이너 아이템입니다.

`Flickable` 자체는 보이지 않지만, `contentItem` 프로퍼티에 할당된 (일반적으로 단일) 자식 아이템의 내용을 표시하고 스크롤하는 기능을 제공합니다. `ListView`, `GridView`, `TextArea` 등 많은 QML 컴포넌트들이 내부적으로 `Flickable`을 사용하여 스크롤 기능을 구현합니다.

## 주요 프로퍼티

| 이름               | 타입        | 기본값 | 설명                                                                                                        |
| :----------------- | :---------- | :----- | :---------------------------------------------------------------------------------------------------------- |
| `contentX`         | `real`      | 0      | 보이는 영역의 왼쪽 상단 모서리에 해당하는 `contentItem`의 X 좌표.                                                  |
| `contentY`         | `real`      | 0      | 보이는 영역의 왼쪽 상단 모서리에 해당하는 `contentItem`의 Y 좌표.                                                  |
| `contentWidth`     | `real`      | 0      | 스크롤 가능한 전체 콘텐츠 영역의 너비. 보통 `contentItem`의 `implicitWidth`나 명시적 `width`에 바인딩됩니다.        |
| `contentHeight`    | `real`      | 0      | 스크롤 가능한 전체 콘텐츠 영역의 높이. 보통 `contentItem`의 `implicitHeight`나 명시적 `height`에 바인딩됩니다.     |
| `contentItem`      | `Item`      | `null` | `Flickable`이 스크롤할 대상 아이템. 일반적으로 `Flickable`의 자식으로 선언하고 이 프로퍼티에 할당합니다.               |
| `flickableDirection`| `enum`     | `Flickable.AutoFlickDirection` | 플릭 방향을 제어 (`AutoFlickDirection`, `HorizontalFlick`, `VerticalFlick`, `HorizontalAndVerticalFlick`, `NoFlick`). |
| `interactive`      | `bool`      | `true` | 사용자가 마우스나 터치로 플릭/드래그할 수 있는지 여부.                                                             |
| `boundsBehavior`   | `enum`      | `Flickable.DragOverBounds` | 콘텐츠가 경계를 넘어 스크롤될 때의 동작 (`StopAtBounds`, `DragOverBounds`, `DragAndOvershootBounds`).            |
| `boundsMovement`   | `enum`      | `Flickable.FollowBoundsBehavior` | 경계 도달 시 콘텐츠 이동 방식 (`StopAtBounds`, `FollowBoundsBehavior`, `OvershootAlways`, `OvershootWhenScrollable`). |
| `flicking`         | `bool`      | `false`| (읽기 전용) 현재 플릭 애니메이션이 진행 중인지 여부.                                                              |
| `moving`           | `bool`      | `false`| (읽기 전용) 현재 사용자의 드래그나 플릭 애니메이션으로 인해 콘텐츠가 이동 중인지 여부.                              |
| `maximumFlickVelocity` | `real`  | `platform dependent` | 플릭 제스처의 최대 속도. 플랫폼 기본값 사용. |
| `pixelAligned`     | `bool`      | `false`| `true`이면 콘텐츠 위치를 픽셀 경계에 맞춥니다. 기본값 `false`. |
| `pressDelay`       | `int`       | `platform dependent` | 터치 시작 후 플릭/드래그 감지를 시작하기까지의 지연 시간(ms). 기본값 플랫폼 종속. |
| `reboundTransition`| `Transition`| -      | `returnToBounds()` 호출 시 사용되는 애니메이션 트랜지션. |
| `syncDirection`    | `enum`      | `Qt.Vertical` | (Qt 6.x+) 스크롤 동기화 방향. 현재 문서에서는 상세 설명 생략. 기본값 `Qt.Vertical`. |
| `atXBeginning`, `atXEnd` | `bool` | `false`| (읽기 전용) 수평 스크롤이 각각 시작 또는 끝 지점에 도달했는지 여부.                                                |
| `atYBeginning`, `atYEnd` | `bool` | `false`| (읽기 전용) 수직 스크롤이 각각 시작 또는 끝 지점에 도달했는지 여부.                                                |
| `visibleArea.xPosition`, `visibleArea.yPosition` | `real` | 0.0    | (읽기 전용) 현재 보이는 영역의 상대적 위치 (0.0 ~ 1.0). `ScrollBar` 등과 바인딩하기 유용.                     |
| `visibleArea.widthRatio`, `visibleArea.heightRatio` | `real` | 1.0    | (읽기 전용) 전체 콘텐츠 대비 보이는 영역의 비율 (0.0 ~ 1.0). `ScrollBar` 등과 바인딩하기 유용.                |

## 주요 시그널

| 이름               | 파라미터 | 반환타입 | 설명                                             |
| :----------------- | :------- | :------- | :----------------------------------------------- |
| `contentXChanged`  | -        | -        | `contentX` 값이 변경되었을 때 발생.             |
| `contentYChanged`  | -        | -        | `contentY` 값이 변경되었을 때 발생.             |
| `movementStarted`  | -        | -        | 콘텐츠 이동(드래그 또는 플릭)이 시작될 때 발생. |
| `movementEnded`    | -        | -        | 콘텐츠 이동이 끝났을 때 발생.                   |
| `flickStarted`     | -        | -        | 플릭 제스처가 감지되었을 때 발생.               |
| `flickEnded`       | -        | -        | 플릭 애니메이션이 끝났을 때 발생.               |

## 주요 메소드

| 이름                  | 파라미터       | 반환타입 | 설명                                                         |
| :-------------------- | :------------- | :------- | :----------------------------------------------------------- |
| `flick(velocityX, velocityY)` | `real, real` | `void`   | 지정된 속도로 프로그래밍 방식으로 플릭을 시작.             |
| `cancelFlick()`       | -              | `void`   | 현재 진행 중인 플릭 애니메이션을 중지.                     |
| `resizeContent(width, height, contentPos)` | `real, real, point` | `void`   | 콘텐츠 크기를 변경하고, 변경 후 특정 지점이 보이도록 스크롤. |
| `returnToBounds()`    | -              | `void`   | 콘텐츠가 경계를 벗어났을 경우, 경계 안으로 되돌리는 애니메이션 시작. |

## 예제

```qml
import QtQuick
import QtQuick.Controls // For ScrollBar

Window {
    width: 300
    height: 200
    visible: true
    title: "Flickable Example"

    Flickable {
        id: flickArea
        anchors.fill: parent
        anchors.rightMargin: scrollBar.width // 스크롤바 공간 확보

        contentWidth: contentRect.width   // 콘텐츠 너비 바인딩
        contentHeight: contentRect.height // 콘텐츠 높이 바인딩
        boundsBehavior: Flickable.StopAtBounds // 경계에서 멈춤

        // 스크롤될 콘텐츠 아이템
        Rectangle {
            id: contentRect
            width: 500 // Flickable보다 넓게
            height: 400 // Flickable보다 높게
            color: "lightyellow"

            Text {
                anchors.centerIn: parent
                text: "Flick or drag this area!\nContent is larger than the view."
                horizontalAlignment: Text.AlignHCenter
            }
            Rectangle { x: 10; y:10; width: 50; height: 50; color: "red" }
            Rectangle { x: 440; y:10; width: 50; height: 50; color: "blue" }
            Rectangle { x: 10; y:340; width: 50; height: 50; color: "green" }
            Rectangle { x: 440; y:340; width: 50; height: 50; color: "purple" }
        }

        // contentItem을 직접 할당할 수도 있음
        // contentItem: Item {
        //     width: 500
        //     height: 400
        //     // ... content items ...
        // }
    }

    // 수직 스크롤바 추가 (QtQuick.Controls 필요)
    ScrollBar {
        id: scrollBar
        anchors.top: flickArea.top
        anchors.right: flickArea.right
        anchors.bottom: flickArea.bottom
        anchors.rightMargin: -width // Flickable 바깥쪽으로 붙임
        width: 15
        policy: ScrollBar.AsNeeded // 필요할 때만 보임

        // Flickable의 보이는 영역과 스크롤바 위치/크기 바인딩
        position: flickArea.visibleArea.yPosition
        size: flickArea.visibleArea.heightRatio

        // 스크롤바 조작 시 Flickable의 contentY 변경
        onPositionChanged: flickArea.contentY = position * (flickArea.contentHeight - flickArea.height)
    }
}
```

## 참고 사항

*   `Flickable`은 일반적으로 하나의 자식 아이템을 `contentItem`으로 가집니다. 여러 아이템을 스크롤하려면 해당 아이템들을 `Item`이나 `ColumnLayout`, `RowLayout` 등으로 감싸서 단일 `contentItem`으로 만들어야 합니다.
*   `contentWidth`와 `contentHeight`를 `contentItem`의 크기에 정확히 바인딩하는 것이 중요합니다. 그렇지 않으면 스크롤 범위가 잘못 계산될 수 있습니다.
*   성능을 위해 `Flickable` 내부에 너무 복잡하거나 많은 아이템을 직접 배치하는 것보다 `ListView`나 `GridView`와 같은 모델 기반 뷰를 사용하는 것이 좋습니다.
*   `ScrollBar` (QtQuick.Controls)와 함께 사용하여 사용자에게 시각적인 스크롤 피드백을 제공할 수 있습니다.

## 공식 문서 링크

*   [Qt Quick Flickable QML Type](https://doc.qt.io/qt-6/qml-qtquick-flickable.html) 