from __future__ import annotations

import AppFiles.AppInterfaceClasses.MainWindow.ModeWindows.TrainingModeWindow.AutoTrainingModeWindow as \
    TrainingModeWindow


class AutoTrainingModeWindowResponder:
    def __init__(self, window: TrainingModeWindow.AutoTrainingModeWindow) -> None:
        self.window = window

    def show(self) -> None:
        pass

    def close(self) -> None:
        pass
