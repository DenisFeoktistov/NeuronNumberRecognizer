from PyQt5.QtWidgets import QApplication
from typing import Any


from AppFiles.AppInterfaceClasses.MainAppInterface import MainAppInterface
from AppFiles.AppLogicClasses.MainAppResponder import MainAppResponder


class App(QApplication):
    def __init__(self, args: Any) -> None:
        super(App, self).__init__(args)

        self.user_screen_geometry = self.desktop().screenGeometry()

        self.main_app_interface = MainAppInterface(self)
        self.main_app_responder = MainAppResponder(self)

    def set_up(self):
        self.main_app_interface.set_up()
        self.main_app_responder.set_up()

    def start(self) -> None:
        self.set_up()
        self.main_app_responder.start()
