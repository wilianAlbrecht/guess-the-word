from random import randint

def word_selection():
    #list of words to be chosen
    word = "house", "program", "play", "game", "computer", "thing", "horse", "desk", "window", "girl"

    #choosing a random word
    i = randint(0, 9)

    return word[i]