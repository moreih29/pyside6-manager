# Popup

## 모듈 정보

```qml
import QtQuick.Controls
```

## 개요

`Popup`은 임시적인 사용자 인터페이스 요소를 표시하는 데 사용되는 기본 컨테이너입니다. `Dialog`, `Menu`, `ToolTip` 등 다른 많은 컨트롤들의 기반 클래스로 사용되며, 직접 사용하여 사용자 정의 팝업 UI를 만들 수도 있습니다.

`Popup`은 일반적으로 특정 이벤트(예: 버튼 클릭)에 의해 열리고, 특정 조건(예: Esc 키 누름, 바깥 영역 클릭)에 따라 닫힙니다. 모달(modal) 또는 비모달(non-modal) 형태로 표시될 수 있습니다.

## 기반 클래스

*   `Item` (간접적으로 `QtQuick`의 `Item`을 기반으로 함)

## 주요 프로퍼티

| 이름           | 타입               | 기본값                  | 설명                                                                                                                                    |
| :------------- | :----------------- | :---------------------- | :-------------------------------------------------------------------------------------------------------------------------------------- |
| `opened`       | `bool`             | `false`                 | 팝업이 현재 열려 있는지(보이는지) 여부. `open()` 및 `close()` 메서드나 직접적인 값 변경으로 제어됩니다.                                        |
| `x`            | `real`             | 0                       | 팝업의 부모 좌표계 기준 가로 위치.                                                                                                          |
| `y`            | `real`             | 0                       | 팝업의 부모 좌표계 기준 세로 위치.                                                                                                          |
| `width`        | `real`             | (암시적 크기)           | 팝업의 너비. 설정하지 않으면 `implicitWidth`를 따릅니다.                                                                                    |
| `height`       | `real`             | (암시적 크기)           | 팝업의 높이. 설정하지 않으면 `implicitHeight`를 따릅니다.                                                                                   |
| `implicitWidth`| `real`             | (계산됨)                | 내용(`contentItem`)에 기반한 암시적 너비.                                                                                                 |
| `implicitHeight`| `real`            | (계산됨)                | 내용(`contentItem`)에 기반한 암시적 높이.                                                                                                 |
| `contentItem`  | `Item`             | `null`                  | 팝업 내부에 표시될 실제 내용을 담는 아이템. 이 아이템의 크기가 `implicitWidth`, `implicitHeight` 계산에 사용됩니다.                                |
| `background`   | `Item`             | (스타일 의존)           | 팝업의 배경 아이템. 스타일링(테두리, 배경색 등)에 사용됩니다.                                                                               |
| `padding`      | `real`             | (스타일 의존)           | `background`와 `contentItem` 사이의 여백.                                                                                                 |
| `modal`        | `bool`             | `false`                 | `true`이면 모달 팝업으로 동작하여 뒤쪽 UI와의 상호작용을 막습니다.                                                                            |
| `dim`          | `bool`             | `modal` 값과 같음       | `true`이고 `modal`일 때 팝업 뒤의 배경을 어둡게 표시할지 여부.                                                                                |
| `focus`        | `bool`             | `true`                  | 팝업이 열렸을 때 키보드 포커스를 받을지 여부.                                                                                                 |
| `parent`       | `Item`             | (설정 필요 또는 자동) | 팝업의 부모 아이템. 팝업의 위치는 이 부모 아이템의 좌표계를 기준으로 합니다. 일반적으로 팝업을 여는 버튼 등이 포함된 컨테이너로 설정합니다. `ApplicationWindow`나 `Overlay`도 사용됩니다. |
| `margins`      | `real`             | 0                       | `parent`의 경계와 팝업 사이의 최소 간격. 팝업이 화면 가장자리를 벗어나지 않도록 위치를 조정할 때 사용됩니다.                                            |
| `closePolicy`  | `Popup.ClosePolicy`| `Popup.CloseOnEscape` | 팝업이 자동으로 닫히는 조건. 여러 플래그 조합 가능 (`CloseOnEscape`, `CloseOnPressOutside`, `CloseOnPressOutsideParent`, `CloseOnReleaseOutside`, `NoAutoClose`). |

## 주요 시그널

