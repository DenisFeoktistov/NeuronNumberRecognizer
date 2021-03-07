from PyQt5.QtWidgets import QMainWindow, QSlider, QLabel, QPushButton
from PyQt5.QtCore import Qt
from random import random, choice

from AppFiles.AppInterfaceClasses.SubsidiaryClasses.MatrixWidget import MatrixWidget
from AppFiles.AppInterfaceClasses.ModeWindows.TraininngModeWindow.TrainingModeWindowResponder import \
    TrainingModeWindowResponder
from AppFiles.AppInterfaceClasses.SubsidiaryClasses.NeuronWidget import NeuronWidget


class TrainingModeWindow(QMainWindow):
    OUTPUTS = 10
    REL_WIDTH, REL_HEIGHT = 0.9, 0.8

    def __init__(self, main_app_interface):
        super().__init__()
        self.main_app_interface = main_app_interface
        self.responder = TrainingModeWindowResponder(self)

        self.width = self.main_app_interface.app.user_screen_geometry.width() * TrainingModeWindow.REL_WIDTH
        self.height = self.main_app_interface.app.user_screen_geometry.height() * TrainingModeWindow.REL_HEIGHT

        self.matrix_widget = MatrixWidget(parent=self, **self.get_matrix_widget_params())

        self.slider = QSlider(orientation=Qt.Vertical, parent=self)

        self.slider_label = QLabel(text="Switch speed", parent=self)

        # self.digit_text_label = QLabel(parent=self, text="Digit:")
        self.digit_label = QLabel(parent=self)

        self.next_button = QPushButton(parent=self, text="Next")

        self.neural_network_answer_label = QLabel(parent=self, text="Neural network answer")

        self.neuron_widgets = [NeuronWidget(parent=self) for _ in range(TrainingModeWindow.OUTPUTS)]
        self.arrows_labels = [QLabel(parent=self) for _ in range(TrainingModeWindow.OUTPUTS)]
        self.digit_labels = [QLabel(parent=self) for _ in range(TrainingModeWindow.OUTPUTS)]
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
        self.set_up_neural_network_answer_label()
        self.set_up_neuron_widgets_arrows_and_digit_labels()
        # self.set_up_digit_text_label()

    def set_up_neuron_widgets_arrows_and_digit_labels(self):
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

            self.arrows_labels[i].setText("➔")
            self.arrows_labels[i].setStyleSheet("font-size: 40px")
            self.arrows_labels[i].resize(2 * radius, 2 * radius)
            self.arrows_labels[i].setAlignment(Qt.AlignCenter)

            self.digit_labels[i].setText(str(i))
            self.digit_labels[i].setStyleSheet("font-size: 50px")
            self.digit_labels[i].resize(2 * radius, 2 * radius)

    def set_up_neural_network_answer_label(self):
        matrix_height = self.matrix_widget.height
        matrix_width = self.matrix_widget.width

        self.neural_network_answer_label.move(self.width // 2 + matrix_width // 2,
                                              self.height // 2 - matrix_height // 2 - self.height // 10)
        self.neural_network_answer_label.resize(self.width // 2 - matrix_width // 2, self.height // 10)
        self.neural_network_answer_label.setAlignment(Qt.AlignCenter)
        self.neural_network_answer_label.setStyleSheet("font-size: 40px")

    def set_up_next_button(self):
        self.next_button.move(self.slider.geometry().x() - self.height // 40,
                              self.height // 2 + self.slider.geometry().y() // 2)
        self.next_button.resize(self.slider.geometry().width() + self.height // 20, self.height // 20)
        self.next_button.setStyleSheet("font-size: 25px; background: rgb(235, 195, 80); border-radius: 5px")

    def set_up_digit_text_label(self):
        matrix_height = self.matrix_widget.height
        matrix_width = self.matrix_widget.width

        self.digit_text_label.setAlignment(Qt.AlignCenter)
        self.digit_text_label.setStyleSheet("font-size: 25px")
        self.digit_text_label.move(self.width // 2 - matrix_width // 2,
                                   self.height // 2 + matrix_height // 2)
        self.digit_text_label.resize(matrix_width, self.height // 15)

    def set_up_digit_label(self):
        matrix_height = matrix_width = self.height * 0.5

        self.digit_label.setAlignment(Qt.AlignCenter)
        self.digit_label.setStyleSheet("font-size: 80px; border: 1px solid black")
        self.digit_label.move(self.width // 2 - matrix_width // 2,
                              self.height // 2 + matrix_height // 2 + self.height // 15)
        self.digit_label.resize(matrix_width, self.height // 10)

    def set_up_window(self):
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

        width = 50
        height = matrix_height * 4 // 7
        self.slider.move(self.width // 2 - matrix_width // 2 - self.width // 15, self.height // 2 - height // 2)
        self.slider.resize(width, height)
        self.slider.setStyleSheet("""
                    QSlider::handle {
                        background: rgb(235, 195, 80);
                        border: 1px solid rgb(70, 70, 70);
                        width: 20px;
                        height: 24px;
                        margin: -6px; 
                        border-radius: 12px;
                    }
                    QSlider::groove {
                        width: 12px;
                        margin: 5px 0;
                        background: rgb(200, 200, 200);
                        border: 1px solid black;
                        border-radius: 5px;
                    }
                    QSlider::sub-page {
                        width: 12px;
                        margin: 5px 0;
                        background: rgb(130, 130, 130);
                        border: 1px solid black;
                        border-radius: 5px;
                    }
                """)

    def set_up_slider_label(self):
        matrix_height = self.matrix_widget.height
        matrix_width = self.matrix_widget.width

        slider_height = self.slider.height()
        self.slider_label.setAlignment(Qt.AlignLeft | Qt.AlignCenter)
        self.slider_label.move(self.width // 2 - matrix_width // 2 - self.width // 13,
                               self.height // 2 - slider_height // 2 - self.height // 25)
        self.slider_label.adjustSize()
        self.slider_label.setStyleSheet("background-color: transparent")
