from __future__ import annotations
from App.AppGUI import AppGUI as App
from App.AppGUI.AppInterfaceClasses.MainWindow.MainWindow import MainWindow
from App.AppGUI.AppInterfaceClasses.StartWindows.SelectNetworkWindow.SelectNetworkWindow import SelectNetworkWindow
from App.AppGUI.AppInterfaceClasses.StartWindows.AddNewNetworkWindow.AddNewNetworkWindow import AddNewNetworkWindow


class MainAppInterface:
    def __init__(self, app: App.App) -> None:
        self.app = app
        self.main_window = MainWindow(self)

        self.select_network_window = SelectNetworkWindow(self)
        self.add_new_network_window = AddNewNetworkWindow(self)

    def set_up(self) -> None:
        self.main_window.set_up()

        self.select_network_window.set_up()
        self.add_new_network_window.set_up()
