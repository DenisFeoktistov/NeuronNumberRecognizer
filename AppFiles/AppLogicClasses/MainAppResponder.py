from __future__ import annotations
from AppFiles.AppLogicClasses.ModeResponders.TrainingModeResponder import TrainModeResponder
import AppFiles.App as App


class MainAppResponder:
    def __init__(self, app: App.App):
        self.app = app

        self.training_mode_responder = TrainModeResponder(self)

    def start(self):
        self.training_mode_responder.start()
