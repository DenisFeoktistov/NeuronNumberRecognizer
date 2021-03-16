from typing import List, Dict
import os
from random import randint
import json


class Network:
    def __init__(self, name):
        self.name = name
        self.data = get_data_by_name(name)


def find_path_by_name(get_name: str) -> str:
    for file in os.listdir("./data/networks"):
        if file.endswith(".json"):
            name = file[:-5]
            iterations = randint(1, 100)
            if name == get_name:
                return "./data/networks" + file
    raise Exception(f"No such file: {get_name}")


def get_data_by_name(name: str) -> dict:  # a little bit hard to set real typee
    path = find_path_by_name(name)
    if path:
        with open(path) as file_json:
            data = json.load(file_json)
        return data


def add_new_network(name: str) -> None:
    with open(f"./data/networks/{name}.json", "w"):
        data = dict()
        data["iterations"] = randint(1, 100)  # test
        data["data"] = create_empty_data()


def create_empty_data() -> list:
    data = list()


def get_info() -> List[dict]:
    res = list()
    for file in os.listdir("./data/networks"):
        if file.endswith(".json"):
            res.append({"name": file[:-5], "iterations": randint(1, 100)})
    return sorted(res, key=lambda info: info["iterations"], reverse=True)


def get_info_by_name(get_name: str) -> dict:
    if find_path_by_name(get_name):
        iterations = randint(1, 100)
        return {"name": get_name, "iterations": iterations}
    return {"name": "ERROR", "iterations": -1}
