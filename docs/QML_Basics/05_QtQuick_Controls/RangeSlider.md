# RangeSlider

**모듈:** `import QtQuick.Controls`

## 개요

`RangeSlider` 컨트롤은 사용자가 두 개의 핸들(handle)을 사용하여 값의 **범위**를 선택할 수 있도록 합니다. `Slider`가 단일 값을 선택하는 것과 달리, `RangeSlider`는 최소값과 최대값으로 구성된 범위를 지정하는 데 사용됩니다.

가격 범위, 시간 간격 등 특정 구간을 선택해야 하는 UI에 유용합니다.

## 기반 클래스

*   `Control`

## 주요 프로퍼티

`RangeSlider`는 `Slider`와 유사한 프로퍼티를 많이 공유하지만, 두 개의 값(`first.value`, `second.value`)과 핸들(`first.handle`, `second.handle`)을 관리합니다.

| 이름             | 타입            | 기본값          | 설명                                                                                                                                       |
| :--------------- | :-------------- | :-------------- | :----------------------------------------------------------------------------------------------------------------------------------------- |
| `from`           | `real`          | 0               | 슬라이더가 나타내는 값의 전체 최소 범위.                                                                                                       |
| `to`             | `real`          | 1               | 슬라이더가 나타내는 값의 전체 최대 범위.                                                                                                       |
| `stepSize`       | `real`          | 0               | 값 변경의 최소 단위. 0이면 연속적인 값 변경이 가능합니다.                                                                                    |
| `snapMode`       | `SnapMode`      | `NoSnap`        | 값이 `stepSize`에 맞춰지는 방식을 결정합니다. (`Slider`와 동일)                                                                                |
| `orientation`    | `Qt.Orientation`| `Qt.Horizontal` | 슬라이더의 방향 (수평 또는 수직).                                                                                                             |
| `live`           | `bool`          | `true`          | `true`이면 사용자가 핸들을 드래그하는 동안 해당 값이 실시간으로 업데이트됩니다.                                                                  |
| `background`     | `Item`          | (스타일 의존)   | 슬라이더의 배경(트랙) 아이템. 스타일링에 사용됩니다.                                                                                           |
| `first`          | `Object`        | (읽기 전용)     | 첫 번째 핸들(일반적으로 왼쪽 또는 아래쪽 핸들)과 관련된 프로퍼티를 담는 객체.                                                                  |
| `  .value`       | `real`          | `from`          | 첫 번째 핸들의 현재 값. `from` 과 `second.value` 사이의 값이어야 합니다.                                                                      |
| `  .position`    | `real`          | (읽기 전용)     | `first.value`에 해당하는 논리적 위치 (0.0 ~ 1.0).                                                                                              |
| `  .visualPosition`| `real`          | (읽기 전용)     | `first.position`과 유사하지만 애니메이션 효과가 적용될 수 있는 실제 시각적 위치.                                                               |
| `  .pressed`     | `bool`          | (읽기 전용)     | 첫 번째 핸들이 현재 눌려있는지 여부.                                                                                                           |
| `  .handle`      | `Item`          | (스타일 의존)   | 첫 번째 핸들 아이템. 스타일링에 사용됩니다.                                                                                                  |
| `  .hovered`     | `bool`          | (읽기 전용)     | 마우스 커서가 첫 번째 핸들 위에 있는지 여부 (`hoverEnabled`가 `true`일 때).                                                                  |
| `second`         | `Object`        | (읽기 전용)     | 두 번째 핸들(일반적으로 오른쪽 또는 위쪽 핸들)과 관련된 프로퍼티를 담는 객체.                                                                  |
| `  .value`       | `real`          | `to`            | 두 번째 핸들의 현재 값. `first.value` 와 `to` 사이의 값이어야 합니다.                                                                         |
| `  .position`    | `real`          | (읽기 전용)     | `second.value`에 해당하는 논리적 위치 (0.0 ~ 1.0).                                                                                             |
| `  .visualPosition`| `real`          | (읽기 전용)     | `second.position`과 유사하지만 애니메이션 효과가 적용될 수 있는 실제 시각적 위치.                                                              |
| `  .pressed`     | `bool`          | (읽기 전용)     | 두 번째 핸들이 현재 눌려있는지 여부.                                                                                                           |
| `  .handle`      | `Item`          | (스타일 의존)   | 두 번째 핸들 아이템. 스타일링에 사용됩니다.                                                                                                  |
| `  .hovered`     | `bool`          | (읽기 전용)     | 마우스 커서가 두 번째 핸들 위에 있는지 여부 (`hoverEnabled`가 `true`일 때).                                                                  |
| `enabled`        | `bool`          | `true`          | 컨트롤의 활성화 상태.                                                                                                                      |
| `focusPolicy`    | `FocusPolicy`   | `Qt.StrongFocus`| 컨트롤이 키보드 포커스를 받는 방식.                                                                                                          |
| `hoverEnabled`   | `bool`          | `true`          | 마우스 호버 효과 활성화 여부.                                                                                                              |
| Tooltip          |                 |                 | 컨트롤 위에 마우스를 올렸을 때 표시되는 툴팁 관련 프로퍼티.                                                                                    |

## 주요 시그널

`RangeSlider`는 각 핸들의 값 변경 및 상태 변경에 대한 시그널을 제공합니다.

