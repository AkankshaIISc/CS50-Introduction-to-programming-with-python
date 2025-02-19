def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(words):
    #words  = word.upper()
    if 2 <= len(words) <= 6 and words[:2].isalpha():
        for i in range(len(words)):
            if words[i] in ["!", " ", ".", ",", ":", "?", "/", ";"]:
                return False
            else:
                if words.isalpha():
                    return True
                for i in range(2, len(words)):
                    if words[i].isdigit():
                        if words[i:].isdigit() and words[i] != '0':
                            return True
                        else:
                            return False
    else:
        return False


if __name__ == "__main__":
    main()
