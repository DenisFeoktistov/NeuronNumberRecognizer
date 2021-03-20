import json


from SubsidiaryFiles.Modules.NetworkFilesAndNames import *
from SubsidiaryFiles.Modules.NetworkMath import *


class Network:
    def __init__(self) -> None:
        self.path: str = None
        self.name: str = None

        self.network: dict = None
        self.data: list = None
        self.template: list = None
        self.iterations: int = None

        self.layers: list = None

    def set_network(self, name: str) -> None:
        self.path = get_path_by_name(name)
        self.name = name

        network = get_network_by_path(self.path)

        self.template = network["template"]
        self.iterations = network["iterations"]

        self.layers = [Layer(layer_data) for layer_data in network["data"]]

    def convert_to_default(self) -> dict:
        res = dict()

        res["template"] = self.template
        res["iterations"] = self.iterations
        res["data"] = [layer.convert_to_default() for layer in self.layers]

        return res

    def save(self) -> None:
        with open(self.path, "w") as output:
            json.dump(self.convert_to_default(), output)

    def process_matrix(self, matrix: np.ndarray) -> None:
        pass

    def get_output(self) -> list:
        return list(self.layers[-1].values)


class Layer:
    def __init__(self, layer_data: dict):
        self.size = len(layer_data["layer_data"])
        self.type = layer_data["layer_type"]

        self.values = np.zeros(self.size)
        if self.type != OUTPUT:
            self.weights = np.array([neuron["output_weights"] for neuron in layer_data["layer_data"]])
        if self.type != INPUT:
            self.biases = np.array([neuron["bias"] for neuron in layer_data["layer_data"]])

    def convert_to_default(self) -> dict:
        res = dict()
        res["layer_type"] = self.type
        res["layer_data"] = list()

        for i in range(self.size):
            res["layer_data"].append(dict)
            if self.type != OUTPUT:
                res["layer_data"][i]["output_weights"] = list(self.weights[i])
            if self.type != INPUT:
                res["layer_data"][i]["bias"] = self.biases[i]

        return res
