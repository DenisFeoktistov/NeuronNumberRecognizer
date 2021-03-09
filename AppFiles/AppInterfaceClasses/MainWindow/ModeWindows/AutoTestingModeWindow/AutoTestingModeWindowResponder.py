from __future__ import annotations

import AppFiles.AppInterfaceClasses.MainWindow.ModeWindows.AutoTestingModeWindow.AutoTestingModeWindow as \
        AutoTestingModeWindow


class AutoTestingModeWindowResponder:
    def __init__(self, window: AutoTestingModeWindow.AutoTestingModeWindow):
        self.window = window

    def show(self):
        pass

    def close(self):
        pass
