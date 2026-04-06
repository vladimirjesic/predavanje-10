import json

def load_file(file_name):
    with open(file_name, "r") as file:
        data = json.load(file)
        return data

def save_file(file_name, data_to_save):
    with open(file_name, "w") as file:
        json.dump(data_to_save, file, indent=4)