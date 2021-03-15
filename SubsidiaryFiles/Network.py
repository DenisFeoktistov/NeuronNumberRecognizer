from typing import List, Dict
import os
from random import randint


def add_new_network(name: str) -> None:
    with open(f"./data/networks/{name}.json", "w"):
        pass


def get_info() -> List[dict]:
    res = list()
    for file in os.listdir("./data/networks"):
        if file.endswith(".json"):
            res.append({"name": file[:-5], "iterations": randint(1, 100)})
    return sorted(res, key=lambda info: info["iterations"], reverse=True)


def get_info_by_name(get_name) -> dict:
    for file in os.listdir("./data/networks"):
        if file.endswith(".json"):
            name = file[:-5]
            iterations = randint(1, 100)
            if name == get_name:
                return {"name": name, "iterations": iterations}
    return {"name": "ERROR", "iterations": -1}
