import inflect

p = inflect.engine()

def main():
    print(adieu("Adieu, adieu, to"))

def adieu(str):
    names_list = []
    while True:
        try:
            name = input("Name: ")
            names_list.append(name)
        except EOFError:
            return f"\n{str} {p.join(names_list)}"

main()
