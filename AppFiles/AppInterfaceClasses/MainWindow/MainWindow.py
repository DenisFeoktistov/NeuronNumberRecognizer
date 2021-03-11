from __future__ import annotations
from PyQt5.QtWidgets import QMainWindow, QSlider, QLabel, QPushButton
from PyQt5.QtCore import Qt

from AppFiles.AppInterfaceClasses.MainWindow.SubsidiaryClasses.MatrixWidget import MatrixWidget
from AppFiles.AppInterfaceClasses.MainWindow.MainWindowResponder import MainWindowResponder
from AppFiles.AppInterfaceClasses.MainWindow.SubsidiaryClasses.NeuronWidget import NeuronWidget

import AppFiles.AppInterfaceClasses.MainAppInterface as MainAppInterface
import AppFiles.AppInterfaceClasses.MainWindow.ModeWindows.AutoTrainingModeWindow.AutoTrainingModeWindow as TrainingModeWindow
import AppFiles.AppInterfaceClasses.MainWindow.ModeWindows.ManualTestingModeWindow.ManualTestingModeWiindow as \
    ManualTestingModeWindow
import AppFiles.AppInterfaceClasses.MainWindow.ModeWindows.AutoTestingModeWindow.AutoTestingModeWindow as \
    AutoTestingModeWindow


