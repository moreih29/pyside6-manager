# Window

**모듈:** `import QtQuick.Window 2.15` (버전은 환경에 따라 다를 수 있음)

## 개요

`Window`는 QML 장면(scene)을 담아 화면에 표시하는 최상위 네이티브 창을 나타냅니다. 모든 QML 애플리케이션 UI는 일반적으로 하나 이상의 `Window` 안에 배치됩니다.

`Window`는 운영체제의 창 시스템과 상호작용하며, 창의 크기, 위치, 제목, 가시성, 상태(최소화, 최대화 등), 투명도 등 다양한 속성을 제어할 수 있습니다.

## 기반 클래스

*   `QObject` (QML 타입 시스템의 일부, 직접적인 시각적 상속은 `QtQuickItem`과 다름)

## 주요 프로퍼티

| 이름              | 타입             | 기본값              | 설명                                                                                                                                                            |
| :---------------- | :--------------- | :------------------ | :-------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `visible`         | `bool`           | `false`             | 창을 화면에 표시할지 여부. `true`로 설정해야 창이 나타납니다.                                                                                                      |
| `width`           | `int`            | (시스템 의존)       | 창의 너비 (픽셀 단위).                                                                                                                                            |
| `height`          | `int`            | (시스템 의존)       | 창의 높이 (픽셀 단위).                                                                                                                                            |
| `x`               | `int`            | (시스템 의존)       | 창의 화면 상 가로 위치 (픽셀 단위).                                                                                                                                |
| `y`               | `int`            | (시스템 의존)       | 창의 화면 상 세로 위치 (픽셀 단위).                                                                                                                                |
| `title`           | `string`         | ""                | 창의 제목 표시줄에 표시될 텍스트.                                                                                                                                   |
| `color`           | `color`          | "white"           | 창의 배경색. `flags`에 `Qt.FramelessWindowHint`가 설정되고 `opacity`가 1.0 미만일 때 투명도 효과와 함께 배경색이 보일 수 있습니다.                                          |
| `opacity`         | `real`           | 1.0                 | 창의 전체 투명도 (0.0: 완전 투명, 1.0: 완전 불투명). 운영체제 및 창 관리자 지원 여부에 따라 동작이 다를 수 있습니다.                                                          |
| `visibility`      | `enumeration`    | `Window.Windowed`   | 창의 표시 상태 (`Windowed`, `Minimized`, `Maximized`, `FullScreen`, `AutomaticVisibility`).                                                                       |
| `active`          | `bool`           | (읽기 전용)         | 창이 현재 활성 상태인지 (키보드/마우스 입력을 받고 있는지) 여부.                                                                                                    |
| `contentItem`     | `Item`           | (읽기 전용)         | 창의 내용을 담는 루트 `Item`. 이 아이템의 자식으로 다른 QML 요소들을 배치합니다. `Window` 자체는 `Item`이 아니므로 `children` 프로퍼티를 직접 사용하지 않습니다.                  |
| `flags`           | `Qt.WindowFlags` | `Qt.Window`         | 창의 모양과 동작을 제어하는 플래그 조합 (`Qt.FramelessWindowHint`, `Qt.WindowStaysOnTopHint`, `Qt.Tool`, `Qt.SplashScreen` 등).                                              |
| `modality`        | `Qt.WindowModality` | `Qt.NonModal`      | 창의 모달(modal) 동작 방식 (`NonModal`, `WindowModal`, `ApplicationModal`). 모달 창은 다른 창과의 상호작용을 차단합니다.                                                 |
| `minimumWidth`    | `int`            | 0                   | 창의 최소 너비.                                                                                                                                                 |
| `minimumHeight`   | `int`            | 0                   | 창의 최소 높이.                                                                                                                                                 |
| `maximumWidth`    | `int`            | (제한 없음)         | 창의 최대 너비.                                                                                                                                                 |
| `maximumHeight`   | `int`            | (제한 없음)         | 창의 최대 높이.                                                                                                                                                 |
| `screen`          | `Screen`         | (읽기 전용, Attached Property) | `Screen.width`, `Screen.height`, `Screen.desktopAvailableWidth` 등 창이 표시되는 화면의 정보를 제공하는 부착 프로퍼티(Attached Property). `Window` 내 어디서든 `Screen.`으로 접근 가능. |

## 주요 시그널

| 이름                 | 파라미터 | 설명                                                                          |
| :------------------- | :------- | :---------------------------------------------------------------------------- |
| `closing(CloseEvent close)` | `CloseEvent` | 창이 닫히려고 할 때 발생합니다. `close.accepted = false`로 설정하여 닫기를 취소할 수 있습니다. |
| `visibleChanged`     |          | `visible` 프로퍼티가 변경될 때 발생합니다.                                      |
| `widthChanged`       |          | `width` 프로퍼티가 변경될 때 발생합니다.                                        |
| `heightChanged`      |          | `height` 프로퍼티가 변경될 때 발생합니다.                                       |
| `xChanged`           |          | `x` 프로퍼티가 변경될 때 발생합니다.                                            |
| `yChanged`           |          | `y` 프로퍼티가 변경될 때 발생합니다.                                            |
| `activeChanged`      |          | `active` 프로퍼티가 변경될 때 발생합니다.                                       |
| `visibilityChanged`  |          | `visibility` 프로퍼티가 변경될 때 발생합니다.                                   |

