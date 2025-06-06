#!/usr/bin/python3
"""Module to convert CSV data to JSON format"""

import csv
import json


def convert_csv_to_json(csv_filename):

    try:
        with open(csv_filename,'r',) as csv_file:
            reader = csv.DictReader(csv_file)
            data = [row for row in reader]

        with open("data.json",'w',) as json_file:
            json.dump(data, json_file)

        return True

    except FileNotFoundError:
        return False
    except Exception:
        return False
