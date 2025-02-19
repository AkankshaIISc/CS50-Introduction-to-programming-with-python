import inflect

p = inflect.engine()
name = []
while True:
    try:
        x = input("Name: ")
        name.append(x)

    except EOFError:
        name_join = p.join(name)
        print()
        print(f"Adieu, adieu, to {name_join}")
        break





