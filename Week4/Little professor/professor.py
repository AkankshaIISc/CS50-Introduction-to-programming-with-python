import random


def main():
    level1 = get_level()
    generate_integer(level1)

    ...


def get_level():
    while True:
        try:
            level = int(input("Level: "))
            if level in [1, 2, 3]:
                return level
            else:
                continue
        except ValueError:
            continue
        break



def generate_integer(level):
    while True:
        try:
            if int(level) == 1:
                while True:
                    score = 0
                    for i in range(10):
                        n1 = random.randint(0,9)
                        n2 = random.randint(0,9)
                        total = n1 + n2
                        for j in range(3):
                            try:
                                x = int(input(f"{n1} + {n2} = "))
                                if x == total:
                                    score+=1
                                    break
                            #break
                                else:
                                    print("EEE")
                                    if j == 2:
                                        print(f"{n1} + {n2} = {total}")
                                    continue
                            except:
                                print("EEE")
                                if j == 2:
                                    print(f"{n1} + {n2} = {total}")
                                    break
                                continue

                    print(f"Score: {score}")



                    break

            elif int(level) == 2:
                while True:
                    score = 0
                    for i in range(10):
                        n1 = random.randint(10,99)
                        n2 = random.randint(10,99)
                        total = n1 + n2
                        for j in range(3):
                            try:
                                x = int(input(f"{n1} + {n2} = "))
                                if x == total:
                                    score+=1
                                    break
                            #break
                                else:
                                    print("EEE")
                                    if j == 2:
                                        print(f"{n1} + {n2} = {total}")
                                    continue
                            except:
                                print("EEE")
                                if j == 2:
                                    print(f"{n1} + {n2} = {total}")
                                    break
                                continue

                    print(f"Score: {score}")


                    break

            elif int(level) == 3:
                while True:
                    score = 0
                    for i in range(10):
                        n1 = random.randint(100,999)
                        n2 = random.randint(100,999)
                        total = n1 + n2
                        for j in range(3):
                            try:
                                x = int(input(f"{n1} + {n2} = "))
                                if x == total:
                                    score+=1
                                    break
                            #break
                                else:
                                    print("EEE")
                                    if j == 2:
                                        print(f"{n1} + {n2} = {total}")
                                    continue
                            except:
                                print("EEE")
                                if j == 2:
                                    print(f"{n1} + {n2} = {total}")
                                    break
                                continue

                    print(f"Score: {score}")


                    break

        except ValueError:
            pass
        break


if __name__ == "__main__":
    main()
