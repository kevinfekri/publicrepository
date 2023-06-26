import json
import requests
import sys


def main():
    try:
        n = sys.argv[1]
        if len(sys.argv) != 2:
            sys.exit("Missing command-line argument")
        elif n.isdigit() == True:
            n = float(n)
        else:
            n = float(n)
    except:
        sys.exit("Command-line argument is not a number")


    try:
        r = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
        response = r.json()
    except requests.RequestException:
        sys.exit()

    print(response["bpi"]["USD"]["rate_float"])
    amount = response["bpi"]["USD"]["rate_float"] * n
    print(f"${amount:,.4f}")


main()
