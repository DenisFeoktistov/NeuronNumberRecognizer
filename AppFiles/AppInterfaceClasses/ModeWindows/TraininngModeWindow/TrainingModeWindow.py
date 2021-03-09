from __future__ import annotations
from PyQt5.QtWidgets import QMainWindow, QSlider, QLabel, QPushButton
from PyQt5.QtCore import Qt
from random import random, choice

from AppFiles.AppInterfaceClasses.SubsidiaryClasses.MatrixWidget import MatrixWidget
from AppFiles.AppInterfaceClasses.ModeWindows.TraininngModeWindow.TrainingModeWindowResponder import \
    TrainingModeWindowResponder
from AppFiles.AppInterfaceClasses.SubsidiaryClasses.NeuronWidget import NeuronWidget
import AppFiles.AppInterfaceClasses.MainAppInterface as MainAppInterface


class TrainingModeWindow(QMainWindow):
    OUTPUTS = 10
    REL_WIDTH, REL_HEIGHT = 0.9, 0.8

    def __init__(self, main_app_interface: MainAppInterface.MainAppInterface) -> None:
        super(TrainingModeWindow, self).__init__()
        self.main_app_interface = main_app_interface
        self.responder = TrainingModeWindowResponder(self)

        self.width = self.main_app_interface.app.user_screen_geometry.width() * TrainingModeWindow.REL_WIDTH
        self.height = self.main_app_interface.app.user_screen_geometry.height() * TrainingModeWindow.REL_HEIGHT
        self.height = min(self.height, self.width * 2 // 3)

        self.matrix_widget = MatrixWidget(parent=self, **self.get_matrix_widget_params())

        self.slider = QSlider(orientation=Qt.Vertical, parent=self)

        self.slider_label = QLabel(text="Switch speed", parent=self)

        # self.digit_text_label = QLabel(parent=self, text="Digit:")
        self.digit_label = QLabel(parent=self)

        self.next_button = QPushButton(parent=self, text="Next")

        self.neural_network_answer_text_label = QLabel(parent=self, text="Neural network answer")

        self.neuron_widgets = [NeuronWidget(parent=self) for _ in range(TrainingModeWindow.OUTPUTS)]
        self.arrows_labels = [QLabel(parent=self, text="➔") for _ in range(TrainingModeWindow.OUTPUTS)]
        self.digit_labels = [QLabel(parent=self, text=str(i)) for i in range(TrainingModeWindow.OUTPUTS)]

        self.modes_buttons = dict([(mode, QLabel(parent=self)) for mode in ["Automatic training", "Automatic testing", "Manual testing"]])

        self.neural_network_answer_label = QLabel(parent=self)
        self.initUI()

        self.responder.end_set_up()

    def initUI(self) -> None:
        # Order of calls is important, because some of methods dependent on other. It is bad, I think, but I don't
        # think that it is fatal error.
        self.set_up_window()
        self.set_up_slider()
        self.set_up_slider_label()

        self.set_up_digit_label()
        self.set_up_next_button()
        self.set_up_neural_network_answer_text_label()
        self.set_up_neuron_widgets_arrows_and_digit_labels()
        self.set_up_neural_network_answer_label()

        self.set_up_modes_buttons()

    def set_up_modes_buttons(self):
        top = self.height * 0.35
        bottom = self.height * 0.65
        width = self.width * 0.25

        font_size = int(self.height / 7 / len(self.modes_buttons))

        step = (bottom - top) / len(self.modes_buttons)
        for i, key in enumerate(self.modes_buttons.keys()):
            self.modes_buttons[key].setText(key)
            self.modes_buttons[key].move(self.width * 0.01, top + step * i)
            self.modes_buttons[key].resize(width, step)
            self.modes_buttons[key].setAlignment(Qt.AlignCenter)
            self.modes_buttons[key].setStyleSheet(f"font-size: {font_size}px;")

    def set_up_neural_network_answer_label(self) -> None:
        bottom = self.digit_labels[0].geometry().y()
        top = self.digit_labels[TrainingModeWindow.OUTPUTS - 1].geometry().y() + self.digit_labels[
            TrainingModeWindow.OUTPUTS - 1].geometry().height()

        left = self.digit_labels[0].geometry().x() + self.digit_labels[0].geometry().width() + self.width // 40
        right = self.width - self.width // 40
        self.neural_network_answer_label.move(left, bottom)
        self.neural_network_answer_label.resize(right - left, top - bottom)
        self.neural_network_answer_label.setAlignment(Qt.AlignCenter)

        font_size = int(self.height // 4 * TrainingModeWindow.REL_HEIGHT)
        self.neural_network_answer_label.setStyleSheet(f"font-size: {font_size}px;")

    def set_up_neuron_widgets_arrows_and_digit_labels(self) -> None:
        top_y = self.height // 2 - self.matrix_widget.height // 2
        step = (self.height - top_y) / TrainingModeWindow.OUTPUTS
        radius = step * 0.9 // 2

        for i in range(TrainingModeWindow.OUTPUTS):
            # test ---------------------------------
            value = random()
            # test ---------------------------------
            self.neuron_widgets[i].move(self.width // 2 + self.matrix_widget.width // 2 + self.width // 20,
                                        top_y + step * i)
            self.neuron_widgets[i].resize(radius)
            self.neuron_widgets[i].set_value(value)

            self.digit_labels[i].move(self.width // 2 + self.matrix_widget.width // 2 + 3 * self.width // 20,
                                      top_y + step * i)
            self.arrows_labels[i].move(self.width // 2 + self.matrix_widget.width // 2 + 2 * self.width // 20,
                                       top_y + step * i)

            font_size1 = int(self.height // 20 * TrainingModeWindow.REL_HEIGHT)
            self.arrows_labels[i].setStyleSheet(f"font-size: {font_size1}px")
            self.arrows_labels[i].resize(2 * radius, 2 * radius)
            self.arrows_labels[i].setAlignment(Qt.AlignCenter)

            font_size2 = int(self.height // 15 * TrainingModeWindow.REL_HEIGHT)
            self.digit_labels[i].setStyleSheet(f"font-size: {font_size2}px")
            self.digit_labels[i].resize(radius, 2 * radius)
            self.digit_labels[i].setAlignment(Qt.AlignCenter)

    def set_up_neural_network_answer_text_label(self) -> None:
        matrix_height = self.matrix_widget.height
        matrix_width = self.matrix_widget.width

        self.neural_network_answer_text_label.move(self.width // 2 + matrix_width // 2,
                                                   self.height // 2 - matrix_height // 2 - self.height // 10)
        self.neural_network_answer_text_label.resize(self.width // 2 - matrix_width // 2, self.height // 10)
        self.neural_network_answer_text_label.setAlignment(Qt.AlignCenter)
        font_size = int(self.height // 20 * TrainingModeWindow.REL_HEIGHT)
        self.neural_network_answer_text_label.setStyleSheet(f"font-size: {font_size}px")

    def set_up_next_button(self) -> None:
        self.next_button.move(self.slider.geometry().x() - self.width // 80,
                              self.height // 2 + self.slider.geometry().y() // 2)
        self.next_button.resize(self.slider.geometry().width() + self.width // 40, self.height // 20)
        font_size = int(self.height // 27 * TrainingModeWindow.REL_HEIGHT)
        self.next_button.setStyleSheet(f"font-size: {font_size}px; background: rgb(235, 195, 80); border-radius: 5px")

    def set_up_digit_text_label(self) -> None:
        matrix_height = self.matrix_widget.height
        matrix_width = self.matrix_widget.width

        self.digit_text_label.setAlignment(Qt.AlignCenter)
        font_size = int(self.height // 27 * TrainingModeWindow.REL_HEIGHT)
        self.digit_text_label.setStyleSheet(f"font-size: {font_size}px")
        self.digit_text_label.move(self.width // 2 - matrix_width // 2,
                                   self.height // 2 + matrix_height // 2)
        self.digit_text_label.resize(matrix_width, self.height // 15)

    def set_up_digit_label(self) -> None:
        matrix_height = matrix_width = self.height * 0.5

        self.digit_label.setAlignment(Qt.AlignCenter)
        font_size = int(self.height // 10 * TrainingModeWindow.REL_HEIGHT)
        self.digit_label.setStyleSheet(f"font-size: {font_size}px; border: 1px solid black")
        self.digit_label.move(self.width // 2 - matrix_width // 2,
                              self.height // 2 + matrix_height // 2 + self.height // 15)
        self.digit_label.resize(matrix_width, self.height // 10)

    def set_up_window(self) -> None:
        self.setFixedSize(self.width, self.height)
        self.move(self.main_app_interface.app.user_screen_geometry.width() * (1 - TrainingModeWindow.REL_WIDTH) / 2,
                  self.main_app_interface.app.user_screen_geometry.height() * (1 - TrainingModeWindow.REL_HEIGHT) / 2)
        self.setWindowTitle('Perceptron')
        self.setStyleSheet('background : rgb(170, 170, 170)')

    def get_matrix_widget_params(self) -> dict:
        width = height = self.height * 0.5

        res = dict()
        res["width"] = width
        res["height"] = height
        res["x"] = self.width / 2 - width / 2
        res["y"] = self.height / 2 - height / 2
        return res

    def set_up_slider(self) -> None:
        matrix_height = self.matrix_widget.height
        matrix_width = self.matrix_widget.width

        width = self.width // 30 * TrainingModeWindow.REL_WIDTH
        height = matrix_height * 4 // 7

        width1 = height1 = int(self.height // 30 * TrainingModeWindow.REL_WIDTH)
        border_radius1 = width1 // 2
        margin1 = -border_radius1 // 2

        width2 = int(self.height // 50 * TrainingModeWindow.REL_WIDTH)
        border_radius2 = margin2 = width2 // 2

        self.slider.move(self.width // 2 - matrix_width // 2 - self.width // 15, self.height // 2 - height // 2)
        self.slider.resize(width, height)
        self.slider.setStyleSheet("""
                    QSlider::handle {
                        background: rgb(235, 195, 80);
                        border: 2px solid rgb(70, 70, 70);
                        width: """ + str(width1) + """px;
                        height: """ + str(height1) + """px;
                        margin: """ + str(margin1) + """px; 
                        border-radius: """ + str(border_radius1) + """px;
                    }
                    QSlider::groove {
                        width: """ + str(width2) + """px;
                        height: """ + str(height * 0.9) + """px;
                        background: rgb(200, 200, 200);
                        border: 1px solid black;
                        border-radius: """ + str(border_radius2) + """px;
                    }
                    QSlider::sub-page {
                        background: rgb(130, 130, 130);
                        border: 1px solid black;
                        border-radius: """ + str(border_radius2) + """px;
                    }
                """)

    def set_up_slider_label(self) -> None:
        matrix_height = self.matrix_widget.height
        matrix_width = self.matrix_widget.width

        slider_height = self.slider.height()
        self.slider_label.setAlignment(Qt.AlignLeft | Qt.AlignCenter)
        self.slider_label.move(self.slider.geometry().x() - self.width // 80,
                               self.slider.geometry().y() - self.height // 20)
        self.slider_label.resize(self.slider.width() + self.width // 40, self.height // 20)
        font_size = int(self.height // 50 * TrainingModeWindow.REL_HEIGHT)
        self.slider_label.setAlignment(Qt.AlignCenter)
        self.slider_label.setStyleSheet(f"font-size: {font_size}px; background-color: transparent")
