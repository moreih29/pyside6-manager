# Window

## 모듈 정보

```qml
import QtQuick
```

## 개요

`Window`는 QML 장면(scene)을 담아 화면에 표시하는 최상위 네이티브 창을 나타냅니다. 모든 QML 애플리케이션 UI는 일반적으로 하나 이상의 `Window` 안에 배치됩니다.

`Window`는 운영체제의 창 시스템과 상호작용하며, 창의 크기, 위치, 제목, 가시성, 상태(최소화, 최대화 등), 투명도 등 다양한 속성을 제어할 수 있습니다.

## 기반 클래스

*   C++: `QQuickWindow`

## 주요 프로퍼티

| 이름                 | 타입                | 기본값                 | 설명                                                                                                                                                            |
| :------------------- | :------------------ | :--------------------- | :-------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `active`             | `bool`              | (읽기 전용)            | 창이 현재 활성 상태인지 (키보드/마우스 입력을 받고 있는지) 여부.                                                                                                    |
| `activeFocusItem`    | `Item`              | (읽기 전용)            | 현재 활성 포커스를 가진 아이템. 없으면 `null`.                                                                                                                    |
| `color`              | `color`             | (시스템 의존)          | 창의 배경색. `flags`에 `Qt.FramelessWindowHint`가 설정되고 `opacity`가 1.0 미만일 때 투명도 효과와 함께 배경색이 보일 수 있습니다.                                          |
| `contentItem`        | `Item`              | (읽기 전용)            | 창의 내용을 담는 보이지 않는 루트 `Item`. 이 아이템의 자식으로 다른 QML 요소들을 배치합니다.                                                                            |
| `contentOrientation` | `Qt::ScreenOrientation` | `Qt.PrimaryOrientation`| 창 콘텐츠의 방향 힌트 (화면 회전 등).                                                                                                                             |
| `data`               | `list<QtObject>`    | `[]`                   | `Window`의 자식 요소(Items, Resources, 다른 Windows)를 포함하는 기본 프로퍼티. 다른 `Window`를 자식으로 두면 transient 관계가 됩니다.                                         |
| `flags`              | `Qt::WindowFlags`   | `Qt.Window`            | 창의 모양과 동작을 제어하는 플래그 조합 (`Qt.FramelessWindowHint`, `Qt.WindowStaysOnTopHint`, `Qt.Dialog`, `Qt.SplashScreen` 등).                                        |
| `height`             | `int`               | (시스템 의존)          | 창의 높이 (픽셀 단위).                                                                                                                                            |
| `maximumHeight`      | `int`               | (제한 없음)            | 창의 최대 높이.                                                                                                                                                 |
| `maximumWidth`       | `int`               | (제한 없음)            | 창의 최대 너비.                                                                                                                                                 |
| `minimumHeight`      | `int`               | 0                      | 창의 최소 높이.                                                                                                                                                 |
| `minimumWidth`       | `int`               | 0                      | 창의 최소 너비.                                                                                                                                                 |
| `modality`           | `Qt::WindowModality`| `Qt.NonModal`          | 창의 모달(modal) 동작 방식 (`NonModal`, `WindowModal`, `ApplicationModal`). 모달 창은 다른 창과의 상호작용을 차단합니다.                                                 |
| `opacity`            | `real`              | 1.0                    | 창의 전체 투명도 (0.0: 완전 투명, 1.0: 완전 불투명). 운영체제 및 창 관리자 지원 여부에 따라 동작이 다를 수 있습니다.                                                          |
| `palette`            | `Palette`           | (시스템 의존, Qt 6.0+) | 창의 색상 팔레트. 운영체제 테마 변경 등에 반응하여 창 색상을 동적으로 변경하는 데 사용될 수 있습니다.                                                               |
| `screen`             | `variant`           | (읽기 전용)            | 창이 현재 표시되고 있는 화면 (QScreen). 여러 화면 정보를 얻으려면 `Screen` 부착 프로퍼티 사용.                                                                           |
| `title`              | `string`            | ""                     | 창의 제목 표시줄에 표시될 텍스트.                                                                                                                                   |
| `transientParent`    | `QWindow`           | `null`                 | 이 창의 임시 부모 창. 다른 `Window` 내부에 선언하면 자동으로 설정될 수 있습니다. 주로 대화상자 등에 사용됩니다.                                                            |
| `visibility`         | `QWindow::Visibility`| `Hidden`              | 창의 표시 상태 (`Hidden`, `Windowed`, `Minimized`, `Maximized`, `FullScreen`, `AutomaticVisibility`). `visible` 프로퍼티와 연동됩니다.                                   |
| `visible`            | `bool`              | `false`                | 창을 화면에 표시할지 여부. `true`로 설정해야 창이 나타납니다. `visibility`가 `Hidden`이 아닌 상태로 변경됩니다.                                                            |
| `width`              | `int`               | (시스템 의존)          | 창의 너비 (픽셀 단위).                                                                                                                                            |
| `x`                  | `int`               | (시스템 의존)          | 창의 화면 상 가로 위치 (픽셀 단위).                                                                                                                                |
| `y`                  | `int`               | (시스템 의존)          | 창의 화면 상 세로 위치 (픽셀 단위).                                                                                                                                |

