import random


def main():
    level = get_level()

    current = 0
    score = 1

    while current != 9:
        tries = 3
        user_ans = None
        x, y, sum = generate_integer(level)
        user_correct = True

        while user_ans != sum:
            if tries == 0:
                print(f"{x} + {y} = {sum}")
                user_correct = False
                break
            try:
                user_ans = int(input(f"{x} + {y} = "))
            except ValueError:
                pass
            tries -= 1
            if user_ans != sum:
                print("EEE")

        if user_correct:
            score += 1

        current += 1

    print("Score =", score)


def get_level():
    while True:
        try:
            a = int(input("Level: "))

            if a < 1 or a > 3:
                raise ValueError

        except ValueError:
            pass
        else:
            return a


def generate_integer(level):
    if level == 1:
        a = 0
        b = 9
    elif level == 2:
        a = 10
        b = 99
    elif level == 3:
        a = 100
        b = 999

    x = random.randint(a, b)
    y = random.randint(a, b)
    sum = x + y

    return x, y, sum


if __name__ == "__main__":
    main()
