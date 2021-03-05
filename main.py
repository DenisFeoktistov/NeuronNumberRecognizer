from PyQt5.QtWidgets import QApplication
from MainWindow import MainWindow
import sys


class App(QApplication):
    def __init__(self, args):
        super().__init__(args)

        self.user_screen_geometry = self.desktop().screenGeometry()
        self.main_window = MainWindow(self)

    def show(self):
        self.main_window.show()


if __name__ == "__main__":
    app = App(sys.argv)
    app.show()
    sys.exit(app.exec())
