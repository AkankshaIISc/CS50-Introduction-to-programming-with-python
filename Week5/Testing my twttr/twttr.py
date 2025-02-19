def main():
    x = input("")
    print(shorten(x))



def shorten(word):
        vowels = ["A", "E", "I", "O", "U", "a","e", "i", "o", "u"]
        word_new = [char for char in word if char not in vowels]
        word_w_v = "".join(word_new)
        return word_w_v


if __name__ == "__main__":
    main()
