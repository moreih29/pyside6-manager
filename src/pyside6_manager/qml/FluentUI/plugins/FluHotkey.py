import keyboard

from PySide6.QtCore import Signal, QObject, Property

# pyright: reportRedeclaration=none


# noinspection PyPep8Naming
class FluHotkey(QObject):
    sequenceChanged = Signal()
    nameChanged = Signal()
    isRegisteredChanged = Signal()
    activated = Signal()

    def hotkeyCallback(self):
        self.activated.emit()

    def __init__(self):
        QObject.__init__(self)
        self._sequence: str = ""
        self._name: str = ""
        self._isRegistered: bool = False

        def handleSequenceChanged():
            # keyboard.remove_hotkey(self.hotkeyCallback)
            try:
                keyboard.add_hotkey(self._sequence, self.hotkeyCallback)
                self.isRegistered = True  # pyright: ignore[reportAttributeAccessIssue]
            except RuntimeError:
                self.isRegistered = False  # pyright: ignore[reportAttributeAccessIssue]

        self.sequenceChanged.connect(lambda: handleSequenceChanged())

    @Property(bool, notify=isRegisteredChanged)
    def isRegistered(self):
        return self._isRegistered

    @isRegistered.setter
    def isRegistered(self, value: bool):
        self._isRegistered = value
        self.isRegisteredChanged.emit()

    @Property(str, notify=nameChanged)
    def name(self):
        return self._name

    @name.setter
    def name(self, value: str):
        self._name = value
        self.nameChanged.emit()

    @Property(str, notify=sequenceChanged)
    def sequence(self):
        return self._sequence

    @sequence.setter
    def sequence(self, value: str):
        self._sequence = value
        self.sequenceChanged.emit()
