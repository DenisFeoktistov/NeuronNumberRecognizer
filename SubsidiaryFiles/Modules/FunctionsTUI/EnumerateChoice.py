def enumerate_choice(options, primary_text, select_text, error_text, input_text):
    print(primary_text)

    print(select_text)
    for i, option in enumerate(options):
        print(f"\tOption {i + 1}: {option}")
    print()
    inp = input(input_text)
    while not (inp.isdigit() and int(inp) in range(1, len(options) + 1)):
        print(error_text)
        inp = input(input_text)
    return int(inp) - 1
