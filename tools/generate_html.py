#! /usr/bin/python3

# How to use this script:
# python3 generate_html.py <file> <output_file>
# <file>: The keybindings file to turn into HTML
# <output_file>: The file to write the HTML to

import json
import sys

if len(sys.argv) != 3:  # The script name counts as an argument
    raise ValueError("There must be two arguments, an input file and an output file.")

with open(sys.argv[1]) as input_file:
    shortcuts = json.load(input_file)
    with open(sys.argv[2], "w") as output:
        output.write("<!DOCTYPE html><html><head><title>Keybindings: {0}</title><body><table><thead><tr>"
                     "<td>Keybinding Description</td><td>Keybinding</td></tr></thead><tbody>".format(sys.argv[1]))

        for shortcut_description in shortcuts:
            output.write("<tr>\n<td>")
            output.write(shortcut_description)
            output.write("</td><td>")
            output.write(str(shortcuts[shortcut_description]))
            output.write("</td><tr>")

        output.write("</tbody></table></body></html>")
