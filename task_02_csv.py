#!/usr/bin/python3
"""Convert CSV data to JSON format"""


import csv
import json

def convert_csv_to_json(csv_file, json_file='data.json'):

    try:
        with open(csv_file, mode='r', newline='', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            data = [row for row in reader]

        with open(json_file, mode='w', encoding='utf-8') as jsonfile:
            json.dump(data, jsonfile, indent=4)

    except Exception:
        pass
