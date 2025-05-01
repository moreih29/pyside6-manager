# Tumbler

## 모듈 정보

```qml
import QtQuick.Controls
```

## 개요

`Tumbler` 컨트롤은 사용자가 위아래로 스크롤 가능한 휠(wheel) 형태의 인터페이스에서 항목을 선택할 수 있도록 합니다. 주로 모바일 장치에서 날짜, 시간 또는 특정 옵션 목록 중 하나를 선택하는 데 사용됩니다.

하나의 `Tumbler`는 하나의 열(column)을 나타내며, 여러 개의 `Tumbler`를 조합하여 복합적인 선택 (예: 날짜 선택기)을 구성할 수 있습니다.

## 기반 클래스

*   `Control`

## 주요 프로퍼티

| 이름                | 타입          | 기본값                   | 설명                                                                                                                               |
| :------------------ | :------------ | :----------------------- | :--------------------------------------------------------------------------------------------------------------------------------- |
| `model`             | `variant`     | `undefined`              | 텀블러에 표시될 데이터 모델. 숫자(항목 개수), 리스트(문자열 또는 숫자), 또는 `ObjectModel`, `ListModel` 등을 사용할 수 있습니다.           |
| `count`             | `int`         | (읽기 전용)              | 모델에 포함된 항목의 총 개수.                                                                                                      |
| `currentIndex`      | `int`         | 0                        | 현재 선택된 항목의 인덱스. `count`가 0이면 -1이 됩니다.                                                                              |
| `currentItem`       | `Item`        | (읽기 전용)              | 현재 선택된 항목을 표시하는 내부 아이템.                                                                                             |
| `delegate`          | `Component`   | (스타일 의존, `Text` 기반)| 모델의 각 항목을 시각적으로 표시하는 방법을 정의하는 컴포넌트. `index`, `modelData`, `Tumbler.tumbler` 등의 컨텍스트/첨부 프로퍼티를 사용할 수 있습니다. |
| `visibleItemCount`  | `int`         | 5                        | 한 번에 화면에 보이는 항목의 개수. 일반적으로 홀수로 설정하여 중앙 항목이 명확하게 보이도록 합니다.                                  |
| `wrap`              | `bool`        | (조건부 기본값)          | `true`로 설정하면 목록의 끝에서 처음으로 (또는 그 반대로) 스크롤이 순환됩니다. `count > visibleItemCount` 일 때 기본값은 `true`. 그렇지 않으면 플랫폼 의존적. (Qt 5.8+) |
| `moving`            | `bool`        | (읽기 전용)              | 현재 텀블러가 사용자의 드래그나 플릭(flick)으로 인해 스크롤(이동) 중인지 여부. (Qt 5.9+)                                                |
| `flickDeceleration` | `int`         | (조건부 기본값)          | 플릭 속도가 감소하는 비율. 높을수록 빨리 멈춥니다. `wrap`이 true일 때 기본 100, 아닐 경우 플랫폼 의존적. 0 이하 값은 허용되지 않습니다. |
| `background`        | `Item`        | (스타일 의존)            | 텀블러의 배경 아이템. 스타일링에 사용됩니다.                                                                                         |
| `contentItem`       | `Flickable`   | (읽기 전용)              | 항목들을 담고 스크롤 기능을 제공하는 내부 `Flickable` 아이템.                                                                        |
| `delegateAlignment` | `Qt.Alignment`| `Qt.AlignHCenter`        | `delegate` 내에서 항목 내용의 수평 정렬 방식.                                                                                      |
| `enabled`           | `bool`        | `true`                   | 컨트롤의 활성화 상태.                                                                                                              |
| `focusPolicy`       | `FocusPolicy` | `Qt.StrongFocus`         | 컨트롤이 키보드 포커스를 받는 방식.                                                                                                  |
| `hoverEnabled`      | `bool`        | `false`                  | 마우스 호버 효과 활성화 여부 (주로 터치 장치용이므로 기본 비활성화).                                                                  |
| `wheelEnabled`      | `bool`        | `true`                   | 마우스 휠 스크롤 활성화 여부.                                                                                                      |

## 첨부 프로퍼티 (Attached Properties)

델리게이트 아이템 내부에서 사용할 수 있는 특별한 프로퍼티입니다.

| 이름                 | 타입    | 설명                                                                                                           |
| :------------------- | :------ | :------------------------------------------------------------------------------------------------------------- |
| `Tumbler.displacement` | `real`  | (읽기 전용) 현재 항목과의 상대적인 거리. `-visibleItemCount / 2` 부터 `visibleItemCount / 2` 까지의 값을 가지며, 0은 현재 항목임을 의미합니다. |
| `Tumbler.tumbler`    | `Tumbler` | (읽기 전용) 이 델리게이트가 속한 `Tumbler` 컨트롤 인스턴스.                                                      |

## 주요 시그널

| 이름                 | 파라미터 | 설명                                               |
| :------------------- | :------- | :------------------------------------------------- |
| `currentIndexChanged`|          | `currentIndex` 프로퍼티가 변경될 때 발생합니다.        |
| `moved`              |          | 텀블러가 스크롤되어 이동했을 때 발생합니다. (Qt 5.9+)   |
| `movementStarted`    |          | 텀블러 스크롤(이동)이 시작될 때 발생합니다.          |
| `movementEnded`      |          | 텀블러 스크롤(이동)이 끝났을 때 발생합니다.            |

## 주요 메서드

