import time
from src.cleancsv import prepare_data_set


DATA = {}
MEMO = []
MEMO_CALL = 0


def knapsack_memoization(bank, n, list_key):
    """
    Recursive function that computes the maximum value obtainable from including or excluding items from a list.
    Use memoization to avoid recomputing results.
    :param bank: The budget to use, represent the weight of the knapsack problem.
    :param n: The index of the current item to consider.
    :param list_key: The list of keys that represent the items to consider.
    :return: A tuple (best_value, selected_items_list) where:
            - best_value is the maximum achievable bank value after two years.
            - selected_items_list is a list of keys corresponding to the actions chosen to achieve this maximum value.
    """
    global MEMO, MEMO_CALL

    # if the result for this state (n, bank) has already been computed, return the result.
    if MEMO[n][bank] is not None:
        MEMO_CALL += 1
        return MEMO[n][bank]

    # if no items are left or no bank remains, return rest of the bank.
    if n == 0 or bank == 0:
        result = bank, []

    # if the cost of the current item exceeds the remaining bank, skip the item.
    elif DATA[list_key[n - 1]][0] > bank:
        result = knapsack_memoization(bank, n - 1, list_key)

    else:
        # include the current item, deduct the item cost from the bank and recurse.
        include_value, new_item_list = knapsack_memoization(
            bank - DATA[list_key[n - 1]][0], n - 1, list_key)
        include_value += DATA[list_key[n - 1]][1]
        new_item_list = new_item_list + [list_key[n - 1]]

        # exclude the current_item and recurse.
        exclude_value, old_item_list = knapsack_memoization(bank, n - 1, list_key)

        # return the case (include or exclude) that yields the higher value.
        if include_value > exclude_value:
            result = include_value, new_item_list
        else:
            result = exclude_value, old_item_list

    # Memorize the result in the cell of an array before returning
    MEMO[n][bank] = result
    return result


def memoization(csv_path):
    """
    Execute the memoization solution to find the best course of action to maximise gain from a CSV file.
    :param csv_path: The file path of the CSV dataset.
    """
    global DATA, MEMO
    DATA = prepare_data_set(csv_path)
    # Sort the keys based on the gain factor.
    list_key = sorted(list(DATA.keys()), key=lambda x: DATA[x][2], reverse=True)
    bank = 50000
    n = len(list_key)
    # Create an array made of empty (None) cell that may receive data MEMO[Item_id][Bank_value]
    MEMO = [[None] * (bank + 1) for _ in range(n + 1)]
    start_time = time.time()
    max_value, selected_items = knapsack_memoization(bank, n, list_key)
    print("--- %s seconds ---" % (time.time() - start_time))
    print("Max possible bank after two years : ", max_value/100)
    print("Selected items to maximise gain : ", selected_items)
    print("Call to memoization : ", MEMO_CALL)


def main():
    memoization("../data/Liste+d'actions+-+P7+Python+-+Feuille+1.csv")


if __name__ == '__main__':
    main()
