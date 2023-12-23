def main ():
    x = input("Greeting: ")
    x = x.strip().lower()
    #print (x)
    print(bank(x))


def bank(n):
    firstH = n.find("h")
    checkHello = n.find("hello")

    if checkHello != -1:
        return ("$0")
    elif firstH == 0:
        return ("$20")
    else:
        return ("$100")



main()
