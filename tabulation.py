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


def knapsack_tabulation(bank, list_key):
    n = len(list_key)

    tab = [[x for x in range(bank + 1)] for _ in range(n + 1)]

    for item in range(1, n + 1):
        item_key = list_key[item - 1]
        item_cost = DATA[item_key][0]
        item_value = DATA[item_key][1]
        for available_money in range(1, bank + 1):
            if item_cost <= available_money:
                include_item = item_value + tab[item - 1][available_money - item_cost]
                exclude_item = tab[item - 1][available_money]
                tab[item][available_money] = max(include_item, exclude_item)
            else:
                tab[item][available_money] = tab[item - 1][available_money]

    for row in tab:
        print(row)

    items_included = []
    w = bank
    for i in range(n, 0, -1):
        if tab[i][w] != tab[i - 1][w]:
            items_included.append(list_key[i - 1])
            w -= DATA[list_key[i - 1]][0]

    print("\nItems included:", items_included)

    return tab[n][bank]


def main():
    list_key = sorted(list(DATA.keys()), key=lambda x: DATA[x][2])
    bank = 500
    print(knapsack_tabulation(bank, list_key))


if __name__ == '__main__':
    start_time = time.time()
    main()
    print("--- %s seconds ---" % (time.time() - start_time))
