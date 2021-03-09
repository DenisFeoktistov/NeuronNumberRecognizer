from __future__ import annotations
from AppFiles.AppLogicClasses.ModeResponders.TrainingModeResponder import TrainModeResponder
import AppFiles.App as App


class MainAppResponder:
    def __init__(self, app: App.App) -> None:
        self.app = app

        self.training_mode_responder = TrainModeResponder(self)

    def set_up(self):
        self.app.main_app_interface.main_window.modes_buttons["Automatic testing"].clicked.connect(
            self.app.main_app_interface.main_window.set_auto_testing_mode)
        self.app.main_app_interface.main_window.modes_buttons["Manual testing"].clicked.connect(
            self.app.main_app_interface.main_window.set_manual_testing_mode)
        self.app.main_app_interface.main_window.modes_buttons["Automatic training"].clicked.connect(
            self.app.main_app_interface.main_window.set_training_mode)

    def start(self) -> None:
        self.app.main_app_interface.show()
        self.training_mode_responder.start()
