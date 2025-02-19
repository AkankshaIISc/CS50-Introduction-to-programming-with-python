def main():

    print(fuel())


def fuel():
    while True:
        fraction = input("Fraction: ")
        # use an if condition for which you would re-prompt the user by using continue
        try:
            x, y = fraction.split("/")
            if int(x) <= int(y):
                frc = (int(x)/int(y)) * 100
                if frc <= 1:
                    return "E"
                elif frc >= 99:
                    return "F"
                else:
                    num = round(frc)
                    return f"{num}%"
            else:
                raise ValueError

        except (ValueError, ZeroDivisionError):
            pass



main()



