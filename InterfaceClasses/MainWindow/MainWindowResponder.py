from InterfaceClasses.MainWindow import MainWindow
from PyQt5.QtCore import QTimer
from LogicClasses.MNISTDataReader import read_info
from random import randint


class MainWindowResponder:
    MIN_INTERVAL = 100
    MAX_INTERVAL = 1000

    def __init__(self, main_window: MainWindow):
        self.main_window = main_window

        self.timer = QTimer(self.main_window)
        self.timer.timeout.connect(self.update_matrix)

    def end_set_up(self):
        self.main_window.slider.setMaximum(100)
        self.main_window.slider.setMinimum(1)
        self.main_window.slider.setValue(1)

        self.update_interval()

    def update_interval(self):
        if self.main_window.slider.value() == 100:
            self.timer.stop()
        else:
            interval = (MainWindowResponder.MIN_INTERVAL + (
                    MainWindowResponder.MAX_INTERVAL - MainWindowResponder.MIN_INTERVAL) *
                             self.main_window.slider.value() // 100)
            self.timer.setInterval(interval)
            self.timer.start()

    def update_matrix(self):
        n = randint(0, 60000)
        self.main_window.matrix_widget.set_matrix(read_info(n, mode="training").matrix)
