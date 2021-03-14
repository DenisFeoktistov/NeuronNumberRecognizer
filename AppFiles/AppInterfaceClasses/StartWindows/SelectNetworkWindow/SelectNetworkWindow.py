from __future__ import annotations
from PyQt5.QtWidgets import QMainWindow, QScrollArea, QPushButton, QWidget, QVBoxLayout, QScrollBar

import AppFiles.AppInterfaceClasses.MainAppInterface as MainAppInterface


class Container(QWidget):
    def __init__(self):
        super().__init__()
        self.setLayout(QVBoxLayout())

    def add_widget(self, widget: QWidget):
        widget.setParent(self)
        self.layout().addWidget(widget)


class MainScrollArea(QScrollArea):
    def __init__(self, parent: QMainWindow):
        super().__init__(parent=parent)
        self.container = Container()
        self.setWidget(self.container)

    def add_widget(self, widget: QWidget):
        self.set_up_widget(widget)
        self.container.add_widget(widget)

    @staticmethod
    def set_up_widget(widget: QWidget):
        widget.setFixedHeight(100)
        widget.setStyleSheet("border: 3px solid black; border-radius: 10px; font-size: 20px; font-weight: 500")


class SelectNetworkWindow(QMainWindow):
    REL_WIDTH, REL_HEIGHT = 0.3, 0.5

    def __init__(self, main_app_interface: MainAppInterface.MainAppInterface) -> None:
        super().__init__()

        self.main_app_interface = main_app_interface

        self.scroll_area = MainScrollArea(parent=self)

        self.width = int(self.main_app_interface.app.user_screen_geometry.width() * SelectNetworkWindow.REL_WIDTH)
        self.height = int(self.main_app_interface.app.user_screen_geometry.height() * SelectNetworkWindow.REL_HEIGHT)

        self.set_up_window()
        self.set_up_scroll_area()

        # test
        for i in range(50):
            button = QPushButton()
            button.setText(str(i) + "\n" + str(i + 1))
            button.resize(self.width * 7 // 10, 50)

            self.scroll_area.add_widget(button)

    def set_up_window(self) -> None:
        self.setFixedSize(self.width, self.height)
        self.move(self.main_app_interface.app.user_screen_geometry.width() * (1 - SelectNetworkWindow.REL_WIDTH) / 2,
                  self.main_app_interface.app.user_screen_geometry.height() * (1 - SelectNetworkWindow.REL_HEIGHT) / 2)
        self.setWindowTitle('Select neural network')
        self.setStyleSheet('background : rgb(170, 170, 170)')

    def set_up_scroll_area(self) -> None:
        self.scroll_area.setFixedSize(self.width * 8 // 10, self.height * 9 // 10)
        self.scroll_area.move(self.width // 10, self.height // 20)
        self.scroll_area.setWidgetResizable(True)
        self.scroll_area.setViewportMargins(10, 0, 30, 0)
        self.scroll_area.setStyleSheet("border: 1px solid black")
        self.scroll_area.verticalScrollBar().setStyleSheet("""
                                QScrollBar {
                                    background: rgb(150, 150, 150);
                                    border: 0px solid black;
                                }
                                QScrollBar::handle {
                                    background: rgb(235, 195, 80);
                                    border: 2px solid rgb(70, 70, 70);
                                    border-radius: 5px;
                                }
                                """)
