from __future__ import annotations


import AppFiles.AppInterfaceClasses.MainWindow.ModeWindows.SubsidiaryFiles.AutoModeTemplateWindow as \
        AutoModeTemplateWindow


class AutoModeTemplateWindowResponder:
    def __init__(self, window: AutoModeTemplateWindow.AutoModeTemplateWindow) -> None:
        self.window = window

    def show(self) -> None:
        pass

    def close(self) -> None:
        pass
