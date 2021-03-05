from PyQt5.QtWidgets import QMainWindow, QSlider, QLabel
from PyQt5.QtCore import Qt
from InterfaceClasses.MainWindow.SubsidiaryClasses.MatrixWidget import MatrixWidget
from InterfaceClasses.MainWindow.MainWindowResponder import MainWindowResponder
from LogicClasses.MNISTDataReader import read_info
from random import randint


class MainWindow(QMainWindow):
    REL_WIDTH, REL_HEIGHT = 0.9, 0.8

    def __init__(self, app):
        super().__init__()
        self.app = app
        self.responder = MainWindowResponder(self)

        self.width = self.app.user_screen_geometry.width() * MainWindow.REL_WIDTH
        self.height = self.app.user_screen_geometry.height() * MainWindow.REL_HEIGHT

        self.matrix_widget = MatrixWidget(parent=self, **self.get_matrix_widget_params())

        self.slider = QSlider(orientation=Qt.Vertical, parent=self)
        self.slider.valueChanged.connect(self.responder.update_interval)
        self.set_up_slider()

        self.slider_label = QLabel(text="Switch speed", parent=self)
        self.set_up_slider_label()

        self.initUI()

        self.responder.end_set_up()

    def initUI(self) -> None:
        self.setFixedSize(self.width, self.height)
        self.move(self.app.user_screen_geometry.width() * (1 - MainWindow.REL_WIDTH) / 2,
                  self.app.user_screen_geometry.height() * (1 - MainWindow.REL_HEIGHT) / 2)
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
        matrix_height = matrix_width = self.height * 0.5

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
        matrix_height = matrix_width = self.height * 0.5
        slider_height = matrix_height * 4 // 7
        self.slider_label.setAlignment(Qt.AlignLeft | Qt.AlignCenter)
        self.slider_label.move(self.width // 2 - matrix_width // 2 - self.width // 13,
                               self.height // 2 - slider_height // 2 - self.height // 25)
        self.slider_label.adjustSize()
        self.slider_label.setStyleSheet("background-color: transparent")
