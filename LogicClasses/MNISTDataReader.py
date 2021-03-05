import numpy as np

MAX_INFO_NUMBER = {"training": int(6e4),
                   "testing": int(1e4)}


class MnistDigitInfo:
    def __init__(self, value=0, matrix=np.array([[0] * 28 for _ in range(28)], dtype=np.uint8)):
        self.value = value
        self.matrix = matrix

    def __str__(self):
        # I think, that this is the best way to show MnistDigitInfo, because it is demonstrative.
        matrix_str = str()
        for row in list(map(lambda row: list(row), self.matrix)):
            matrix_str += "\t".join(map(str, row))
            matrix_str += "\n"
        return f"Value: {self.value}\n" + f"Matrix:\n{matrix_str}"


def read_info(n: int, mode: str):
    check_input_correctness(n, mode)
    return get_nth_info(n, mode)


def check_input_correctness(n: int, mode: str):
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
