from __future__ import annotations

import AppFiles.AppInterfaceClasses.MainWindow.ModeWindows.AutoTestingModeWindow.AutoTestingModeWindow as \
    AutoTestingModeWindow
import AppFiles.AppInterfaceClasses.MainWindow.ModeWindows.SubsidiaryFiles.AutoModeTemplateWindowResponder as \
    AutoModeTemplateWindowResponder


class AutoTestingModeWindowResponder(AutoModeTemplateWindowResponder.AutoModeTemplateWindowResponder):
    def __init__(self, window: AutoTestingModeWindow.AutoTestingModeWindow) -> None:
        super().__init__(window)

    def set_up(self) -> None:
        pass
