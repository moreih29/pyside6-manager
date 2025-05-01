# PageIndicator

## 모듈 정보

```qml
import QtQuick.Controls
```

## 개요

`PageIndicator`는 여러 페이지 뷰(예: `SwipeView`, `ListView` 등)에서 현재 보이는 페이지가 전체 페이지 중 어디에 해당하는지를 시각적으로 표시하는 컨트롤입니다. 일반적으로 일련의 점(dot)으로 표현되며, 현재 페이지에 해당하는 점이 다른 점들과 다르게 표시됩니다.

## 기반 클래스

*   `Control`

## 주요 프로퍼티

| 이름             | 타입        | 기본값        | 설명                                                                                                 |
| :--------------- | :---------- | :------------ | :--------------------------------------------------------------------------------------------------- |
| `count`          | `int`       | 0             | 표시할 전체 페이지(점)의 개수. 일반적으로 연동된 뷰의 페이지 수와 동일하게 설정합니다.                     |
| `currentIndex`   | `int`       | 0             | 현재 활성화된 페이지의 인덱스 (0부터 시작). 이 인덱스에 해당하는 점이 활성 상태로 표시됩니다.             |
| `delegate`       | `Component` | (스타일 의존) | 각 페이지(점)를 시각적으로 표현하는 델리게이트 컴포넌트. `index`, `pressed`, `current` 등의 컨텍스트 프로퍼티 사용 가능. |
| `interactive`    | `bool`      | `true`        | 사용자가 인디케이터의 점을 클릭하여 페이지를 전환할 수 있는지 여부.                                        |
| `background`     | `Item`      | (스타일 의존) | 인디케이터의 배경 아이템. 스타일링에 사용됩니다.                                                         |
| `contentItem`    | `Item`      | (스타일 의존) | 델리게이트들을 담는 컨테이너 아이템. 내부 레이아웃(예: `Row`) 등을 포함할 수 있습니다.                        |
| `spacing`        | `real`      | (스타일 의존) | 각 델리게이트(점) 사이의 간격.                                                                         |
| `enabled`        | `bool`      | `true`        | 컨트롤의 활성화 상태.                                                                                  |
| `focusPolicy`    | `FocusPolicy`| `Qt.TabFocus` | 컨트롤이 키보드 포커스를 받는 방식.                                                                    |
| `hoverEnabled`   | `bool`      | `false`       | 마우스 호버 효과 활성화 여부.                                                                          |

## 주요 시그널

`PageIndicator`는 상속받은 `Control`의 일반적인 시그널을 가집니다.

## 예제

```qml
import QtQuick
import QtQuick.Controls
import QtQuick.Layouts

Window {
    width: 400
    height: 300
    visible: true
    title: "PageIndicator Example"

    ColumnLayout {
        anchors.fill: parent
        spacing: 0

        // SwipeView로 페이지 구현
        SwipeView {
            id: swipeView
            Layout.fillWidth: true
            Layout.fillHeight: true // 높이 채우기
            currentIndex: pageIndicator.currentIndex // 인디케이터와 인덱스 동기화

            Repeater {
                model: 5 // 5개의 페이지 생성
                Rectangle {
                    color: Qt.rgba(Math.random(), Math.random(), Math.random(), 1)
                    Label {
                        text: "Page " + (index + 1)
                        anchors.centerIn: parent
                        font.pointSize: 20
                        color: "white"
                    }
                }
            }
        }

        // PageIndicator
        PageIndicator {
            id: pageIndicator
            Layout.alignment: Qt.AlignHCenter
            Layout.bottomMargin: 10 // 하단 여백 추가
            count: swipeView.count // SwipeView의 페이지 수와 연동
            currentIndex: swipeView.currentIndex // SwipeView의 현재 인덱스와 연동

            // 간단한 델리게이트 커스터마이징 예시
            delegate: Rectangle {
                implicitWidth: 10
                implicitHeight: 10
                radius: 5
                // 'current' 컨텍스트 프로퍼티 대신 id를 통해 currentIndex와 index 비교
                color: pageIndicator.currentIndex === index ? "steelblue" : "lightgray"
                opacity: pressed ? 0.7 : 1.0 // 눌렸을 때 투명도 조절

                Behavior on color { ColorAnimation { duration: 100 } }
            }
        }
    }
}
```

## 참고 사항

*   `count`와 `currentIndex` 프로퍼티는 일반적으로 `SwipeView`나 `ListView`와 같은 페이지 뷰 컴포넌트의 해당 프로퍼티와 바인딩하여 사용합니다.
*   `interactive` 프로퍼티를 `true`로 설정하면 사용자가 인디케이터를 클릭하여 직접 페이지를 전환할 수 있습니다. 이때 `clicked` 시그널을 사용하여 페이지 뷰의 `currentIndex`를 업데이트해야 합니다.
*   `delegate` 프로퍼티를 사용하여 각 점의 모양, 크기, 색상 등을 커스터마이징할 수 있습니다. 델리게이트 내에서 `index`(점의 인덱스), `pressed`(눌림 상태), `current`(현재 페이지 여부) 등의 컨텍스트 프로퍼티를 활용하여 상태에 따른 시각적 변화를 줄 수 있습니다.
*   스타일에 따라 기본 모양과 동작이 제공되지만, `background`, `contentItem`, `delegate` 등을 통해 완전히 새로운 디자인을 적용하는 것도 가능합니다. 

## 공식 문서 링크

*   [PageIndicator QML Type ](https://doc.qt.io/qt-6/qml-qtquick-controls-pageindicator.html) 