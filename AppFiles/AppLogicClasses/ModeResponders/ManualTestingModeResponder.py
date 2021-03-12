from __future__ import annotations

import AppFiles.AppLogicClasses.MainAppResponder as MainAppResponder


class ManualTestingModeResponder:
    def __init__(self, main_app_responder: MainAppResponder.MainAppResponder) -> None:
        self.main_app_responder = main_app_responder

    def start(self) -> None:
        self.main_app_responder.app.main_app_interface.main_window.set_manual_testing_mode()

    def set_up(self) -> None:
        pass

    def close(self) -> None:
        pass
