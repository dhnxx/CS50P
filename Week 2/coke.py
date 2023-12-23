def main():
    coke()


def coke():
    cost = 50

    while cost > 0:
        print("Amount Due:", cost)
        user_cash = int(input("Insert Coin: "))
        if user_cash == 25 or user_cash == 10 or user_cash == 5:
            cost -= user_cash

    if cost < 0:
        print("Change Owed:", (cost * -1))
    else:
        print("Change Owed: 0")


main()
