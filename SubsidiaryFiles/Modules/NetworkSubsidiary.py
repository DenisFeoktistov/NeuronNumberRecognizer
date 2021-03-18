import os
from random import random, randint
import json
import numpy as np


from SubsidiaryFiles.Modules.Constants import *


def get_network_by_name(name: str) -> dict:  # a little bit hard to set real type
    path = get_path_by_name(name)
    return get_network_by_path(path)


def add_new_network(name: str) -> None:
    network = dict()
    network["iterations"] = 0
    network["template"] = NETWORK_MAIN_TEMPLATE_INDEX
    network["data"] = create_empty_data()

    with open(f"{NETWORKS_DIRECTORY_PATH}/{name}.json", "w") as new_network_file:
        json.dump(network, new_network_file)


def get_network_by_path(path: str) -> dict:
    with open(f"{path}") as network_file:
        network = json.load(network_file)
    return network


def create_empty_data() -> list:
    data = list()
    for i in range(len(NETWORK_MAIN_TEMPLATE)):
        data.append(list())

        for j in range(NETWORK_MAIN_TEMPLATE[i]):
            bias = randint(-10, 10)

            neuron_output = list()

            if i != len(NETWORK_MAIN_TEMPLATE) - 1:
                neuron_output = [random() for _ in range(NETWORK_MAIN_TEMPLATE[i + 1])]
            data[i].append({"output": neuron_output, "bias": bias})
    return data


def convert_data_to_list(data: np.array) -> list:
    new_data = list()
    for i in range(len(NETWORK_MAIN_TEMPLATE)):
        new_data.append(list())
        for j in range(NETWORK_MAIN_TEMPLATE[i]):
            neuron = data[i][j]

            new_neuron = {"output": list(neuron["output"]), "bias": neuron["bias"]}
            new_data[i].append(new_neuron)
    return new_data


def convert_data_to_numpy(data: list) -> np.array:
    new_data = list()
    for i in range(len(NETWORK_MAIN_TEMPLATE)):
        new_data.append(list())
        for j in range(NETWORK_MAIN_TEMPLATE[i]):
            neuron = data[i][j]

            new_neuron = {"output": np.array(neuron["output"]), "bias": neuron["bias"]}
            new_data[i].append(new_neuron)
    new_data = np.array(new_data)
    return new_data


def get_all_primary_info() -> list:
    res = list()
    for file in os.listdir(NETWORKS_DIRECTORY_PATH):
        if file.endswith(".json"):
            res.append(get_info_by_path(NETWORKS_DIRECTORY_PATH + file))
    return sorted(res, key=lambda info: info["iterations"], reverse=True)


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
