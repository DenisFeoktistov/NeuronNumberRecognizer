from __future__ import annotations
import json
from typing import List

from SubsidiaryFiles.Modules.NetworkFilesAndNames import *
from SubsidiaryFiles.Modules.NetworkMath import *


class Network:
    def __init__(self) -> None:
        self.path: str
        self.name: str

        self.template: List[int]
        self.iterations: int
        self.mini_batch_iterations: int

        self.values: List[np.ndarray]
        self.act_values: List[np.ndarray]

        self.weights: List[np.ndarray]
        self.delta_weights: List[np.ndarray]
        self.biases: List[np.ndarray]
        self.delta_biases: List[np.ndarray]

    def process_matrix(self, matrix: np.ndarray, correct_answer: int) -> None:
        self.feed_forward(matrix)

        self.back_propagation(correct_answer)

        self.iterations += 1
        self.mini_batch_iterations += 1

        if not self.mini_batch_iterations % ITERATIONS_FOR_MINI_BATCH:
            self.update_parameters()

    def update_parameters(self) -> None:
        self.weights = [weight - delta_weight * (MAIN_LEARNING_SPEED / ITERATIONS_FOR_MINI_BATCH) for
                        weight, delta_weight in
                        zip(self.weights, self.delta_weights)]
        self.biases = [biases - delta_biases * (MAIN_LEARNING_SPEED / ITERATIONS_FOR_MINI_BATCH) for
                       biases, delta_biases in
                       zip(self.biases, self.delta_biases)]
        self.delta_weights = [np.zeros(layer.shape) for layer in self.weights]
        self.delta_biases = [np.zeros(layer.shape) for layer in self.biases]

    def feed_forward(self, matrix: np.ndarray) -> None:
        self.values[0] = self.act_values[0] = process_color_matrix(matrix.ravel()).reshape((matrix.size, 1))

        for i in range(len(self.template) - 1):
            self.values[i + 1] = np.dot(self.weights[i], self.act_values[i]) + self.biases[i]
            self.act_values[i + 1] = activation_function(self.values[i + 1])

    def back_propagation(self, correct: int) -> None:
        correct = np.array([1. if i == correct else 0. for i in range(10)]).reshape((10, 1))
        local_delta_weights = [np.zeros(layer.shape) for layer in self.weights]
        local_delta_biases = [np.zeros(layer.shape) for layer in self.biases]

        delta = derivative_of_cost_function(self.act_values[-1], correct) * derivative_of_activation_function(
            self.values[-1])
        local_delta_biases[-1] = delta
        local_delta_weights[-1] = np.dot(delta, self.act_values[-2].transpose())

        for i in range(2, len(self.template)):
            der1 = derivative_of_activation_function(self.values[-i])
            delta = np.dot(self.weights[-i + 1].transpose(), delta) * der1
            local_delta_biases[-i] = delta
            local_delta_weights[-i] = np.dot(delta, self.act_values[-i - 1].transpose())

        self.delta_weights = [delta_weight_layer + local_delta_weight_layer for
                              local_delta_weight_layer, delta_weight_layer in
                              zip(local_delta_weights, self.delta_weights)]

        self.delta_biases = [delta_bias_layer + local_delta_bias_layer for local_delta_bias_layer, delta_bias_layer in
                             zip(local_delta_biases, self.delta_biases)]

    def get_output(self) -> List[float]:
        return list(self.act_values[-1].ravel())

    def set_network(self, name: str) -> None:
        self.path = get_path_by_name(name)
        self.name = name

        network = get_network_by_path(self.path)

        self.template = network["template"]
        self.iterations = network["iterations"]

        self.weights = [np.array([np.array(neuron["output_weights"]) for neuron in layer["layer_data"]]).transpose() for
                        layer in
                        network["data"][:-1]]
        self.delta_weights = [np.zeros(layer.shape) for layer in self.weights]
        self.biases = [
            np.array([neuron["bias"] for neuron in layer["layer_data"]]).reshape((len(layer["layer_data"]), 1)) for
            layer in
            network["data"][1:]]
        self.delta_biases = [np.zeros(layer.shape) for layer in self.biases]
        self.values = [np.zeros((layer, 1)) for layer in self.template]
        self.act_values = [np.zeros(layer.shape) for layer in self.values]

        self.mini_batch_iterations = 0

    def convert_to_default(self) -> dict:
        res = dict()

        res["template"] = self.template
        res["iterations"] = self.iterations
        res["data"] = [dict() for _ in range(len(self.values))]

        biases = [layer_biases.transpose().ravel() for layer_biases in self.biases]
        weights = [layer_weights.transpose() for layer_weights in self.weights]

        for i in range(len(self.template)):
            if i == 0:
                type = INPUT
            elif i == len(self.template) - 1:
                type = OUTPUT
            else:
                type = HIDDEN

            res["data"][i]["layer_type"] = type
            res["data"][i]["layer_data"] = list()

            for j in range(self.template[i]):
                if type != INPUT:
                    neuron_bias = biases[i - 1][j]
                    if type != OUTPUT:
                        neuron_weights = list(weights[i][j])
                        res["data"][i]["layer_data"].append({"bias": neuron_bias, "output_weights": neuron_weights})
                    else:
                        res["data"][i]["layer_data"].append({"bias": neuron_bias})
                else:
                    neuron_weights = list(weights[i][j])
                    res["data"][i]["layer_data"].append({"output_weights": neuron_weights})

        return res

    def save_changes(self) -> None:
        with open(self.path, "w") as output:
            json.dump(self.convert_to_default(), output)
