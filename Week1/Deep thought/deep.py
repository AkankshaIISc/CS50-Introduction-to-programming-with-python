
def message(letter):
    return letter.lower()


def main():
    ans = ("42", "forty two", "forty-two")
    x = input("What is the Answer to the Great Question of Life, the Universe, and Everything?")

    answer = "Yes" if message(x).strip() in ans else "No"
    print(answer)

main()



