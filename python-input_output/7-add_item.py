#!/usr/bin/python3
"""
This script adds all command line arguments to a Python list
and saves them to a file.
"""
import sys
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

filename = "add_item.json"

try:
    # Load existing list from file
    my_list = load_from_json_file(filename)
except FileNotFoundError:
    # If file doesn't exist, start with an empty list
    my_list = []

# Add command line arguments to the list (excluding the script name)
my_list.extend(sys.argv[1:])

# Save the updated list to the file
save_to_json_file(my_list, filename)
