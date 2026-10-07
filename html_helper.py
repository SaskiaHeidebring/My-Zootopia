def get_ul_begin():
    """Returns a string for opening a html ul element"""

    return "<ul>"


def get_ul_end():
    """Returns a string for ending a html ul element"""

    return "</ul>"


def get_li_begin(class_name=None):
    """Returns a string for opening a html li element"""

    class_string = f"class='{class_name}'" if class_name else ""
    return f"<li {class_string}>\n"


def get_li_end():
    """Returns a string for ending a html li element"""

    return "</li>\n"


def get_name_div(animal_name):
    """Returns the animal div string if the animal name if not None"""

    if animal_name:
        return f"<div class='card__title'>{animal_name}</div>\n"
    else:
        return ""


def get_div_begin():
    """Returns a string for opening a div html element"""

    return "<div class='card__text'>\n"


def get_div_end():
    """Returns a string for endling a div html element"""

    return "</div>"
