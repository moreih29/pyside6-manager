from aiohttp import ClientSession

from pyside6_manager.qml.FluentUI.plugins.Singleton import Singleton


# noinspection PyPep8Naming
@Singleton
class _Async:
    def __init__(self):
        self.http = None

    async def boot(self):
        self.http = ClientSession()

    def getHttp(self) -> ClientSession:
        return self.http


async def boot():
    await _Async().boot()


async def delete():
    await _Async().getHttp().close()


def http() -> ClientSession:
    return _Async().getHttp()
