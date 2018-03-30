#! /usr/bin/python3

# How to use this script:
# python3 generate_html.py <file> <output_file>
# <file>: The keybindings file to turn into HTML
# <output_file>: The file to write the HTML to

import json
import sys

if len(sys.argv) != 3:  # The script name counts as an argument
    raise ValueError("There must be two arguments, an input file and an output file.")


def create_table_row(description, shortcut):
    return "<tr><td>{0}</td><td>{1}</td><tr>".format(description, shortcut)


with open(sys.argv[1]) as input_file:
    shortcuts = json.load(input_file)
    with open(sys.argv[2], "w") as output:
        output.write("<!DOCTYPE html><html><head><title>Keybindings: {0}</title><body><table><thead><tr>"
                     "<td>Keybinding Description</td><td>Keybinding</td></tr></thead><tbody>".format(sys.argv[1]))

        for shortcut_description in shortcuts:
            if type(shortcuts[shortcut_description]) == list:
                for each in shortcuts[shortcut_description]:
                    output.write(create_table_row(shortcut_description, each))
            else:
                output.write(create_table_row(shortcut_description, shortcuts[shortcut_description]))

        output.write("</tbody></table></body></html>")
