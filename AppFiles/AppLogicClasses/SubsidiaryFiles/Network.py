from typing import List
import os
from random import randint


def add_new_network(name: str) -> None:
    with open(f"./data/networks/{name}.json", "w"):
        pass


def get_info() -> list:
    res = list()
    for file in os.listdir("./data/networks"):
        if file.endswith(".json"):
            res.append({"name": file[:-5], "iterations": randint(1, 100)})
    return sorted(res, key=lambda info: info["iterations"], reverse=True)
