import json

def get_test_data(key):
    with open("test_data/login_data.json") as f:
        data = json.load(f)
    return data[key]