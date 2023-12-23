def main():

    print(f"{display_price("Item: ")}")

def display_price(prompt):

    total = 0

    d = {
    "Baja Taco": 4.25,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00
    }

    while True:
        try:
            x = input(prompt).title()
            total += d[x]
        except (ValueError,KeyError):
            pass
        except EOFError:
            return ""
        else:
            print(f"Total: ${total:.2f}")

main()
