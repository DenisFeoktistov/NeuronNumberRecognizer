from __future__ import annotations
import os


import AppFiles.AppInterfaceClasses.StartWindows.AddNewNetworkWindow.AddNewNetworkWindow as AddNewNetworkWindow
from SubsidiaryFiles.Classes.Network import add_new_network


class AddNewNetworkWindowResponder:
    def __init__(self, window: AddNewNetworkWindow.AddNewNetworkWindow) -> None:
        self.window = window

    def add_network(self) -> None:
        new_name = self.window.name_line.text()
        names = os.listdir("./data/networks")
        for i in range(len(names)):
            if (names[i]).find(".") != -1:
                names[i] = names[i][:names[i].index(".")]
        if new_name not in names and self.check_name(new_name):
            self.finish(new_name)
        else:
            self.window.set_error()

    def check_name(self, name: str):
        return name != "" and name.find(" ") == -1

    def finish(self, new_name: str) -> None:
        add_new_network(new_name)

        self.window.main_app_interface.app.main_app_responder.add_new_network_finish()
