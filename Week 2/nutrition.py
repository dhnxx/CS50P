def main():

    x = input("Item: ").lower().replace(" ","_")
    print(nutrition(x))


def nutrition(n):
    fruits = {"apple": 130,
              "avocado": 50,
              "banana": 110,
              "cantaloupe": 50,
              "grapes": 90,
              "honeydew_melon": 50,
              "kiwifruit": 90,
              "lemon": 15,
              "lime": 20,
              "nectarine": 60,
              "orange": 80,
              "peach": 60,
              "pear": 100,
              "pineapple": 50,
              "plums": 70,
              "strawberries": 50,
              "sweet_cherries": 100,
              "tangerine": 50,
              "watermelon": 80,}

    if not n in fruits:
        return ""
    else:
        return fruits[n]

main()
