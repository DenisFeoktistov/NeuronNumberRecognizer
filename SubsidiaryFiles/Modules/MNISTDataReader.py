from random import randint
import numpy as np
from typing import Union

MAX_INFO_NUMBER = {"training": int(6e4),
                   "testing": int(1e4)}


class MnistDigitInfo:
    def __init__(self, value: Union[int, float] = 0,
                 matrix: np.array = np.array([[0] * 28 for _ in range(28)], dtype=np.uint8)) -> None:
        self.value = value
        self.matrix = matrix

    def __str__(self) -> str:
        # I think, that this is the best way to show MnistDigitInfo, because it is demonstrative.
        matrix_str = str()
        for row in list(map(lambda row: list(row), self.matrix)):
            matrix_str += "\t".join(map(str, row))
            matrix_str += "\n"
        return f"Value: {self.value}\n" + f"Matrix:\n{matrix_str}"


def read_info(n: int, mode: str) -> MnistDigitInfo:
    check_input_correctness(n, mode)
    return get_nth_info(n, mode)


def check_input_correctness(n: int, mode: str) -> None:
    if mode not in MAX_INFO_NUMBER.keys():
        raise Exception(f"Incorrect mode! Possible modes: {', '.join(MAX_INFO_NUMBER.keys())}. Input: {mode}.")
    if n < 0 or n >= MAX_INFO_NUMBER[mode]:
        Exception(f"Wrong info number! Max possible: {MAX_INFO_NUMBER[mode]}. Input: {n}.")


def get_nth_info(n: int, mode: str) -> MAX_INFO_NUMBER:
    labels_file = open(f"data/mnist/{mode}_labels", "rb")
    images_file = open(f"data/mnist/{mode}_images", "rb")

    labels_file_indent = 8  # special info at the start of the file, that we don't need
    images_file_indent = 16  # special info at the start of the file, that we don't need

    images_bytes_for_block = 28 * 28
    labels_bytes_for_block = 1

    images_file.seek(images_file_indent + images_bytes_for_block * n)
    labels_file.seek(labels_file_indent + labels_bytes_for_block * n)

    digit_info = MnistDigitInfo()

    digit_info.value = ord(labels_file.read(1))
    for i in range(28):
        for j in range(28):
            digit_info.matrix[j][i] = ord(images_file.read(1))

    labels_file.close()
    images_file.close()

    return digit_info


def get_random_info(mode: str) -> MnistDigitInfo:
    n = randint(0, MAX_INFO_NUMBER[mode] - 1)
    try:
        return get_nth_info(n, mode)
    except Exception as e:
        # I found out, that something goes wrong sometimes, so I want to catch an error
        print(f"Something went wrong with n = {n}..." + "\n" + str(e))
        return get_random_info(mode)
