from PyQt5.QtWidgets import QPushButton, QLabel


class NeuronWidget:
    MIN_COLOR = (0, 255, 255)
    MAX_COLOR = (255, 69, 0)

    def __init__(self, parent, value=0, x=0, y=0, radius=0):
        self.parent = parent
        self.radius = radius
        self.x = x
        self.y = y

        self.value = min(1, max(0, value))
        self.color = (0, 0, 0)
        self.update_color()

        self.circle = QPushButton(parent=self.parent)
        self.circle.resize(self.radius * 2, self.radius * 2)
        self.circle.setStyleSheet(
            f"border-radius: {self.radius}px; border: 1px solid black; background: rgb{self.color}")
        self.circle.move(self.x, self.y)

        self.label = QLabel(parent=self.parent, text=str(round(self.value, ndigits=2)))
        self.label.move(self.x, self.y)
        self.label.resize(self.radius * 2, self.radius * 2)
        self.label.setStyleSheet("font-size: 30px")

    def move(self, x, y):
        self.x = x
        self.y = y
        self.label.move(self.x, self.y)
        self.circle.move(self.x, self.y)

    def resize(self, radius):
        self.radius = radius
        self.circle.resize(self.radius * 2, self.radius * 2)
        self.label.resize(self.radius * 2, self.radius * 2)

    def set_value(self, value):
        self.value = min(1, max(0, value))
        self.update_color()

    def update_color(self):
        self.color = [NeuronWidget.MIN_COLOR[i] + (NeuronWidget.MAX_COLOR[i] - NeuronWidget.MIN_COLOR[i]) * self.value
                      for i in range(3)]
        self.circle.setStyleSheet(f"background: rgb{self.color}")
