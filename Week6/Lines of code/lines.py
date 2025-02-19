import sys

if len(sys.argv) == 1:
    sys.exit("Too few command-line arguments")

elif len(sys.argv) > 2:
    sys.exit("Too many command-line arguments")

else:
    code_file = sys.argv[1]
    if "." in code_file and "py" in code_file.split("."):
        try:
            with open(f"{code_file}") as file:
                count = 0
                for line in file:
                    if line.lstrip().startswith("#") or line.isspace():
                        pass
                    else:
                        count += 1
                print(f"{count}")

        except FileNotFoundError:
            print("File does not exist")

    else:
        sys.exit("Not a Python file")
