import sys
import requests
import json


def main():
    if len(sys.argv) > 2:
        sys.exit("Missing command-line argument ")
    try:
        input = float(sys.argv[1])
    except ValueError:
        sys.exit("Command-line argument is not a number")
    else:
        response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
        bit_json = response.json()
        currency = bit_json["bpi"]["USD"]["rate"]
        currency = float(currency.replace(",", ""))

    amount = bitCalc(currency, input)

    print(f"${amount:,.4f}")


def bitCalc(currency, input):
    total = currency * input

    return total


main()
