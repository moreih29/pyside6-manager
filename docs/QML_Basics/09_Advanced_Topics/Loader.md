# Loader

## 모듈 정보

```qml
import QtQuick
```

## 개요

`Loader` 요소는 QML 컴포넌트를 동적으로 로드하거나 언로드하는 데 사용됩니다. 즉, 필요할 때만 특정 UI 부분을 로드하여 애플리케이션의 초기 로딩 시간을 단축하고 메모리 사용량을 최적화할 수 있습니다.

`Loader`는 로드된 아이템을 위한 플레이스홀더 역할을 하며, `source` (외부 QML 파일 URL) 또는 `sourceComponent` (내부 `Component` 객체) 프로퍼티를 통해 로드할 대상을 지정합니다. 로드된 아이템은 `Loader`의 `item` 프로퍼티를 통해 접근할 수 있습니다.

`source`나 `sourceComponent`가 변경되면 이전에 인스턴스화된 아이템은 파괴됩니다. `source`를 빈 문자열로 설정하거나 `sourceComponent`를 `undefined`로 설정하면 현재 로드된 객체가 파괴되어 리소스를 해제하고 `Loader`를 비웁니다.

## 기반 클래스

* `Item`

## 주요 프로퍼티

| 이름              | 타입        | 기본값      | 설명                                                                                                                               |
| :---------------- | :---------- | :---------- | :--------------------------------------------------------------------------------------------------------------------------------- |
| `active`          | `bool`      | `true`      | `true`이면 `source`나 `sourceComponent`가 유효할 때 컴포넌트를 로드하고 활성화합니다. `false`이면 로드된 컴포넌트를 언로드(파괴)하고 비활성화합니다. |
| `asynchronous`    | `bool`      | `false`     | `true`로 설정하면 컴포넌트를 비동기적으로 로드합니다. UI 스레드 차단을 방지하여 부드러운 사용자 경험을 제공하는 데 도움이 됩니다. **권장되는 설정입니다.** |
| `item`            | `QtObject`  | `null`      | (읽기 전용) 로드된 QML 아이템 객체입니다. 로딩이 완료되면 이 프로퍼티를 통해 로드된 객체에 접근할 수 있습니다. 로드되지 않았거나 실패하면 `null`입니다. `Item`에서 상속되지 않은 객체일 수도 있으므로 타입은 `QtObject`입니다. |
| `progress`        | `real`      | `0.0` or `1.0` | (읽기 전용) 컴포넌트 로딩 진행률 (0.0 ~ 1.0). `asynchronous: true`일 때 의미가 있으며, 로딩 과정을 시각적으로 표시하는 데 사용할 수 있습니다. 동기 로딩 시에는 0.0 또는 1.0만 가집니다. |
| `source`          | `url`       | `""`        | 로드할 컴포넌트가 정의된 외부 QML 파일의 URL입니다.                                                                                  |
| `sourceComponent` | `Component` | `undefined` | 로드할 내부 `Component` 객체입니다. `source`와 `sourceComponent` 중 하나만 사용해야 합니다.                                                 |
| `status`          | `enumeration`| `Null`      | (읽기 전용) `Loader`의 현재 상태 (`Loader.Null`, `Loader.Ready`, `Loader.Loading`, `Loader.Error`). 상태 변화를 감지하여 UI 업데이트나 로직 처리에 사용할 수 있습니다. |

## 주요 시그널

| 이름     | 파라미터 | 반환타입 | 설명                                                                 |
| :------- | :------- | :------- | :------------------------------------------------------------------- |
| `loaded` | -        | -        | 컴포넌트 로딩이 성공적으로 완료되었을 때 발생합니다. 이 시그널 이후에 `item` 프로퍼티가 유효해지고 `status`가 `Loader.Ready`로 변경됩니다. `onLoaded` 핸들러를 사용합니다. |

## 주요 메소드

