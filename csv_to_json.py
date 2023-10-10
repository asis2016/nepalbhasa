import csv
import json


lang_key = 'English'
csv_file_path = 'dictionary.csv'
json_file_path = 'dictionary.json'
json_minified_file_path = 'dictionary.minified.json'


def main():
    """
    Main
    """
    csv_to_json(csv_file_path, json_file_path, lang_key)
    minify_json(json_file_path)


def csv_to_json(csv_file, json_file, lang_key):
    """
    Function to convert CSV to JSON.
    """
    data = []
    with open(csv_file, 'r') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            data.append(row)
    
    # Sort the data list of dictionaries by the `lang_key`
    for item in data:
        item[lang_key] = item[lang_key].lower()
    sorted_data = sorted(data, key=lambda x: x[lang_key])

    with open(json_file, 'w') as json_file:
        json.dump(sorted_data, json_file, indent=4)


def minify_json(json_file):
    """
    Minify the JSON.
    """
    with open(json_file, 'r') as json_file:
        data = json.load(json_file)

    minfied_json = json.dumps(data, separators=(',', ':'))

    with open(json_minified_file_path, 'w') as output_file:
        output_file.write(minfied_json)

main()