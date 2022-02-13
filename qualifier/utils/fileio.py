# -*- coding: utf-8 -*-
"""Helper functions to load and save CSV data.

This contains a helper function for loading and saving CSV files.

"""
import csv
import questionary
import sys
from pathlib import Path

def load_csv(csvpath):
    """Reads the CSV file from path provided.

    Args:
        csvpath (Path): The csv file path.

    Returns:
        A list of lists that contains the rows of data from the CSV file.

    """
    with open(csvpath, "r") as csvfile:
        data = []
        csvreader = csv.reader(csvfile, delimiter=",")

        # Skip the CSV Header
        next(csvreader)

        # Read the CSV data
        for row in csvreader:
            data.append(row)
    return data

def save_qualifying_loans(qualifying_loan_list):
    """Saves the CSV file from path provided.

    Args:
        csvpath (Path): The CSV file path.
        data (list of lists): A list of the rows of data for the CSV file.
        header (list): An optional header for the CSV.

    """
    print (qualifying_loan_list)

    confirm_save = questionary.confirm("Are you sure you want to save this loan list?").ask()

    if confirm_save: 
        header = ["Loan Name"]
        file_save_location = questionary.text("What is the location you want to save your file? Enter path:").ask()
        file_save_location = file_save_location + questionary.text("What is the file name you want to use?").ask()
        output_path = Path(file_save_location)
        
        with open(output_path, "w") as csvfile:
            csvwriter = csv.writer(csvfile)
            csvwriter.writerow(header)
            for row in qualifying_loan_list:
                csvwriter.writerow([row])
        print("Successful! Your file is saved.")
        sys.exit()
    else:
        print("Thanks for using the Loan Qualifier App")
        sys.exit()
