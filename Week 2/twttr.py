def main():

    x = twttr(input("Input: "))
    print(x)

def twttr(s):

    vowel = ["a", "e", "i", "o", "u"]
    new_word = ""

    for c in s:
        if not c.lower() in vowel:
            new_word += c
    return new_word

main()
