from __future__ import annotations
from PyQt5.QtWidgets import QMainWindow, QPushButton, QLabel
from PyQt5.QtCore import Qt

import AppFiles.AppInterfaceClasses.MainAppInterface as MainAppInterface


class SelectInterfaceWindow(QMainWindow):
    REL_WIDTH, REL_HEIGHT = 0.3, 0.3

    def __init__(self, main_app_interface: MainAppInterface.MainAppInterface) -> None:
        super().__init__()

        self.main_app_interface = main_app_interface

        self.width = int(self.main_app_interface.app.user_screen_geometry.width() * SelectInterfaceWindow.REL_WIDTH)
        self.height = int(self.main_app_interface.app.user_screen_geometry.height() * SelectInterfaceWindow.REL_HEIGHT)

        self.set_up_window()

        self.add_widgets()

    def set_up(self):
        self.text_button.clicked.connect(self.select_event)
        self.gui_button.clicked.connect(self.select_event)

    def add_widgets(self) -> None:
        self.add_gui_button()
        self.add_text_button()
        self.add_label()

    def add_label(self) -> None:
        text = "Text interface is much better for training,\n because it works much faster than GUI.\n" \
               "I recommend to use GUI for testing."
        self.label = QLabel(parent=self, text=text)
        self.label.move(self.width // 10, self.height // 2)
        self.label.resize(self.width // 10 * 8, self.height // 2)
        self.label.setAlignment(Qt.AlignCenter)
        font_size = self.height // 15
        self.label.setStyleSheet(f"font-size: {font_size}px; font-weight: 300")

    def add_gui_button(self):
        self.gui_button = QPushButton(parent=self, text="Graphical interface")
        self.gui_button.move(self.width // 10, self.height // 7)
        self.gui_button.resize(self.width // 2 - self.width // 20 - self.width // 10, self.height // 4)
        font_size = self.height // 18
        self.gui_button.setStyleSheet(
            f"font-size: {font_size}px; background: rgb(235, 195, 80); border: 2px solid black; "
            f"border-radius: 5px; color: rgb(0, 0, 0); font-weight: 500")

    def add_text_button(self):
        self.text_button = QPushButton(parent=self, text="Text interface")
        self.text_button.move(self.width // 20 + self.width // 2, self.height // 7)
        self.text_button.resize(self.width // 2 - self.width // 20 - self.width // 10, self.height // 4)
        font_size = self.height // 18
        self.text_button.setStyleSheet(
            f"font-size: {font_size}px; background: rgb(235, 195, 80); border: 2px solid black; "
            f"border-radius: 5px; color: rgb(0, 0, 0); font-weight: 500")

    def set_up_window(self) -> None:
        self.setFixedSize(self.width, self.height)
        self.move(self.main_app_interface.app.user_screen_geometry.width() * (1 - SelectInterfaceWindow.REL_WIDTH) / 2,
                  self.main_app_interface.app.user_screen_geometry.height() * (
                          1 - SelectInterfaceWindow.REL_HEIGHT) / 2)
        self.setWindowTitle('Select interface')
        self.setStyleSheet('background : rgb(170, 170, 170)')

    def select_event(self) -> None:
        if self.sender() == self.text_button:
            self.main_app_interface.app.main_app_responder.start_text_interface()
        elif self.sender() == self.gui_button:
            self.main_app_interface.app.main_app_responder.start_gui_interface()

    def closeEvent(self, event) -> None:
        self.main_app_interface.app.main_app_responder.select_interface_window_closed()
