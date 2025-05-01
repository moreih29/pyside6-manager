# ProgressBar

**모듈:** `import QtQuick.Controls`

## 개요

`ProgressBar`는 작업의 진행 상태를 시각적으로 나타내는 컨트롤입니다. 일반적으로 0%에서 100% 사이의 값을 사용하여 작업 완료율을 표시하며, 특정 범위 내의 값을 보여줄 수도 있습니다. 또한, 진행 상태를 알 수 없는 경우 '무한' 또는 '미정' 상태를 표시할 수도 있습니다.

## 기반 클래스

*   `Control`

## 주요 프로퍼티

| 이름             | 타입        | 기본값          | 설명                                                                                                                                   |
| :--------------- | :---------- | :-------------- | :------------------------------------------------------------------------------------------------------------------------------------- |
| `from`           | `real`      | 0               | 진행률의 최소값.                                                                                                                         |
| `to`             | `real`      | 1               | 진행률의 최대값.                                                                                                                       |
| `value`          | `real`      | 0               | 현재 진행률 값. `from`과 `to` 사이의 값이어야 합니다.                                                                                    |
| `indeterminate`  | `bool`      | `false`         | `true`로 설정하면 명확한 진행률 대신 '미정' 상태를 표시합니다 (예: 로딩 애니메이션). `value`는 무시됩니다.                               |
| `position`       | `real`      | (읽기 전용)     | 현재 `value`에 해당하는 논리적 위치 (0.0 ~ 1.0).                                                                                       |
| `visualPosition` | `real`      | (읽기 전용)     | `position`과 유사하지만 RTL 레이아웃을 고려한 시각적 위치.                                                                               |

(`Control`에서 상속받는 `enabled`, `focusPolicy`, `hoverEnabled` 등과 스타일링 관련 프로퍼티 `background`, `contentItem` 등도 사용 가능합니다.)

## 주요 시그널

`ProgressBar`는 주로 값 변경을 알리는 시그널은 없지만, 상속받은 `Control`의 일반적인 시그널 (`enabledChanged`, `hoveredChanged` 등)을 가집니다.

## 예제

```qml
import QtQuick
import QtQuick.Controls
import QtQuick.Layouts

Window {
    width: 400
    height: 200
    visible: true
    title: "ProgressBar Example"

    ColumnLayout {
        anchors.fill: parent
        anchors.margins: 10
        spacing: 15

        // 기본 ProgressBar (0-100 값 범위)
        Label { text: "Download Progress:" }
        ProgressBar {
            id: downloadProgress
            Layout.fillWidth: true
            from: 0
            to: 100
            value: 65 // 예시 값
        }

        // 미정 상태 ProgressBar (Indeterminate)
        Label { text: "Loading Data..." }
        ProgressBar {
            Layout.fillWidth: true
            indeterminate: true
        }

        // 값 조절 가능한 예제
        Label { text: "Adjust Value:" }
        RowLayout {
            Layout.fillWidth: true
            Slider {
                id: valueSlider
                Layout.fillWidth: true
                from: 0
                to: 100
                value: downloadProgress.value // 첫 번째 프로그레스 바와 연동
                onValueChanged: downloadProgress.value = value
            }
            Label { text: Math.round(valueSlider.value) + "%" }
        }
    }
}
```

## 참고 사항

*   `from`과 `to` 프로퍼티를 설정하여 프로그레스 바의 값 범위를 정의합니다. 백분율 표시가 일반적이므로 `to`를 100으로 설정하는 경우가 많습니다.
*   `value` 프로퍼티를 업데이트하여 진행 상태를 반영합니다.
*   정확한 진행률을 알 수 없을 때는 `indeterminate` 프로퍼티를 `true`로 설정하여 사용자가 작업이 진행 중임을 인지하도록 합니다.
*   `background`와 `contentItem` 프로퍼티를 통해 프로그레스 바의 모양(색상, 테두리 등)을 사용자 정의할 수 있습니다. 

## 공식 문서 링크

*   [ProgressBar QML Type ](https://doc.qt.io/qt-6/qml-qtquick-controls-progressbar.html) 