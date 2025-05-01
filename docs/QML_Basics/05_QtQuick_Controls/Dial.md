# Dial

**모듈:** `import QtQuick.Controls`

## 개요

`Dial` 컨트롤은 사용자가 원형 다이얼을 돌려 특정 범위 내의 값을 선택하거나 조절할 수 있게 해줍니다. `Slider`와 유사하게 값 범위를 가지지만, 시각적인 표현 방식이 다릅니다. 주로 속도계, 볼륨 조절 등 원형 인터페이스가 직관적인 경우에 사용됩니다.

## 기반 클래스

*   `Control`

## 주요 프로퍼티

| 이름             | 타입         | 기본값          | 설명                                                                                                                          |
| :--------------- | :----------- | :-------------- | :---------------------------------------------------------------------------------------------------------------------------- |
| `value`          | `real`       | 0               | 다이얼의 현재 값. `from`과 `to` 사이의 값입니다.                                                                                |
| `from`           | `real`       | 0               | 다이얼이 나타내는 값의 최소 범위.                                                                                             |
| `to`             | `real`       | 1               | 다이얼이 나타내는 값의 최대 범위.                                                                                             |
| `stepSize`       | `real`       | 0               | 값 변경의 최소 단위. 0이면 연속적인 값 변경이 가능합니다.                                                                       |
| `position`       | `real`       | (읽기 전용)     | 현재 `value`에 해당하는 논리적 위치 (0.0 ~ 1.0).                                                                                |
| `visualPosition` | `real`       | (읽기 전용)     | `position`과 유사하지만, 애니메이션 효과가 적용될 수 있는 실제 시각적 위치.                                                       |
| `pressed`        | `bool`       | (읽기 전용)     | 현재 사용자가 다이얼 핸들을 누르고 있는지 여부.                                                                                 |
| `handle`         | `Item`       | (스타일 의존)   | 다이얼의 핸들(손잡이) 아이템. 스타일링에 사용됩니다.                                                                            |
| `background`     | `Item`       | (스타일 의존)   | 다이얼의 배경 아이템. 스타일링에 사용됩니다.                                                                                  |
| `snapMode`       | `SnapMode`   | `NoSnap`        | 값이 `stepSize`에 맞춰지거나(`SnapAlways`, `SnapOnRelease`), 맞춰지지 않는(`NoSnap`) 방식을 결정합니다. (`Slider`와 유사)            |
| `wrap`           | `bool`       | `false`         | `true`로 설정하면 `to` 값에서 `from` 값으로 (또는 그 반대로) 값이 순환합니다.                                                     |
| `live`           | `bool`       | `true`          | `true`이면 사용자가 핸들을 드래그하는 동안 `value`가 실시간으로 업데이트됩니다. `false`이면 드래그를 놓았을 때만 업데이트됩니다.      |
| `focusPolicy`    | `FocusPolicy`| `Qt.StrongFocus`| 컨트롤이 키보드 포커스를 받는 방식.                                                                                             |
| `hoverEnabled`   | `bool`       | `true`          | 마우스 호버 효과 활성화 여부.                                                                                                 |
| `hovered`        | `bool`       | (읽기 전용)     | 현재 마우스 커서가 컨트롤 위에 있는지 여부.                                                                                     |
| `tooltip`        |              |                 | 컨트롤 위에 마우스를 올렸을 때 표시되는 툴팁 관련 프로퍼티.                                                                       |

## 주요 시그널

| 이름             | 파라미터 | 설명                                                               |
| :--------------- | :------- | :----------------------------------------------------------------- |
| `valueChanged`   |          | `value` 프로퍼티가 변경될 때 발생합니다.                               |
| `moved`          |          | 사용자가 핸들을 드래그하여 `visualPosition`이 변경될 때 발생합니다 (live=true 일 때). |
| `pressedChanged` |          | `pressed` 프로퍼티가 변경될 때 발생합니다.                             |

## 주요 메서드

| 이름       | 설명                              |
| :--------- | :-------------------------------- |
| `increase()` | `value`를 `stepSize`만큼 증가시킵니다. |
| `decrease()` | `value`를 `stepSize`만큼 감소시킵니다. |

## 예제

```qml
import QtQuick
import QtQuick.Controls
import QtQuick.Layouts

Window {
    width: 300
    height: 350
    visible: true
    title: "Dial Example"

    ColumnLayout {
        anchors.fill: parent
        anchors.margins: 10
        spacing: 10

        Label {
            id: valueLabel
            Layout.alignment: Qt.AlignHCenter
            text: "Value: " + Math.round(volumeDial.value)
            font.pointSize: 14
        }

        Dial {
            id: volumeDial
            Layout.alignment: Qt.AlignHCenter
            from: 0
            to: 100
            stepSize: 10 // 10 단위로 스냅
            snapMode: Dial.SnapAlways
            value: 50

            // 값 변경 시 라벨 업데이트
            onValueChanged: {
                valueLabel.text = "Value: " + Math.round(value)
            }

            // 간단한 핸들 스타일링 예시 (기본 스타일 위에 추가)
            handle: Rectangle {
                x: volumeDial.width / 2 - width / 2
                y: volumeDial.height * 0.1 // 핸들 위치 조정 (상대적)
                width: 10
                height: 10
                radius: 5
                color: "red"
                border.color: "darkred"
                antialiasing: true
                // 핸들을 다이얼 값에 따라 회전 (visualPosition 사용)
                transform: Rotation {
                    origin.x: width / 2
                    origin.y: volumeDial.height / 2 - y
                    angle: -135 + volumeDial.visualPosition * 270
                }
            }
        }

        Dial {
            Layout.alignment: Qt.AlignHCenter
            from: 0
            to: 360
            wrap: true // 값 순환 활성화
            stepSize: 1
            value: 180
        }
    }
}
```

## 참고 사항

*   `from`, `to`, `stepSize` 프로퍼티를 사용하여 다이얼의 값 범위와 단위를 설정합니다.
*   `value` 프로퍼티를 통해 현재 값을 얻거나 설정할 수 있습니다.
*   `snapMode`를 사용하여 값이 `stepSize`에 맞춰지도록 할 수 있습니다.
*   `wrap` 프로퍼티를 `true`로 설정하면 값이 최대값에서 최소값으로, 또는 그 반대로 순환됩니다.
*   `handle`과 `background` 아이템을 커스터마이징하여 다이얼의 외형을 변경할 수 있습니다. 스타일 시스템에 따라 기본 모양이 제공됩니다.
*   `tickmarks` 관련 프로퍼티를 사용하여 다이얼 주위에 눈금을 표시할 수 있습니다. (스타일 지원 필요)

## 공식 문서 링크

*   [Dial QML Type ](https://doc.qt.io/qt-6/qml-qtquick-controls-dial.html) 