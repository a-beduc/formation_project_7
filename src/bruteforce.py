import time
from src.cleancsv import prepare_data_set


DATA = {}


def knapsack_brute_force(bank, n, list_key):
    """
    Recursive function that computes the maximum value obtainable from including or excluding items from a list.
    :param bank: The budget to use, represent the weight of the knapsack problem.
    :param n: The index of the current item to consider.
    :param list_key: The list of keys that represent the items to consider.
    :return: A tuple (best_value, selected_items_list) where:
            - best_value is the maximum achievable bank value after two years.
            - selected_items_list is a list of keys corresponding to the actions chosen to achieve this maximum value.
    """
    # if no items are left or no bank remains, return rest of the bank.
    if n == 0 or bank == 0:
        return bank, []

    # if the cost of the current item exceeds the remaining bank, skip the item.
    elif DATA[list_key[n - 1]][0] > bank:
        return knapsack_brute_force(bank, n - 1, list_key)

    else:
        # include the current item, deduct the item cost from the bank and recurse.
        include_value, new_item_list = knapsack_brute_force(
            bank - DATA[list_key[n - 1]][0], n - 1, list_key)
        include_value += DATA[list_key[n - 1]][1]
        new_item_list = new_item_list + [list_key[n - 1]]

        # exclude the current_item and recurse.
        exclude_value, old_item_list = knapsack_brute_force(bank, n - 1, list_key)

        # return the case (include or exclude) that yields the higher value.
        if include_value > exclude_value:
            return include_value, new_item_list
        else:
            return exclude_value, old_item_list


def brute_force(csv_path):
    """
    Execute the brute-force solution to find the best course of action to maximise gain from a CSV file.
    :param csv_path: The file path of the CSV dataset.
    """
    global DATA
    DATA = prepare_data_set(csv_path)
    # Sort the keys based on the gain factor.
    list_key = sorted(list(DATA.keys()), key=lambda x: DATA[x][2])
    bank = 50000
    n = len(list_key)
    start_time = time.time()
    max_value, selected_items = knapsack_brute_force(bank, n, list_key)
    print("--- %s seconds ---" % (time.time() - start_time))
    print("Max possible bank after two years : ", max_value / 100)
    print("Selected items to maximise gain : ", selected_items)


def main():
    brute_force("../data/Liste+d'actions+-+P7+Python+-+Feuille+1.csv")


if __name__ == '__main__':
    main()
