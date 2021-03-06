from InterfaceClasses.MainWindow import MainWindow
from PyQt5.QtCore import QTimer
from LogicClasses.MNISTDataReader import MnistDigitInfo
from random import randint


class MainWindowResponder:
    def __init__(self, main_window: MainWindow):
        self.main_window = main_window

    def end_set_up(self):
        self.main_window.slider.setMaximum(100)
        self.main_window.slider.setMinimum(1)
        self.main_window.slider.setValue(50)

    def get_switch_speed_coefficient(self):
        return self.main_window.slider.value() ** 2 // 10000

    def set_up_new_info(self, info: MnistDigitInfo):
        self.main_window.matrix_widget.set_matrix(info.matrix)
