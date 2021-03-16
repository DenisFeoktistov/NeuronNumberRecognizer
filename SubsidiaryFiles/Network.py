from typing import List, Dict
import os
from random import randint, random
import json


from SubsidiaryFiles.Constants import *


class Network:
    def __init__(self, name):
        self.name = name
        self.data = get_data_by_name(name)


def find_path_by_name(get_name: str) -> str:
    for file in os.listdir(NETWORKS_DIRECTORY_PATH):
        if file.endswith(".json"):
            name = file[:-5]
            iterations = randint(1, 100)
            if name == get_name:
                return NETWORKS_DIRECTORY_PATH + file
    raise Exception(f"No such file: {get_name}")


def get_data_by_name(name: str) -> dict:  # a little bit hard to set real type
    path = find_path_by_name(name)
    if path:
        with open(path) as file_json:
            data = json.load(file_json)
        return data


def add_new_network(name: str) -> None:
    with open(f"{NETWORKS_DIRECTORY_PATH}/{name}.json", "w"):
        data = dict()
        data["iterations"] = randint(1, 100)  # test
        data["data"] = create_empty_data()


def create_empty_data() -> list:
    data = list()
    for i, row in enumerate(NETWORK_TEMPLATE1["rows"]):
        data.append(list())

        for neuron in range(row):
            neuron_input = list()
            neuron_output = list()
            if i != 0:
                neuron_input = random()
            neuron_data = []


def get_info() -> List[dict]:
    res = list()
    for file in os.listdir(NETWORKS_DIRECTORY_PATH):
        if file.endswith(".json"):
            res.append({"name": file[:-5], "iterations": randint(1, 100)})
    return sorted(res, key=lambda info: info["iterations"], reverse=True)


def get_info_by_name(get_name: str) -> dict:
    if find_path_by_name(get_name):
        iterations = randint(1, 100)
        return {"name": get_name, "iterations": iterations}
    return {"name": "ERROR", "iterations": -1}
