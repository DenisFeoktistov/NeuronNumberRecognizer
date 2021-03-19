import json


from SubsidiaryFiles.Modules.NetworkSubsidiary import *


class Network:
    def __init__(self) -> None:
        self.path = None
        self.name = None

        self.network = None
        self.data = None
        self.template = None
        self.iterations = None

        self.values = None

    def set_network(self, name: str) -> None:
        self.path = get_path_by_name(name)
        self.name = name

        self.network = get_network_by_path(self.path)

        self.data = self.network["data"]
        self.template = self.network["template"]
        self.iterations = self.network["iterations"]

        self.values = [np.array([0.] * row_size) for row_size in self.template]
        self.values = np.array(self.values, dtype=np.ndarray)

    def save_changes(self):
        with open(self.path, "w") as network_file:
            json.dump(self.network, network_file)
