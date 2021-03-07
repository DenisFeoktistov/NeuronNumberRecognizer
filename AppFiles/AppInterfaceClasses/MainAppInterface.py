from __future__ import annotations
from AppFiles.AppInterfaceClasses.ModeWindows.TraininngModeWindow.TrainingModeWindow import TrainingModeWindow
import AppFiles.App as App


class MainAppInterface:
    def __init__(self, app: App.App):
        self.app = app
        self.training_mode_window = TrainingModeWindow(self)
