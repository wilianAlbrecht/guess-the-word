from random import randint

def word_selection():
    word = "carro", "perfume", "casa", "maçaneta", "computador", "hidraulico", "cachoeira", "cachorro", "profissao", "aluguel"

    i = randint(0, 9)

    return word[i]