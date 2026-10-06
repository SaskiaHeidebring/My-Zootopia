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


def print_animal_data():
    """Loads animal data from a given json file and prints it to the console"""
    animals_data = load_data("animals_data.json")

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

        print_single_animal_attribute("Name", animal_name)
        print_single_animal_attribute("Diet", animal_diet)
        print_single_animal_attribute("Location", animal_location)
        print_single_animal_attribute("Type", animal_type)
        print()


def print_single_animal_attribute(attr_name, attr_value):
    """Prints a single attribute of an animal if it not None"""

    if attr_value:
        print(f"{attr_name}: {attr_value}")


def main():
    print_animal_data()


if __name__ == "__main__":
    main()
