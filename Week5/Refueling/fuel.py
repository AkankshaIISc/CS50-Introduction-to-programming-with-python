def main():
        while True:
             try:
                fraction = input("Fraction: ")
                fraction_num = convert(fraction)
                print(gauge(fraction_num))
                break

             except (ValueError, ZeroDivisionError):
                pass




def convert(fraction):
# use an if condition for which you would re-prompt the user by using continue
    x, y = fraction.split("/")
    if int(y) == 0:
        raise ZeroDivisionError
    elif int(x) <= int(y):
        frc = (int(x)/int(y)) * 100
        return round(frc)
    else:
        raise ValueError




def gauge(percentage):
     if percentage <= 1:
        return "E"
     elif percentage >= 99:
        return "F"
     else:
        return f"{percentage}%"



if __name__ == "__main__":
    main()
