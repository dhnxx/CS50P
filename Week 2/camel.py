def main():
    a = input("camelCase: ")
    print(camel(a))


def camel(input):
    a = ""
    for index, x in enumerate(input):
        if x.isupper():
            x = x.lower()
            a += ("_"+x)
        else:
            a += x

    #a = (input[:upper] + "_" + input[upper:]).lower()
    return a


main()
