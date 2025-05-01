# WorkerScript

**모듈:** `import QtQuick`

## 개요

`WorkerScript` 요소는 JavaScript 코드를 메인 UI 스레드와 별도의 백그라운드 스레드에서 실행할 수 있게 해줍니다. 이를 통해 시간이 많이 걸리는 계산, 데이터 처리, 네트워크 통신 등의 작업을 UI 스레드 차단 없이 수행하여 애플리케이션의 반응성을 유지할 수 있습니다.

`WorkerScript` 내부의 코드는 QML UI 요소에 직접 접근할 수 없으며, `sendMessage()` 메소드와 `onMessage` 핸들러를 통해 메인 스레드와 메시지를 주고받아 통신합니다.

## 사용 방법

`WorkerScript` 요소를 QML 파일에 추가하고 `source` 프로퍼티에 백그라운드에서 실행될 JavaScript 파일의 URL을 지정합니다. 또는 `WorkerScript` 내부에 직접 스크립트를 작성할 수도 있습니다 (덜 일반적).

**메인 QML 파일 (예: `Main.qml`)**

```qml
import QtQuick
import QtQuick.Controls
import QtQuick.Layouts

ApplicationWindow {
    visible: true
    width: 400; height: 300
    title: "WorkerScript Example"

    ColumnLayout {
        anchors.fill: parent
        anchors.margins: 10

        TextArea {
            id: outputArea
            Layout.fillWidth: true
            Layout.fillHeight: true
            readOnly: true
            text: "Waiting for worker..."
        }

        Button {
            id: startButton
            Layout.alignment: Qt.AlignHCenter
            text: "Start Heavy Calculation"
            onClicked: {
                outputArea.text = "Calculation started..."
                // WorkerScript에 메시지 보내기 (계산 시작 요청)
                worker.sendMessage({ command: 'calculate', data: 10000000 });
                startButton.enabled = false // 중복 실행 방지
            }
        }
    }

    // WorkerScript 요소 정의
    WorkerScript {
        id: worker
        source: "qrc:/workers/heavy_calculator.js" // 백그라운드 스크립트 파일 경로

        // WorkerScript로부터 메시지 수신
        onMessage: (messageObject) => {
            console.log("Message from worker:", JSON.stringify(messageObject))
            if (messageObject.reply === 'calculationComplete') {
                outputArea.text = "Calculation Result: " + messageObject.result + "\n(Calculated in " + messageObject.duration + " ms)";
                startButton.enabled = true // 버튼 다시 활성화
            } else if (messageObject.reply === 'error') {
                outputArea.text = "Error in worker: " + messageObject.error;
                startButton.enabled = true
            }
        }
    }
}
```

**백그라운드 JavaScript 파일 (예: `workers/heavy_calculator.js`)**

```javascript
// QML의 WorkerScript 요소와 통신하기 위한 API 임포트
// Qt 5 및 일부 환경에서는 Qt.include 사용:
// Qt.include("qrc:/qt-project.org/imports/QtQuick/workerscript/mt_bootstrap.js")
// Qt 6 및 표준 JavaScript 환경에서는 importScripts 사용 권장:
importScripts("qrc:/qt-project.org/imports/QtQuick/workerscript/mt_bootstrap.js")

// 메인 스레드로부터 메시지를 받았을 때 호출될 함수
WorkerScript.onMessage = function(message) {
    console.log("Message received in worker:", JSON.stringify(message));

    if (message.command === 'calculate') {
        try {
            var startTime = Date.now();
            var n = message.data;
            var result = 0;
            // 오래 걸리는 계산 시뮬레이션
            for (var i = 0; i < n; ++i) {
                result += Math.sqrt(i) * Math.sin(i / 1000.0);
                // 중간 진행 상황 보고 (선택 사항)
                // if (i % 1000000 === 0) {
                //     WorkerScript.sendMessage({ status: 'progress', value: (i / n) * 100 });
                // }
            }
            var endTime = Date.now();
            var duration = endTime - startTime;

            // 계산 완료 메시지를 메인 스레드로 전송
            WorkerScript.sendMessage({
                reply: 'calculationComplete',
                result: result,
                duration: duration
            });
        } catch (e) {
            // 오류 발생 시 메시지 전송
            WorkerScript.sendMessage({
                reply: 'error',
                error: e.toString()
            });
        }
    } else {
        console.log("Unknown command received in worker");
    }
}
```

