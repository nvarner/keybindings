#! /usr/bin/python3

# How to use this script:
# python3 json_to_csv.py <file> <output_file>
# <file>: The JSON file to make CSV
# <output_file>: The file to write the CSV to
import csv
import json
import sys

if len(sys.argv) != 3:  # The script name counts as an argument
    raise ValueError("There must be two arguments, an input file and an output file.")

FILE = sys.argv[1]
OUTPUT = sys.argv[2]

with open(FILE) as file:
    json_file = json.load(file)
    keybindings = json_file["keybindings"]
    metadata = json_file["metadata"]
    with open(OUTPUT, "w") as output:
        csv_writer = csv.writer(output, quotechar="\"", quoting=csv.QUOTE_ALL)
        csv_writer.writerow(["metadata"] + list(metadata.items()))
        for description in keybindings:
            keybinding = keybindings[description]
            if type(keybinding) == list:
                for binding in keybinding:
                    csv_writer.writerow([description, binding])
            else:
                csv_writer.writerow([description, keybinding])
