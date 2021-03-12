from __future__ import annotations
from PyQt5.QtCore import QTimer
import random

from AppFiles.AppLogicClasses.SubsidiaryFiles.MNISTDataReader import get_random_info
import AppFiles.AppLogicClasses.MainAppResponder as MainAppResponder


class AutoModeTemplateResponder:
    MIN_INTERVAL = 10
    MAX_INTERVAL = 1000

    def __init__(self, main_app_responder: MainAppResponder.MainAppResponder, mode: str) -> None:
        self.main_app_responder = main_app_responder
        self.mode = mode

        self.timer = QTimer()
        self.timer.timeout.connect(self.switch)

    def set_up(self) -> None:
        self.main_app_responder.app.main_app_interface.main_window.next_button.clicked.connect(self.switch)

    def start(self) -> None:
        self.switch()

        self.update_timer()

    def update_timer(self) -> None:
        coefficient = self.main_app_responder.app.main_app_interface.main_window.responder.get_switch_speed_coefficient()
        if coefficient == 0:
            self.timer.stop()
        else:
            interval = AutoModeTemplateResponder.MAX_INTERVAL - (
                    AutoModeTemplateResponder.MAX_INTERVAL - AutoModeTemplateResponder.MIN_INTERVAL) * coefficient
            self.timer.setInterval(interval)
            self.timer.start()

    def switch(self) -> None:
        info = get_random_info(self.mode)
        answer = [random.random() for _ in range(10)]
        self.main_app_responder.app.main_app_interface.main_window.responder.set_up_new_info(info)
        self.main_app_responder.app.main_app_interface.main_window.responder.set_up_network_answer(answer)
        self.main_app_responder.app.main_app_interface.main_window.slider.valueChanged.connect(
            self.update_timer)

    def close(self) -> None:
        self.timer.stop()