| 이름         | 파라미터 | 설명                                                                 |
| :----------- | :------- | :------------------------------------------------------------------- |
| `opened()`   | -        | `open()` 메서드가 호출되거나 `opened`가 `true`로 변경되어 팝업이 열렸을 때 발생합니다. |
| `closed()`   | -        | `close()` 메서드가 호출되거나 `opened`가 `false`로 변경되어 팝업이 닫혔을 때 발생합니다. |
| `aboutToShow()`| -       | `open()`이 호출된 직후, 팝업이 실제로 화면에 나타나기 전에 발생합니다.      |
| `aboutToHide()`| -       | `close()`가 호출된 직후, 팝업이 실제로 화면에서 사라지기 전에 발생합니다.     |

## 주요 메소드

| 이름      | 파라미터 | 반환타입 | 설명                                            |
| :-------- | :------- | :------- | :---------------------------------------------- |
| `open()`  | -        | -        | 팝업을 엽니다 (`opened = true`).                 |
| `close()` | -        | -        | 팝업을 닫습니다 (`opened = false`).              |

## 예제

```qml
import QtQuick
import QtQuick.Controls
import QtQuick.Layouts

ApplicationWindow {
    width: 400; height: 300
    visible: true
    title: "Popup Example"

    // 간단한 메시지를 보여주는 Popup 정의
    Popup {
        id: simplePopup
        x: (parent.width - width) / 2 // 부모 중앙에 위치
        y: 100
        width: 200
        modal: true // 모달로 설정
        focus: true // 포커스 받기
        closePolicy: Popup.CloseOnEscape | Popup.CloseOnPressOutside // Esc 또는 바깥 클릭 시 닫기

        // 팝업 내용
        contentItem: Label {
            text: "This is a simple popup!"
            padding: 20
            background: Rectangle { color: "lightyellow"; border.color: "orange" }
        }

        // 팝업 배경 (기본 스타일 대신 약간의 그림자 효과 추가)
        background: Rectangle {
            color: "transparent" // 배경 자체는 투명하게
            Rectangle {
                anchors.fill: parent
                anchors.margins: -2 // 약간 확장하여 그림자 공간 확보
                color: "#DDDDDD" // 그림자 색상
                opacity: 0.5
                radius: 5
                Rectangle {
                    anchors.fill: parent
                    anchors.margins: 2 // 안쪽 실제 배경
                    color: "white"
                    radius: 3
                }
            }
        }

        onOpened: console.log("Simple Popup opened")
        onClosed: console.log("Simple Popup closed")
    }

    // 버튼 클릭 시 팝업 열기
    Button {
        text: "Show Simple Popup"
        anchors.centerIn: parent
        onClicked: {
            simplePopup.open()
        }
    }
}
```

## 참고 사항

*   `Popup`은 `QtQuick.Controls` 모듈에 속합니다.
*   `open()` 메소드를 호출하여 팝업을 표시하고 `close()` 메소드를 호출하여 닫습니다. `opened` 프로퍼티를 직접 `true`/`false`로 설정할 수도 있습니다.
*   팝업의 내용은 `contentItem` 프로퍼티에 배치합니다. `contentItem`의 크기에 따라 팝업의 `implicitWidth`, `implicitHeight`가 결정될 수 있습니다.
*   `parent` 프로퍼티를 설정하여 팝업의 위치 기준을 정하는 것이 중요합니다. 일반적으로 팝업을 여는 컨트롤이 포함된 레이아웃이나 `ApplicationWindow`의 `overlay` (`ApplicationWindow.overlay`) 를 부모로 설정합니다.
*   `x`, `y` 프로퍼티를 사용하여 `parent` 내에서의 위치를 지정합니다.
*   `modal: true`로 설정하면 팝업이 열려 있는 동안 다른 UI와의 상호작용이 차단됩니다. `dim: true`는 배경을 어둡게 처리합니다.
*   `closePolicy`를 사용하여 Esc 키, 팝업 바깥 영역 클릭 등 어떤 조건에서 팝업이 자동으로 닫힐지 설정할 수 있습니다.
*   `background` 프로퍼티를 통해 팝업의 배경(테두리, 그림자 등)을 사용자 정의할 수 있습니다.
*   `Dialog`, `Menu`, `ToolTip`은 `Popup`을 기반으로 특정 목적에 맞게 확장된 컨트롤입니다. 

## 공식 문서 링크

* [Popup QML Type ](https://doc.qt.io/qt-6/qml-qtquick-controls-popup.html) 