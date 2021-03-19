import math


def activation_function(x: float) -> float:
    return 1 / (1 + math.e ** (-x))


def derivative_of_activation_function(x: float) -> float:
    return activation_function(x) * activation_function(1 - activation_function(x))

