import csv
import os
from Classes.database import conn

def csv_import():
    print("For csv file importation, save your csv file in this project's folder then press enter")
    print("Ensure it follows the format (amount, transaction type (income/expense), description, date(YYYY-MM-DD), account_id, category_id)")
    print("Do not include headers")
    input()
    file_name = input("Please enter your file's name (with or without .csv): ")

    if not file_name.lower().endswith(".csv"):
        file_name += ".csv"

    # if not os.path.exists(file_name):
    #     print("File not found. Please try again")
    #     csv_import()
        

    try:
        with open(file_name, 'r') as csv_file:
            reader = csv.reader(csv_file)
            count = 0
            for row in reader:
                if len(row) < 6:
                    print(f"Error on row {count+1}. Skipping...")
                    continue

                amount = float(row[0])
                transaction_type = row[1].strip().lower()
                description = row[2].strip()
                date = row[3].strip()
                account_id = int(row[4])
                category_id = int(row[5])

                conn.execute(
                    """
                        INSERT INTO transactions (amount, type, description, date, account_id, category_id)
                        VALUES (?, ?, ?, ?, ?, ?)
                    """,
                    (amount, transaction_type, description, date, account_id, category_id)
                )

                count += 1

            conn.commit()
            print(f"Successfully imported {count} transactions!")

                
    except ValueError as e:
        print(f"Data type error in CSV formatting: {e}. Ensure amounts/IDs are numbers and dates are in the format YYYY-MM-DD")

    except Exception as e:
        print(f"An error occured during import: {e}")
