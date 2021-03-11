from __future__ import annotations
import AppFiles.App as App
from AppFiles.AppInterfaceClasses.MainWindow.MainWindow import MainWindow


class MainAppInterface:
    def __init__(self, app: App.App) -> None:
        self.app = app
        self.main_window = MainWindow(self)

    def set_up(self) -> None:
        pass

    def show(self) -> None:
        self.main_window.set_auto_training_mode()

    def set_auto_training_mode(self) -> None:
        self.main_window.set_auto_training_mode()

    def set_auto_testing_mode(self) -> None:
        self.main_window.set_auto_testing_mode()

    def set_manual_testing_mode(self) -> None:
        self.main_window.set_manual_testing_mode()
