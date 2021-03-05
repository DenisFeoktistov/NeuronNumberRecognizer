from PyQt5.QtWidgets import QMainWindow
from InterfaceClasses.MatrixWidget import MatrixWidget
from MNISTDataReader import read_info
from random import randint


class MainWindow(QMainWindow):
    REL_WIDTH, REL_HEIGHT = 0.9, 0.8

    def __init__(self, app):
        super().__init__()
        self.app = app

        self.width = self.app.user_screen_geometry.width() * MainWindow.REL_WIDTH
        self.height = self.app.user_screen_geometry.height() * MainWindow.REL_HEIGHT

        self.matrix_widget = MatrixWidget(window=self, **self.get_matrix_widget_params())

        # test ------------------------------------------------------------
        n = randint(0, int(6e4))
        self.matrix_widget.set_matrix(read_info(n, mode="training").matrix)
        # test ------------------------------------------------------------

        self.initUI()

    def initUI(self):
        self.setFixedSize(self.width, self.height)
        self.move(self.app.user_screen_geometry.width() * (1 - MainWindow.REL_WIDTH) / 2,
                  self.app.user_screen_geometry.height() * (1 - MainWindow.REL_HEIGHT) / 2)
        self.setWindowTitle('Perceptron')
        self.setStyleSheet('background : rgb(170, 170, 170)')

    def get_matrix_widget_params(self):
        width = height = self.height * 0.5

        res = dict()
        res["width"] = width
        res["height"] = height
        res["x"] = self.width / 2 - width / 2
        res["y"] = self.height / 2 - height / 2
        return res
