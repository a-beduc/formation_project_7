import time


DATA = {
    "#0001": 20,
    "#0002": 30,
    "#0003": 50,
    "#0004": 70,
    "#0005": 60,
    "#0006": 80,
    "#0007": 22,
    "#0008": 26,
    "#0009": 48,
    "#0010": 34,
    "#0011": 42,
    "#0012": 110,
    "#0013": 38,
    "#0014": 14,
    "#0015": 18,
    "#0016": 8,
    "#0017": 4,
    "#0018": 10,
    "#0019": 24,
    "#0020": 114
}

GAIN_AFTER_TWO_YEARS = {
    "#0001": 21,
    "#0002": 33,
    "#0003": 57.5,
    "#0004": 84,
    "#0005": 70.2,
    "#0006": 100,
    "#0007": 23.54,
    "#0008": 28.86,
    "#0009": 54.24,
    "#0010": 43.18,
    "#0011": 49.14,
    "#0012": 119.9,
    "#0013": 46.74,
    "#0014": 14.14,
    "#0015": 18.54,
    "#0016": 8.64,
    "#0017": 4.48,
    "#0018": 11.4,
    "#0019": 29.04,
    "#0020": 134.52
}

OUTPUT = set()
MAPPING_OF_SUMS = {}


def initiate_mapping(starting_available_key):
    sum_of_values = sum(DATA.values())
    for i in range(len(starting_available_key)):
        MAPPING_OF_SUMS[i] = sum_of_values
        sum_of_values -= DATA[starting_available_key[i]]


def starting_path_research(bank, starting_available_key):
    for i in range(len(starting_available_key) - 1):
        if MAPPING_OF_SUMS[i] <= bank:
            OUTPUT.add(tuple(starting_available_key[i:]))
            return

        key = starting_available_key[i]
        cost = DATA[key]

        if bank - cost >= 0:
            current_path_key = [key]
            new_bank = bank - cost
            find_path(new_bank, current_path_key, starting_available_key, i + 1)


def find_path(bank, current_path_key, list_available_key, start_index):
    extended = False

    for i in range(start_index, len(list_available_key)):
        key = list_available_key[i]
        cost = DATA[key]
        if bank - cost >= 0:
            extended = True
            new_bank = bank - cost
            new_current_path_key = current_path_key + [key]
            find_path(new_bank, new_current_path_key, list_available_key, i + 1)
        else:
            break
    if not extended and current_path_key:
        OUTPUT.add(tuple(current_path_key))


def main():
    bank = 500
    starting_available_key = sorted(list(DATA.keys()), key=lambda x: DATA[x])
    initiate_mapping(starting_available_key)
    starting_path_research(bank, starting_available_key)
    dict_of_values = {}
    for path in OUTPUT:
        total_cost = sum(DATA[key] for key in path)
        remaining_bank = bank - total_cost
        total_gain_from_items = sum(GAIN_AFTER_TWO_YEARS[key] for key in path)
        total_gain = total_gain_from_items + remaining_bank
        dict_of_values[path] = total_gain

    max_gain = max(dict_of_values.values())
    best_paths = [path for path, gain in dict_of_values.items() if gain == max_gain]

    print(max_gain)
    print(best_paths)


if __name__ == '__main__':
    start_time = time.time()
    main()
    print("--- %s seconds ---" % (time.time() - start_time))
