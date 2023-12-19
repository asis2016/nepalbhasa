__author__ = 'amaharjan.de'

import csv
import json


def main():
    '''
    This method does the following:
        1. converts CSV to JSON
        2. And, sorts and minifies the JSON
    '''
    # 1st, English
    csv_to_json(csv_file_path, json_file, lang_key)
    minify_json(json_file, json_minified_en)

    # 2nd, NepalBhasa
    nepalbhasa(json_file, json_minified_nb)


def csv_to_json(csv_file, json_file, lang_key):
    '''
    Function to convert CSV to JSON.
    '''
    print(f'[info] Converting CSV ({csv_file}) to JSON.')
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


def minify_json(json_in, json_out):
    '''
    Minify the JSON.
    '''
    print(f'[info] Minifying JSON ({json_in})')

    with open(json_in, 'r') as file:
        data = json.load(file)

    minfied_json = json.dumps(data, separators=(',', ':'))

    with open(json_out, 'w') as file:
        file.write(minfied_json)


def nepalbhasa(json_in, json_out):
    '''
    Sorts by key `NepalBhasa` and minifies `dictionary.json` into  `dictionary.nb.minified.json`.
    '''
    with open(json_in, 'r') as file:
        data = json.load(file)

    sorted_data = sorted(data, key=lambda x: x['NepalBhasa'])
    minfied_json = json.dumps(sorted_data, separators=(',', ':'))

    with open(json_out, 'w') as file:
        file.write(minfied_json)


if __name__ == '__main__':
    lang_key = 'English'
    csv_file_path = './assets/dictionary/dictionary.csv'
    json_file = './assets/dictionary/dictionary.json'
    json_minified_en = './assets/dictionary/dictionary.en.minified.json'
    json_minified_nb = './assets/dictionary/dictionary.nb.minified.json'
    json_minified_np = './assets/dictionary/dictionary.np.minified.json'
    json_minified_de = './assets/dictionary/dictionary.de.minified.json'
    
    main()