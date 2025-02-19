import re
import sys


def main():
    ip = input("IPv4 Address: ")
    print(validate(ip))


def validate(num):
    try:
        if values := re.search(r"^([0-9]{1,3})\.([0-9]{1,3})\.([0-9]{1,3})\.([0-9]{1,3})$", num):
            if 0 <= int(values.group(1)) <= 255:
                i = 2
                for i in range(2, 5):
                    if 0 <= int(values.group(i)) <= 255:
                        i += 1
                    else:
                        return False
                return True
            else:
                return False
        else:
            return False
    except ValueError:
        return False


if __name__ == "__main__":
    main()
