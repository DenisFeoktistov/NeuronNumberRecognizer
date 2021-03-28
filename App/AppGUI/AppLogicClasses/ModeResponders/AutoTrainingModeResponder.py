from __future__ import annotations

import App.AppGUI.AppLogicClasses.ModeResponders.AutoModeTemplateResponder as AutoModeTemplateResponder
import App.AppGUI.AppLogicClasses.MainAppResponder as MainAppResponder


class AutoTrainingModeResponder(AutoModeTemplateResponder.AutoModeTemplateResponder):
    def __init__(self, main_app_responder: MainAppResponder.MainAppResponder):
        super().__init__(main_app_responder, "training")

    def start(self) -> None:
        self.main_app_responder.app.main_app_interface.main_window.set_auto_training_mode()
        super().start()
