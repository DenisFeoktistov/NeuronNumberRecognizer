from __future__ import annotations
from AppFiles.AppLogicClasses.ModeResponders.TrainingModeResponder import TrainModeResponder
import AppFiles.App as App


class MainAppResponder:
    def __init__(self, app: App.App) -> None:
        self.app = app

        self.auto_training_mode_responder = TrainModeResponder(self)

    def set_up(self) -> None:
        self.auto_training_mode_responder.set_up()

        self.app.main_app_interface.main_window.modes_buttons["Automatic testing"].clicked.connect(
            self.app.main_app_interface.set_auto_testing_mode)
        self.app.main_app_interface.main_window.modes_buttons["Manual testing"].clicked.connect(
            self.app.main_app_interface.set_manual_testing_mode)
        self.app.main_app_interface.main_window.modes_buttons["Automatic training"].clicked.connect(
            self.app.main_app_interface.set_auto_training_mode)

    def start(self) -> None:
        self.app.main_app_interface.main_window.show()

        self.app.main_app_interface.main_window.set_auto_training_mode()
        self.auto_training_mode_responder.start()
