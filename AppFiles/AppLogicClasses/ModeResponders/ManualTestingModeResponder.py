from __future__ import annotations

import AppFiles.AppLogicClasses.MainAppResponder as MainAppResponder


class ManualTestingModeResponder:
    def __init__(self, main_app_responder: MainAppResponder.MainAppResponder) -> None:
        self.main_app_responder = main_app_responder

    def start(self) -> None:
        self.main_app_responder.app.main_app_interface.main_window.set_manual_testing_mode()
        self.main_app_responder.app.main_app_interface.main_window.matrix_widget.clear()

    def clear_matrix(self):
        self.main_app_responder.app.main_app_interface.main_window.matrix_widget.clear()

    def set_up(self) -> None:
        self.main_app_responder.app.main_app_interface.main_window.clear_button.clicked.connect(self.clear_matrix)

    def close(self) -> None:
        pass
