import json
import os

file_path = "data.json"

def generate_id(taks):
    return len(taks) + 1 if taks else 1

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