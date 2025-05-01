# ScrollBar

## 모듈 정보

```qml
import QtQuick.Controls
```

## 개요

`ScrollBar`는 `Flickable`이나 `ScrollView`와 같은 스크롤 가능한 뷰의 현재 스크롤 위치를 시각적으로 나타내고, 사용자가 직접 스크롤 위치를 제어할 수 있게 해주는 컨트롤입니다.

일반적으로 스크롤 가능한 뷰의 가장자리에 수평 또는 수직으로 배치됩니다.

## 기반 클래스

*   `Control`

## 주요 프로퍼티

| 이름             | 타입            | 기본값          | 설명                                                                                                                                 |
| :--------------- | :-------------- | :-------------- | :----------------------------------------------------------------------------------------------------------------------------------- |
| `orientation`    | `Qt.Orientation`| `Qt.Vertical`   | 스크롤바의 방향 (수직 또는 수평). 일반적으로 연결된 뷰의 스크롤 방향과 일치시킵니다.                                                    |
| `position`       | `real`          | 0               | 현재 스크롤 위치. 0.0 (시작) 부터 1.0 (끝) 사이의 값을 가집니다. 일반적으로 `Flickable`의 `contentX/Y`와 `visibleArea.width/heightRatio`를 이용해 계산/바인딩합니다. |
| `size`           | `real`          | 0               | 스크롤바 핸들(thumb)의 크기. 0.0 부터 1.0 사이의 값을 가지며, 뷰에서 보이는 영역의 비율을 나타냅니다. (`visibleArea.width/heightRatio`)           |
| `active`         | `bool`          | (읽기 전용)     | 스크롤바가 현재 활성 상태인지 (예: 스크롤 가능 영역이 뷰 크기보다 클 때) 여부.                                                              |
| `pressed`        | `bool`          | (읽기 전용)     | 사용자가 스크롤바 핸들을 누르고 있는지 여부.                                                                                             |
| `policy`         | `ScrollBarPolicy`| `AsNeeded`      | 스크롤바의 표시 정책 (`AlwaysOn`, `AlwaysOff`, `AsNeeded`). `AsNeeded`는 스크롤이 필요할 때만 표시합니다.                                        |
| `background`     | `Item`          | (스타일 의존)   | 스크롤바의 배경(트랙) 아이템. 스타일링에 사용됩니다.                                                                                   |
| `contentItem`    | `Item`          | (스타일 의존)   | 스크롤바의 핸들(thumb) 아이템. 스타일링에 사용됩니다.                                                                                    |
| `snapMode`       | `SnapMode`      | `NoSnap`        | 스크롤바 핸들을 놓았을 때 특정 위치에 맞춰지는 방식을 결정합니다 (`NoSnap`, `SnapAlways`, `SnapOnRelease`).                                     |
| `stepSize`       | `real`          | (스타일 의존)   | 스크롤바의 빈 공간을 클릭했을 때 이동하는 단계 크기 (0.0 ~ 1.0).                                                                         |
| `interactive`    | `bool`          | `true`          | 사용자가 스크롤바와 상호작용(클릭, 드래그)할 수 있는지 여부.                                                                                |
| `enabled`        | `bool`          | `true`          | 컨트롤의 활성화 상태.                                                                                                                |
| `focusPolicy`    | `FocusPolicy`   | `Qt.StrongFocus`| 컨트롤이 키보드 포커스를 받는 방식.                                                                                                    |
| `hoverEnabled`   | `bool`          | `true`          | 마우스 호버 효과 활성화 여부.                                                                                                        |

## 주요 시그널

| 이름             | 파라미터 | 설명                                                  |
| :--------------- | :------- | :---------------------------------------------------- |
| `positionChanged`|          | `position` 프로퍼티가 변경될 때 발생합니다.               |
| `pressedChanged` |          | `pressed` 프로퍼티가 변경될 때 발생합니다.                |

## 예제

