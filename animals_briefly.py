"""A simple Python script that reads the content of animals_data.json,
iterates through the animals, and for each one prints:
+ Name
+ Diet
+ The first location from the locations list
+ Type"""

import json


def load_data(file_path: str) -> list:
    """Loads a JSON file"""
    with open(file_path, "r") as fd:
        return json.load(fd)


def print_animal(animal: dict):
    """Briefly prints an animal-dictionary."""
    output: str = str()
    if "name" in animal:
        output += f"Name: {animal['name']}\n"
    if "diet" in animal["characteristics"]:
        output += f"Diet: {animal['characteristics']['diet']}\n"
    if "locations" in animal:
        output += f"Location: {animal['locations'][0]}\n"
    if "type" in animal["characteristics"]:
        output += f"Type: {animal['characteristics']['type']}\n"
    print(f"{output}")


def main():
    animals = load_data("animals_data.json")

    for animal in animals:
        print_animal(animal)


if __name__ == "__main__":
    main()
