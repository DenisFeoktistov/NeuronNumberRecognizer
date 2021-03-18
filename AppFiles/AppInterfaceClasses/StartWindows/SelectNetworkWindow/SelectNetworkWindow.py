from __future__ import annotations
from PyQt5.QtWidgets import QMainWindow, QScrollArea, QPushButton, QWidget, QVBoxLayout

import AppFiles.AppInterfaceClasses.MainAppInterface as MainAppInterface
from SubsidiaryFiles.Classes.Network import get_all_primary_info


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
        self.add_new_button()

        self.add_widgets()

    def show(self) -> None:
        super().show()

        self.clear()
        self.add_widgets()

    def clear(self) -> None:
        self.scroll_area.clear()

    def set_up(self) -> None:
        self.new_button.clicked.connect(self.main_app_interface.app.main_app_responder.add_new_network_start)

    def set_up_window(self) -> None:
        self.setFixedSize(self.width, self.height)
        self.move(self.main_app_interface.app.user_screen_geometry.width() * (1 - SelectNetworkWindow.REL_WIDTH) / 2,
                  self.main_app_interface.app.user_screen_geometry.height() * (1 - SelectNetworkWindow.REL_HEIGHT) / 2)
        self.setWindowTitle('Select neural network')
        self.setStyleSheet('background : rgb(170, 170, 170)')

    def set_up_scroll_area(self) -> None:
        self.scroll_area.setFixedSize(self.width * 8 // 10, self.height * 8 // 10)
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
                                    border: 3px solid rgb(70, 70, 70);
                                    border-radius: 5px;
                                }
                                """)

    def add_new_button(self) -> None:
        self.new_button = QPushButton(parent=self, text="Add new network")
        self.new_button.resize(self.width // 2, self.height // 10)
        self.new_button.move(self.width // 2 - self.new_button.width() // 2,
                             self.height * 39 // 40 - self.new_button.height())
        font_size = self.height // 20
        self.new_button.setStyleSheet(
            f"font-size: {font_size}px; background: rgb(235, 195, 80); border: 2px solid black; "
            f"border-radius: 5px; color: rgb(0, 0, 0)")

    def add_widgets(self) -> None:
        for d in get_all_primary_info():
            new_widget = NetworkInfoButton(name=d["name"], iterations=d["iterations"],
                                           height=self.height // 10,
                                           width=self.width)
            self.scroll_area.add_widget(new_widget)
            new_widget.clicked.connect(self.select_event)

    def select_event(self) -> None:
        self.main_app_interface.app.main_app_responder.select_network_event(self.sender().name)


class MainScrollArea(QScrollArea):
    def __init__(self, parent: QMainWindow) -> None:
        super().__init__(parent=parent)
        self.container = Container()
        self.setWidget(self.container)

    def add_widget(self, widget: QWidget) -> None:
        self.set_up_widget(widget)
        self.container.add_widget(widget)

    def clear(self) -> None:
        self.container.clear()

    @staticmethod
    def set_up_widget(widget: QWidget) -> None:
        widget.setFixedHeight(100)
        widget.setStyleSheet(
            "border: 3px solid black; border-radius: 10px; font-size: 20px; font-weight: 700; background: rgb(150, 150, 150); color: black")


class Container(QWidget):
    def __init__(self) -> None:
        super().__init__()
        self.setLayout(QVBoxLayout())

    def add_widget(self, widget: QWidget) -> None:
        widget.setParent(self)
        self.layout().addWidget(widget)

    def clear(self) -> None:
        for i in reversed(range(self.layout().count())):
            self.layout().itemAt(i).widget().setParent(None)


class NetworkInfoButton(QPushButton):
    def __init__(self, name: str, iterations: int, height: int, width: int) -> None:
        super().__init__()

        self.name = name
        self.iterations = iterations
        self.width = width
        self.height = height

        self.setText(f"Name: {self.name}\n"
                     f"Iterations: {self.iterations}")
        self.resize(self.width, self.height)

    def resize(self, width: int, height: int) -> None:
        self.width = width
        self.height = height
        super().resize(self.width, self.height)

        font_size = self.height // 5
        self.setStyleSheet(f"font-size: {font_size}px; color: black")
