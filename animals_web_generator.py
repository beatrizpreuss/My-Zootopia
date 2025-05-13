import json


def load_data(file_path):
  """ Loads a JSON file """
  with open(file_path, "r") as handle:
    return json.load(handle)


def get_html(html_file):
    html = open(html_file)
    return html.read()


def get_info():
    animals_data = load_data('animals_data.json')
    output = ""
    for animal in animals_data:
        try:
            output += (f"Name: {animal["name"]}\n"
                       f"Diet: {animal["characteristics"]["diet"]}\n"
                       f"Location: {animal["locations"][0]}\n"
                       f"Type: {animal["characteristics"]["type"]}\n"
                       f"\n")
        except KeyError:
            continue
    return output


def replace_info():
    original_html = get_html("animals_template.html")
    animals_info = get_info()
    new_html = original_html.replace("__REPLACE_ANIMALS_INFO__", animals_info)
    return new_html


def write_html():
    info = replace_info()
    with open("animals.html", "a") as new_html:
        new_html.write(info)


def main():
    write_html()


if __name__ == "__main__":
    main()