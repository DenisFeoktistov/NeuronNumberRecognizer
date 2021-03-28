from App.AppGUI.AppGUI import AppGUI
from App.AppTUI.AppTUI import AppTUI

from SubsidiaryFiles.Modules.FunctionsTUI.EnumerateChoice import enumerate_choice
from SubsidiaryFiles.Modules.FunctionsTUI.MakeIndent import make_indent


import os


def cls():
    os.system('cls' if os.name == 'nt' else 'clear')


class App:
    GUI = "Graphical User Interface (GUI)"
    TUI = "Text User Interface (TUI)"
    INTERFACES = [GUI, TUI]

    def __init__(self, args):
        self.app_gui = AppGUI(args)
        self.app_tui = AppTUI()

    def start(self):
        ui = self.select_ui()
        if ui == App.GUI:
            self.app_gui.start()
        elif ui == App.TUI:
            make_indent()
            self.app_tui.start()
        else:
            raise Exception("Something went wrong while selecting User Interface...")

    def select_ui(self):
        primary_text = "Hello! I am glad that you are using my program!\n" \
                       "\n" \
                       "If you want to test network, to see how does it work you'd better to use GUI interface.\n" \
                       "But if you want to teach fast network - TUI is your option.\n" \
                       "But remember, that it is not possible to swap between GUI and TUI while program is working!\n"
        select_text = "So, please, select interface: "
        error_text = "\nIncorrect input! Try again!"
        input_text = "Your choice: "
        return App.INTERFACES[enumerate_choice(App.INTERFACES, primary_text, select_text, error_text, input_text)]

    def exec(self):
        self.app_gui.exec()
