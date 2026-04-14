# Import the csv module for reading CSV files
import csv


# Function to read test data from a CSV file and return it as a list of dictionaries
def read_test_data(file_path):
    # Initialize an empty list to store the test data rows
    data = []
    # Open the CSV file in read mode with newline='' for proper line ending handling
    with open(file_path, newline='') as file:
        # Create a DictReader object to read the CSV file, using first row as headers
        reader = csv.DictReader(file)
        # Iterate through each row in the CSV file
        for row in reader:
            # Append each row (as a dictionary) to the data list
            data.append(row)
    # Return the complete list of dictionaries containing all test data
    return data