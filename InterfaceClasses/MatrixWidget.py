from PyQt5.QtWidgets import QPushButton, QMainWindow
import numpy as np


class MatrixWidget:
    MIN_BRIGHTNESS = 40

    def __init__(self, window: QMainWindow, x=0, y=0, width=300, height=300, cols=28, rows=28):
        self.window = window
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.cols = cols
        self.rows = rows

        self.gaps_between_line = 0
        self.button_width = (self.width - self.gaps_between_line * (cols - 1)) / self.cols
        self.button_height = (self.height - self.gaps_between_line * (cols - 1)) / self.rows

        self.matrix = np.array([[0] * self.rows for _ in range(self.cols)], dtype=np.uint8)
        self.buttons = np.array(
            [[QPushButton(parent=self.window) for __ in range(self.rows)] for _ in range(self.cols)],
            dtype=QPushButton)

        for row in self.buttons:
            for button in row:
                button.resize(self.button_width, self.button_height)

        self.move(x, y)
        self.update()

    def move(self, x, y):
        for i in range(self.cols):
            for j in range(self.rows):
                self.buttons[i][j].move(x + i * self.width / self.cols, y + j * self.height / self.rows)
            print()

    def update(self):
        for i in range(self.cols):
            for j in range(self.rows):
                color = max(MatrixWidget.MIN_BRIGHTNESS, self.matrix[i][j])
                self.buttons[i][j].setStyleSheet(f"background-color: rgb{tuple([color for _ in range(3)])}")

    def set_matrix(self, matrix: np.array):
        self.cols = matrix.shape[0]
        self.rows = matrix.shape[1]

        self.matrix = matrix
        self.update()
