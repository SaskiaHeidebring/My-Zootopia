import json


def load_data(file_path):
    """Loads json from a file and returns it as a Python object."""

    try:
        with open(file_path, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        print(f"File {file_path} could not be found")
    except PermissionError:
        print(f"File {file_path} could not be opend")
    except json.JSONDecodeError:
        print(f"File {file_path} does not contain valid json")
    except Exception as e:
        print(f"An unexpected error occured: {e}")


def load_template(file_path):
    """Loads the html string from a file and returns it"""

    try:
        with open(file_path, "r") as f:
            return f.read()
    except FileNotFoundError:
        print(f"File {file_path} could not be found")
    except PermissionError:
        print(f"File {file_path} could not be opend")
    except Exception as e:
        print(f"An unexpected error occured: {e}")


def write_html(file_path, content):
    """Writes a content into a given file"""

    try:
        with open(file_path, "w") as f:
            f.write(content)
    except FileNotFoundError:
        print(f"File {file_path} could not be found")
    except PermissionError:
        print(f"File {file_path} could not be written")
    except Exception as e:
        print(f"An unexpected error occured: {e}")


def get_animal_data_from_json_file(file_path):
    """Loads animal data from a given json file and returns it as a string"""

    animals_data = load_data(file_path)
    animals_string = ""
    for animal in animals_data:
        animal_data = get_animal_data(animal)
        animals_string += serialize_animal(animal_data)

    return animals_string


def get_animal_data(animal):
    """
    Returns an dictionary from an animal data set with the animals name, diet, location and type.
    If one of those attributes does not exist, the correspoding field in the dictionary is None
    """

    animal_name = animal.get("name")
    animal_location = None
    animal_diet = None
    animal_type = None
    animal_characteristics = animal.get("characteristics")

    if animal_characteristics:
        animal_diet = animal_characteristics.get("diet")
        animal_type = animal_characteristics.get("type")
    animal_locations = animal.get("locations")
    if animal_locations and len(animal_locations) > 0:
        animal_location = animal_locations[0]

    animal_data = {}
    animal_data["name"] = animal_name
    animal_data["diet"] = animal_diet
    animal_data["location"] = animal_location
    animal_data["type"] = animal_type

    return animal_data


def serialize_animal(animal_data):
    """Returns the html for a single animal"""

    animal_data_string = ""
    animal_data_string += get_li_begin()
    animal_data_string += get_name_div(animal_data["name"])
    animal_data_string += get_p_begin()
    animal_data_string += add_single_animal_attribute("Diet", animal_data["diet"])
    animal_data_string += add_single_animal_attribute(
        "Location", animal_data["location"]
    )
    animal_data_string += add_single_animal_attribute("Type", animal_data["type"])
    animal_data_string += get_p_end()
    animal_data_string += get_li_end()

    return animal_data_string


def add_single_animal_attribute(attr_name, attr_value):
    """
    Returns a strong tag for a single attribute of an animal if it is not None.
    If it is None, it returns an empty string
    """

    if attr_value:
        return f"<strong/>{attr_name}: </strong>{attr_value}<br/>\n"
    else:
        return ""


def get_li_begin():
    """Returns a string for opening a html li element"""

    return "<li class='cards__item'>\n"


def get_li_end():
    """Returns a string for ending a html li element"""

    return "</li>\n"


def get_name_div(animal_name):
    """Returns the animal div string if the animal name if not None"""

    if animal_name:
        return f"<div class='card__title'>{animal_name}</div>\n"
    else:
        return ""


def get_p_begin():
    """Returns a string for opening a p html element"""

    return "<p class='card__text'>\n"


def get_p_end():
    """Returns a string for endling a html element"""

    return "</p>"


def replace_template_with_string(template_path, html_path, data_string):
    """
    Loads the html template, replaces the placeholder with the data string and writes the html to a given path
    """

    template_string = load_template(template_path)
    html_string = template_string.replace("__REPLACE_ANIMALS_INFO__", data_string)
    write_html(html_path, html_string)


def main():
    animal_data_string = get_animal_data_from_json_file("animals_data.json")
    replace_template_with_string(
        "animals_template.html", "animal.html", animal_data_string
    )


if __name__ == "__main__":
    main()
