import json
import os

file_path = "data.json"

def generate_id(taks):
    tasks = cargar()
    n = []
    if tasks:
        for i in tasks:
            id = i["id"]
            n.append(id)
    if n == []:
        return 1
    else:
        return n[-1] + 1

def cargar():
    if os.path.exists(file_path):
        with open(file_path, "r") as file:
            try:
                data = json.load(file)
                if isinstance(data, list):
                    return data
            except json.JSONDecodeError:
                pass
    return []

def guardar(task):
    with open(file_path, "w") as file:
        json.dump(task, file, indent=4)
