from __future__ import annotations


import AppFiles.AppInterfaceClasses.MainWindow.ModeWindows.ManualTestingModeWindow.ManualTestingModeWiindow as \
    ManualTestingWindow


class ManualTestingModeWindowResponder:
    def __init__(self, window: ManualTestingWindow.ManualTestingModeWindow):
        self.window = window

    def show(self):
        pass

    def close(self):
        pass
