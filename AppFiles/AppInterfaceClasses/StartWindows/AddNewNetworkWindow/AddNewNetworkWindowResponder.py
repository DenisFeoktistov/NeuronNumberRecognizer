from __future__ import annotations
import os


import AppFiles.AppInterfaceClasses.StartWindows.AddNewNetworkWindow.AddNewNetworkWindow as AddNewNetworkWindow
from SubsidiaryFiles.Network import add_new_network


class AddNewNetworkWindowResponder:
    def __init__(self, window: AddNewNetworkWindow.AddNewNetworkWindow) -> None:
        self.window = window

    def add_network(self) -> None:
        new_name = self.window.name_line.text()
        names = os.listdir("./data/networks")
        for i in range(len(names)):
            if names[i].index(".") != -1:
                names[i] = names[:names[i].index(".")]
        if new_name not in names:
            self.finish(new_name)
        else:
            self.window.set_error()

    def finish(self, new_name: str) -> None:
        add_new_network(new_name)

        self.window.main_app_interface.app.main_app_responder.add_new_network_finish()
