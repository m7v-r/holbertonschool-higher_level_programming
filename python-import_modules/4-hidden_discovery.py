#!/usr/bin/python3
if __name__ == "__main__":
    import hidden_4

    # Get all names defined in the module
    all_names = dir(hidden_4)

    # Sort the names alphabetically
    all_names.sort()

    # Filter and print names that do not start with "__"
    for name in all_names:
        if not name.startswith("__"):
            print("{}".format(name))
