
def main():
    print(food())

def food():
    Food = {"Baja Taco": 4.25, "Burrito": 7.50, "Bowl": 8.50, "Nachos": 11.00, "Quesadilla": 8.50, "Super Burrito": 8.50, "Super Quesadilla": 9.50, "Taco": 3.00, "Tortilla Salad": 8.00}
    food_item = {x.lower(): y for x, y in Food.items()}
    total = 0
    while True:
        try:
            item = input("Item: ")
            items = item.lower()
            if items in food_item:
                total += food_item[items]
                print(f"Total: ${total:.2f}")
            else:
                continue
        except (EOFError, KeyError):
            pass


main()







