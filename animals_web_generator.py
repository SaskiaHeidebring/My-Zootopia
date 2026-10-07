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
    animal_data_string = ""
    for animal in animals_data:
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

        animal_data_string += get_li_begin()
        animal_data_string += add_single_animal_attribute("Name", animal_name)
        animal_data_string += add_single_animal_attribute("Diet", animal_diet)
        animal_data_string += add_single_animal_attribute("Location", animal_location)
        animal_data_string += add_single_animal_attribute("Type", animal_type)
        animal_data_string += get_li_end()

    return animal_data_string


def add_single_animal_attribute(attr_name, attr_value):
    """
    Returns a string for a single attribute of an animal if it is not None.
    If it is None, it returns an empty string
    """

    if attr_value:
        return f"{attr_name}: {attr_value}<br/>\n"
    else:
        return ""


def get_li_begin():
    """Returns a string for opening an html li element"""

    return "<li class='cards__item'>\n"


def get_li_end():
    """Returns a string for ending an html li element"""

    return "</li>\n"


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
