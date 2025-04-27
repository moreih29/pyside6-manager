from PySide6.QtCore import QObject, Slot, QSettings
from PySide6.QtGui import QGuiApplication

from pyside6_manager.qml.FluentUI.plugins.Singleton import Singleton

from .. import PROJECT_ROOT


# noinspection PyPep8Naming
@Singleton
class SettingsHelper(QObject):
    def __init__(self):
        super().__init__(QGuiApplication.instance())
        self._settings = QSettings()
        iniFilePath = (PROJECT_ROOT / "settings.ini").as_posix()
        self._settings = QSettings(iniFilePath, QSettings.Format.IniFormat)

    def _save(self, key, val):
        self._settings.setValue(key, val)

    def _get(self, key, default):
        data = self._settings.value(key)
        if data is None:
            return default
        return data

    @Slot(result=int)
    def getDarkMode(self) -> int:
        return int(self._get("darkMode", 0))

    @Slot(int)
    def saveDarkMode(self, darkMode: int):
        self._save("darkMode", darkMode)

    @Slot(result=bool)
    def getUseSystemAppBar(self) -> bool:
        return bool(self._get("useSystemAppBar", "false") == "true")

    @Slot(bool)
    def saveUseSystemAppBar(self, useSystemAppBar: bool):
        self._save("useSystemAppBar", useSystemAppBar)

    @Slot(result=str)
    def getLanguage(self) -> str:
        return str(self._get("language", "en_US"))

    @Slot(str)
    def saveLanguage(self, language: str):
        self._save("language", language)
