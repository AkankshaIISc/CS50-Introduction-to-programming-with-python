from fuel import convert
from fuel import gauge
import pytest

def test_convert():
    assert convert("1/4") == 25
    assert convert("4/4") == 100
    assert convert("0/4") == 0
    assert convert("3/4") == 75

def test_gauge():
    assert gauge(25) == "25%"
    assert gauge(75) == "75%"
    assert gauge(0) == "E"
    assert gauge(100) == "F"
    assert gauge(1) == "E"
    assert gauge(99) == "F"


def test_greater():
    with pytest.raises(ValueError):
        convert("2/1")

def test_zero():
    with pytest.raises(ZeroDivisionError):
        convert("10/0")

def test_str():
    with pytest.raises(ValueError):
        convert("cat/dog")
