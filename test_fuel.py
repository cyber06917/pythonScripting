import fuel
import pytest
from fuel import convert, gauge


def test_convert():
    assert convert("1/4") == 25
    assert convert("1/2") == 50
    assert convert("3/4") == 75
    assert convert("1/1") == 100
    assert convert("0/1") == 0
    assert convert("2/3") == 66
    assert convert("5/6") == 83
    assert convert("3/8") == 37
    assert convert("7/8") == 86

    with pytest.raises(ZeroDivisionError):
        convert("1/0")

    with pytest.raises(ValueError):
        convert("2/1")
    with pytest.raises(ValueError):
        convert("invalid")



def test_gauge():
    assert gauge(25) == "25%"
    assert gauge(50) == "50%"
    assert gauge(75) == "75%"
    assert gauge(76) == "76%"
    assert gauge(100) == "F"
    assert gauge(99) == "F"
    assert gauge(67) == "67%"
    assert gauge(83) == "83%"
    assert gauge(38) == "38%"
    assert gauge(0) == "E"
    assert gauge(1) == "E"