| 이름        | 파라미터                               | 반환타입 | 설명                                                                                                                                                              |
| :---------- | :------------------------------------- | :------- | :---------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `setSource()` | `source`: `url`, `properties`: `object` | `object` | 비동기적으로 지정된 `source` URL에서 컴포넌트를 로드하고, 선택적으로 초기 `properties`를 설정합니다. 로드된 아이템을 반환하는 대신 로딩을 시작합니다. `active`가 `false`여도 로딩을 시작하지만, `active`가 `true`가 되어야 화면에 표시됩니다. `asynchronous` 설정의 영향을 받습니다. |

## 주요 열거형 (Loader.)

| 이름      | 설명                                           |
| :-------- | :--------------------------------------------- |
| `Null`    | 초기 상태 또는 유효한 소스가 없는 상태.        |
| `Ready`   | 컴포넌트가 성공적으로 로드되어 `item`이 유효한 상태. |
| `Loading` | 컴포넌트가 현재 로딩 중인 상태 (주로 `asynchronous: true` 시). |
| `Error`   | 컴포넌트 로딩 중 오류가 발생한 상태.             |

## 예제

```qml
import QtQuick
import QtQuick.Controls
import QtQuick.Window // Window 사용을 위해 추가

Window { // Window로 감싸서 단독 실행 가능하게 함
    width: 400; height: 300
    visible: true
    title: "Loader Example"

    // 로드할 컴포넌트 정의 (예: 내부 Component)
    Component {
        id: myDynamicComponent
        Rectangle {
            id: loadedRect
            width: 150; height: 100
            color: "lightcoral"
            border.color: "red"

            property bool canToggleColor: true // 예시 프로퍼티
            signal componentClicked // 예시 시그널

            Text {
                anchors.centerIn: parent
                text: "Dynamically Loaded"
                font.bold: true
            }
            MouseArea { // 로드된 아이템 내 상호작용 예시
                anchors.fill: parent
                onClicked: loadedRect.componentClicked()
            }
        }
    }

    // Loader 요소 배치
    Loader {
        id: dynamicLoader
        anchors.centerIn: parent
        // Loader 자체의 크기를 명시적으로 지정하면 로드된 아이템이 이 크기에 맞춰짐
        // width: 200
        // height: 150

        // 초기에는 아무것도 로드하지 않음 (active: false 사용)
        active: false
        // 비동기 로딩 사용 권장
        asynchronous: true

        // 로드할 컴포넌트 지정 (버튼 클릭 시 설정됨)
        // sourceComponent: myDynamicComponent
        // 또는 외부 파일: source: "MyItem.qml"

        // 로드 완료 시그널 핸들러
        onLoaded: {
            console.log("Component loaded!");
            // 로드된 item의 프로퍼티 접근 및 시그널 연결
            if (item) { // item이 유효한지 확인
                item.color = "lightgreen"; // 로드 후 프로퍼티 변경
                // 로드된 아이템의 시그널에 연결
                item.componentClicked.connect(handleComponentClick);
            }
        }
    }

    // 로드된 아이템의 시그널을 처리하는 함수
    function handleComponentClick() {
        console.log("Loaded component was clicked!");
        if (dynamicLoader.item && dynamicLoader.item.canToggleColor) {
            dynamicLoader.item.color = (dynamicLoader.item.color == "lightcyan" ? "lightgreen" : "lightcyan");
        }
    }

    Column { // 버튼들을 위한 레이아웃
        anchors.bottom: parent.bottom; anchors.horizontalCenter: parent.horizontalCenter; spacing: 10; anchors.bottomMargin: 10

        Button {
            text: "Load Component"
            enabled: !dynamicLoader.active // 비활성화 상태일 때만 로드 가능
            onClicked: {
                dynamicLoader.sourceComponent = myDynamicComponent;
                dynamicLoader.active = true; // 로드 활성화 (비동기 로딩 시작)
            }
        }

        Button {
            text: "Unload Component"
            enabled: dynamicLoader.active // 활성화 상태일 때만 언로드 가능
            onClicked: {
                dynamicLoader.active = false; // 로드 비활성화 (아이템 파괴)
                // 또는 명시적 언로드:
                // dynamicLoader.source = ""
                // dynamicLoader.sourceComponent = undefined
            }
        }

        Button {
            text: "Access Item Property"
            enabled: dynamicLoader.status === Loader.Ready // 로드 완료 상태일 때만 접근 가능
            onClicked: {
                if (dynamicLoader.item) { // item 유효성 재확인
                    console.log("Loaded item color:", dynamicLoader.item.color);
                    // 로드된 아이템의 프로퍼티 직접 변경 가능
                    dynamicLoader.item.border.color = Qt.rgba(Math.random(), Math.random(), Math.random(), 1);
                }
            }
        }
    }

    Text { // 상태 표시
        id: statusText
        anchors.top: parent.top; anchors.horizontalCenter: parent.horizontalCenter; anchors.margins: 10
        // 상태 변화에 따라 텍스트 업데이트
        text: {
            switch(dynamicLoader.status) {
                case Loader.Null: return "Status: Null";
                case Loader.Ready: return "Status: Ready";
                case Loader.Loading: return "Status: Loading (" + (dynamicLoader.progress * 100).toFixed(0) + "%)";
                case Loader.Error: return "Status: Error";
                default: return "Status: Unknown";
            }
        }
        font.pixelSize: 14
    }
}
```

