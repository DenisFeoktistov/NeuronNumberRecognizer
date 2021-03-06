from PyQt5.QtCore import QTimer
from LogicClasses.MNISTDataReader import get_random_info


class TrainModeResponder:
    MIN_INTERVAL = 10
    MAX_INTERVAL = 1000

    def __init__(self, main_app_responder):
        self.main_app_responder = main_app_responder

        self.timer = QTimer()
        self.timer.timeout.connect(self.switch)

    def start(self):
        self.main_app_responder.app.main_window.show()

        self.update_timer()

    def update_timer(self):
        coefficient = self.main_app_responder.app.main_window.main_window_responder.get_switch_speed_coefficient()
        if coefficient == 1:
            self.timer.stop()
        else:
            interval = TrainModeResponder.MIN_INTERVAL + (
                        TrainModeResponder.MAX_INTERVAL - TrainModeResponder.MIN_INTERVAL) * coefficient
            self.timer.setInterval(interval)
            self.timer.start()

    def switch(self):
        info = get_random_info("training")
        self.main_app_responder.app.main_window.main_window_responder.set_up_new_info(info)
