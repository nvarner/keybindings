#! /usr/bin/python3

# How to use this script:
# python3 search.py <file> <search_term>
# <file>: The keybindings file to search in, relative to the script
# <search_term>: The search term for the function. Putting spaces in the term will create multiple terms that will be
#   searched.

import json
import re
import sys

if len(sys.argv) < 3:  # The script name counts as an argument
    raise ValueError("There must be two arguments, a file and a search term.")


def search_to_regex(search):
    search = search.split(" ")
    return re.compile("(" + "|".join(search) + ")+", re.IGNORECASE)


with open(sys.argv[1]) as file:
    shortcuts = json.load(file)
    regex = search_to_regex(" ".join(sys.argv[2:]))

    for shortcut_function in shortcuts:
        if regex.search(shortcut_function):
            valid_shortcuts = shortcuts[shortcut_function]
            if type(valid_shortcuts) == list:
                for valid_shortcut in valid_shortcuts:
                    print(shortcut_function + ": " + valid_shortcut)
            else:
                print(shortcut_function + ": " + valid_shortcuts)
