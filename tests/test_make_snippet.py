import pytest
from lib.make_snippet import *

"""takes a string and if less than 5, returns the string
in a lower string"""
def test_takes_string_less_than_5_returns_string():
    result = update_string("hello")
    assert result == "hello"

"""Takes a string and returns if less than 5, 
converts the word to lower"""
def test_takes_string_less_than_5_returns_string_lower():
    result = update_string("Hello")
    assert result == "hello"

"""takes a string and if greater than 5 cuts the rests of
the word and adds ... to the end"""
def test_takes_string_and_more_than_5_add_elipses():
    result = update_string("longer")
    assert result == "longe..."

"""takes a string and if greater than 5 cuts the rests of
the word and adds ... to the end, converts string to lower"""
def test_takes_word_adds_elipses_and_converts_to_lower():
    result = update_string("LONGer")
    assert result == "longe..."

"""takes a string and if empty, returns an error"""
def test_if_empty_string_throw_error():
    with pytest.raises(Exception) as err:
        update_string("")
    assert str(err.value) == "This is an empty string"
