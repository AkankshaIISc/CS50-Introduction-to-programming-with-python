from bank import value

def test_hello():
    assert value("hello, world") == 0
    assert value("Hello, sun") == 0
    assert value("hello") == 0

def test_h():
    assert value("Hi, moon") == 20
    assert value("hi, earth") == 20
    assert value("Hi") == 20

def test_no():
    assert value("Live life") == 100
    assert value("nice, one") == 100
    assert value("grow, big") == 100



