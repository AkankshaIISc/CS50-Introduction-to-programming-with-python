from plates import is_valid

def test_alphabets():
    assert is_valid("AA") == True
    assert is_valid("AAAAAA") == True
    assert is_valid("AABBCC") == True
    assert is_valid("AA22") == True
    assert is_valid("A") == False


def test_numeric():
    assert is_valid("AA22") == True
    assert is_valid("AAA22B") == False
    assert is_valid("AAB022") == False


def test_number():
    assert is_valid("2345") == False
    assert is_valid("023AAA") == False
    assert is_valid("A2232") == False

def test_punc():
    assert is_valid("!!AA!") == False
    assert is_valid("HI.HI") == False
    assert is_valid("AA2 BC") == False

def test_zero():
    assert is_valid("AA2200") == True
    assert is_valid("AA022") == False
    assert is_valid("AB70") == True





