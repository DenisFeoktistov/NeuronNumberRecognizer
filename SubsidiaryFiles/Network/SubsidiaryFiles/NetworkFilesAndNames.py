import os
from random import random, randint, choice
import json
import numpy as np

from SubsidiaryFiles.Modules.Constants import *

INPUT = 1
HIDDEN = 2
OUTPUT = 3


def check_name(name: str) -> bool:
    exist = False
    for info in get_all_primary_info():
        if name == info["name"]:
            exist = True
            break
    return name != "" and name.find(" ") == -1 and not exist


def get_network_by_name(name: str) -> dict:  # a little bit hard to set real type
    path = get_path_by_name(name)
    return get_network_by_path(path)


def add_new_network(name: str, template: list = MAIN_NETWORK_TEMPLATE) -> None:
    network = dict()
    network["template"] = template

    network["iterations"] = 0
    network["batches"] = 0
    network["batch size"] = MAIN_BATCH_SIZE
    network["learning speed"] = MAIN_LEARNING_SPEED

    network["data"] = create_empty_data()

    with open(f"{NETWORKS_DIRECTORY_PATH}/{name}.json", "w") as new_network_file:
        json.dump(network, new_network_file)


def get_network_by_path(path: str) -> dict:
    with open(f"{path}") as network_file:
        network = json.load(network_file)
    return network


def create_empty_data() -> list:
    data = list()
    for row in range(len(MAIN_NETWORK_TEMPLATE)):
        data.append(dict())
        data[row]["layer_type"] = -1

        if row == 0:
            data[row]["layer_type"] = INPUT
        elif row == len(MAIN_NETWORK_TEMPLATE) - 1:
            data[row]["layer_type"] = OUTPUT
        else:
            data[row]["layer_type"] = HIDDEN

        data[row]["layer_data"] = list()

        for j in range(MAIN_NETWORK_TEMPLATE[row]):
            bias = np.random.randn(1)[0]

            neuron_output = list()

            if data[row]["layer_type"] != OUTPUT:
                neuron_output = [np.random.randn(1)[0] for _ in
                                 range(MAIN_NETWORK_TEMPLATE[row + 1])]
            if data[row]["layer_type"] != INPUT:
                data[row]["layer_data"].append(
                    {"output_weights": neuron_output, "bias": bias / MAIN_NETWORK_TEMPLATE[row - 1]})
            else:
                data[row]["layer_data"].append({"output_weights": neuron_output})
    return data


def get_all_primary_info() -> list:
    res = list()
    for file in os.listdir(NETWORKS_DIRECTORY_PATH):
        if file.endswith(".json"):
            res.append(get_info_by_path(NETWORKS_DIRECTORY_PATH + file))
    return sorted(res, key=lambda info: (-info["batches"], info["name"]), reverse=False)


def get_info_by_name(name: str) -> dict:
    return get_network_by_path(get_path_by_name(name))


def get_info_by_path(path: str) -> dict:
    name = get_name_from_path(path=path)
    with open(path) as network:
        network = json.load(network)
    template = network["template"]

    iterations = network["iterations"]
    batches = network["batches"]
    batch_size = network["batch size"]
    learning_speed = network["learning speed"]
    return {"name": name, "batches": batches, "iterations": iterations, "batch size": batch_size, "learning_speed": learning_speed,
            "template": template}


def get_path_by_name(name: str) -> str:
    return NETWORKS_DIRECTORY_PATH + name + ".json"


def get_name_from_path(path: str) -> str:
    return crop_json(path[len(NETWORKS_DIRECTORY_PATH):])


def crop_json(file: str) -> str:
    if file.endswith(".json"):
        file = file[:-5]
    return file
