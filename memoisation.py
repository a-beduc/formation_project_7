import time


DATA = {
    "#0001": (20, 21, 0.05),
    "#0002": (30, 33, 0.10),
    "#0003": (50, 57.5, 0.15),
    "#0004": (70, 84, 0.20),
    "#0005": (60, 70.2, 0.17),
    "#0006": (80, 100, 0.25),
    "#0007": (22, 23.54, 0.07),
    "#0008": (26, 28.86, 0.11),
    "#0009": (48, 54.24, 0.13),
    "#0010": (34, 43.18, 0.27),
    "#0011": (42, 49.14, 0.17),
    "#0012": (110, 119.9, 0.09),
    "#0013": (38, 46.74, 0.23),
    "#0014": (14, 14.14, 0.01),
    "#0015": (18, 18.54, 0.03),
    "#0016": (8, 8.64, 0.08),
    "#0017": (4, 4.48, 0.12),
    "#0018": (10, 11.4, 0.14),
    "#0019": (24, 29.04, 0.21),
    "#0020": (114, 134.52, 0.18),
}

MEMO = []
MEMO_CALL = 0

def knapsack_memoization(bank, n, list_key):
    global MEMO, MEMO_CALL

    if MEMO[n][bank] is not None:
        MEMO_CALL += 1
        return MEMO[n][bank]

    if n == 0 or bank == 0:
        result = bank, []

    elif DATA[list_key[n - 1]][0] > bank:
        result = knapsack_memoization(bank, n - 1, list_key)

    else:
        include_value, new_item_list = knapsack_memoization(
            bank - DATA[list_key[n - 1]][0], n - 1, list_key)
        include_value += DATA[list_key[n - 1]][1]
        new_item_list = new_item_list + [list_key[n - 1]]

        exclude_value, old_item_list = knapsack_memoization(bank, n - 1, list_key)

        if include_value > exclude_value:
            result = include_value, new_item_list
        else:
            result = exclude_value, old_item_list

    MEMO[n][bank] = result
    return result


def main():
    global MEMO
    list_key = sorted(list(DATA.keys()), key=lambda x: DATA[x][2], reverse=True)
    bank = 500
    n = len(list_key)
    MEMO = [[None] * (bank + 1) for _ in range(n + 1)]
    max_value, selected_items = knapsack_memoization(bank, n, list_key)
    print("Max possible bank after two years : ", max_value)
    print("Selected items to maximise gain : ", selected_items)
    print("Call to memoization : ", MEMO_CALL)


if __name__ == '__main__':
    start_time = time.time()
    main()
    print("--- %s seconds ---" % (time.time() - start_time))

