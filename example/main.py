import os
import sys
from pathlib import Path

sys.path.append(str(Path(__file__).parent.parent))

import asyncio
from qasync import QEventLoop

from PySide6.QtCore import QProcess, QUrl
from PySide6.QtGui import QGuiApplication
from PySide6.QtQml import QQmlApplicationEngine, qmlRegisterType
from PySide6.QtQuick import QQuickWindow, QSGRendererInterface

from pyside6_manager.qml.FluentUI import registerTypes

from example.AppInfo import AppInfo
from example.component.CircularReveal import CircularReveal
from example.component.FileWatcher import FileWatcher
from example.component.FpsItem import FpsItem
from example.component.OpenGLItem import OpenGLItem
from example.helper.InitializrHelper import InitializrHelper
from example.helper.SettingsHelper import SettingsHelper
from example.helper.TranslateHelper import TranslateHelper
from example.component.Callback import Callback
from example.helper import Async
from example.imports import resource_rc as rc  # noqa: F401

_uri = "example"
_major = 1
_minor = 0


# noinspection PyTypeChecker
def main():
    os.environ["QT_QUICK_CONTROLS_STYLE"] = "Basic"
    QQuickWindow.setGraphicsApi(QSGRendererInterface.GraphicsApi.OpenGL)
    QGuiApplication.setApplicationName("FluentUI Example")
    QGuiApplication.setApplicationDisplayName("FluentUI Example")
    app = QGuiApplication(sys.argv)

    qmlRegisterType(Callback, _uri, _major, _minor, "Callback")
    qmlRegisterType(CircularReveal, _uri, _major, _minor, "CircularReveal")
    qmlRegisterType(FileWatcher, _uri, _major, _minor, "FileWatcher")
    qmlRegisterType(FpsItem, _uri, _major, _minor, "FpsItem")
    qmlRegisterType(OpenGLItem, _uri, _major, _minor, "OpenGLItem")

    engine = QQmlApplicationEngine()

    event_loop = QEventLoop(app)
    asyncio.set_event_loop(event_loop)
    app_close_event = asyncio.Event()
    event_loop.create_task(Async.boot())

    app.aboutToQuit.connect(engine.deleteLater)
    app.aboutToQuit.connect(app_close_event.set)
    app.aboutToQuit.connect(lambda: event_loop.create_task(Async.delete()))

    context = engine.rootContext()
    TranslateHelper().init(engine)
    context.setContextProperty("AppInfo", AppInfo())

    context.setContextProperty("InitializrHelper", InitializrHelper())
    context.setContextProperty("SettingsHelper", SettingsHelper())
    context.setContextProperty("TranslateHelper", TranslateHelper())
    registerTypes(engine)
    qml_file = QUrl("qrc:/example/qml/App.qml")
    engine.load(qml_file)
    if not engine.rootObjects():
        sys.exit(-1)
    with event_loop:
        result = event_loop.run_until_complete(app_close_event.wait())
        if result == 931:
            QProcess.startDetached(
                QGuiApplication.instance().applicationFilePath(),
                QGuiApplication.instance().arguments(),
            )
        sys.exit(result)


if __name__ == "__main__":
    main()