```qml
import QtQuick
import QtQuick.Controls
import QtQuick.Layouts

Window {
    width: 300
    height: 250
    visible: true
    title: "ScrollBar Example"

    // Flickable과 ScrollBar를 함께 사용
    Flickable {
        id: flickable
        anchors.fill: parent
        anchors.rightMargin: verticalScrollBar.width // 스크롤바 공간 확보
        anchors.bottomMargin: horizontalScrollBar.height
        contentWidth: contentRect.width
        contentHeight: contentRect.height
        clip: true // 내용을 경계 밖으로 그리지 않음

        // 스크롤될 내용
        Rectangle {
            id: contentRect
            width: 600
            height: 500
            gradient: Gradient {
                GradientStop { position: 0.0; color: "lightblue" }
                GradientStop { position: 1.0; color: "steelblue" }
            }
            Label {
                text: "Scrollable Content Area"
                anchors.centerIn: parent
                font.pointSize: 18
            }
        }
    }

    // 수직 스크롤바
    ScrollBar {
        id: verticalScrollBar
        anchors.top: flickable.top
        anchors.right: flickable.right
        anchors.bottom: flickable.bottom
        anchors.rightMargin: -width // Flickable 옆에 붙임
        hoverEnabled: true
        active: flickable.movingVertically || flickable.contentHeight > flickable.height // 스크롤 중이거나 필요할 때 활성화
        orientation: Qt.Vertical
        size: flickable.visibleArea.heightRatio
        position: flickable.visibleArea.yPosition

        // 스크롤바 조작 시 Flickable 위치 업데이트
        onPositionChanged: {
            if (pressed) { // 사용자가 직접 조작할 때만
                flickable.contentY = position * (flickable.contentHeight - flickable.height)
            }
        }
    }

    // 수평 스크롤바
    ScrollBar {
        id: horizontalScrollBar
        anchors.left: flickable.left
        anchors.right: flickable.right
        anchors.bottom: flickable.bottom
        anchors.bottomMargin: -height // Flickable 아래에 붙임
        hoverEnabled: true
        active: flickable.movingHorizontally || flickable.contentWidth > flickable.width
        orientation: Qt.Horizontal
        size: flickable.visibleArea.widthRatio
        position: flickable.visibleArea.xPosition

        onPositionChanged: {
            if (pressed) {
                flickable.contentX = position * (flickable.contentWidth - flickable.width)
            }
        }
    }
}
```

## 참고 사항

*   `ScrollBar`는 일반적으로 `Flickable` 또는 `ScrollView`와 함께 사용됩니다.
*   `orientation` 프로퍼티를 설정하여 스크롤바의 방향(수직 또는 수평)을 지정해야 합니다.
*   `position`과 `size` 프로퍼티는 연결된 `Flickable`의 `visibleArea` 관련 프로퍼티 (`xPosition`, `yPosition`, `widthRatio`, `heightRatio`)와 바인딩하여 스크롤 상태를 반영하고 제어합니다.
*   `onPositionChanged` 시그널 핸들러 내에서 `pressed` 상태를 확인하여 사용자의 직접적인 조작과 프로그램적인 위치 변경을 구분하는 것이 좋습니다. 사용자가 스크롤바를 직접 조작할 때만 연결된 뷰의 스크롤 위치 (`contentX`, `contentY`)를 업데이트해야 무한 루프를 방지할 수 있습니다.
*   `policy` 프로퍼티를 사용하여 스크롤바가 항상 보이거나(`AlwaysOn`), 필요할 때만 보이도록(`AsNeeded`) 설정할 수 있습니다.
*   `background`와 `contentItem` (핸들)을 커스터마이징하여 스크롤바의 외형을 변경할 수 있습니다.
*   `ScrollView` 컴포넌트는 내부적으로 `Flickable`과 `ScrollBar`를 포함하고 있어 더 간편하게 스크롤 뷰를 구현할 수 있습니다. 

## 공식 문서 링크

*   [ScrollBar QML Type ](https://doc.qt.io/qt-6/qml-qtquick-controls-scrollbar.html) 