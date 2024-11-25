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

BEST_GAIN = 0
BEST_PATH = []


def find_path(bank, current_path, current_gain, sorted_keys, start_index):
    global BEST_GAIN, BEST_PATH

    for i in range(start_index, len(sorted_keys)):
        key = sorted_keys[i]
        cost = DATA[key]
        gain = GAIN_AFTER_TWO_YEARS[key]

        if bank - cost >= 0:
            new_bank = bank - cost
            new_path = current_path + [key]
            new_gain = current_gain + gain
            find_path(new_bank, new_path, new_gain, sorted_keys, i + 1)
        else:
            break

    if (bank + current_gain) > BEST_GAIN:
        BEST_GAIN = bank + current_gain
        BEST_PATH = [current_path]
    elif current_gain == BEST_GAIN:
        BEST_PATH.append(current_path)


def main():
    global BEST_GAIN, BEST_PATH
    bank = 500
    sorted_keys = sorted(DATA.keys(), key=lambda x: DATA[x])
    find_path(bank, [], 0, sorted_keys, 0)
    print(f"Maximum Gain: {BEST_GAIN}")
    print(f"Best Paths: {BEST_PATH}")


if __name__ == '__main__':
    start_time = time.time()
    main()
    print("--- %s seconds ---" % (time.time() - start_time))
