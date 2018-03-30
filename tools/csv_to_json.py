#! /usr/bin/python3

# How to use this script:
# python3 csv_to_json.py <file> <output_file> <desc_index> <keybinding_index> <delimiter> (<quote>)
# <file>: The CSV file to make JSON
# <output_file>: The file to write the JSON to
# <desc_index>: The index in each row that the description is on
# <keybinding_index>: The index in each row that the keybinding is on
# <delimiter>: The character that seperates values, usually a comma
# <quote>: The character that quotes values
import csv
import json
import sys

if len(sys.argv) < 6:  # The script name counts as an argument
    raise ValueError("There must be five arguments, an input file, an output file, a desc index, a keybinding index, "
                     "and a delimiter.")

FILE = sys.argv[1]
OUTPUT = sys.argv[2]
DESC_INDEX = int(sys.argv[3])
KEYBINDING_INDEX = int(sys.argv[4])
DELIMITER = sys.argv[5]
QUOTE = "" if len(sys.argv) == 6 else sys.argv[6]

with open(FILE) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=DELIMITER, quotechar=QUOTE)
    keybindings_object = {}
    for row in csv_reader:
        desc = row[DESC_INDEX]
        keybinding = row[KEYBINDING_INDEX]
        if desc not in keybindings_object.keys():
            keybindings_object[desc] = keybinding
        elif type(keybindings_object[desc]) == list and keybinding not in keybindings_object[desc]:
            keybindings_object[desc].append(keybinding)
        elif keybindings_object[desc] != keybinding and type(keybindings_object[desc]) != list:
            keybindings_object[desc] = [keybindings_object[desc], keybinding]
    with open(OUTPUT, "w") as json_file:
        json.dump(keybindings_object, json_file, indent=2)
