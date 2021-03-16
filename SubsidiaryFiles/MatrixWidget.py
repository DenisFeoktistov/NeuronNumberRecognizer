from PyQt5.QtWidgets import QPushButton, QMainWindow, QWidget
from PyQt5 import QtGui, QtCore
import numpy as np
from math import sqrt
from typing import Union


class MatrixWidget(QWidget):
    MIN_BRIGHTNESS = 40
    MAX_BRIGHTNESS = 230
    MAX_WIDTH = 1.75
    MIN_WIDTH = 1.25

    pictureChanged = QtCore.pyqtSignal()

    def __init__(self, parent: QMainWindow, x: int = 0, y: int = 0,
                 width: int = 300, height: int = 300, cols: int = 28,
                 rows: int = 28, draw_mode: bool = False) -> None:
        super().__init__(parent=parent)
        self.draw_mode = draw_mode

        self.setMouseTracking(True)

        self.parent = parent
        self.x = int(x)
        self.y = int(y)
        self.width = int(width)
        self.height = int(height)
        self.cols = cols
        self.rows = rows

        self.button_width = self.width // self.cols + 1
        self.button_height = self.height // self.rows + 1

        self.matrix = np.array([[0] * self.cols for _ in range(self.rows)], dtype=np.uint8)
        self.buttons = np.array(
            [[QPushButton(parent=self.parent) for __ in range(self.cols)] for _ in range(self.rows)],
            dtype=QPushButton)

        for row in self.buttons:
            for button in row:
                button.resize(self.button_width, self.button_height)
                self.stackUnder(button)
                button.setEnabled(False)

        self.resize(self.width, self.height)
        self.move(self.x, self.y)
        self.update()

    def set_draw_line_coefficient(self, draw_line_coefficient: float):
        draw_line_coefficient = min(1., max(0., draw_line_coefficient))
        self.line_width = MatrixWidget.MIN_WIDTH + (
                MatrixWidget.MAX_WIDTH - MatrixWidget.MIN_WIDTH) * draw_line_coefficient

    def set_draw_mode(self, draw_mode: bool) -> None:
        self.draw_mode = draw_mode

    def move(self, x: int, y: int) -> None:
        self.x = x
        self.y = y
        super().move(x, y)
        for i in range(self.cols):
            for j in range(self.rows):
                self.buttons[i][j].move(x + i * self.width // self.cols, y + j * self.height // self.rows)

    def resize(self, width: int, height: int) -> None:
        super().resize(width, height)
        self.width = width
        self.height = height
        self.move(self.x, self.y)  # yes, move also work as resizer

    def update(self) -> None:
        for i in range(self.cols):
            for j in range(self.rows):
                color = max(MatrixWidget.MIN_BRIGHTNESS, self.matrix[i][j])
                self.matrix[i][j] = color
                color2 = MatrixWidget.MIN_BRIGHTNESS - 20
                self.buttons[i][j].setStyleSheet(
                    f"background-color: rgb{tuple([color for _ in range(3)])}; "
                    f"border: 1px solid rgb{tuple([color2] * 3)}")

    def set_matrix(self, matrix: np.array) -> None:
        self.cols = matrix.shape[0]
        self.rows = matrix.shape[1]

        self.matrix = matrix
        self.update()

    def clear(self):
        self.matrix = np.array([[0] * self.rows for _ in range(self.cols)], dtype=np.uint8)
        self.update()

    def set_color(self, i, j, color):
        if 0 <= i < self.rows and 0 <= j < self.cols:
            self.matrix[i][j] = max(self.matrix[i][j], color)
            color = self.matrix[i][j]
            color2 = MatrixWidget.MIN_BRIGHTNESS - 20
            self.buttons[i][j].setStyleSheet(f"background: rgb{tuple([color] * 3)};"
                                             f"border: 1px solid rgb{tuple([color2] * 3)}")

    def mouseMoveEvent(self, e: QtGui.QMouseEvent) -> None:
        if self.draw_mode:
            if 0 <= e.x() < self.width and 0 <= e.y() < self.height and e.buttons():
                i, j = self.get_indexes_by_coords(e.x(), e.y())
                self.draw_point_in_coords(i, j)
                self.pictureChanged.emit()

    def mousePressEvent(self, e: QtGui.QMouseEvent) -> None:
        if self.draw_mode:
            i, j = self.get_indexes_by_coords(e.x(), e.y())

            self.draw_point_in_coords(i, j)
            self.pictureChanged.emit()

    def draw_point_in_coords(self, i: int, j: int):
        temp2 = (int(self.line_width) + 1) // 2
        for i1 in range(i - temp2, i + temp2 + 1):
            for j1 in range(j - temp2, j + temp2 + 1):
                delta_i = abs(i - i1)
                delta_j = abs(j - j1)
                color = int(
                    MatrixWidget.MIN_BRIGHTNESS + (MatrixWidget.MAX_BRIGHTNESS - MatrixWidget.MIN_BRIGHTNESS) * min(
                        1, self.line_width - delta_i - delta_j))
                self.set_color(i1, j1, color)

    def get_indexes_by_coords(self, x: int, y: int):
        i = int(x // self.button_width)
        j = int(y // self.button_height)
        return i, j
