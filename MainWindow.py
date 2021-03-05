from PyQt5.QtWidgets import QMainWindow


class MainWindow(QMainWindow):
    REL_WIDTH, REL_HEIGHT = 0.9, 0.8

    def __init__(self, app):
        super().__init__()

        self.app = app
        self.initUI()

    def initUI(self):
        self.setFixedSize(self.app.user_screen_geometry.width() * MainWindow.REL_WIDTH,
                          self.app.user_screen_geometry.height() * MainWindow.REL_HEIGHT)
        self.move(self.app.user_screen_geometry.width() * (1 - MainWindow.REL_WIDTH) / 2,
                  self.app.user_screen_geometry.height() * (1 - MainWindow.REL_HEIGHT) / 2)
        self.setWindowTitle('Perceptron')
        self.setStyleSheet('background : rgb(170, 170, 170)')
