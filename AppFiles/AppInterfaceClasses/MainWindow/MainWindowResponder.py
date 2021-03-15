from __future__ import annotations
from SubsidiaryFiles.MNISTDataReader import MnistDigitInfo
import AppFiles.AppInterfaceClasses.MainWindow.MainWindow as MainWindow
from SubsidiaryFiles.Network import get_info_by_name


class MainWindowResponder:
    MIN_VALUE = 0
    MAX_VALUE = 100
    SPEED_INIT_VALUE = 50
    WIDTH_INIT_VALUE = 50

    def __init__(self, window: MainWindow.MainWindow) -> None:
        self.window = window

    def show(self, name: str):
        info = get_info_by_name(name)
        self.window.set_name(info["name"])
        self.window.set_iterations(info["iterations"])

    def set_up(self) -> None:
        pass

    def finish_init(self) -> None:
        self.window.switch_speed_slider.setMaximum(MainWindowResponder.MAX_VALUE)
        self.window.switch_speed_slider.setMinimum(MainWindowResponder.MIN_VALUE)
        self.window.switch_speed_slider.setValue(MainWindowResponder.SPEED_INIT_VALUE)

        self.window.line_width_slider.setMaximum(MainWindowResponder.MAX_VALUE)
        self.window.line_width_slider.setMinimum(MainWindowResponder.MIN_VALUE)
        self.window.line_width_slider.setValue(MainWindowResponder.WIDTH_INIT_VALUE)

        # test
        self.window.set_name("Main_network")
        self.window.set_iterations(1543)

    def get_switch_speed_coefficient(self) -> float:
        return (self.window.switch_speed_slider.value() / (
                MainWindowResponder.MAX_VALUE - MainWindowResponder.MIN_VALUE)) ** 0.5

    def get_line_width_coefficient(self) -> float:
        return (self.window.line_width_slider.value() / (
                MainWindowResponder.MAX_VALUE - MainWindowResponder.MIN_VALUE))

    def set_up_new_info(self, info: MnistDigitInfo) -> None:
        self.window.matrix_widget.set_matrix(info.matrix)
        self.window.digit_label.setText(str(info.value))

    def set_up_network_answer(self, answer: list) -> None:
        for i, neuron_widget in enumerate(self.window.neuron_widgets):
            neuron_widget.set_value(answer[i])

        self.window.neural_network_answer_label.setText(str(answer.index(max(answer))))