*(참고: 위 JavaScript 파일이 동작하려면 Qt Resource System (`.qrc`)에 등록되어야 하며, `mt_bootstrap.js` 파일은 Qt 설치 경로의 QML 모듈 디렉토리에 있습니다. 실제 경로를 확인해야 할 수 있습니다. `Qt.include` 또는 `importScripts` 중 환경에 맞는 방식을 사용해야 합니다.)*

## 주요 프로퍼티

| 이름     | 타입  | 기본값 | 설명                                                                 |
| :------- | :---- | :----- | :------------------------------------------------------------------- |
| `source` | `url` | `""`   | 백그라운드 스레드에서 실행될 JavaScript 코드 파일의 URL입니다. 필수 프로퍼티입니다. |

## 주요 메소드

| 이름           | 파라미터                    | 반환타입 | 설명                                                                                                                               |
| :------------- | :-------------------------- | :------- | :--------------------------------------------------------------------------------------------------------------------------------- |
| `sendMessage()`| `message`: `variant`        | -        | 백그라운드 스레드(Worker)로 메시지를 보냅니다. `message`는 일반적으로 JSON과 유사한 JavaScript 객체입니다. 백그라운드 스크립트의 `WorkerScript.onMessage` 핸들러가 이 메시지를 받습니다. |

## 주요 시그널 핸들러

| 이름        | 파라미터                 | 설명                                                                                                                                 |
| :---------- | :----------------------- | :----------------------------------------------------------------------------------------------------------------------------------- |
| `onMessage` | `message`: `variant` | 백그라운드 스레드에서 `WorkerScript.sendMessage()`를 호출하여 보낸 메시지를 수신했을 때 메인 UI 스레드에서 실행되는 핸들러입니다. `message`는 백그라운드에서 보낸 객체입니다. |

## 백그라운드 스크립트 API (`WorkerScript` 객체)

백그라운드 JavaScript 파일 내에서는 `WorkerScript`라는 전역 객체를 통해 메인 스레드와 통신합니다.

*   `WorkerScript.onMessage = function(message) { ... }`: 메인 스레드에서 보낸 메시지를 처리하는 함수를 할당합니다.
*   `WorkerScript.sendMessage(message)`: 메인 스레드로 메시지를 보냅니다. 메인 QML의 `WorkerScript` 요소의 `onMessage` 핸들러가 이 메시지를 받습니다.

## 참고 사항

*   `WorkerScript` 내부의 코드는 별도의 JavaScript 환경에서 실행되므로, 메인 QML 컨텍스트의 변수, 함수, 객체(UI 요소 포함)에 직접 접근할 수 없습니다. 모든 데이터 교환은 `sendMessage`와 `onMessage`를 통해 이루어져야 합니다.
*   메시지로 전달되는 데이터는 직렬화 가능한 타입이어야 합니다 (예: 숫자, 문자열, 배열, 간단한 객체). QML 객체 자체를 직접 전달할 수는 없습니다.
*   백그라운드 스크립트 파일 경로(`source`)는 일반적으로 Qt Resource System (`qrc:/`)을 사용하거나 상대 경로 또는 절대 URL을 사용합니다.
*   오류 처리: 백그라운드 스크립트 내에서 발생할 수 있는 오류를 `try...catch`로 잡아서 메인 스레드로 오류 메시지를 보내는 것이 좋습니다.
*   Qt 6부터는 JavaScript 환경 및 스레딩 모델에 변화가 있을 수 있으므로, 최신 Qt 버전을 사용하는 경우 관련 문서를 확인하는 것이 좋습니다. 

## 공식 문서 링크

* [WorkerScript QML Type ](https://doc.qt.io/qt-6/qml-qtqml-workerscript-workerscript.html) 