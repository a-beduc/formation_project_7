import csv


def clean_row(cost, gain):
    """
    Clean strings extracted from a csv.
    :param cost: A string representing the initial cost.
    :param gain: A string representing the gain as a percentage.
    :return: A tuple containing
            - cleaned_cost(int) : The cost multiplied by 100 as an int.
            - value_after_two_years(float) : The value of the action after two years multiplied by 100 as a float.
            - cleaned_gain : The gain as a decimal (10% -> 0.10).
    """
    cleaned_cost = int(float(cost) * 100)
    cleaned_gain = round(float(gain.replace("%", "")) / 100, 4)
    value_after_two_years = round(cleaned_cost * (1 + cleaned_gain), 2)
    return cleaned_cost, value_after_two_years, cleaned_gain


def prepare_data_set(csv_path):
    """
    Open a CSV file, filter out rows with non-positive or null cost, and produce a dictionary with cleaned data.
    :param csv_path: A string to the file path of the CSV file.
    :return: A dictionary where:
            - Keys are actions_id
            - Values are tuples produced by 'clean_row'.
    """
    dataset = {}
    with open(csv_path) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        next(csv_reader)
        for row in csv_reader:
            if float(row[1]) <= 0:
                continue
            dataset[row[0]] = clean_row(row[1], row[2])
    return dataset


def main():
    data = prepare_data_set("../data/dataset2_Python+P7.csv")
    print(data)


if __name__ == '__main__':
    main()
