from __future__ import annotations
from AppFiles.AppLogicClasses.SubsidiaryFiles.MNISTDataReader import MnistDigitInfo
import AppFiles.AppInterfaceClasses.MainWindow.MainWindow


class MainWindowResponder:
    MIN_VALUE = 0
    MAX_VALUE = 100
    INIT_VALUE = 50

    def __init__(self, window: AppFiles.AppInterfaceClasses.MainWindow.MainWindow) -> None:
        self.window = window

    def end_set_up(self) -> None:
        self.window.slider.setMaximum(MainWindowResponder.MAX_VALUE)
        self.window.slider.setMinimum(MainWindowResponder.MIN_VALUE)
        self.window.slider.setValue(MainWindowResponder.INIT_VALUE)

    def get_switch_speed_coefficient(self) -> float:
        return (self.window.slider.value() / (
                MainWindowResponder.MAX_VALUE - MainWindowResponder.MIN_VALUE)) ** 0.5

    def set_up_new_info(self, info: MnistDigitInfo) -> None:
        self.window.matrix_widget.set_matrix(info.matrix)
        self.window.digit_label.setText(str(info.value))

    def set_up_network_answer(self, answer: list) -> None:
        for i, neuron_widget in enumerate(self.window.neuron_widgets):
            neuron_widget.set_value(answer[i])

        self.window.neural_network_answer_label.setText(str(answer.index(max(answer))))
