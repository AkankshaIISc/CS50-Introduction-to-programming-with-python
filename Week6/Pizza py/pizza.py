from tabulate import tabulate
import sys
import csv

if len(sys.argv) == 1:
    sys.exit("Too few command-line arguments")

elif len(sys.argv) > 2:
    sys.exit("Too many command-line arguments")

else:
    table_file = sys.argv[1]
    if "." in table_file and "csv" in table_file.split("."):
        try:
            with open(f"{table_file}") as file:
                file_read = csv.reader(file)
                headers = next(file_read)
                data = list(file_read)
                print(tabulate(data, headers, tablefmt = "grid"))
        except FileNotFoundError:
            sys.exit("File does not exist")
    else:
        sys.exit("Not a CSV file")
