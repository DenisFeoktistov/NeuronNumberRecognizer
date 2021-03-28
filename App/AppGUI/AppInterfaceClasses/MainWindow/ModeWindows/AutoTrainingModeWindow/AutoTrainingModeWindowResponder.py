from __future__ import annotations

import App.AppGUI.AppInterfaceClasses.MainWindow.ModeWindows.AutoTrainingModeWindow.AutoTrainingModeWindow as \
    AutoTrainingModeWindow
import App.AppGUI.AppInterfaceClasses.MainWindow.ModeWindows.SubsidiaryFiles.AutoModeTemplateWindowResponder as \
    AutoModeTemplateWindowResponder


class AutoTrainingModeWindowResponder(AutoModeTemplateWindowResponder.AutoModeTemplateWindowResponder):
    def __init__(self, window: AutoTrainingModeWindow.AutoTrainingModeWindow) -> None:
        super().__init__(window)

    def set_up(self) -> None:
        pass
