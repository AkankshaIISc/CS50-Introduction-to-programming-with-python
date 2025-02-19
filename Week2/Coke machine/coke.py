def balance(amount_due=50):
    print(f"Amount Due: {amount_due}")
    while True:
        x = int(input("Insert Coin: "))
        if x in [5,10,25]:
            amount_due-=x
            if amount_due > 0:
                print(f"Amount Due: {amount_due}")
                continue
            else:
                print(f"Change Owed: {-1*amount_due}")
                break
        else:
            print(f"Amount Due: {amount_due}")


def main():
    balance()

main()
