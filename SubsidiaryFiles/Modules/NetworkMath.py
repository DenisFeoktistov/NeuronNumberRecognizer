import math
import numpy as np


def activation_function(x: np.ndarray) -> np.ndarray:
    return 1 / (1 + math.e ** (-x))


def process_color_matrix(x: np.ndarray) -> np.ndarray:
    return x / 255


def derivative_of_activation_function(x: np.ndarray) -> np.ndarray:
    return activation_function(x) * activation_function(1 - activation_function(x))
