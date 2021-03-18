from SubsidiaryFiles.NetworkSubsidiary import *


class Network:
    def __init__(self) -> None:
        self.path = None
        self.name = None

        self.network = None
        self.data = None
        self.template = None
        self.iterations = None

    def set_network(self, name: str) -> None:
        self.path = get_path_by_name(name)
        self.name = name

        self.network = get_network_by_path(self.path)

        self.data = self.network["data"]
        self.template = self.network["template"]
        self.iterations = self.network["iterations"]
