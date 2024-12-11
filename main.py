from src import bruteforce, memoization, tabulation


def input_loop():
    """
    Prompt the user to select an algorithm and a dataset to run it.
    Show the user the time it tooks the algorithm to compute.
    The value the user would have after two years.
    The list of Action to buy to achieve the best possible value after two years.
    """
    links = {"1": "data/Liste+d'actions+-+P7+Python+-+Feuille+1.csv",
             "2": "data/dataset1_Python+P7.csv",
             "3": "data/dataset2_Python+P7.csv"}
    algorithm = {"1": bruteforce.brute_force,
                 "2": memoization.memoization,
                 "3": tabulation.tabulation}

    print("Which algorithm do you want to use.\n")
    selected_algorithm = 0
    while selected_algorithm not in ("1", "2", "3"):
        print("\nPress a number to select an algorithm\n"
              "(1) : bruteforce\n"
              "(2) : memoisation\n"
              "(3) : tabulation\n")
        selected_algorithm = input("Press a number: ")
    if selected_algorithm == "1":
        print("\nYou have selected the Bruteforce algorithm, test with Basic dataset (20 actions).")
        algorithm[selected_algorithm](links["1"])
    else:
        print("Choose a dataset.\n")
        selected_dataset = 0
        while selected_dataset not in ("1", "2", "3"):
            print("\nPress a number to select a dataset.\n"
                  "(1) : Basic dataset (20 actions)\n"
                  "(2) : Dataset 1\n"
                  "(3) : Dataset 2\n")
            selected_dataset = input("Press a number: ")
        algorithm[selected_algorithm](links[selected_dataset])


def main():
    while True:
        input_loop()
        print("To exit, press CTRL+Z")
        input()


if __name__ == '__main__':
    main()
