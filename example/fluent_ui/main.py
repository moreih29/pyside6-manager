import sys
from pathlib import Path

from PySide6.QtGui import QGuiApplication
from PySide6.QtQml import QQmlApplicationEngine
from PySide6.QtQuick import QQuickWindow, QSGRendererInterface

from pyside6_manager.qml import FluentUI


ROOT = Path(__file__).parent.resolve()


def main() -> int:
    QQuickWindow.setGraphicsApi(QSGRendererInterface.GraphicsApi.OpenGL)
    app = QGuiApplication(sys.argv)
    engine = QQmlApplicationEngine()
    FluentUI.registerTypes(engine)
    engine.load(ROOT / "main.qml")

    if not engine.rootObjects():
        return -1

    return app.exec()


if __name__ == "__main__":
    main()
