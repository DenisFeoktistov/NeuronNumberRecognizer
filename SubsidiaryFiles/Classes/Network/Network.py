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

        self.values: list = None
        self.act_values: list = None

        self.weights: list = None
        self.delta_weights: list = None
        self.biases: list = None
        self.delta_biases: list = None

        self.epoch_iterations = 0

    def process_matrix(self, matrix, correct_answer):
        self.values[0] = matrix.ravel()
        self.act_values[0] = activation_function(self.values[0])
        self.values[0] = self.values[0].reshape(self.values[0].size, 1)
        self.act_values[0] = self.act_values[0].reshape(self.act_values[0].size, 1)

        for i in range(len(self.template) - 1):
            self.values[i + 1] = np.dot(self.weights[i], self.act_values[i]) + self.biases[i]
            self.act_values[i + 1] = activation_function(self.values[i + 1])

        self.epoch_iterations += 1

        self.back_propagation(correct_answer)
        if self.epoch_iterations == ITERATIONS_FOR_EPOCH:
            print("EPOCH")
            self.weights = [weight - delta_weight * LEARNING_SPEED / ITERATIONS_FOR_EPOCH for weight, delta_weight in zip(self.weights, self.delta_weights)]
            self.biases = [biases - delta_biases * LEARNING_SPEED / ITERATIONS_FOR_EPOCH for biases, delta_biases in zip(self.biases, self.delta_biases)]
            self.epoch_iterations = 0

            self.delta_weights = [np.zeros(layer.shape) for layer in self.weights]
            self.delta_biases = [np.zeros(layer.shape) for layer in self.biases]

    def back_propagation(self, correct):
        correct = np.array([1 if i == correct else 0 for i in range(10)]).reshape((10, 1))
        local_delta_weights = [np.zeros(layer.shape) for layer in self.weights]
        local_delta_biases = [np.zeros(layer.shape) for layer in self.biases]

        delta = derivative_of_cost_function(self.act_values[-1], correct)
        local_delta_biases[-1] = delta
        local_delta_weights[-1] = np.dot(delta, self.act_values[-2].transpose())

        for i in range(2, len(self.template)):
            der1 = derivative_of_activation_function(self.values[-i])
            delta = np.dot(self.weights[-i + 1].transpose(), delta) * der1
            local_delta_biases[-i] = delta
            local_delta_weights[-i] = np.dot(delta, self.act_values[-i - 1].transpose())

        self.delta_weights = [delta_weight_layer + local_delta_weight_layer for local_delta_weight_layer, delta_weight_layer in zip(local_delta_weights, self.delta_weights)]

        self.delta_biases = [delta_bias_layer + local_delta_bias_layer for local_delta_bias_layer, delta_bias_layer in zip(local_delta_biases, self.delta_biases)]

    def get_output(self):
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
        self.biases = [np.array([neuron["bias"] for neuron in layer["layer_data"]]).reshape((len(layer["layer_data"]), 1)) for layer in
                       network["data"][1:]]
        self.delta_biases = [np.zeros(layer.shape) for layer in self.biases]
        self.values = [np.zeros((layer, 1)) for layer in self.template]
        self.act_values = [np.zeros(layer.shape) for layer in self.values]

    def convert_to_default(self) -> dict:
        res = dict()

        res["template"] = self.template
        res["iterations"] = self.iterations
        res["data"] = [dict() for _ in range(len(self.values))]

        biases = [layer_biases.transpose().ravel() for layer_biases in self.biases]
        weights = [layer_weights.transpose() for layer_weights in self.weights]

        for i in range(len(self.template)):
            res["data"][i]["layer_type"] = -1
            if i == 0:
                res["data"][i]["layer_type"] = INPUT
            elif i == len(self.template) - 1:
                res["data"][i]["layer_type"] = OUTPUT
            else:
                res["data"][i]["layer_type"] = HIDDEN

            res["data"][i]["layer_data"] = list()

            for j in range(self.template[i]):
                if i != 0:
                    neuron_bias = biases[i - 1][j]
                    if i != len(self.template) - 1:
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
