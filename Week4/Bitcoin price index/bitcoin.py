import sys
import requests
import json



if len(sys.argv) != 2:
    sys.exit("Missing command-line argument")
else:
    try:
        x = float(sys.argv[1])
        response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
        coin = response.json()
        j = coin["bpi"]["USD"]["rate"]
        cost = float(j.replace(",", ""))
        print(f"${x*cost:,.4f}")

    except ValueError:
        sys.exit("Command-line argument is not a number")


#



