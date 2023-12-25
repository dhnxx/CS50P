import pytest
from fuel import convert
from fuel import gauge


def main():
    test_zero_division()
    test_value_error()


def test_zero_division():
    with pytest.raises(ZeroDivisionError):
        convert("1/0")
    with pytest.raises(ZeroDivisionError):
        convert("0/0")

def test_value_error():
    with pytest.raises(ValueError):
        convert("2/1")
    with pytest.raises(ValueError):
        convert("5/2")
    with pytest.raises(ValueError):
        convert("cat/dog")

def test_convert():
    assert convert("1/2") == 50
    assert convert ("3/4") == 75

def test_gauge_ends():
    assert gauge(0.89) == "E"
    assert gauge(99.02) == "F"
    assert gauge(1) == "E"
    assert gauge(99) == "F"


def test_gauge_between():
    assert gauge(50) == "50%"
    assert gauge(75) == "75%"


if __name__ == "__main__":
    main()