## 주요 메소드

| 이름           | 파라미터 | 반환타입 | 설명                                                                       |
| :------------- | :------- | :------- | :------------------------------------------------------------------------- |
| `show()`       | -        | -        | `visibility`를 `Window.Windowed`로 설정하고 `visible`을 `true`로 만듭니다.    |
| `hide()`       | -        | -        | `visible`을 `false`로 설정합니다.                                            |
| `close()`      | -        | -        | 창 닫기를 시도합니다 (`closing` 시그널 발생).                                |
| `raise()`      | -        | -        | 창을 다른 창들 위로 올립니다.                                                |
| `lower()`      | -        | -        | 창을 다른 창들 아래로 내립니다.                                                |
| `requestActivate()`| -       | -        | 운영체제에 창 활성화를 요청합니다.                                           |
| `showMinimized()`| -       | -        | `visibility`를 `Window.Minimized`로 설정합니다.                             |
| `showMaximized()`| -       | -        | `visibility`를 `Window.Maximized`로 설정합니다.                             |
| `showFullScreen()`| -      | -        | `visibility`를 `Window.FullScreen`로 설정합니다.                            |
| `showNormal()`   | -        | -        | `visibility`를 `Window.Windowed`로 설정합니다 (최소화/최대화/전체 화면 해제). |

## 예제

```qml
import QtQuick
import QtQuick.Window 2.15
import QtQuick.Controls
import QtQuick.Layouts

// 기본 Window 생성
Window {
    id: mainWindow
    width: 640
    height: 480
    visible: true // 창을 보이도록 설정
    title: qsTr("My QML Application") // 창 제목 설정
    color: "whitesmoke" // 배경색 (Frameless 시 유용)

    // 화면 중앙에 위치시키기 (Screen Attached Property 사용)
    x: (Screen.width - width) / 2
    y: (Screen.height - height) / 2

    // 창 닫기 시 확인 (closing 시그널 사용)
    onClosing: function(close) {
        // close.accepted = false // 이렇게 하면 창 닫기가 취소됨
        console.log("Window is closing!")
    }

    // 창 내용 (contentItem의 자식으로 추가)
    ColumnLayout {
        anchors.fill: parent
        anchors.margins: 10

        Label {
            text: "Hello from QML Window!"
            font.pointSize: 16
            Layout.alignment: Qt.AlignHCenter
        }

        Button {
            text: "Show Maximized"
            Layout.alignment: Qt.AlignHCenter
            onClicked: mainWindow.showMaximized()
        }

        Button {
            text: "Show FullScreen"
            Layout.alignment: Qt.AlignHCenter
            onClicked: mainWindow.showFullScreen()
        }

        Button {
            text: "Show Normal"
            Layout.alignment: Qt.AlignHCenter
            onClicked: mainWindow.showNormal()
        }

         Button {
            text: "Close Window"
            Layout.alignment: Qt.AlignHCenter
            onClicked: mainWindow.close()
        }
    }
}
```

## 참고 사항

*   QML 애플리케이션의 루트 요소는 일반적으로 `Window` 또는 `ApplicationWindow`입니다.
*   `Window` 내부에 UI 요소들을 배치할 때는 `Window`의 직접 자식이 아닌, `Window`의 `contentItem`의 자식으로 추가해야 합니다. 하지만 QML 문법상 편의를 위해 `Window { ... }` 안에 바로 UI 요소들을 선언하면 자동으로 `contentItem`의 자식이 됩니다.
*   `visible: true`를 설정해야 창이 화면에 나타납니다.
*   `flags` 프로퍼티를 사용하여 창 테두리 제거(`Qt.FramelessWindowHint`), 항상 위에 표시(`Qt.WindowStaysOnTopHint`) 등 다양한 창 스타일 및 동작을 지정할 수 있습니다.
*   `Screen` 부착 프로퍼티(`Screen.width`, `Screen.height` 등)를 사용하면 창이 표시되는 화면의 크기 및 사용 가능한 영역 정보를 얻어 창의 위치나 크기를 조절하는 데 유용합니다.
*   `ApplicationWindow` (`QtQuick.Controls`)는 `Window`를 기반으로 메뉴 바, 툴 바 등을 쉽게 추가할 수 있는 기능을 제공하므로, 일반적인 데스크톱 애플리케이션 UI에는 `ApplicationWindow`가 더 편리할 수 있습니다. 