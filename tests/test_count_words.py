from lib.count_words import *
import pytest

def tests_count_of_words():
    result = word_count("great")
    assert result == 5

def test_if_string_is_empty_return_error():
    with pytest.raises(Exception) as err:
        word_count("")
    assert str(err.value) == "This is an empty string"