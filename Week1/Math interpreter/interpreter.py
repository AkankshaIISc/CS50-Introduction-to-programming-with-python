def interpreter(express):
    operator = express.split(" ")

    x = float(operator[0])
    y = operator[1]
    z = float(operator[2])

    if y == "+":
        return x + z
    elif y == "*":
        return x * z
    elif y == "/":
        if z == 0:
            return "Division by zero"
        else:
            return x / z
    elif y == "-":
        return x - z
    else:
        return "Enter valid input"
def main():
    user = input("Expression:")
    users = interpreter(user)
    print(users)

main()


