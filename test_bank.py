from bank import value


def test_value():
    assert value("h") == 20
    assert value("hello") == 0

