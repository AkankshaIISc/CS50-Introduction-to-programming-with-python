def vowels():
    str1 = input("Input: ")
    omit_value = ["A", "E", "I", "O", "U", "a","e", "i", "o", "u"]
    filtered = [char for char in str1 if char not in omit_value]
    fil = "".join(filtered)
    print("Output: ", fil)

def main():
    vowels()

main()