| 이름                       | 파라미터              | 설명                                                                                                                            |
| :------------------------- | :-------------------- | :------------------------------------------------------------------------------------------------------------------------------ |
| `decrementCurrentIndex()`  |                       | `currentIndex`를 1 감소시킵니다.                                                                                                  |
| `incrementCurrentIndex()`  |                       | `currentIndex`를 1 증가시킵니다.                                                                                                  |
| `positionViewAtIndex(index, mode)` | `int`, `PositionMode` | 지정된 인덱스의 항목이 `mode`에 지정된 위치(`Beginning`, `Center`, `End` 등)에 오도록 뷰를 스크롤합니다. (Qt 5.12+)                      |

## 예제

```qml
import QtQuick
import QtQuick.Controls
import QtQuick.Layouts

Window {
    width: 300
    height: 300
    visible: true
    title: "Tumbler Example"

    ColumnLayout {
        anchors.fill: parent
        anchors.margins: 10
        spacing: 10

        Label {
            id: selectionLabel
            Layout.alignment: Qt.AlignHCenter
            text: "Selected: Month " + (monthTumbler.currentIndex + 1)
                   + ", Year " + yearTumbler.model.get(yearTumbler.currentIndex).year // ListModel 접근 수정됨
            font.pointSize: 12
        }

        // 월(Month)과 년(Year) 선택을 위한 텀블러 조합
        RowLayout {
            Layout.alignment: Qt.AlignHCenter
            spacing: 5

            // 월(Month) 텀블러 (1-12)
            Tumbler {
                id: monthTumbler
                model: 12 // 0부터 11까지 인덱스 생성 (총 12개 항목)
                visibleItemCount: 5
                wrap: true // 순환 스크롤

                delegate: Component {
                    Text {
                        text: index + 1 // 0-11 인덱스를 1-12로 표시 (modelData 사용 가능)

                        // 부모 Tumbler 접근: Tumbler.tumbler
                        // font: Tumbler.tumbler.font
                        // 현재 항목 확인: Tumbler.displacement 사용
                        color: Tumbler.displacement == 0 ? "blue" : "black"

                        horizontalAlignment: Text.AlignHCenter
                        verticalAlignment: Text.AlignVCenter
                        // 상대 위치(displacement)와 부모 Tumbler의 visibleItemCount 사용
                        opacity: 1.0 - Math.abs(Tumbler.displacement) / (Tumbler.tumbler.visibleItemCount / 2)
                    }
                }

                onCurrentIndexChanged: {
                    updateSelectionLabel()
                }
            }

            // 년(Year) 텀블러 (ListModel 사용)
            Tumbler {
                id: yearTumbler
                model: ListModel {
                    ListElement { year: 2022 }
                    ListElement { year: 2023 }
                    ListElement { year: 2024 }
                    ListElement { year: 2025 }
                    ListElement { year: 2026 }
                }
                visibleItemCount: 5
                currentIndex: 2 // 초기 선택: 2024

                delegate: Component {
                    Text {
                        // ListModel 역할 접근: modelData 사용 (초기화 시점 방어 코드 추가)
                        text: modelData.year ? modelData.year : ""

                        // 부모 Tumbler 접근: Tumbler.tumbler
                        // font: Tumbler.tumbler.font
                        // 현재 항목 확인: Tumbler.displacement 사용
                        color: Tumbler.displacement == 0 ? "blue" : "black"

                        horizontalAlignment: Text.AlignHCenter
                        verticalAlignment: Text.AlignVCenter
                        // 상대 위치(displacement)와 부모 Tumbler의 visibleItemCount 사용
                        opacity: 1.0 - Math.abs(Tumbler.displacement) / (Tumbler.tumbler.visibleItemCount / 2)
                    }
                }

                onCurrentIndexChanged: {
                    updateSelectionLabel()
                }
            }
        }
    }

    // 선택된 값 업데이트 함수
    function updateSelectionLabel() {
        // ListModel 데이터 접근 시 get()과 역할 이름 사용
        selectionLabel.text = "Selected: Month " + (monthTumbler.currentIndex + 1)
                               + ", Year " + yearTumbler.model.get(yearTumbler.currentIndex).year;
    }
}
```

## 참고 사항

*   `model` 프로퍼티에 다양한 데이터 소스 (숫자, 리스트, `ListModel`, `ObjectModel` 등)를 지정할 수 있습니다.
*   `delegate`를 사용하여 각 항목의 표시 방식을 커스터마이징할 수 있습니다. 델리게이트 내에서는 다음과 같은 유용한 컨텍스트 및 첨부 프로퍼티를 사용할 수 있습니다:
    *   `index`: 항목의 인덱스.
    *   `modelData`: 해당 인덱스의 모델 데이터. 모델 타입에 따라 실제 값이 다릅니다 (예: 숫자는 인덱스 자체, `ListModel`은 역할 객체).
    *   `Tumbler.tumbler`: 델리게이트가 속한 `Tumbler` 인스턴스.
    *   `Tumbler.displacement`: 현재 항목으로부터의 상대적인 거리 (`0`이 현재 항목).
*   `visibleItemCount`는 일반적으로 홀수로 설정하여 중앙 항목이 명확하게 선택된 항목으로 보이도록 합니다.
*   `wrap` 프로퍼티를 통해 스크롤 순환 여부를 제어할 수 있습니다. 기본 동작은 모델 항목 수(`count`)와 `visibleItemCount`에 따라 달라집니다.
*   여러 개의 `Tumbler`를 `RowLayout` 등으로 배치하여 날짜 선택기, 시간 선택기 등 복합적인 선택 UI를 구성할 수 있습니다.

## 공식 문서 링크

*   [Tumbler QML Type ](https://doc.qt.io/qt-6/qml-qtquick-controls-tumbler.html) 