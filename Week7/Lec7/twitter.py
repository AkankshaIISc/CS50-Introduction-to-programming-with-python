import re

url = input("URL: ").strip()

# username = url.replace("https://twitter.com/", "")
# print(f"username: {username}")

# username = re.sub(r"^(https?://)?(www\.)?twitter\.com/", "", url)
# print(f"username: {username}")

matches = re.search(r"^https?://(?:www\.)?twitter\.com/([a-z0-9_]+)", url, re.IGNORECASE)
if matches:
    print(f"Username:", matches.group(1))
