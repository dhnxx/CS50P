def main():

    print(f"{fuel("Fraction: ")}")

def fuel(prompt):

    while True:
        try:
            a,b = input(prompt).split("/")

            a = int(a)
            b = int(b)

            if a > b:
                raise ValueError
        except (ValueError,ZeroDivisionError):
            pass
        else:
            c = round((a/b)*100)

            if c <= 1:
                return "E"
            elif c >= 99:
                return "F"
            else:
                return f"{c}%"

main()
