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
        self.layers[0].values = process_color_matrix(matrix.ravel())
        self.layers[0].values = self.layers[0].values.reshape((self.layers[0].values.size, 1))

        for i in range(1, len(self.layers)):
            self.layers[i].values = np.dot(self.layers[i - 1].weights, self.layers[i - 1].act_values) + self.layers[
                i].biases

        self.back_propagation(correct_answer)
        self.epoch_iterations += 1

        if self.epoch_iterations == ITERATIONS_FOR_EPOCH:
            print("EPOCH")
            for layer, delta_layer in zip(self.layers, self.delta_layers):
                if layer.type != OUTPUT:
                    layer.weights -= delta_layer.delta_weights * LEARNING_SPEED / ITERATIONS_FOR_EPOCH
                if layer.type != INPUT:
                    layer.biases -= delta_layer.delta_biases * LEARNING_SPEED / ITERATIONS_FOR_EPOCH

            self.clear_delta_layers()
            self.epoch_iterations = 0

    def clear_delta_layers(self):
        for delta_layer in self.delta_layers:
            delta_layer.clear()

    def back_propagation(self, correct_value):
        correct = np.array([1 if i == correct_value else 0 for i in range(10)])
        correct = correct.reshape(correct.size, 1)

        cost = [np.zeros((layer.size, 1)) for layer in self.layers]
        local_delta_layers = [DeltaLayer(layer) for layer in self.layers]

        cost[-1] = derivative_of_cost_function(self.layers[-1].act_values, correct)

        local_delta_layers[-1].delta_biases = cost[-1]
        local_delta_layers[-2].delta_weights = np.dot(cost[-1], self.layers[-2].act_values.transpose())

        for i in range(2, len(self.layers)):
            der1 = derivative_of_activation_function(self.layers[-i].values)
            cost[-i] = np.dot(self.layers[-i].weights.transpose(), cost[-i + 1]) * der1
            local_delta_layers[-i].delta_biases = cost[-i]
            local_delta_layers[-i - 1].delta_weights = np.dot(cost[-i], self.layers[-i - 1].values.transpose())

        for local_delta_layer, delta_layer in zip(local_delta_layers, self.delta_layers):
            if delta_layer.type != OUTPUT:
                delta_layer.delta_weights += local_delta_layer.delta_weights
            if delta_layer.type != INPUT:
                delta_layer.delta_biases += local_delta_layer.delta_biases

    def get_output(self) -> list:
        return list(map(lambda arr: arr[0], self.layers[-1].values))


class Layer:
    def __init__(self, layer_data: dict):
        self.size = len(layer_data["layer_data"])
        self.type = layer_data["layer_type"]

        self._values = np.zeros(shape=(self.size, 1))
        self.act_values = activation_function(self.values)
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

    def get_values(self):
        return self._values

    def set_values(self, new_values):
        self._values = new_values
        self.act_values = activation_function(self.values)

    values = property(get_values, set_values, None)


class DeltaLayer:
    def __init__(self, layer: Layer):
        self.type = layer.type

        if self.type != OUTPUT:
            self.delta_weights = np.zeros(layer.weights.shape)
        if self.type != INPUT:
            self.delta_biases = np.zeros(layer.biases.shape)

    def __iadd__(self, other: DeltaLayer):
        self.delta_weights = self.delta_weights + other.delta_weights
        self.delta_biases = self.delta_biases + other.delta_biases

    def clear(self):
        if self.type != OUTPUT:
            self.delta_weights = np.zeros(self.delta_weights.shape)
        if self.type != INPUT:
            self.delta_biases = np.zeros(self.delta_biases.shape)
