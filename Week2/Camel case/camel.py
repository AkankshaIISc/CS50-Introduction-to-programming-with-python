def convert(x):
    snake_case = []
    for char in x:
        if char.isupper():
            snake_case.append('_')
        snake_case.append(char.lower())
    return ''.join(snake_case)

def main():
    user = input("camelCase: ")
    snake = convert(user)
    print("snake_case: ", snake)

main()

