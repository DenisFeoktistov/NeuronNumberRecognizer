import os
from random import random, randint, choice
import json
import numpy as np

from SubsidiaryFiles.Modules.Constants import *

INPUT = 1
HIDDEN = 2
OUTPUT = 3


def get_network_by_name(name: str) -> dict:  # a little bit hard to set real type
    path = get_path_by_name(name)
    return get_network_by_path(path)


def add_new_network(name: str) -> None:
    network = dict()
    network["iterations"] = 0
    network["template"] = NETWORK_TEMPLATES[NETWORK_MAIN_TEMPLATE_INDEX]
    network["data"] = create_empty_data()

    with open(f"{NETWORKS_DIRECTORY_PATH}/{name}.json", "w") as new_network_file:
        json.dump(network, new_network_file)


def get_network_by_path(path: str) -> dict:
    with open(f"{path}") as network_file:
        network = json.load(network_file)
    return network


def create_empty_data() -> list:
    data = list()
    for row in range(len(NETWORK_MAIN_TEMPLATE)):
        data.append(dict())
        data[row]["layer_type"] = -1

        if row == 0:
            data[row]["layer_type"] = INPUT
        elif row == len(NETWORK_MAIN_TEMPLATE) - 1:
            data[row]["layer_type"] = OUTPUT
        else:
            data[row]["layer_type"] = HIDDEN

        data[row]["layer_data"] = list()

        for j in range(NETWORK_MAIN_TEMPLATE[row]):
            bias = np.random.randn(1)[0]

            neuron_output = list()

            if data[row]["layer_type"] != OUTPUT:
                neuron_output = [np.random.randn(1)[0] for _ in
                                 range(NETWORK_MAIN_TEMPLATE[row + 1])]
            if data[row]["layer_type"] != INPUT:
                data[row]["layer_data"].append({"output_weights": neuron_output, "bias": bias / NETWORK_MAIN_TEMPLATE[row - 1]})
            else:
                data[row]["layer_data"].append({"output_weights": neuron_output})
    return data


def get_all_primary_info() -> list:
    res = list()
    for file in os.listdir(NETWORKS_DIRECTORY_PATH):
        if file.endswith(".json"):
            res.append(get_info_by_path(NETWORKS_DIRECTORY_PATH + file))
    return sorted(res, key=lambda info: (-info["iterations"], info["name"]), reverse=False)


def get_info_by_name(name: str) -> dict:
    return get_network_by_path(get_path_by_name(name))


def get_info_by_path(path: str) -> dict:
    name = get_name_from_path(path=path)
    with open(path) as network:
        network = json.load(network)
    iterations = network["iterations"]
    return {"name": name, "iterations": iterations}


def get_path_by_name(name: str) -> str:
    return NETWORKS_DIRECTORY_PATH + name + ".json"


def get_name_from_path(path: str) -> str:
    return crop_json(path[len(NETWORKS_DIRECTORY_PATH):])


def crop_json(file: str) -> str:
    if file.endswith(".json"):
        file = file[:-5]
    return file
