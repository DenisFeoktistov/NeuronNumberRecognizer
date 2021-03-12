from __future__ import annotations

import AppFiles.AppLogicClasses.MainAppResponder as MainAppResponder


class ManualTestingModeResponder:
    def __init__(self, main_app_responder: MainAppResponder.MainAppResponder) -> None:
        self.main_app_responder = main_app_responder

    def start(self) -> None:
        self.main_app_responder.app.main_app_interface.main_window.set_manual_testing_mode()
        self.main_app_responder.app.main_app_interface.main_window.matrix_widget.clear()
        self.main_app_responder.app.main_app_interface.main_window.matrix_widget.set_draw_mode(True)

    def clear_matrix(self):
        self.main_app_responder.app.main_app_interface.main_window.matrix_widget.clear()

    def set_up(self) -> None:
        self.main_app_responder.app.main_app_interface.main_window.clear_button.clicked.connect(self.clear_matrix)
        self.main_app_responder.app.main_app_interface.main_window.matrix_widget.pictureChanged.connect(
            self.update_answer)

    def close(self) -> None:
        self.main_app_responder.app.main_app_interface.main_window.matrix_widget.set_draw_mode(False)

    def update_answer(self) -> None:
        pass
