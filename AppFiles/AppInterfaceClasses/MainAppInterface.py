from __future__ import annotations
import AppFiles.App as App
from AppFiles.AppInterfaceClasses.MainWindow.MainWindow import MainWindow
from AppFiles.AppInterfaceClasses.StartWindows.SelectNetworkWindow.SelectNetworkWindow import SelectNetworkWindow
from AppFiles.AppInterfaceClasses.StartWindows.AddNewNetworkWindow.AddNewNetworkWindow import AddNewNetworkWindow
from AppFiles.AppInterfaceClasses.StartWindows.SelectInterfaceWindow.SelectInterfaceWindow import SelectInterfaceWindow


class MainAppInterface:
    def __init__(self, app: App.App) -> None:
        self.app = app
        self.main_window = MainWindow(self)

        self.select_network_window = SelectNetworkWindow(self)
        self.select_interface_window = SelectInterfaceWindow(self)
        self.add_new_network_window = AddNewNetworkWindow(self)

    def set_up(self) -> None:
        self.main_window.set_up()

        self.select_network_window.set_up()
        self.add_new_network_window.set_up()
        self.select_interface_window.set_up()
