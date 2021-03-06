from PyQt5.QtWidgets import QApplication


from AppFiles.AppInterfaceClasses.MainAppInterface import MainAppInterface
from AppFiles.AppLogicClasses.MainAppResponder import MainAppResponder


class App(QApplication):
    def __init__(self, args):
        super().__init__(args)

        self.user_screen_geometry = self.desktop().screenGeometry()

        self.main_app_interface = MainAppInterface(self)
        self.main_app_responder = MainAppResponder(self)

    def start(self):
        self.main_app_responder.start()