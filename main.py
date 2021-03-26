import sys


from AppFiles.App import App
from TextApp.TextApp import TextApp


GUI, TUI = "gui", "tui"


def select_interface():
    text = "SELECT INTERFACE.\nText interface is intended only for fast network learning. In other cases select GUI.\n"
    input_text = "Graphical interface(0) / Text interface(1): "
    error_message = "\nIncorrect input! Try again."

    print(text)
    answer = input(input_text)
    while answer not in ["0", "1"]:
        print(error_message)
        answer = input(input_text)
    if answer == "0":
        return GUI
    else:
        return TUI


if __name__ == "__main__":
    if select_interface() == GUI:
        app = App(sys.argv)
        app.start()
        sys.exit(app.exec())
    else:
        app = TextApp()
        app.start()
