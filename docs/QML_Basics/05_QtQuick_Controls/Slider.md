# Slider

**모듈:** `import QtQuick.Controls`

## 개요

`Slider`는 사용자가 특정 범위 내의 값을 선택하거나 조절할 수 있도록 하는 컨트롤입니다. 일반적으로 핸들(handle)을 트랙(track) 위에서 드래그하여 값을 변경하며, 수평 또는 수직 방향으로 배치될 수 있습니다.

## 기반 클래스

*   `Range` (간접적으로 `Control` 상속)

## 주요 프로퍼티

`Range` 모델에서 상속받은 값 관련 프로퍼티와 `Slider` 자체 프로퍼티를 포함합니다.

| 이름             | 타입             | 기본값          | 설명                                                                                                                               |
| :--------------- | :--------------- | :-------------- | :--------------------------------------------------------------------------------------------------------------------------------- |
| `value`          | `real`           | 0.0             | 슬라이더의 현재 값. `from`과 `to` 사이의 값입니다.                                                                                   |
| `from`           | `real`           | 0.0             | 슬라이더가 나타내는 값의 최소 범위.                                                                                                  |
| `to`             | `real`           | 1.0             | 슬라이더가 나타내는 값의 최대 범위.                                                                                                  |
| `stepSize`       | `real`           | 0.0             | 슬라이더 값을 변경할 때의 최소 단위 (스텝). 0이면 연속적인 값 변경 가능. 키보드 조작이나 `increase()`/`decrease()` 호출 시 사용됩니다.           |
| `orientation`    | `Qt::Orientation`| `Qt.Horizontal` | 슬라이더의 방향 (`Qt.Horizontal` 또는 `Qt.Vertical`).                                                                              |
| `position`       | `real`           | (`value` 기반) | (읽기 전용) 슬라이더 핸들의 상대적 위치 (0.0 ~ 1.0). `value`, `from`, `to` 값에 따라 계산됩니다. 시각적 표현 업데이트에 주로 사용됨.          |
| `pressed`        | `bool`           | `false`         | (읽기 전용) 사용자가 슬라이더 핸들을 현재 누르고(드래그 중) 있는지 여부.                                                              |
| `handle`         | `Item`           | (스타일 의존)  | 슬라이더 핸들(사용자가 드래그하는 부분) 아이템. 스타일 커스터마이징에 사용.                                                            |
| `track`          | `Item`           | (스타일 의존)  | 슬라이더 핸들이 움직이는 트랙 아이템. 스타일 커스터마이징에 사용.                                                                      |
| `snapMode`       | `enum`           | `Slider.NoSnap` | 핸들을 놓았을 때 값이 특정 위치(스텝)에 맞춰지도록 하는 모드 (`NoSnap`, `SnapAlways`, `SnapOnRelease`). `stepSize`가 0보다 커야 의미 있음. |
| `tickmarks.enabled`| `bool`          | `false`         | 트랙 위에 눈금(tickmark)을 표시할지 여부.                                                                                           |
| `tickmarks.stepSize`| `real`         | `stepSize`      | 눈금 간격. 기본값은 `stepSize`를 따름.                                                                                              |
| `tickmarks.position`| `enum`         | (스타일 의존)   | 눈금 표시 위치 (`TicksAbove`, `TicksBelow`, `TicksLeft`, `TicksRight`).                                                            |
| `live`           | `bool`           | `true`          | 사용자가 핸들을 드래그하는 동안 `value` 프로퍼티를 실시간으로 업데이트할지 여부. `false`이면 드래그를 놓았을 때만 업데이트.                   |
| `enabled`        | `bool`           | `true`          | 슬라이더가 활성화되어 사용자와 상호작용할 수 있는지 여부.                                                                              |
| `hoverEnabled`   | `bool`           | `true`          | 마우스 호버 효과를 사용할지 여부.                                                                                                  |
| `hovered`        | `bool`           | `false`         | (읽기 전용) 마우스 커서가 슬라이더(주로 핸들) 위에 있는지 여부.                                                                     |
| `background`     | `Item`           | (스타일 의존)  | 슬라이더 전체의 배경 아이템. 스타일 커스터마이징에 사용.                                                                             |
| `focusPolicy`    | `Qt::FocusPolicy`| `Qt.StrongFocus`| 슬라이더가 키보드 포커스를 받는 방식.                                                                                                |
| `wheelEnabled`   | `bool`           | `false`         | 마우스 휠 스크롤로 슬라이더 값을 변경할 수 있는지 여부.                                                                              |
| `ToolTip.visible`, `ToolTip.text`, `ToolTip.delay` | `bool`, `string`, `int` | - | 슬라이더(주로 핸들)에 마우스를 올렸을 때 표시될 툴팁 설정.                                                                           |

