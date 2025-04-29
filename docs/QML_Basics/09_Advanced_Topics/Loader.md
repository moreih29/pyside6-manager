# Loader

**모듈:** `import QtQuick`

## 개요

`Loader` 요소는 QML 컴포넌트를 동적으로 로드하거나 언로드하는 데 사용됩니다. 즉, 필요할 때만 특정 UI 부분을 로드하여 애플리케이션의 초기 로딩 시간을 단축하고 메모리 사용량을 최적화할 수 있습니다.

`Loader`는 로드된 아이템을 위한 플레이스홀더 역할을 하며, `source` 또는 `sourceComponent` 프로퍼티를 통해 로드할 대상을 지정합니다. 로드된 아이템은 `Loader`의 자식처럼 동작하며, `item` 프로퍼티를 통해 접근할 수 있습니다.

## 사용 방법

`Loader`는 로드할 컴포넌트를 외부 파일(`source`) 또는 내부 `Component` 객체(`sourceComponent`)로 지정할 수 있습니다.

```qml
import QtQuick
import QtQuick.Controls

Item {
    width: 400; height: 300

    // 로드할 컴포넌트 정의 (예: 외부 파일 MyItem.qml 또는 내부 Component)
    Component {
        id: myDynamicComponent
        Rectangle {
            width: 150; height: 100
            color: "lightcoral"
            border.color: "red"
            Text {
                anchors.centerIn: parent
                text: "Dynamically Loaded"
                font.bold: true
            }
        }
    }

    // Loader 요소 배치
    Loader {
        id: dynamicLoader
        anchors.centerIn: parent
        width: 150 // Loader 자체의 크기 (로드된 아이템 크기와 다를 수 있음)
        height: 100

        // 초기에는 아무것도 로드하지 않음 (active: false 또는 source/sourceComponent 미지정)
        active: false
    }

    Row {
        anchors.bottom: parent.bottom; anchors.horizontalCenter: parent.horizontalCenter; spacing: 10

        Button {
            text: "Load Component"
            onClicked: {
                // sourceComponent를 사용하여 내부 Component 로드
                dynamicLoader.sourceComponent = myDynamicComponent
                // 또는 외부 파일 로드:
                // dynamicLoader.source = "MyItem.qml"
                dynamicLoader.active = true // 로드 활성화
            }
        }

        Button {
            text: "Unload Component"
            enabled: dynamicLoader.status === Loader.Ready || dynamicLoader.status === Loader.Error
            onClicked: {
                dynamicLoader.active = false // 로드 비활성화 (언로드)
                // 또는 명시적 언로드:
                // dynamicLoader.source = ""
                // dynamicLoader.sourceComponent = undefined
            }
        }

        Button {
            text: "Access Item"
            enabled: dynamicLoader.status === Loader.Ready
            onClicked: {
                if (dynamicLoader.item) {
                    console.log("Loaded item color:", dynamicLoader.item.color)
                    dynamicLoader.item.color = "lightblue" // 로드된 아이템의 프로퍼티 변경
                }
            }
        }
    }

    Text {
        anchors.top: parent.top; anchors.horizontalCenter: parent.horizontalCenter; anchors.margins: 10
        text: "Loader Status: " + dynamicLoader.statusString
    }

}

// Helper function to get status string (optional)
function statusToString(status) {
    if (status === Loader.Null) return "Null";
    if (status === Loader.Ready) return "Ready";
    if (status === Loader.Loading) return "Loading";
    if (status === Loader.Error) return "Error";
    return "Unknown";
}

// Add this binding to the Text element above:
// text: "Loader Status: " + statusToString(dynamicLoader.status)
```

## 주요 프로퍼티

| 이름              | 타입        | 기본값      | 설명                                                                                                                               |
| :---------------- | :---------- | :---------- | :--------------------------------------------------------------------------------------------------------------------------------- |
| `active`          | `bool`      | `true`      | `true`이면 `source`나 `sourceComponent`가 유효할 때 컴포넌트를 로드하고 활성화합니다. `false`이면 로드된 컴포넌트를 언로드하고 비활성화합니다.        |
| `asynchronous`    | `bool`      | `false`     | `true`로 설정하면 컴포넌트를 비동기적으로 로드합니다. UI 스레드 차단을 방지하여 부드러운 사용자 경험을 제공하는 데 도움이 됩니다. (권장)              |
| `item`            | `Object`    | `null`      | (읽기 전용) 로드된 QML 아이템 객체입니다. 로딩이 완료되면 이 프로퍼티를 통해 로드된 객체에 접근할 수 있습니다. 로드되지 않았거나 실패하면 `null`입니다. |
| `progress`        | `real`      | `0.0` or `1.0` | (읽기 전용) 컴포넌트 로딩 진행률 (0.0 ~ 1.0). `asynchronous: true`일 때 의미가 있으며, 로딩 과정을 시각적으로 표시하는 데 사용할 수 있습니다.      |
| `source`          | `url`       | `""`        | 로드할 컴포넌트가 정의된 외부 QML 파일의 URL입니다.                                                                                  |
| `sourceComponent` | `Component` | `undefined` | 로드할 내부 `Component` 객체입니다. `source`와 `sourceComponent` 중 하나만 사용해야 합니다.                                                 |
| `status`          | `enumeration`| `Null`      | (읽기 전용) `Loader`의 현재 상태 (`Loader.Null`, `Loader.Ready`, `Loader.Loading`, `Loader.Error`).                                       |

## 주요 시그널

| 이름     | 파라미터 | 반환타입 | 설명                                                                 |
| :------- | :------- | :------- | :------------------------------------------------------------------- |
| `loaded` | -        | -        | 컴포넌트 로딩이 성공적으로 완료되었을 때 발생합니다. `item` 프로퍼티가 유효해집니다. |

## 주요 열거형 (Loader.)

| 이름      | 설명                                           |
| :-------- | :--------------------------------------------- |
| `Null`    | 초기 상태 또는 유효한 소스가 없는 상태.        |
| `Ready`   | 컴포넌트가 성공적으로 로드되어 `item`이 유효한 상태. |
| `Loading` | 컴포넌트가 현재 로딩 중인 상태 (주로 `asynchronous: true` 시). |
| `Error`   | 컴포넌트 로딩 중 오류가 발생한 상태.             |

## 참고 사항

*   `Loader`는 로드된 `item`을 자신의 자식처럼 관리하지만, `Loader` 자체의 `children` 리스트에는 포함되지 않습니다.
*   `Loader`의 크기는 로드될 아이템의 크기와 독립적입니다. `Loader`는 플레이스홀더 역할만 하며, 로드된 `item`은 `Loader`의 좌표계를 기준으로 배치됩니다. `item`의 크기가 `Loader`의 크기를 초과할 수 있습니다.
*   `active: false`로 설정하거나 `source`/`sourceComponent`를 빈 값으로 설정하면 현재 로드된 아이템이 파괴(destroy)됩니다. 다시 `active: true`로 설정하면 컴포넌트를 새로 로드합니다.
*   복잡하거나 큰 컴포넌트를 로드할 때는 `asynchronous: true`를 사용하여 UI 끊김 현상을 방지하는 것이 좋습니다.
*   `onLoaded` 시그널 핸들러 또는 `status` 변경 감지를 통해 로드 완료 시점에 특정 작업을 수행할 수 있습니다 (예: 로드된 아이템의 프로퍼티 설정, 시그널 연결). 