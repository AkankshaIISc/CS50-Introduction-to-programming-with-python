def main():
    x = input("Greeting:")
    #y = x.strip()
    if len(x.strip()) >= 5 and x.strip()[0:5] == "Hello":
        print("$0")
    elif x[0].strip() == "H":
        print("$20")
    else:
        print("$100")

main()
