def convert(str1):
    # if ":)" in str1:
    #     return str1.replace(":)", "🙂")
    # elif ":(" in str1:
    #     return str1.replace(":(", "🙁")
    # else:
    #     return str1
    return str1.replace(":)", "🙂").replace(":(", "🙁")

def main():
    word = input("")
    print(convert(word))




main()



