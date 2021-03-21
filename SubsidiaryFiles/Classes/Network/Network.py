from __future__ import annotations
import json
from typing import List, Dict

from SubsidiaryFiles.Modules.NetworkFilesAndNames import *
from SubsidiaryFiles.Modules.NetworkMath import *


class Network:
    def __init__(self) -> None:
        self.path: str = None
        self.name: str = None

        self.template: list = None
        self.iterations: int = None

        self.layers: List[Layer] = None

        self.delta_layers: List[DeltaLayer] = None
        self.epoch_iterations: int = None

    def set_network(self, name: str) -> None:
        self.path = get_path_by_name(name)
        self.name = name

        network = get_network_by_path(self.path)

        self.template = network["template"]
        self.iterations = network["iterations"]

        self.layers = [Layer(layer_data) for layer_data in network["data"]]
        self.delta_layers = [DeltaLayer(layer) for layer in self.layers]

        self.epoch_iterations = 0

    def convert_to_default(self) -> dict:
        res = dict()

        res["template"] = self.template
        res["iterations"] = self.iterations
        res["data"] = [layer.convert_to_default() for layer in self.layers]

        return res

    def save_changes(self) -> None:
        with open(self.path, "w") as output:
            json.dump(self.convert_to_default(), output)

    def process_matrix(self, matrix: np.ndarray, correct_answer: int) -> None:
        self.layers[0].values = activation_function(process_color_matrix(matrix.ravel()))
        self.layers[0].values = self.layers[0].values.reshape((self.layers[0].values.size, 1))

        for i in range(1, len(self.layers)):
            self.layers[i].values = activation_function(
                np.dot(self.layers[i - 1].weights, self.layers[i - 1].values) + (
                    self.layers[i].biases if self.layers[i - 1].type != INPUT else np.zeros((self.layers[i].size, 1))))

        self.back_propagation(correct_answer)

        if self.epoch_iterations == ITERATIONS_FOR_EPOCH:
            for layer, delta_layer in zip(self.layers, self.delta_layers):
                layer.weights += delta_layer.delta_weights / ITERATIONS_FOR_EPOCH
                layer.biases += delta_layer.delta_biases / ITERATIONS_FOR_EPOCH

            self.clear_delta_layers()
            self.epoch_iterations = 0

    def clear_delta_layers(self):
        for delta_layer in self.delta_layers:
            delta_layer.clear()

    def back_propagation(self, correct_value):
        correct = np.array([1 if i == correct_value else 0 for i in range(10)])

        cost = [np.zeros(layer.size) for layer in self.layers]
        delta_weights = [np.zeros(layer.weights.shape) for layer in self.layers]
        delta_biases = [np.zeros(layer.biases.shape) for layer in self.layers]

        cost[-1] = get_cost(self.layers[-1].values.ravel(), correct)

    def get_output(self) -> list:
        return list(map(lambda arr: arr[0], self.layers[-1].values))


class Layer:
    def __init__(self, layer_data: dict):
        self.size = len(layer_data["layer_data"])
        self.type = layer_data["layer_type"]

        self.values = np.zeros(shape=(self.size, 1))
        if self.type != OUTPUT:
            self.weights = np.array([neuron["output_weights"] for neuron in layer_data["layer_data"]]).transpose()
        if self.type != INPUT:
            self.biases = np.array([neuron["bias"] for neuron in layer_data["layer_data"]]).transpose()
            self.biases = self.biases.reshape((self.biases.size, 1))

    def convert_to_default(self) -> dict:
        res = dict()
        res["layer_type"] = self.type
        res["layer_data"] = list()

        if self.type != OUTPUT:
            weights = self.weights.transpose()
        if self.type != INPUT:
            biases = self.biases.reshape((self.biases.size,))

        for i in range(self.size):
            res["layer_data"].append(dict())
            if self.type != OUTPUT:
                res["layer_data"][i]["output_weights"] = list(weights[i])
            if self.type != INPUT:
                res["layer_data"][i]["bias"] = biases[i]

        return res


class DeltaLayer:
    def __init__(self, layer: Layer):
        self.delta_weights = np.zeros(layer.weights.shape)
        self.delta_biases = np.zeros(layer.biases.shape)

    def __iadd__(self, other: DeltaLayer):
        self.delta_weights = self.delta_weights + other.delta_weights
        self.delta_biases = self.delta_biases + other.delta_biases

    def clear(self):
        self.delta_weights = np.zeros(self.delta_weights.shape)
        self.delta_biases = np.zeros(self.delta_biases.shape)