| 이름                       | 파라미터 | 설명                                                                   |
| :------------------------- | :------- | :--------------------------------------------------------------------- |
| `first.valueChanged`       |          | `first.value` 프로퍼티가 변경될 때 발생합니다.                             |
| `first.moved`              |          | 사용자가 첫 번째 핸들을 드래그하여 `first.visualPosition`이 변경될 때 발생합니다 (live=true 일 때). |
| `first.pressedChanged`     |          | `first.pressed` 프로퍼티가 변경될 때 발생합니다.                           |
| `second.valueChanged`      |          | `second.value` 프로퍼티가 변경될 때 발생합니다.                            |
| `second.moved`             |          | 사용자가 두 번째 핸들을 드래그하여 `second.visualPosition`이 변경될 때 발생합니다 (live=true 일 때). |
| `second.pressedChanged`    |          | `second.pressed` 프로퍼티가 변경될 때 발생합니다.                          |

## 주요 메서드

`RangeSlider`는 각 핸들을 개별적으로 증가/감소시키는 메서드를 제공합니다.

| 이름                 | 설명                                         |
| :------------------- | :------------------------------------------- |
| `first.increase()`   | `first.value`를 `stepSize`만큼 증가시킵니다.   |
| `first.decrease()`   | `first.value`를 `stepSize`만큼 감소시킵니다.   |
| `second.increase()`  | `second.value`를 `stepSize`만큼 증가시킵니다.  |
| `second.decrease()`  | `second.value`를 `stepSize`만큼 감소시킵니다.  |

## 예제

```qml
import QtQuick
import QtQuick.Controls
import QtQuick.Layouts

Window {
    width: 400
    height: 200
    visible: true
    title: "RangeSlider Example"

    ColumnLayout {
        anchors.fill: parent
        anchors.margins: 10
        spacing: 10

        Label {
            id: rangeLabel
            Layout.alignment: Qt.AlignHCenter
            text: "Selected Range: " + Math.round(priceRangeSlider.first.value)
                  + " - " + Math.round(priceRangeSlider.second.value)
            font.pointSize: 12
        }

        // 가격 범위 선택 슬라이더
        RangeSlider {
            id: priceRangeSlider
            Layout.fillWidth: true
            from: 0
            to: 1000
            first.value: 200 // 초기 최소값
            second.value: 800 // 초기 최대값
            stepSize: 10 // 10 단위로 조절
            snapMode: RangeSlider.SnapAlways

            // 값이 변경될 때마다 라벨 업데이트
            onFirstValueChanged: updateRangeLabel()
            onSecondValueChanged: updateRangeLabel()

            // 간단한 핸들 및 트랙 스타일링 (기본 스타일 위에 추가)
            background: Rectangle {
                x: priceRangeSlider.leftPadding
                y: priceRangeSlider.topPadding + priceRangeSlider.availableHeight / 2 - height / 2
                implicitWidth: 200
                implicitHeight: 4
                width: priceRangeSlider.availableWidth
                height: implicitHeight
                radius: 2
                color: "lightgray"

                // 선택된 범위 표시
                Rectangle {
                    x: priceRangeSlider.first.visualPosition * width
                    width: (priceRangeSlider.second.visualPosition - priceRangeSlider.first.visualPosition) * parent.width
                    height: parent.height
                    color: "steelblue"
                    radius: 2
                }
            }

            first.handle: Rectangle {
                x: priceRangeSlider.leftPadding + priceRangeSlider.first.visualPosition * priceRangeSlider.availableWidth - width / 2
                y: priceRangeSlider.topPadding + priceRangeSlider.availableHeight / 2 - height / 2
                implicitWidth: 16
                implicitHeight: 16
                radius: 8
                color: priceRangeSlider.first.pressed ? "gray" : "lightblue"
                border.color: "steelblue"
            }

            second.handle: Rectangle {
                x: priceRangeSlider.leftPadding + priceRangeSlider.second.visualPosition * priceRangeSlider.availableWidth - width / 2
                y: priceRangeSlider.topPadding + priceRangeSlider.availableHeight / 2 - height / 2
                implicitWidth: 16
                implicitHeight: 16
                radius: 8
                color: priceRangeSlider.second.pressed ? "gray" : "lightblue"
                border.color: "steelblue"
            }
        }

        // 수직 RangeSlider 예시
        RangeSlider {
            Layout.preferredHeight: 100
            orientation: Qt.Vertical
            from: 0
            to: 100
            first.value: 25
            second.value: 75
        }
    }

    function updateRangeLabel() {
        rangeLabel.text = "Selected Range: " + Math.round(priceRangeSlider.first.value)
                         + " - " + Math.round(priceRangeSlider.second.value)
    }
}
```

## 참고 사항

*   `RangeSlider`는 두 개의 값(`first.value`, `second.value`)과 두 개의 핸들(`first.handle`, `second.handle`)을 가집니다.
*   `first.value`는 항상 `second.value`보다 작거나 같아야 합니다. 핸들을 드래그할 때 이 제약 조건이 자동으로 유지됩니다.
*   `from`, `to`, `stepSize`, `snapMode`, `orientation` 등은 `Slider`와 동일하게 작동합니다.
*   각 핸들의 값 변경(`valueChanged`) 및 상태 변경(`pressedChanged`, `moved`) 시그널을 개별적으로 처리할 수 있습니다.
*   `first.handle`, `second.handle`, `background` 아이템을 커스터마이징하여 `RangeSlider`의 외형을 변경할 수 있습니다. 