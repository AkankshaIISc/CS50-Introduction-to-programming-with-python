from twttr import shorten

def test_twttr_str():
    assert shorten("Edit up my twitter") == "dt p my twttr"

def test_num():
    assert shorten("My handle is 234") == "My hndl s 234"

def test_punc():
    assert shorten("My handle is xx!") == "My hndl s xx!"
