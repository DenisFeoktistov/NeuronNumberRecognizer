from typing import List, Dict
import os
from random import randint, random
import json
import numpy as np


from SubsidiaryFiles.Constants import *


class Network:
    def __init__(self):
        pass


def get_data_by_name(name: str) -> dict:  # a little bit hard to set real type
    path = find_path_by_name(name)
    if path:
        with open(path) as file_json:
            data = json.load(file_json)
        return data


def add_new_network(name: str) -> None:
    with open(f"{NETWORKS_DIRECTORY_PATH}/{name}.json", "w") as new_network:
        data = dict()
        data["iterations"] = 0
        data["template"] = NETWORK_MAIN_TEMPLATE_INDEX
        data["data"] = create_empty_data()

        json.dump(data, new_network)


def create_empty_data() -> list:
    data = list()
    for i in range(len(NETWORK_MAIN_TEMPLATE["row sizes"])):
        data.append(list())

        for j in range(NETWORK_MAIN_TEMPLATE["row sizes"][i]):
            neuron_input = list()
            neuron_output = list()

            if i != 0:
                for k in range(NETWORK_MAIN_TEMPLATE["row sizes"][i - 1]):
                    neuron_input.append(data[i - 1][k]["output"][j])
            if i != len(NETWORK_MAIN_TEMPLATE["row sizes"]) - 1:
                neuron_output = [random() for _ in range(NETWORK_MAIN_TEMPLATE["row sizes"][i + 1])]
            neuron_data = {"output": neuron_output, "input": neuron_input}
            data[i].append(neuron_data)
    return data


def convert_data_to_list(data: np.array) -> list:
    new_data = list()
    for i in range(len(NETWORK_MAIN_TEMPLATE["row sizes"])):
        new_data.append(list())
        for j in range(NETWORK_MAIN_TEMPLATE["row sizes"][i]):
            new_data[i].append({"input": list(data[i][j]["input"]), "output": list(data[i][j]["output"])})
    return new_data


def convert_data_to_numpy(data: list) -> np.array:
    new_data = list()
    for i in range(len(NETWORK_MAIN_TEMPLATE["row sizes"])):
        new_data.append(list())
        for j in range(NETWORK_MAIN_TEMPLATE["row sizes"][i]):
            new_data[i].append({"input": np.array(data[i][j]["input"]), "output": np.array(data[i][j]["output"])})
    new_data = np.array(new_data)
    return new_data


def get_all_primary_info() -> List[dict]:
    res = list()
    for file in os.listdir(NETWORKS_DIRECTORY_PATH):
        if file.endswith(".json"):
            res.append(get_info_by_name(file[:-5]))
    return sorted(res, key=lambda info: info["iterations"], reverse=True)


def get_info_by_path(get_path: str) -> dict:
    return get_info_by_name(get_name_from_path(get_path))


def get_info_by_name(get_name: str) -> dict:
    if find_path_by_name(get_name):
        iterations = randint(1, 100)
        return {"name": get_name, "iterations": iterations}
    return {"name": "ERROR", "iterations": -1}


def find_path_by_name(get_name: str) -> str:
    for file in os.listdir(NETWORKS_DIRECTORY_PATH):
        if file.endswith(".json"):
            name = file[:-5]
            if name == get_name:
                return NETWORKS_DIRECTORY_PATH + file
    raise Exception(f"No such file: {get_name}")


def get_name_from_path(path: str) -> str:
    return path[len(NETWORKS_DIRECTORY_PATH):-5]

