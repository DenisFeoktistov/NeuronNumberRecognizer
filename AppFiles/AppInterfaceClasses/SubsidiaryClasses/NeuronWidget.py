from PyQt5.QtWidgets import QPushButton, QLabel
from PyQt5.QtCore import Qt


class NeuronWidget:
    def __init__(self, parent, value=0, x=0, y=0, radius=0):
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
        self.label.setStyleSheet("font-size: 15px; background: transparent")

        self.update()

    def move(self, x, y):
        self.x = x
        self.y = y
        self.label.move(self.x + self.radius // 2, self.y + self.radius // 2)
        self.circle.move(self.x, self.y)

    def resize(self, radius):
        self.radius = radius
        self.circle.resize(self.radius * 2, self.radius * 2)
        self.label.resize(self.radius, self.radius)
        self.move(self.x, self.y)

    def set_value(self, value):
        self.value = min(1, max(0, value))
        self.update()

    def update(self):
        self.label.setText(str(round(self.value, ndigits=2)))
        self.color = self.get_gradient()
        self.circle.setStyleSheet(
            f"border-radius: {self.radius}px; border: 3px solid black; background: rgb{self.color}")

    def get_gradient(self):
        # if self.value < 0.5:
        #     r = 0
        # elif 0.5 < self.value < 0.59:
        #     r = 255 * (0.59 - self.value) / (0.59 - 0.5)
        # else:
        #     r = 255
        #
        # if self.value < 0.5:
        #     g = self.value / 0.5 * 255
        # else:
        #     g = (1 - self.value) / 0.5 * 255
        #
        # if self.value > 0.5:
        #     b = 0
        # else:
        #     b = (0.5 - self.value) / 0.5 * 255
        # r = 255
        # g = (1 - self.value) * 255
        # b = 0
        r = 235
        g = (195 - 120) * (1 - self.value) + 120
        b = 80

        r, g, b = max(0, r), max(0, g), max(0, b)
        print("Value: ", self.value)
        print("R: ", r)
        print("G: ", g)
        print("B: ", b)
        return r, g, b
