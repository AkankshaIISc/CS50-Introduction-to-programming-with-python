def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(words):
    #words  = word.upper()
    if 2 <= len(words) <= 6 and words[:2].isalpha():
        if words.isalpha():
            return True
        for i in range(2, len(words)):
            if words[i].isdigit():
                if words[i:].isdigit() and words[i] != '0':
                    return True
                else:
                    return False


main()






