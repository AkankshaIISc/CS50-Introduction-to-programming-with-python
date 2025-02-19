import re

email = input("What's your email? ").strip()

# if "@" in email and "." in email:
#     print("valid")
# else:
#     print("Invalid")

# username, domain = email.split("@")
# if username and "." in domain.endswith(".edu"):
#     print("Valid")
# else:
#     print("Invalid")

###### regex #######
# re.search(pattern, string, flags = 0)
# . : any character except a newline
# * : 0 or more repetitions
# + : 1 or more repetition
# ? : 0 or 1 repetition
# {m} : m repetitions
# {m, n} : m-n repetitions
# ^ : matches the start fo the string
# $ : matches the end of the string or just before the newline at the end of the string
# [] : set of characters
# [^] : complementing the set
# \w : represents alpha numeric characters
# \d : decimal digit
# \D : not a decimal digit
# \s : whitespace character
# \S : not a whitespace character
# \w : word character including underscore
# \W : not a word character
# A|B : either A or B
# (...) : a group
# (?...) : non-capturing version
# re.IGNORECASE : treat case insensitively
# re.MULTILINE : if u want to match different lines of input
# re.DOTALL : any character plus new line


# if re.search("@", email): #same as first condition
#     print("Valid")
# else:
#     print("Invalid")


# if re.search(r".+@.+\.edu", email): #return valid even if we give a sentence as input (example: My name is malan@harvard.edu)
#     print("Valid")
# else:
#     print("Invalid")


# if re.search(r"^.+@.+\.edu$", email):
#     print("Valid")
# else:
#     print("Invalid")



# if re.search(r"^[^@]+@[^@]\.edu$", email): # [^@] every character except @ sign
#     print("Valid")
# else:
#     print("Invalid")



# if re.search(r"^[a-zA-Z0-9_]+@[a-zA-Z0-9_]+\.edu$", email): # [^@] every character except @ sign
#     print("Valid")
# else:
#     print("Invalid")

# if re.search(r"^\w+@(\w+\.)?\w+\.edu$", email, re.IGNORECASE): # anything before ? is optional it can either be there or not there
#     print("valid")
# else:
#      print("Invalid")

# if re.search(r"^\w+@\w+\.(com|edu|gov|net|org)$", email)
# if re.search(r"^(\w|\s)+@\w+\.(com|edu|gov|net|org)$", email)
# if re.search(r"^\w+@\w+\.\w+\.edu$", email, re.IGNORECASE)
