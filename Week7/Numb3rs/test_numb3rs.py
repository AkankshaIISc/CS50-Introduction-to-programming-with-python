from numb3rs import validate

def test_num():
    assert validate("127.0.0.1") == True
    assert validate("255.255.255.255") == True
    assert validate("28.250.25.2") == True
    assert validate("120.21.255.0") == True

def test_invalid():
    assert validate("cat") == False
    assert validate("275.3.6.28") == False
    assert validate("1.3.2.1000") == False
    assert validate("512.512.512.512") == False

def test_first_value():
    assert validate("25.257.280.900") == False
    assert validate("855.255.255.255") == False
    assert validate("150.255.255.255") == True
    assert validate("200.255.255.255") == True



