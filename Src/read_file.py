import json

def load_data():
    try:
        with open("Data.json", "r") as file:
            data = json.load(file)
            return data
    
    except FileNotFoundError:
        return{"students":[], "professors":[]}