## 부착 프로퍼티 (Attached Properties)

`Window` 요소 내부의 모든 `Item`에서 사용할 수 있습니다.

| 이름              | 타입                | 설명                                                            |
| :---------------- | :------------------ | :-------------------------------------------------------------- |
| `Window.active`   | `bool`              | (읽기 전용) 아이템이 속한 창이 현재 활성 상태인지 여부.           |
| `Window.activeFocusItem` | `Item`       | (읽기 전용) 아이템이 속한 창에서 현재 활성 포커스를 가진 아이템. |
| `Window.contentItem` | `Item`          | (읽기 전용) 아이템이 속한 창의 `contentItem` (루트 아이템).       |
| `Window.height`   | `int`               | (읽기 전용) 아이템이 속한 창의 높이.                            |
| `Window.visibility`| `QWindow::Visibility`| (읽기 전용) 아이템이 속한 창의 현재 가시성 상태.                |
| `Window.width`    | `int`               | (읽기 전용) 아이템이 속한 창의 너비.                            |
| `Window.window`   | `Window`            | (읽기 전용) 아이템이 속한 `Window` 객체.                       |

## 주요 시그널

| 이름                          | 파라미터                         | 설명                                                                                                                               |
| :---------------------------- | :------------------------------- | :--------------------------------------------------------------------------------------------------------------------------------- |
| `afterAnimating()`            | -                                | (애니메이션 관련) 씬 그래프 동기화 전에 GUI 스레드에서 발생합니다.                                                                      |
| `closing(CloseEvent close)`   | `CloseEvent`                     | 창이 닫히려고 할 때 발생합니다. `close.accepted = false`로 설정하여 닫기를 취소할 수 있습니다.                                               |
| `frameSwapped()`              | -                                | 프레임이 화면에 표시(큐)될 때 발생합니다.                                                                                             |
| `sceneGraphError(error, message)`| `SceneGraphError`, `QString` | 씬 그래프 초기화 중 오류 발생 시 발생합니다. 이 시그널을 처리하지 않으면 애플리케이션이 종료될 수 있습니다.                                    |
| `visibilityChanged()`         | -                                | `visibility` 프로퍼티가 변경될 때 발생합니다. (다른 프로퍼티 변경 시그널 `widthChanged`, `heightChanged`, `xChanged`, `yChanged`, `activeChanged` 등도 존재) |

## 주요 메소드

