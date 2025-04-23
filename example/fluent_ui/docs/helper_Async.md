# `Async.py` 문서

이 파일은 애플리케이션 전반에서 사용될 비동기 작업, 특히 `aiohttp`를 이용한 HTTP 클라이언트 세션을 관리하는 헬퍼 모듈입니다.

## `_Async` 클래스 (싱글톤)

*   `@Singleton` 데코레이터를 사용하여 애플리케이션 내에서 단 하나의 인스턴스만 생성되도록 보장합니다.
*   주요 역할은 `aiohttp.ClientSession` 인스턴스를 관리하는 것입니다.

**메서드:**

*   `__init__(self)`: 생성자. `http` 속성(ClientSession 저장용)을 `None`으로 초기화합니다.
*   `async boot(self)`: 비동기 메서드. 새로운 `aiohttp.ClientSession` 객체를 생성하여 `self.http`에 할당합니다. 애플리케이션 시작 시 호출되어 HTTP 통신을 준비합니다.
*   `getHttp(self) -> ClientSession`: 현재 관리 중인 `ClientSession` 인스턴스를 반환합니다.

## 전역 함수

*   `async def boot()`: 싱글톤 `_Async` 인스턴스의 `boot()` 코루틴을 호출합니다. `main.py`에서 애플리케이션 시작 시 이 함수를 호출하여 비동기적으로 HTTP 세션을 초기화합니다.
*   `async def delete()`: 싱글톤 `_Async` 인스턴스에서 `ClientSession`을 가져와 비동기적으로 `close()` 메서드를 호출합니다. `main.py`에서 애플리케이션 종료 시 이 함수를 호출하여 열려 있는 HTTP 연결을 안전하게 종료합니다.
*   `def http() -> ClientSession`: 싱글톤 `_Async` 인스턴스의 `getHttp()` 메서드를 호출하여 현재 활성화된 `ClientSession` 객체를 다른 모듈에서 쉽게 접근할 수 있도록 제공합니다.

**요약:**

이 모듈은 `aiohttp`를 사용한 비동기 HTTP 통신을 위한 중앙 관리 지점 역할을 합니다. 애플리케이션의 시작과 종료 시점에 맞춰 HTTP 세션을 적절히 생성하고 소멸시키는 작업을 담당하며, 다른 부분에서 필요할 때 해당 세션 객체에 접근할 수 있는 인터페이스를 제공합니다. 