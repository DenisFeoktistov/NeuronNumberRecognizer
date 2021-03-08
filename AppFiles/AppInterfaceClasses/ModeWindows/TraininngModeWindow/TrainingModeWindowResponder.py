from __future__ import annotations
import AppFiles.AppInterfaceClasses.ModeWindows.TraininngModeWindow as TrainingModeWindow
from AppFiles.AppLogicClasses.SubsidiaryFiles.MNISTDataReader import MnistDigitInfo


class TrainingModeWindowResponder:
    MIN_VALUE = 0
    MAX_VALUE = 100
    INIT_VALUE = 50

    def __init__(self, window: TrainingModeWindow.TrainingModeWindow) -> None:
        self.window = window

    def end_set_up(self) -> None:
        self.window.slider.setMaximum(TrainingModeWindowResponder.MAX_VALUE)
        self.window.slider.setMinimum(TrainingModeWindowResponder.MIN_VALUE)
        self.window.slider.setValue(TrainingModeWindowResponder.INIT_VALUE)

    def get_switch_speed_coefficient(self) -> float:
        return (self.window.slider.value() / (
                    TrainingModeWindowResponder.MAX_VALUE - TrainingModeWindowResponder.MIN_VALUE)) ** 0.5

    def set_up_new_info(self, info: MnistDigitInfo) -> None:
        self.window.matrix_widget.set_matrix(info.matrix)
        self.window.digit_label.setText(str(info.value))

    def set_up_network_answer(self, answer: list):
        for i, neuron_widget in enumerate(self.window.neuron_widgets):
            neuron_widget.set_value(answer[i])

        self.window.neural_network_answer_label.setText(str(answer.index(max(answer))))
