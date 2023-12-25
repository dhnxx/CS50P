import pytest
from twttr import shorten


def main():
    test_uppercase()
    test_lowercase()
    test_mixedcase()
    test_withoutvowel()
    test_omitnumber()
    test_omitpunct()


def test_uppercase():
    assert shorten("TWITTER") == "TWTTR"


def test_lowercase():
    assert shorten("twitter") == "twttr"


def test_mixedcase():
    assert shorten("TwItteR") == "TwttR"


def test_withoutvowel():
    assert shorten("BCDFGH") == "BCDFGH"


def test_omitnumber():
    assert shorten("1234") == "1234"


def test_omitpunct():
    assert shorten(",?!.") == ",?!."


if __name__ == "__main__":
    main()
