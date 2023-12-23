import random
import sys

def main():

    print(game())
    sys.exit(1)

def game():

    level = 0

    while level <= 0:

        try:
            level = int(input("Level: "))
            if level == 0:
                raise ValueError
        except ValueError:
            pass
        else:
            guess_number = random.randint(1, level)

    while True:

        try:
            user_guess = int(input("Guess: "))

        except ValueError:
            pass

        else:
            if user_guess < guess_number:
                print("Too small!")
            elif user_guess > guess_number:
                print("Too large!")
            else:
                return "Just right!"


main()
