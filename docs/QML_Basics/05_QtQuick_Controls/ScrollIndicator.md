# ScrollIndicator

## 모듈 정보

```qml
import QtQuick.Controls
```

## 개요

`ScrollIndicator`는 `Flickable`이나 `ScrollView`와 같은 스크롤 가능한 뷰의 스크롤 위치를 시각적으로 표시하는 인디케이터입니다. `ScrollBar`와 유사한 목적을 가지지만, 일반적으로 더 얇고, 사용자와의 직접적인 상호작용(핸들 드래그 등)보다는 스크롤 상태를 보여주는 데 중점을 둡니다. 터치 기반 인터페이스나 미니멀한 디자인에 더 적합할 수 있습니다.

스크롤이 발생할 때 잠시 나타났다가 사라지는 동작이 기본 스타일인 경우가 많습니다.

## 기반 클래스

*   `Control`

## 주요 프로퍼티

| 이름             | 타입            | 기본값        | 설명                                                                                                                         |
| :--------------- | :-------------- | :------------ | :--------------------------------------------------------------------------------------------------------------------------- |
| `orientation`    | `Qt.Orientation`| `Qt.Vertical` | 인디케이터의 방향 (수직 또는 수평). 연결된 뷰의 스크롤 방향과 일치시킵니다.                                                        |
| `position`       | `real`          | 0             | 현재 스크롤 위치 (0.0 ~ 1.0). `Flickable`의 `visibleArea.x/yPosition`과 바인딩합니다.                                            |
| `size`           | `real`          | 0             | 인디케이터 핸들의 크기 (0.0 ~ 1.0). 뷰에서 보이는 영역의 비율을 나타냅니다. (`Flickable`의 `visibleArea.width/heightRatio`)      |
| `active`         | `bool`          | `false`       | 인디케이터가 현재 활성화되어 표시되어야 하는지 여부. 일반적으로 `Flickable`의 `moving` 또는 `dragging` 상태와 연결하여 제어합니다. |
| `minimumSize`    | `real`          | (스타일 의존) | 핸들의 최소 크기 (픽셀 단위). `size` 프로퍼티로 계산된 크기가 이 값보다 작으면 이 크기로 표시됩니다. (Qt 5.11+)                     |
| `visualPosition` | `real`          | (읽기 전용)   | `position`과 유사하지만 RTL 및 애니메이션 효과가 적용된 실제 시각적 위치.                                                        |
| `visualSize`     | `real`          | (읽기 전용)   | `size`와 유사하지만 `minimumSize` 및 애니메이션 효과가 적용된 실제 시각적 크기. (Qt 5.11+)                                  |
| `background`     | `Item`          | (스타일 의존) | 인디케이터의 배경 아이템. 일반적으로 투명하거나 거의 보이지 않습니다.                                                          |
| `contentItem`    | `Item`          | (스타일 의존) | 인디케이터의 핸들(막대) 아이템. 스타일링에 사용됩니다.                                                                         |
| `enabled`        | `bool`          | `true`        | 컨트롤의 활성화 상태.                                                                                                      |
| `focusPolicy`    | `FocusPolicy`   | `Qt.NoFocus`  | 기본적으로 포커스를 받지 않습니다.                                                                                             |
| `hoverEnabled`   | `bool`          | `false`       | 마우스 호버 효과 활성화 여부.                                                                                              |

## 주요 시그널

`ScrollIndicator`는 주로 상태 변경을 알리는 시그널은 없지만, 상속받은 `Control`의 일반적인 시그널을 가집니다.

## 예제

```qml
import QtQuick
import QtQuick.Controls
import QtQuick.Layouts

Window {
    width: 300
    height: 250
    visible: true
    title: "ScrollIndicator Example"

    Flickable {
        id: flickable
        anchors.fill: parent
        contentWidth: contentRect.width
        contentHeight: contentRect.height
        clip: true
        // 스크롤 중일 때만 인디케이터가 보이도록 설정
        ScrollIndicator.vertical: ScrollIndicator { }
        ScrollIndicator.horizontal: ScrollIndicator { }

        Rectangle {
            id: contentRect
            width: 600
            height: 500
            color: "lightcoral"
            Label {
                text: "Flick Me!"
                anchors.centerIn: parent
                font.pointSize: 24
            }
        }
    }

    /*
    // ScrollIndicator를 수동으로 배치하고 연결하는 경우 (참고용)
    Flickable {
        id: manualFlickable
        // ... Flickable 설정 ...
    }

    ScrollIndicator {
        anchors.top: manualFlickable.top
        anchors.right: manualFlickable.right
        anchors.bottom: manualFlickable.bottom
        anchors.margins: 2
        orientation: Qt.Vertical
        size: manualFlickable.visibleArea.heightRatio
        position: manualFlickable.visibleArea.yPosition
        active: manualFlickable.movingVertically // 스크롤 중일 때 활성화
    }

    ScrollIndicator {
        anchors.left: manualFlickable.left
        anchors.right: manualFlickable.right
        anchors.bottom: manualFlickable.bottom
        anchors.margins: 2
        orientation: Qt.Horizontal
        size: manualFlickable.visibleArea.widthRatio
        position: manualFlickable.visibleArea.xPosition
        active: manualFlickable.movingHorizontally
    }
    */
}
```

## 참고 사항

*   `ScrollIndicator`는 `Flickable` 또는 `ScrollView`와 함께 사용됩니다.
*   가장 간단한 사용법은 `Flickable`의 `ScrollIndicator.vertical` 및 `ScrollIndicator.horizontal` 부착 프로퍼티(attached property)를 사용하는 것입니다. 이렇게 하면 `Flickable`이 스크롤될 때 자동으로 인디케이터가 나타나고 사라집니다.
*   수동으로 `ScrollIndicator`를 배치하고 연결할 경우, `orientation`, `position`, `size` 프로퍼티를 `Flickable`의 해당 상태와 정확히 바인딩해야 합니다.
*   `active` 프로퍼티를 사용하여 인디케이터의 표시 여부를 제어할 수 있습니다. 일반적으로 `Flickable`의 `moving` 또는 `dragging` 상태와 연결하여 스크롤 중에만 표시되도록 합니다.
*   `ScrollIndicator`는 기본적으로 사용자와의 상호작용(클릭, 드래그)을 지원하지 않지만, 스타일링을 통해 시각적인 피드백만 제공합니다.
*   `background`와 `contentItem`을 커스터마이징하여 인디케이터의 모양과 동작(예: fade-in/out 애니메이션)을 변경할 수 있습니다. 

## 공식 문서 링크

*   [ScrollIndicator QML Type ](https://doc.qt.io/qt-6/qml-qtquick-controls-scrollindicator.html) 