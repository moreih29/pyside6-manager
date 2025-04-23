# `Callback.py` 문서

이 파일은 비동기 작업이나 시간이 오래 걸리는 작업의 진행 상태(시작, 성공, 오류, 완료)를 QML에 알리기 위한 간단한 콜백 객체를 정의합니다.

## `Callback` 클래스

`QObject`를 상속받아 QML과 상호작용할 수 있는 시그널들을 제공합니다.

**주요 기능:**

*   작업의 각 단계(시작, 성공, 오류, 완료)에 해당하는 시그널을 정의하여 QML에서 해당 상태 변화를 감지하고 처리할 수 있도록 합니다.

**시그널:**

*   `start`: 작업이 시작될 때 발생합니다.
*   `finish`: 작업이 완료되었을 때 (성공/실패 여부와 관계없이) 발생합니다.
*   `error(code: int, errorString: str, result: str)`: 작업 중 오류가 발생했을 때 발생합니다. 오류 코드, 오류 메시지, 관련 결과 문자열을 전달할 수 있습니다.
*   `success(result: str)`: 작업이 성공적으로 완료되었을 때 발생합니다. 선택적으로 결과 문자열을 전달할 수 있습니다.

**메서드:**

*   `onStart(self)`: `start` 시그널을 발생시킵니다.
*   `onFinish(self)`: `finish` 시그널을 발생시킵니다.
*   `onSuccess(self, result: str = "")`: `success` 시그널을 발생시킵니다.
*   `onError(self, code: int = -1, errorString: str = "", result: str = "")`: `error` 시그널을 발생시킵니다.

**사용 예 (QML):**

```qml
import example 1.0

Item {
    // Python에서 Callback 객체를 생성하여 "myCallback" 이름으로 컨텍스트 속성 설정 필요
    // Connections {
    //     target: myCallback
    //     function onStart() { console.log("Task started"); }
    //     function onFinish() { console.log("Task finished"); }
    //     function onSuccess(result) { console.log("Task success:", result); }
    //     function onError(code, errorString, result) { console.error("Task error:", code, errorString, result); }
    // }
}
```

**사용 예 (Python):**

```python
# QML 엔진 및 컨텍스트 설정 후
callback = Callback()
context.setContextProperty("myCallback", callback)

# 작업 수행 중...
callback.onStart()
try:
    # ... 작업 수행 ...
    result_data = "Operation successful!"
    callback.onSuccess(result_data)
except Exception as e:
    callback.onError(500, str(e), "Failed")
finally:
    callback.onFinish()
``` 