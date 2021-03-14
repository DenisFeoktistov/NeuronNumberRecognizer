from __future__ import annotations
import AppFiles.App as App
from AppFiles.AppInterfaceClasses.MainWindow.MainWindow import MainWindow
from AppFiles.AppInterfaceClasses.StartWindows.SelectNetworkWindow.SelectNetworkWindow import SelectNetworkWindow


class MainAppInterface:
    def __init__(self, app: App.App) -> None:
        self.app = app
        self.main_window = MainWindow(self)
        self.select_network_window = SelectNetworkWindow(self)

    def set_up(self) -> None:
        self.main_window.set_up()
