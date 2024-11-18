DATA = {"a": 80, "b": 20, "c": 30, "d": 40}
OUTPUT = set(())


def find_path(bank, current_path_key, list_available_key):
    copy_available_keys = list_available_key.copy()
    current_path_key = current_path_key.copy()

    # Rebuild a list of key where we remove a key if the cost to reach it is too much
    available_keys = [key for key in copy_available_keys if bank - DATA[key] >= 0]

    test_path = current_path_key + list_available_key

    # Break out of recursion if the remaining possible paths is already reached by another branch
    if tuple(sorted(test_path)) in OUTPUT:
        return

    # Store the path if the available path are non-existent (meaning, the list of possible key is empty)
    if len(available_keys) == 0:
        if tuple(sorted(current_path_key)) not in OUTPUT:
            OUTPUT.add(tuple(sorted(current_path_key)))
        return

    # Recursion on available paths
    for key in available_keys:
        new_bank = bank - DATA[key]
        new_current_path_key = current_path_key + [key]
        new_available_keys = available_keys.copy()
        new_available_keys.remove(key)
        find_path(new_bank, new_current_path_key, new_available_keys)


def main():
    bank = 100
    starting_available_key = ["a", "b", "c", "d"]
    find_path(bank, [], starting_available_key)
    print(OUTPUT)


if __name__ == '__main__':
    main()
