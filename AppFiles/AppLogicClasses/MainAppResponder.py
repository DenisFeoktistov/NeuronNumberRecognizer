from __future__ import annotations
import AppFiles.AppLogicClasses.ModeResponders.AutoTrainingModeResponder as AutoTrainingModeResponder
import AppFiles.AppLogicClasses.ModeResponders.AutoTestingModeResponder as AutoTestingModeResponder
import AppFiles.AppLogicClasses.ModeResponders.ManualTestingModeResponder as ManualTestingModeResponder
import AppFiles.App as App


class MainAppResponder:
    def __init__(self, app: App.App) -> None:
        self.app = app

        self.auto_training_mode_responder = AutoTrainingModeResponder.AutoTrainingModeResponder(self)
        self.auto_testing_mode_responder = AutoTestingModeResponder.AutoTestingModeResponder(self)
        self.manual_testing_mode_responder = ManualTestingModeResponder.ManualTestingModeResponder(self)

    def set_up(self) -> None:
        self.auto_training_mode_responder.set_up()
        self.auto_testing_mode_responder.set_up()
        self.manual_testing_mode_responder.set_up()

        self.app.main_app_interface.main_window.modes_buttons["Automatic testing"].clicked.connect(
            self.set_auto_testing_mode)
        self.app.main_app_interface.main_window.modes_buttons["Manual testing"].clicked.connect(
            self.set_manual_testing_mode)
        self.app.main_app_interface.main_window.modes_buttons["Automatic training"].clicked.connect(
            self.set_auto_training_mode)

    def start(self) -> None:
        self.app.main_app_interface.select_network_window.show()

    def set_auto_testing_mode(self) -> None:
        self.auto_training_mode_responder.close()
        self.manual_testing_mode_responder.close()

        self.auto_testing_mode_responder.start()

    def set_auto_training_mode(self) -> None:
        self.auto_testing_mode_responder.close()
        self.manual_testing_mode_responder.close()

        self.auto_training_mode_responder.start()

    def set_manual_testing_mode(self) -> None:
        self.auto_testing_mode_responder.close()
        self.auto_training_mode_responder.close()

        self.manual_testing_mode_responder.start()

    def add_new_network_finish(self) -> None:
        self.app.main_app_interface.add_new_network_window.close()
        self.app.main_app_interface.select_network_window.show()

    def add_new_network_start(self) -> None:
        self.app.main_app_interface.select_network_window.close()
        self.app.main_app_interface.add_new_network_window.show()

    def select_network_event(self, name) -> None:
        self.app.main_app_interface.select_network_window.close()

        self.app.network.set_network(name)

        self.app.main_app_interface.main_window.show()
        self.set_auto_training_mode()

    def close_main_window(self) -> None:
        self.app.main_app_interface.main_window.close()
        self.app.main_app_interface.select_network_window.show()
        self.app.network.save_changes()
