import json


def load_data(file_path):
  """ Loads a JSON file """
  with open(file_path, "r") as handle:
    return json.load(handle)


def get_info():
    animals_data = load_data('animals_data.json')
    for animal in animals_data:
        try:
            name = animal["name"]
            diet = animal["characteristics"]["diet"]
            location = animal["locations"][0]
            type = animal["characteristics"]["type"]
        except KeyError:
            continue
        print(f"Name: {name}\n"
              f"Diet: {diet}\n"
              f"Location: {location}\n"
              f"Type: {type}\n")

get_info()