## 주요 시그널

| 이름           | 파라미터 | 반환타입 | 설명                                                                          |
| :------------- | :------- | :------- | :---------------------------------------------------------------------------- |
| `valueChanged` | -        | -        | `value` 프로퍼티 값이 변경되었을 때 발생.                                       |
| `moved`        | -        | -        | 사용자가 핸들을 드래그하여 `position`이 변경되었을 때 발생 (`live`가 `true`일 때). |
| `pressedChanged`| -       | -        | `pressed` 프로퍼티 값이 변경되었을 때 발생.                                    |
| `pressAndHold` | -        | -        | 핸들을 일정 시간 동안 누르고 있을 때 발생 (플랫폼/스타일 의존적일 수 있음).       |

## 주요 메소드

| 이름        | 파라미터 | 반환타입 | 설명                                 |
| :---------- | :------- | :------- | :----------------------------------- |
| `increase()`| -        | `void`   | `value`를 `stepSize`만큼 증가시킴.  |
| `decrease()`| -        | `void`   | `value`를 `stepSize`만큼 감소시킴.  |

## 예제

```qml
import QtQuick
import QtQuick.Controls
import QtQuick.Layouts

Window {
    width: 400
    height: 200
    visible: true
    title: "Slider Example"

    RowLayout {
        anchors.centerIn: parent
        spacing: 20

        // 수평 슬라이더
        ColumnLayout {
            spacing: 10
            Label { id: hLabel; text: "Horizontal Slider: " + Math.round(hSlider.value * 100) / 100 }

            Slider {
                id: hSlider
                Layout.minimumWidth: 150
                from: 0.0
                to: 1.0
                stepSize: 0.1 // 0.1 단위로 스텝
                value: 0.5 // 초기값
                snapMode: Slider.SnapAlways // 항상 스텝에 맞춤
                tickmarks.enabled: true // 눈금 표시

                onValueChanged: {
                    hLabel.text = "Horizontal Slider: " + Math.round(value * 100) / 100
                }
            }
        }

        // 수직 슬라이더
        ColumnLayout {
             spacing: 10
             Label { id: vLabel; text: "Vertical" }
             Slider {
                 id: vSlider
                 Layout.minimumHeight: 100
                 orientation: Qt.Vertical // 수직 방향
                 from: 10
                 to: 50
                 value: 25
                 live: false // 놓았을 때만 값 업데이트

                 onValueChanged: {
                     vLabel.text = "Value: " + Math.round(value)
                 }
                 // moved 시그널은 live가 true일 때 더 유용
                 // onMoved: console.log("Vertical Slider moved, position:", position)
             }
        }
    }
}
```

## 참고 사항

*   `from`, `to`, `value`, `stepSize` 프로퍼티를 사용하여 슬라이더의 값 범위와 단위를 설정합니다.
*   `orientation` 프로퍼티로 수평 또는 수직 슬라이더를 만듭니다.
*   `position` 프로퍼티는 `value`를 0.0 ~ 1.0 범위로 정규화한 값으로, 슬라이더 핸들의 시각적 위치를 계산하는 데 유용합니다.
*   `snapMode`와 `stepSize`를 함께 사용하여 슬라이더 값이 특정 단위(스텝)에 맞춰지도록 할 수 있습니다.
*   `live` 프로퍼티는 사용자가 핸들을 드래그하는 동안 `value` 업데이트 빈도를 제어합니다.
*   `handle`, `track`, `background` 프로퍼티와 `tickmarks` 관련 속성을 통해 슬라이더의 모양을 커스터마이징할 수 있습니다. 