class MainWindow(QMainWindow):
    OUTPUTS = 10
    REL_WIDTH, REL_HEIGHT = 0.9, 0.8

    def __init__(self, main_app_interface: MainAppInterface.MainAppInterface) -> None:
        super(MainWindow, self).__init__()
        self.main_app_interface = main_app_interface
        self.responder = MainWindowResponder(self)

        self.width = self.main_app_interface.app.user_screen_geometry.width() * MainWindow.REL_WIDTH
        self.height = self.main_app_interface.app.user_screen_geometry.height() * MainWindow.REL_HEIGHT
        self.height = min(self.height, self.width * 2 // 3)

        self.set_up_window()
        self.add_widgets()

        self.auto_training_mode_window = TrainingModeWindow.AutoTrainingModeWindow(self)
        self.auto_testing_mode_window = AutoTestingModeWindow.AutoTestingModeWindow(self)
        self.manual_testing_mode_window = ManualTestingModeWindow.ManualTestingModeWindow(self)

        self.finish_init()

    def finish_init(self) -> None:
        self.next_button.setEnabled(False)
        self.next_button.setVisible(False)

        self.clear_button.setEnabled(False)
        self.clear_button.setVisible(False)

        self.switch_speed_label.setVisible(False)
        self.line_width_label.setVisible(False)

        self.digit_label.setVisible(False)

        for label in self.outlines_for_modes_buttons.values():
            label.setVisible(False)
        self.responder.finish_init()

    def set_up(self) -> None:
        self.auto_training_mode_window.set_up()
        self.auto_testing_mode_window.set_up()
        self.manual_testing_mode_window.set_up()
        self.responder.set_up()

    def set_auto_testing_mode(self) -> None:
        self.manual_testing_mode_window.close()
        self.auto_training_mode_window.close()

        self.auto_testing_mode_window.show()

    def set_manual_testing_mode(self) -> None:
        self.auto_training_mode_window.close()
        self.auto_testing_mode_window.close()

        self.manual_testing_mode_window.show()

    def set_auto_training_mode(self) -> None:
        self.manual_testing_mode_window.close()
        self.auto_testing_mode_window.close()

        self.auto_training_mode_window.show()

    def set_up_window(self) -> None:
        self.setFixedSize(self.width, self.height)
        self.move(self.main_app_interface.app.user_screen_geometry.width() * (1 - MainWindow.REL_WIDTH) / 2,
                  self.main_app_interface.app.user_screen_geometry.height() * (1 - MainWindow.REL_HEIGHT) / 2)
        self.setWindowTitle('Perceptron')
        self.setStyleSheet('background : rgb(170, 170, 170)')

    # Further only graphics initialization
    # ------------------------------------
    def add_widgets(self):
        self.add_matrix_widget()

        self.add_slider()

        # Yes, this buttons will be absolutely same, but it is design coincidence, because logically they are not the
        # same. The same situation with next_button and clear button. Actually, with slider too, but I think, that I
        # can leave slider like that.
        self.add_speed_switch_label()
        self.add_line_width_label()

        self.add_digit_label()

        self.add_next_button()
        self.add_clear_button()

        self.add_neural_network_answer_text_label()

        self.add_neuron_widgets_and_digit_labels()

        self.add_mode_buttons_and_outlines()

        self.add_neural_network_answer_label()

    def add_neural_network_answer_label(self):
        self.neural_network_answer_label = QLabel(parent=self)
        bottom = self.digit_labels[0].geometry().y()
        top = self.digit_labels[MainWindow.OUTPUTS - 1].geometry().y() + self.digit_labels[
            MainWindow.OUTPUTS - 1].geometry().height()

        left = self.digit_labels[0].geometry().x() + self.digit_labels[0].geometry().width() + self.width // 40
        right = self.width - self.width // 40
        self.neural_network_answer_label.move(left, bottom)
        self.neural_network_answer_label.resize(right - left, top - bottom)
        self.neural_network_answer_label.setAlignment(Qt.AlignCenter)

        font_size = int(self.height // 4 * MainWindow.REL_HEIGHT)
        self.neural_network_answer_label.setStyleSheet(f"font-size: {font_size}px;")

    def add_mode_buttons_and_outlines(self):
        self.modes_buttons = dict(
            [(mode, QPushButton(parent=self)) for mode in ["Automatic training", "Automatic testing", "Manual testing"]])
        self.outlines_for_modes_buttons = dict(
            [(mode, QLabel(parent=self)) for mode in ["Automatic training", "Automatic testing", "Manual testing"]])

        top = self.height * 0.35
        bottom = self.height * 0.65
        width = self.width * 0.2

        font_size = int(self.height / 9 / len(self.modes_buttons))

        step = (bottom - top) / len(self.modes_buttons)
        for i, key in enumerate(self.modes_buttons.keys()):
            self.modes_buttons[key].setText(key)

            self.modes_buttons[key].move(self.width * 0.01, top + step * i)
            self.modes_buttons[key].resize(width, step)

            border_size = self.height // 400
            self.outlines_for_modes_buttons[key].setStyleSheet(
                f"background: transparent; border: {border_size} solid rgb(235, 195, 80); border-radius: 5px")
            self.outlines_for_modes_buttons[key].move(self.width * 0.01, top + step * i)
            self.outlines_for_modes_buttons[key].resize(width, step)

            self.modes_buttons[key].setStyleSheet(f"border: 0px solid black; font-size: {font_size}px;")

    def add_neuron_widgets_and_digit_labels(self):
        self.neuron_widgets = [NeuronWidget(parent=self) for _ in range(MainWindow.OUTPUTS)]
        self.arrows_labels = [QLabel(parent=self, text="➔") for _ in range(MainWindow.OUTPUTS)]
        self.digit_labels = [QLabel(parent=self, text=str(i)) for i in range(MainWindow.OUTPUTS)]

        top_y = self.height // 2 - self.matrix_widget.height // 2
        step = (self.height - top_y) / MainWindow.OUTPUTS
        radius = step * 0.9 // 2

        for i in range(MainWindow.OUTPUTS):
            self.neuron_widgets[i].move(self.width // 2 + self.matrix_widget.width // 2 + self.width // 20,
                                        top_y + step * i)
            self.neuron_widgets[i].resize(radius)

            self.digit_labels[i].move(self.width // 2 + self.matrix_widget.width // 2 + 3 * self.width // 20,
                                      top_y + step * i)
            self.arrows_labels[i].move(self.width // 2 + self.matrix_widget.width // 2 + 2 * self.width // 20,
                                       top_y + step * i)

            font_size1 = int(self.height // 20 * MainWindow.REL_HEIGHT)
            self.arrows_labels[i].setStyleSheet(f"font-size: {font_size1}px")
            self.arrows_labels[i].resize(2 * radius, 2 * radius)
            self.arrows_labels[i].setAlignment(Qt.AlignCenter)

            font_size2 = int(self.height // 15 * MainWindow.REL_HEIGHT)
            self.digit_labels[i].setStyleSheet(f"font-size: {font_size2}px")
            self.digit_labels[i].resize(radius, 2 * radius)
            self.digit_labels[i].setAlignment(Qt.AlignCenter)

    def add_neural_network_answer_text_label(self):
        self.neural_network_answer_text_label = QLabel(parent=self, text="Neural network answer")
        matrix_height = self.matrix_widget.height
        matrix_width = self.matrix_widget.width

        self.neural_network_answer_text_label.move(self.width // 2 + matrix_width // 2,
                                                   self.height // 2 - matrix_height // 2 - self.height // 10)
        self.neural_network_answer_text_label.resize(self.width // 2 - matrix_width // 2, self.height // 10)
        self.neural_network_answer_text_label.setAlignment(Qt.AlignCenter)
        font_size = int(self.height // 20 * MainWindow.REL_HEIGHT)
        self.neural_network_answer_text_label.setStyleSheet(f"font-size: {font_size}px")

    def add_next_button(self):
        self.next_button = QPushButton(parent=self, text="Next")
        self.set_up_under_slider_button(self.next_button)

    def add_clear_button(self):
        self.clear_button = QPushButton(parent=self, text="Clear")
        self.set_up_under_slider_button(self.clear_button)

    def add_digit_label(self):
        self.digit_label = QLabel(parent=self)

        matrix_width = self.matrix_widget.width
        matrix_height = self.matrix_widget.height

        self.digit_label.setAlignment(Qt.AlignCenter)
        font_size = int(self.height // 10 * MainWindow.REL_HEIGHT)
        self.digit_label.setStyleSheet(f"font-size: {font_size}px; border: 1px solid black")
        self.digit_label.move(self.width // 2 - matrix_width // 2,
                              self.height // 2 + matrix_height // 2 + self.height // 15)
        self.digit_label.resize(matrix_width, self.height // 10)

    def add_speed_switch_label(self):
        self.switch_speed_label = QLabel(parent=self, text="Switch speed")
        self.set_up_slider_label(self.switch_speed_label)

    def add_line_width_label(self):
        self.line_width_label = QLabel(parent=self, text="Line width")
        self.set_up_slider_label(self.line_width_label)

    def add_slider(self):
        self.slider = QSlider(orientation=Qt.Vertical, parent=self)

        matrix_height = self.matrix_widget.height
        matrix_width = self.matrix_widget.width

        width = self.width // 30 * MainWindow.REL_WIDTH
        height = matrix_height * 4 // 7

        width1 = height1 = int(self.height // 30 * MainWindow.REL_WIDTH)
        border_radius1 = width1 // 2
        margin1 = -border_radius1 // 2

        width2 = int(self.height // 50 * MainWindow.REL_WIDTH)
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

    def add_matrix_widget(self):
        width = height = self.height * 0.5

        res = dict()
        x = self.width / 2 - width / 2
        y = self.height / 2 - height / 2
        self.matrix_widget = MatrixWidget(parent=self, x=x, y=y, width=width, height=height)

    def set_up_under_slider_button(self, button: QPushButton) -> None:
        button.move(self.slider.geometry().x() - self.width // 80,
                    self.height // 2 + self.slider.geometry().y() // 2)
        button.resize(self.slider.geometry().width() + self.width // 40, self.height // 20)
        font_size = int(self.height // 27 * MainWindow.REL_HEIGHT)
        button.setStyleSheet(f"font-size: {font_size}px; background: rgb(235, 195, 80); border-radius: 5px")

    def set_up_slider_label(self, label: QLabel) -> None:
        label.setAlignment(Qt.AlignLeft | Qt.AlignCenter)
        label.move(self.slider.geometry().x() - self.width // 80,
                   self.slider.geometry().y() - self.height // 20)
        label.resize(self.slider.width() + self.width // 40, self.height // 20)
        font_size = int(self.height // 50 * MainWindow.REL_HEIGHT)
        label.setAlignment(Qt.AlignCenter)
        label.setStyleSheet(f"font-size: {font_size}px; background-color: transparent")
