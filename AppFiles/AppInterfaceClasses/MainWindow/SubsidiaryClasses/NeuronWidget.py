from PyQt5.QtWidgets import QPushButton, QLabel, QMainWindow
from PyQt5.QtCore import Qt, QRect
from typing import Union, Tuple


class NeuronWidget:
    def __init__(self, parent: QMainWindow, value: Union[int, float] = 0, x: Union[int, float] = 0,
                 y: Union[int, float] = 0, radius: Union[int, float] = 0) -> None:
        self.parent = parent
        self.radius = radius
        self.x = x
        self.y = y

        self.value = min(1, max(0, value))
        self.color = (0, 0, 0)

        self.circle = QPushButton(parent=self.parent)
        self.circle.resize(self.radius * 2, self.radius * 2)
        self.circle.setStyleSheet(
            f"border-radius: {self.radius}px; border: 3px solid black; background: rgb{self.color}")
        self.circle.move(self.x, self.y)
        self.circle.adjustSize()

        self.label = QLabel(parent=self.parent, text=str(round(self.value, ndigits=2)))
        self.label.setAlignment(Qt.AlignCenter)
        self.label.move(self.x + self.radius // 2, self.y + self.radius // 2)
        self.label.resize(self.radius, self.radius)
        self.label.setStyleSheet(f"background: transparent")

        self.update()

    def move(self, x: Union[int, float], y: Union[int, float]) -> None:
        self.x = x
        self.y = y
        self.label.move(self.x + self.radius // 2, self.y + self.radius // 2)
        self.circle.move(self.x, self.y)

    def resize(self, radius: Union[int, float]) -> None:
        self.radius = radius
        self.circle.resize(self.radius * 2, self.radius * 2)
        self.label.resize(self.radius, self.radius)
        self.move(self.x, self.y)
        font_size = int(self.radius / 2)
        self.label.setStyleSheet(f"font-size: {font_size}px; background: transparent; color: rgb(0, 0, 0)")

    def set_value(self, value: Union[int, float]) -> None:
        self.value = min(1, max(0, value))
        self.update()

    def update(self) -> None:
        self.label.setText(str(round(self.value, ndigits=2)))
        self.color = self.get_gradient()
        border_size = int(self.radius / 8)
        self.circle.setStyleSheet(
            f"border-radius: {self.radius}px; border: {border_size}px solid black; background: rgb{self.color}")

    def get_gradient(self) -> Tuple[int, int, int]:
        r = 235
        g = (195 - 120) * (1 - self.value) + 160  # Yes, some of values in this formula aren't described,
        # but it is really hard to do this. All I wanna say is that it is special formula to get orange gradient.
        b = 80

        r, g, b = min(255, max(0, r)), min(255, max(0, g)), min(255, max(0, b))  # these min and max just for be sure
        return r, g, b

    def geometry(self) -> QRect:
        return self.circle.geometry()
