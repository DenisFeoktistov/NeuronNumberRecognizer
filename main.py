from PyQt5.QtWidgets import QApplication


from AppInterfaceClasses.MainAppInterface import MainAppInterface
from AppLogicClasses.MainAppResponder import MainAppResponder
import sys


class App(QApplication):
    def __init__(self, args):
        super().__init__(args)

        self.user_screen_geometry = self.desktop().screenGeometry()

        self.main_app_interface = MainAppInterface(self)
        self.main_app_responder = MainAppResponder(self)

    def start(self):
        self.main_app_responder.start()


if __name__ == "__main__":
    app = App(sys.argv)
    app.start()
    sys.exit(app.exec())
