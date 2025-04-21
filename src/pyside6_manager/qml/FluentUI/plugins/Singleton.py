from typing import Any, Callable


# noinspection PyPep8Naming
def Singleton(cls: type) -> Callable[[], Any]:
    instances: dict[type, object] = {}

    def wrapper(*args: Any, **kwargs: Any) -> object:
        if cls not in instances:
            instances[cls] = cls(*args, **kwargs)
        return instances[cls]

    return wrapper
