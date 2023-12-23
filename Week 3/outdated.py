def main():
    print(date())


def date():
    while True:
        try:
            n = input("Date: ").strip()

            if n[0].isdecimal():
                m, d, y = num_date(n)

            elif n[0].isalpha():
                m, d, y = alpha_date(n)

            if int(m) > 12 or int(d) > 31:
                raise ValueError

        except ValueError:
            pass
        else:
            return f"{y}-{str(m).zfill(2)}-{str(d).zfill(2)}"


def num_date(n):
    m, d, y = n.split("/")

    return m, d, y


def alpha_date(n):
    x = [
        "January",
        "February",
        "March",
        "April",
        "May",
        "June",
        "July",
        "August",
        "September",
        "October",
        "November",
        "December",
    ]

    m, d, y = n.split(" ")

    if d.find(",") != -1:
        d = d.replace(",", "")
    else:
        raise ValueError

    m = x.index(m)
    m += 1

    return m, d, y


main()
