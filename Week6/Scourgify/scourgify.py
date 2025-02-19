import csv
import sys

if len(sys.argv) < 3:
    sys.exit("Too few command-line arguments")
elif len(sys.argv) > 3:
    sys.exit("Too many command-line arguments")
else:
    before = sys.argv[1]
    after = sys.argv[2]
    if "." in before and "csv" in before.split("."):
        try:
            with open(f"{before}") as file:
                reader = csv.DictReader(file)
                with open(f"{after}", "w", newline ="") as output_file:
                    writer = csv.DictWriter(output_file, fieldnames = ['first', 'last', 'house'])
                    writer.writeheader()
                    for line in reader:
                        lastname, firstname = line['name'].split(", ")
                        housename = line['house']
                        writer.writerow({'first': firstname, 'last': lastname, 'house': housename})
        except FileNotFoundError:
            sys.exit(f"Could not read {sys.argv[1]}")
    else:
        sys.exit("Not a csv file")




