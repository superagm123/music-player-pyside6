from PySide6.QtCore import Signal, QObject


class MusicPlayerSignals(QObject):
    songInfoChanged = Signal(object)
    songDurationChanged = Signal(int)
    songPositionChanged = Signal(int)