def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):

    if not s.isalnum():
        return False

    if len(s) < 2 or len(s) > 6 :
        return False

    if s.isalpha():
        return True

    if not s[:1].isalpha():
        return False

    for index,x in enumerate(s):
        if x.isalpha() == False:
            if x == "0":
                return False
            if not s[index:].isdigit():
                return False
            else:
                return True



main()
