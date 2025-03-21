"""bring animal data into html"""

import json


def load_data(file_path: str) -> list:
    """Loads a JSON file"""
    with open(file_path, "r") as fd:
        return json.load(fd)


def get_html_template(file_path: str) -> str:
    """Loads a HTML template"""
    with open(file_path, "r") as fd:
        return fd.read(-1)


def get_animal_cards(animals_list: [dict]):
    """Briefly prints an animal-dictionary."""
    output: str = str()
    for animal in animals_list:
        output += '<li class="cards__item">\n'
        if "name" in animal:
            output += f'<div class="card__title">{animal["name"]}</div>\n'
        output += '<p class="card__text"><ul>'
        if "scientific_name" in animal["taxonomy"]:
            output += f"<li><strong>Scientific Name:</strong> {animal['taxonomy']['scientific_name']}</li>\n"
        if "lifespan" in animal["characteristics"]:
            output += f"<li><strong>Lifespan:</strong> {animal['characteristics']['lifespan']}</li>\n"
        if "diet" in animal["characteristics"]:
            output += f"<li><strong>Diet:</strong> {animal['characteristics']['diet']}</li>\n"
        if "locations" in animal:
            output += f"<li><strong>Location:</strong> {animal['locations'][0]}</li>\n"
        if "type" in animal["characteristics"]:
            output += f"<li><strong>Type:</strong> {animal['characteristics']['type']}</li>\n"
        output += "</ul>\n</p>\n</li>\n"
    return output


def main():
    animals = load_data("animals_data.json")

    template = get_html_template("animals_template.html")
    animals_info = get_animal_cards(animals)

    with open("animals.html", "w") as fd:
        fd.write(template.replace("__REPLACE_ANIMALS_INFO__", animals_info))


if __name__ == "__main__":
    main()
