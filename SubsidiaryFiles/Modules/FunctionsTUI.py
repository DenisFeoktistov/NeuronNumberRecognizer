from typing import List, Union


def enumerate_choice(options: List[str], primary_text: str, select_text: str,
                     error_text: str = "\nIncorrect input! Try again!",
                     input_text: str = "Your choice: ") -> Union[str, dict]:
    print(primary_text)

    print(select_text)
    for i, option in enumerate(options):
        if isinstance(option, str):
            print(f"\tOption {i + 1}: {option}")
        if isinstance(option, dict):
            pairs = list(zip(option.keys(), option.values()))
            print(f"\tOption {i + 1}: {pairs[0][0]}: {pairs[0][1]}")
            for pair in pairs[1:]:
                indent = ' ' * len(f'Option {i + 1}:')
                print(f"\t{indent} {pair[0]}: {pair[1]}")
    print()
    inp = input(input_text)
    while not (inp.isdigit() and int(inp) in range(1, len(options) + 1)):
        print(error_text)
        inp = input(input_text)
    return options[int(inp) - 1]


def make_indent(n: int = 10) -> None:
    print("\n" * n)


def get_int_info(input_text: str, error_text: str = "Incorrect input! Try again."):
    number = input(input_text)
    while not number.isdigit():
        print(error_text)
        number = input(input_text)
    return int(number)
