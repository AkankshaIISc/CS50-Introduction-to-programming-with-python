def main():
    x = input("Greeting: ")
    print(value(x))

def value(greeting):
    if greeting.lower().replace(",", "").split(" ")[0] == "hello":
        return "$0"
    elif greeting.lower()[0] == "h":
        return "$20"
    else:
        return "$100"

if __name__ == "__main__":
    main()
