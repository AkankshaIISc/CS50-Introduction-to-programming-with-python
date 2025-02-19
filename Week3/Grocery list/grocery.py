def main():
    try:
        grow = []
        while True:
            fr = input("")
            fr_upper = fr.upper()
            grow.append(fr_upper)
    except EOFError:
         pass
    except KeyError:
            pass
    grocery_count = grocery(grow)
    count_gro(grocery_count)


def grocery(count):
    count_item = {}
    for key in count:
        counts = count_item.get(key, 0)
        count_item[key] = counts + 1
    return count_item

def count_gro(dic1):
    for key, value in sorted(dic1.items()):
       print(f"{value} {key}")

main()


