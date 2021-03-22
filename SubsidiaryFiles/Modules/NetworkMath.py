import math
import numpy as np


def activation_function(x: np.ndarray) -> np.ndarray:
    return 1.0 / (1.0 + np.exp(-x))


def process_color_matrix(x: np.ndarray) -> np.ndarray:
    return x / 255


def derivative_of_activation_function(x: np.ndarray) -> np.ndarray:
    return activation_function(x) * (1 - activation_function(x))


# def cost_function(output: np.ndarray, correct: np.ndarray) -> np.ndarray:
#     return 0.5 * (output - correct) ** 2


def derivative_of_cost_function(output: np.ndarray, correct: np.ndarray) -> np.ndarray:
    return output - correct