## 참고 사항

*   `Loader`는 로드된 `item`을 자신의 자식처럼 관리하지만, `Loader` 자체의 `children` 리스트에는 포함되지 않습니다. `item`은 `Loader`의 시각적 부모 역할을 합니다.
*   `active: false`로 설정하거나 `source`/`sourceComponent`를 빈 값/`undefined`로 설정하면 현재 로드된 아이템이 파괴(destroy)됩니다. 다시 로드하면 완전히 새로운 인스턴스가 생성됩니다.
*   복잡하거나 리소스를 많이 사용하는 컴포넌트를 로드할 때는 `asynchronous: true`를 사용하여 UI 끊김 현상을 방지하는 것이 매우 중요합니다.
*   `item` 프로퍼티에 접근할 때는 항상 `status`가 `Loader.Ready`인지 확인하거나 `item` 객체가 `null`이 아닌지 확인하는 것이 안전합니다.
*   **크기 조정 동작**:
    *   `Loader`에 명시적인 크기(width, height 또는 앵커링)가 지정되지 않으면, 컴포넌트 로딩 완료 시 로드된 아이템의 크기에 맞춰 `Loader`의 크기가 자동으로 조정됩니다.
    *   `Loader`에 명시적인 크기가 지정되면, 로드된 아이템이 `Loader`의 크기에 맞춰 조정됩니다.
    *   두 경우 모두 `Loader`와 로드된 `item`의 크기는 동일하게 유지됩니다.
*   **로드된 객체의 시그널 수신**: 로드된 `item` 객체가 발생시키는 시그널은 `onLoaded` 핸들러 내에서 또는 `item` 프로퍼티가 유효해진 후 `Connections` 요소를 사용하거나 JavaScript에서 동적으로 연결하여 수신할 수 있습니다.
    ```qml
    Loader {
        id: myLoader
        source: "MyItemWithSignal.qml"

        onLoaded: {
            if (item) {
                item.someSignal.connect(handleItemSignal);
            }
        }
        // 또는 Connections 사용 (item이 유효할 때 활성화됨)
        Connections {
            target: myLoader.item
            function onSomeSignal() { // Qt 6 스타일 핸들러
                handleItemSignal();
            }
            // ignoreUnknownSignals: true // target이 null일 때 오류 방지
        }
    }
    function handleItemSignal() { /* ... */ }
    ```

## 공식 문서 링크

* [Loader QML Type ](https://doc.qt.io/qt-6/qml-qtquick-loader.html) 