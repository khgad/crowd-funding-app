import json

def read_json_file(filename):
    """Reads data from a JSON file and returns it as a Python object."""
    with open(filename, 'r') as file:
        data = json.load(file)
    return data

def write_json_file(filename, data):
    """Writes data to a JSON file."""
    with open(filename, 'w') as file:
        json.dump(data, file, indent=4, default=str)

def get_next_id(data):
    """Returns the next ID for a new item in the given data."""
    if len(data) == 0:
        return 1
    else:
        return data[-1]['id'] +1