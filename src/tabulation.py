import time
from src.cleancsv import prepare_data_set

DATA = {}


def knapsack_tabulation(bank, list_key):
    """
    Function that generate an array containing the maximum value obtainable when selected items with a certain budget.
    :param bank: The budget to use, represent the weight of the knapsack problem.
    :param list_key: The list of keys that represent the items to consider.
    :return:
    """
    n = len(list_key)

    # Create a 2D array with dimension (n+1) x (bank+1).
    # Initialize each row with a simple range of values, where the value is equal to the bank, it will be overwritten.
    tab = [[x for x in range(bank + 1)] for _ in range(n + 1)]

    # Select every row one after the other.
    for item in range(1, n + 1):
        item_key = list_key[item - 1]
        item_cost = DATA[item_key][0]
        item_value = DATA[item_key][1]
        # Iterate all possible budget capacities from 1 to bank
        for available_money in range(1, bank + 1):
            # If the price of the item is bigger than the budget, include or exclude the item.
            if item_cost <= available_money:
                include_item = item_value + tab[item - 1][available_money - item_cost]
                exclude_item = tab[item - 1][available_money]
                tab[item][available_money] = max(include_item, exclude_item)
            # If the price of the item is smaller than the budget, use the previous best result for this budget.
            else:
                tab[item][available_money] = tab[item - 1][available_money]

    # Backtrack to find which items need to be selected.
    items_included = []
    w = bank
    for i in range(n, 0, -1):
        # If the result at tab[i][w] differs from tab[i-1][w], it means the current item need to be selected.
        if tab[i][w] != tab[i - 1][w]:
            items_included.append(list_key[i - 1])
            w -= DATA[list_key[i - 1]][0]

    return tab[n][bank], items_included


def tabulation(csv_path):
    """
    Execute the tabulation solution to find the best combination of items to maximize the bank value after two years.
    :param csv_path: The file path of the CSV dataset.
    """
    global DATA
    DATA = prepare_data_set(csv_path)
    # Sort the keys based on the gain factor.
    list_key = sorted(list(DATA.keys()), key=lambda x: DATA[x][2])
    bank = 50000
    start_time = time.time()
    max_value, selected_items = knapsack_tabulation(bank, list_key)
    print("--- %s seconds ---" % (time.time() - start_time))
    print("Max possible bank after two years : ", max_value / 100)
    print("Selected items to maximise gain : ", selected_items)


def main():
    tabulation("../data/Liste+d'actions+-+P7+Python+-+Feuille+1.csv")


if __name__ == '__main__':
    main()
