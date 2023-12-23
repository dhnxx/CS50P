from pyfiglet import Figlet
import random
import sys


def main():
    figlet = Figlet()
    f = figlet.getFonts()

    if len(sys.argv) == 1:
        random_font(figlet)
    elif len(sys.argv) == 3:
        if not sys.argv[2] in f:
            sys.exit(1)
        if sys.argv[1] != "-f" and sys.argv[1] != "--font":
            sys.exit(1)
        else:
            specified_font(figlet)
    else:
        sys.exit(1)


def random_font(figlet):
    s = input()
    f = random.choice(figlet.getFonts())
    figlet.setFont(font=f)
    print(figlet.renderText(s))


def specified_font(figlet):
    s = input()
    f = sys.argv[2]
    figlet.setFont(font=f)
    print(figlet.renderText(s))


main()
