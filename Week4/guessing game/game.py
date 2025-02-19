import random
while True:
    try:
        x = input("Level: ")
        if int(x) > 0:
            n = random.randint(1, int(x))
            while True:
                try:
                    guess = input("Guess: ")
                    if int(guess) < 0:
                        continue
                    if int(guess) < int(n):
                        print(f"Too small!")
                        continue
                    elif int(guess) > int(n):
                        print(f"Too large!")
                        continue
                    else:
                        print(f"just right!")
                        break
                except ValueError:
                    pass
            break

    except ValueError:
        pass


