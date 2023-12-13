def main():
    a = input()
    print(faces(a))

def faces(word):

    word = word.replace(":)", "🙂")
    word = word.replace(":(", "🙁")

    return word

main()
