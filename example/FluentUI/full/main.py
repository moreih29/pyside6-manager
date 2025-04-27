import sys
from pathlib import Path


from qasync import asyncSlot

from PySide6.QtCore import QObject, Signal, Property
from PySide6.QtGui import QGuiApplication
from PySide6.QtQml import qmlRegisterType

from pyside6_manager.qml.FluentUI import QFluentGuiApplication
from pyside6_manager.qml.FluentUI.plugins.Singleton import Singleton

sys.path.append(str(Path(__file__).parents[3]))
from example.FluentUI.full import PROJECT_ROOT
from example.FluentUI.full.component.CircularReveal import CircularReveal
from example.FluentUI.full.component.FileWatcher import FileWatcher
from example.FluentUI.full.component.FpsItem import FpsItem
from example.FluentUI.full.component.OpenGLItem import OpenGLItem
from example.FluentUI.full.helper.InitializrHelper import InitializrHelper
from example.FluentUI.full.helper.SettingsHelper import SettingsHelper
from example.FluentUI.full.helper.TranslateHelper import TranslateHelper
from example.FluentUI.full.helper import Async
from example.FluentUI.full.component.Callback import Callback

_uri = "full"
_major = 1
_minor = 0


@Singleton
class AppInfo(QObject):
    versionChanged = Signal()

    @Property(str, notify=versionChanged)
    def version(self):
        return self._version

    @version.setter
    def version(self, value):
        self._version = value
        self.versionChanged.emit()

    def __init__(self):
        super().__init__(QGuiApplication.instance())
        self._version = "1.7.6"

    @asyncSlot(Callback)
    async def checkUpdate(self, callback: Callback):
        callback.onStart()
        try:
            r = await Async.http().get(
                "https://api.github.com/repos/zhuzichu520/FluentUI/releases/latest"
            )
            callback.onSuccess(await r.text())
        except Exception as exc:
            callback.onError(errorString="Error: {}".format(exc))
        finally:
            callback.onFinish()


# noinspection PyTypeChecker
def main():
    app = QFluentGuiApplication(sys.argv, application_display_name="FluentUI Full Demo")

    qmlRegisterType(Callback, _uri, _major, _minor, "Callback")
    qmlRegisterType(CircularReveal, _uri, _major, _minor, "CircularReveal")
    qmlRegisterType(FileWatcher, _uri, _major, _minor, "FileWatcher")
    qmlRegisterType(FpsItem, _uri, _major, _minor, "FpsItem")
    qmlRegisterType(OpenGLItem, _uri, _major, _minor, "OpenGLItem")

    app.event_loop.create_task(Async.boot())
    app.aboutToQuit.connect(lambda: app.event_loop.create_task(Async.delete()))

    TranslateHelper().init(app.engine)
    context = app.engine.rootContext()
    context.setContextProperty("AppInfo", AppInfo())
    context.setContextProperty("InitializrHelper", InitializrHelper())
    context.setContextProperty("SettingsHelper", SettingsHelper())
    context.setContextProperty("TranslateHelper", TranslateHelper())

    # app.run(PROJECT_ROOT / "imports/example/qml/App.qml", base_path=PROJECT_ROOT)
    app.run("qrc:/example/qml/App.qml", base_path=PROJECT_ROOT, debug=True)


if __name__ == "__main__":
    main()
