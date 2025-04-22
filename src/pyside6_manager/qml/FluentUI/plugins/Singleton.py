from typing import Any, Callable, TypeVar

T = TypeVar("T")  # 제네릭 타입 변수 선언


# noinspection PyPep8Naming
# cls는 Type[T] 타입이고, 반환되는 wrapper 함수는 어떤 인자든 받고 T 타입의 인스턴스를 반환합니다.
def Singleton(cls: type[T]) -> Callable[..., T]:
    # 인스턴스를 저장하는 딕셔너리. 키는 타입(cls), 값은 해당 타입 T의 인스턴스입니다.
    # 하지만 딕셔너리 타입 힌트에서는 값 타입을 object 대신 T로 명시하여 타입 추론을 돕습니다.
    instances: dict[type[T], T] = {}

    # wrapper 함수는 어떤 인자든 받을 수 있으며, T 타입의 인스턴스를 반환합니다.
    def wrapper(*args: Any, **kwargs: Any) -> T:
        if cls not in instances:
            instances[cls] = cls(*args, **kwargs)
        return instances[cls]

    return wrapper
