"""A function called count_words that takes a string
as an argument and returns the number of letters in that string."""

def word_count(word):
    if len(word) == 0:
        raise Exception("This is an empty string")
    return len(word)