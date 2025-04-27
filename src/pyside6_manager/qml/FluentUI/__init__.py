from pathlib import Path

from PySide6.QtQml import QQmlApplicationEngine

from .runner import QFluentGuiApplication
from .plugins.FluentUI import registerTypes


__all__ = ["init", "registerTypes", "QFluentGuiApplication"]


def init(engine: QQmlApplicationEngine) -> None:
    current_module_path = Path(__file__).parent.parent.resolve()
    engine.addImportPath(current_module_path)
