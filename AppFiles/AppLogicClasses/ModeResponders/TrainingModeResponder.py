from __future__ import annotations
from PyQt5.QtCore import QTimer


from AppFiles.AppLogicClasses.SubsidiaryFiles.MNISTDataReader import get_random_info
import AppFiles.AppLogicClasses.MainAppResponder as MainAppResponder


class TrainModeResponder:
    MIN_INTERVAL = 10
    MAX_INTERVAL = 1000

    def __init__(self, main_app_responder: MainAppResponder.MainAppResponder) -> None:
        self.main_app_responder = main_app_responder

        self.timer = QTimer()
        self.timer.timeout.connect(self.switch)

    def start(self) -> None:
        self.main_app_responder.app.main_app_interface.training_mode_window.show()
        self.main_app_responder.app.main_app_interface.training_mode_window.next_button.clicked.connect(self.switch)
        self.switch()

        self.update_timer()

    def update_timer(self) -> None:
        coefficient = self.main_app_responder.app.main_app_interface.training_mode_window.responder.get_switch_speed_coefficient()
        if coefficient == 0:
            self.timer.stop()
        else:
            interval = TrainModeResponder.MAX_INTERVAL - (
                    TrainModeResponder.MAX_INTERVAL - TrainModeResponder.MIN_INTERVAL) * coefficient
            self.timer.setInterval(interval)
            self.timer.start()

    def switch(self) -> None:
        info = get_random_info("training")
        self.main_app_responder.app.main_app_interface.training_mode_window.responder.set_up_new_info(info)
        self.main_app_responder.app.main_app_interface.training_mode_window.slider.valueChanged.connect(self.update_timer)
