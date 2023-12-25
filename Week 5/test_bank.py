from bank import value


def main():
    test_check_values()


def test_check_values():
    assert value("HeLlo") == 0
    assert value("HoWdy") == 20
    assert value("GoOd") == 100


def test_check_phrase():
    assert value("Good Morning") == 100
    assert value("How are you?") == 20
    assert value("Hello, World") == 0


if __name__ == "__main__":
    main()
