import csv
import json


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
    sorted_data = sorted(data, key=lambda x: x[lang_key])

    with open(json_file, 'w') as json_file:
        json.dump(sorted_data, json_file, indent=4)

# Usage
lang_key = 'English'
csv_file_path = 'dictionary.csv'  # Replace with the path to your CSV file
json_file_path = 'dictionary.json'  # Replace with the desired path for the output JSON file

csv_to_json(csv_file_path, json_file_path, lang_key)
