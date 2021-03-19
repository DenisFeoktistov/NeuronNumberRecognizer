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

    def set_network(self, name: str) -> None:
        self.path = get_path_by_name(name)
        self.name = name

        network = get_network_by_path(self.path)

        self.template = self.network["template"]
        self.iterations = self.network["iterations"]

        self.data = list()

        for row in network["data"]:
            self.data.append(list())
            for neuron_dict in row:
                self.data[-1].append(Neuron(neuron_dict))

    def save_changes(self):
        data = list()

        for row in self.data:
            data.append(list())
            for neuron in row:
                data[-1].append(neuron.convert_to_dict())

        res = {"template": self.template, "iterations": self.iterations, "data": data}

        with open(self.path, "w") as network_file:
            json.dump(res, network_file)

    def process_matrix(self, matrix: np.ndarray) -> None:
        matrix = matrix.ravel()
        for i in range(matrix.size):
            self.data[0][i].value = matrix[i]

        for i in range(len(self.data[:-1])):
            for j1 in range(len(self.data[i])):
                self.data[i][j1].process_value()

                for j2 in range(len(self.data[i + 1])):
                    self.data[i][j2] += self.data[i][j1].value * self.data[i][j1].output_weights[j2]

        for j in range(len(self.data[-1])):
            self.data[-1][j].process_value()

    def get_output(self) -> list:
        return self.data[-1]


class Neuron:
    def __init__(self, neuron_dict: dict) -> None:
        self.value = 0.

        self.output_weights = neuron_dict["output_weights"]
        self.bias = neuron_dict["bias"]

    def process_value(self) -> None:
        self.value += self.bias
        self.value = activation_function(self.value)

    def convert_to_dict(self) -> dict:
        res = dict()
        res["output_weights"] = self.output_weights
        res["bias"] = self.bias
        return res
