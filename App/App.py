import os
import sys


from App.AppGUI.AppGUI import AppGUI
from App.AppTUI.AppTUI import AppTUI

from SubsidiaryFiles.Modules.FunctionsTUI import enumerate_choice, make_indent


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
        make_indent()
        if ui == App.GUI:
            self.app_gui.start()
            self.app_gui.exec()
        elif ui == App.TUI:
            self.app_tui.start()
            sys.exit()
        else:
            raise Exception("Something went wrong while selecting User Interface...")

    def select_ui(self):
        primary_text = "Hello! I am glad that you are using my program!\n" \
                       "\n" \
                       "If you want to test network, to see how does it work you'd better to use GUI interface.\n" \
                       "But if you want to teach fast network - TUI is your option.\n" \
                       "But remember, that it is not possible to swap between GUI and TUI while program is working!\n"
        select_text = "So, please, select interface: "
        return enumerate_choice(App.INTERFACES, primary_text, select_text)
