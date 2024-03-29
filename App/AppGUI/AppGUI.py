from PyQt5.QtWidgets import QApplication
from typing import Any


from App.AppGUI.AppInterfaceClasses.MainAppInterface import MainAppInterface
from App.AppGUI.AppLogicClasses.MainAppResponder import MainAppResponder
from SubsidiaryFiles.Network.Network import Network


class AppGUI(QApplication):
    def __init__(self, args: Any) -> None:
        super().__init__(args)

        self.user_screen_geometry = self.desktop().screenGeometry()

        self.main_app_interface = MainAppInterface(self)
        self.main_app_responder = MainAppResponder(self)
        self.network = Network()

        self.set_up()

    def set_up(self) -> None:
        self.main_app_interface.set_up()
        self.main_app_responder.set_up()

    def start(self) -> None:
        self.main_app_responder.start()
