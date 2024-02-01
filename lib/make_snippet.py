def update_string(word):
    new_word = word
    if len(word) > 5:
        new_word = word.lower()[0:5] + "..."
    elif len(word) == 0:
        raise Exception ("This is an empty string")
    return new_word.lower()