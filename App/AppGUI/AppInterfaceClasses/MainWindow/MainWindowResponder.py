from __future__ import annotations
from SubsidiaryFiles.Modules.MNISTDataReader import MnistDigitInfo
import App.AppGUI.AppInterfaceClasses.MainWindow.MainWindow as MainWindow


class MainWindowResponder:
    def __init__(self, window: MainWindow.MainWindow) -> None:
        self.window = window

    def show(self):
        name = self.window.main_app_interface.app.network.name
        batches = self.window.main_app_interface.app.network.batches
        template = self.window.main_app_interface.app.network.template
        self.window.set_name(name)
        self.window.set_batches(batches)
        self.window.set_template(template)

    def set_up(self) -> None:
        pass

    def set_up_new_info(self, info: MnistDigitInfo) -> None:
        self.window.matrix_widget.set_matrix(info.matrix)
        self.window.digit_label.setText(str(info.value))

    def set_up_network_answer(self, answer: list) -> None:
        for i, neuron_widget in enumerate(self.window.neuron_widgets):
            neuron_widget.set_value(answer[i])

        self.window.neural_network_answer_label.setText(str(answer.index(max(answer))))

    def close(self) -> None:
        self.window.main_app_interface.app.main_app_responder.close_main_window()