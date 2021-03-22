import math
import numpy as np


def activation_function(x: np.ndarray) -> np.ndarray:
    return 1 / (1 + math.e ** (-x))


def process_color_matrix(x: np.ndarray) -> np.ndarray:
    return x / 255


def derivative_of_activation_function(x: np.ndarray) -> np.ndarray:
    return activation_function(x) * activation_function(1 - activation_function(x))


def cost_function(output: np.ndarray, correct: np.ndarray) -> np.ndarray:
    return 0.5 * (output - correct) ** 2


def derivative_of_cost_function(output: np.ndarray, correct: np.ndarray) -> np.ndarray:
    print("Output: ", output.ravel())
    print("Correct: ", correct.ravel())
    return output - correct
