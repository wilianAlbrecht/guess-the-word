from random import randint

def word_selection():
    word = "house", "program", "play", "game", "computer", "thing", "horse", "desk", "window", "girl"

    i = randint(0, 9)

    return word[i]