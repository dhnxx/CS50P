def main ():
    x = input("What is the Answer to the Great Question of Life, the Universe, and Everything? ").strip().lower()
    #print (x)
    print(fortytwo(x))


def fortytwo(n):

    match n:
        case "42" | "forty two" | "forty-two" :
            return "Yes"
        case _:
            return "No"

main()
