import csv


def read_test_data(file_path):
    data = []
    with open(file_path, newline='') as file:
        reader = csv.DictReader(file)
        for row in reader:
            data.append(row)
    return data