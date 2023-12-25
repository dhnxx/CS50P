from plates import is_valid


def main():
    test_zero_number_placement()
    test_beginning_alpha()
    test_length()
    test_alphanumeric()


def test_zero_number_placement():
    assert is_valid("123") == False
    assert is_valid("CS05") == False
    assert is_valid("1234BC") == False


def test_beginning_alpha():
    assert is_valid("ABC123") == True
    assert is_valid("123ABC") == False
    assert is_valid("12") == False
    assert is_valid("2A") == False
    assert is_valid("AA") == True
    assert is_valid("22") == False


def test_length():
    assert is_valid("ABCD1234") == False
    assert is_valid("ABC12345") == False
    assert is_valid("CS50") == True
    assert is_valid("ABC12A") == False


def test_alphanumeric():
    assert is_valid(",.,.?.") == False
    assert is_valid("   CS50   ") == False
    assert is_valid("@CS50 ") == False
    assert is_valid("@CS.50@") == False
    assert is_valid("PI3.14") == False
    assert is_valid("PI3!14") == False
    


if __name__ == "__main__":
    main()
