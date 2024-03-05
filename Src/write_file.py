import json

def save_data(data):
    with open("Data.jason", "w") as file:
        json.dump(data, file)