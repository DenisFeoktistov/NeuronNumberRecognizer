from __future__ import annotations
import AppFiles.App as App
from AppFiles.AppInterfaceClasses.MainWindow.MainWindow import MainWindow


class MainAppInterface:
    def __init__(self, app: App.App) -> None:
        self.app = app
        self.main_window = MainWindow(self)

    def set_up(self) -> None:
        self.main_window.set_up()
