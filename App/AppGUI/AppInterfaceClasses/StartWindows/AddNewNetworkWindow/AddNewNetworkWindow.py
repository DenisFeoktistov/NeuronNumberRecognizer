from __future__ import annotations

from PyQt5.QtWidgets import QMainWindow, QPushButton, QLineEdit
from PyQt5.QtCore import Qt
import App.AppGUI.AppInterfaceClasses.MainAppInterface as MainAppInterface
import App.AppGUI.AppInterfaceClasses.StartWindows.AddNewNetworkWindow.AddNewNetworkWindowResponder as AddNewNetworkWindowResponder


class AddNewNetworkWindow(QMainWindow):
    REL_WIDTH, REL_HEIGHT = 0.3, 0.2

    def __init__(self, main_app_interface: MainAppInterface.MainAppInterface) -> None:
        super().__init__()

        self.main_app_interface = main_app_interface
        self.responder = AddNewNetworkWindowResponder.AddNewNetworkWindowResponder(self)

        self.width = int(self.main_app_interface.app.user_screen_geometry.width() * AddNewNetworkWindow.REL_WIDTH)
        self.height = int(self.main_app_interface.app.user_screen_geometry.height() * AddNewNetworkWindow.REL_HEIGHT)

        self.set_up_window()
        self.add_name_line()
        self.add_create_button()

    def set_up(self) -> None:
        self.create_button.clicked.connect(self.responder.add_network)

    def set_up_window(self) -> None:
        self.setFixedSize(self.width, self.height)
        self.move(self.main_app_interface.app.user_screen_geometry.width() * (1 - AddNewNetworkWindow.REL_WIDTH) / 2,
                  self.main_app_interface.app.user_screen_geometry.height() * (1 - AddNewNetworkWindow.REL_HEIGHT) / 2)
        self.setWindowTitle('Add new network')
        self.setStyleSheet('background : rgb(170, 170, 170)')

    def add_name_line(self) -> None:
        self.name_line = QLineEdit(parent=self)
        self.name_line.resize(self.width * 3 // 4, self.height // 3)
        self.name_line.move(self.width // 2 - self.name_line.width() // 2, self.height // 8)
        font_size = self.height // 6
        self.name_line.setStyleSheet(
            f"font-color: black; border: 3px solid black; font-size: {font_size}px; background: rgb(190, 190, 190);")
        self.name_line.setAttribute(Qt.WA_MacShowFocusRect, False)

    def add_create_button(self) -> None:
        self.create_button = QPushButton(parent=self, text="Add new network")
        self.create_button.resize(self.width // 2, self.height // 3)
        self.create_button.move(self.width // 2 - self.create_button.width() // 2,
                                self.height * 3 // 5)
        font_size = self.height // 10
        self.create_button.setStyleSheet(
            f"font-size: {font_size}px; background: rgb(235, 195, 80); border: 2px solid black; "
            f"border-radius: 5px; color: rgb(0, 0, 0)")

    def set_error(self) -> None:
        self.name_line.setText("Incorrect name!")

    def show(self) -> None:
        super().show()
        self.name_line.setText("")