| 이름              | 파라미터     | 반환타입 | 설명                                                                       |
| :---------------- | :----------- | :------- | :------------------------------------------------------------------------- |
| `alert(msec?)`    | `int`        | -        | 지정된 시간(밀리초) 동안 또는 창이 다시 활성화될 때까지 사용자 주의를 요구하는 상태로 만듭니다 (예: 작업 표시줄 깜빡임). |
| `close()`         | -            | -        | 창 닫기를 시도합니다 (`closing` 시그널 발생).                                |
| `hide()`          | -            | -        | 창을 숨깁니다 (`visible = false` 또는 `visibility = Hidden` 설정과 동일).     |
| `lower()`         | -            | -        | 창을 다른 창들 아래로 내립니다.                                                |
| `raise()`         | -            | -        | 창을 다른 창들 위로 올립니다.                                                |
| `requestActivate()`| -           | -        | 운영체제에 창 활성화를 요청합니다 (키보드 포커스 받기).                           |
| `show()`          | -            | -        | 플랫폼 기본 동작에 따라 창을 표시합니다 (`showNormal`, `showMaximized`, `showFullScreen` 중 하나와 유사). |
| `showFullScreen()`| -           | -        | 창을 전체 화면으로 표시합니다 (`visibility = FullScreen` 설정과 동일).      |
| `showMaximized()` | -           | -        | 창을 최대화하여 표시합니다 (`visibility = Maximized` 설정과 동일).        |
| `showMinimized()` | -           | -        | 창을 최소화하여 표시합니다 (`visibility = Minimized` 설정과 동일).        |
| `showNormal()`    | -            | -        | 창을 기본 크기(최대화/최소화/전체 화면 아님)로 표시합니다 (`visibility = Windowed` 설정과 동일). |

## 예제

```qml
import QtQuick
import QtQuick.Controls // Button, Label 사용을 위해 추가
import QtQuick.Layouts // ColumnLayout 사용을 위해 추가

// 기본 Window 생성
Window {
    id: mainWindow
    width: 640
    height: 480
    visible: true // 창을 보이도록 설정
    title: qsTr("My QML Application") // 창 제목 설정
    color: "whitesmoke" // 배경색 (Frameless 시 유용)

    // 화면 중앙에 위치시키기 (Screen Attached Property 사용)
    // Screen 부착 프로퍼티를 사용하려면 QtQuick 모듈 외 추가 임포트 불필요
    x: (Screen.width - width) / 2
    y: (Screen.height - height) / 2

    // 창 닫기 시 확인 (closing 시그널 사용)
    onClosing: function(close) {
        console.log("Window is closing!")
        // 예시: 닫기 취소
        // if (someConditionNotMet) {
        //     close.accepted = false
        // }
    }

    // 창 내용 (contentItem의 자식으로 추가)
    ColumnLayout {
        anchors.fill: parent
        anchors.margins: 10

        Label {
            // 아이템 내부에서 Window 부착 프로퍼티 사용 예시
            text: "Window Active: " + Window.active
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
*   `Window` 내부에 UI 요소들을 배치할 때는 자동으로 `contentItem`의 자식이 됩니다.
*   `visible: true`를 설정하거나 `show()` 계열 메소드를 호출해야 창이 화면에 나타납니다.
*   `flags` 프로퍼티를 사용하여 창 테두리 제거(`Qt.FramelessWindowHint`), 항상 위에 표시(`Qt.WindowStaysOnTopHint`) 등 다양한 창 스타일 및 동작을 지정할 수 있습니다.
*   `Screen` 부착 프로퍼티(`Screen.width`, `Screen.height` 등)를 사용하면 창이 표시되는 화면의 크기 및 사용 가능한 영역 정보를 얻어 창의 위치나 크기를 조절하는 데 유용합니다. `Window` 내의 모든 `Item`에서 `Screen.`으로 접근 가능합니다.
*   `ApplicationWindow` (`QtQuick.Controls`)는 `Window`를 기반으로 메뉴 바, 툴 바 등을 쉽게 추가할 수 있는 기능을 제공하므로, 일반적인 데스크톱 애플리케이션 UI에는 `ApplicationWindow`가 더 편리할 수 있습니다.

## 공식 문서 링크

* [Window QML Type ](https://doc.qt.io/qt-6/qml-qtquick-window.html) 