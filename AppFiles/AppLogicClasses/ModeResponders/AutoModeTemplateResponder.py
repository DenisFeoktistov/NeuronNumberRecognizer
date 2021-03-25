from __future__ import annotations
from PyQt5.QtCore import QTimer
import random

from SubsidiaryFiles.Modules.MNISTDataReader import get_random_info
import AppFiles.AppLogicClasses.MainAppResponder as MainAppResponder


class AutoModeTemplateResponder:
    MIN_VALUE = 0
    MAX_VALUE = 100

    MIN_INTERVAL = 1
    MAX_INTERVAL = 1000

    SPEED_INIT_VALUE = 50
    CONNECTED = False

    def __init__(self, main_app_responder: MainAppResponder.MainAppResponder, mode: str) -> None:
        self.main_app_responder = main_app_responder
        self.mode = mode

        self.timer = QTimer()
        self.timer.timeout.connect(self.switch)

    def set_up(self) -> None:
        if not AutoModeTemplateResponder.CONNECTED:
            AutoModeTemplateResponder.CONNECTED = True

            self.main_app_responder.app.main_app_interface.main_window.switch_speed_slider.setMaximum(
                AutoModeTemplateResponder.MAX_VALUE)
            self.main_app_responder.app.main_app_interface.main_window.switch_speed_slider.setMinimum(
                AutoModeTemplateResponder.MIN_VALUE)

            self.main_app_responder.app.main_app_interface.main_window.next_button.clicked.connect(self.switch)
            self.main_app_responder.app.main_app_interface.main_window.switch_speed_slider.valueChanged.connect(
                self.update_timer)
            self.main_app_responder.app.main_app_interface.main_window.switch_speed_slider.setValue(
                AutoModeTemplateResponder.SPEED_INIT_VALUE)

            self.timer.stop()

    def start(self) -> None:
        self.switch()

        self.update_timer()

    def update_timer(self) -> None:
        coefficient = self.get_switch_speed_coefficient()
        if coefficient == 0:
            self.timer.stop()
        else:
            interval = AutoModeTemplateResponder.MAX_INTERVAL - (
                    AutoModeTemplateResponder.MAX_INTERVAL - AutoModeTemplateResponder.MIN_INTERVAL) * coefficient
            self.timer.setInterval(interval)
            self.timer.start()

    def switch(self) -> None:
        info = get_random_info(self.mode)

        self.main_app_responder.app.network.process_matrix(info.matrix, info.value)
        answer = self.main_app_responder.app.network.get_output()
        batches = self.main_app_responder.app.network.batches

        self.main_app_responder.app.main_app_interface.main_window.responder.set_up_new_info(info)
        self.main_app_responder.app.main_app_interface.main_window.responder.set_up_network_answer(answer)
        self.main_app_responder.app.main_app_interface.main_window.set_batches(batches)

    def close(self) -> None:
        self.timer.stop()

    def get_switch_speed_coefficient(self) -> float:
        return (self.main_app_responder.app.main_app_interface.main_window.switch_speed_slider.value() / (
                AutoModeTemplateResponder.MAX_VALUE - AutoModeTemplateResponder.MIN_VALUE)) ** 0.5
