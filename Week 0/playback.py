def main():
    a = input()
    print(playback(a))

def playback(word):
    return word.replace(" ", "...")

main()
