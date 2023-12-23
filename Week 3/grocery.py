def main():
    list = grocery()
    for i,j in sorted(list.items()):
        print(f"{j} {i}")


def grocery():
    d = {}
    try:
        while True:
            x = input().upper()
            if x in d:
                d[x] += 1
            else:
                d.update({x: 1})
    except EOFError:
        return d

main()
