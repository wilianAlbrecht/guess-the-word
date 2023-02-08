from random import randint

def word_selection():
    #lista de palavras a ser escolhidas
    word = "carro", "perfume", "casa", "maçaneta", "computador", "hidraulico", "cachoeira", "cachorro", "profissao", "aluguel"

    #escolhe aleatoriamente uma palavra
    i = randint(0, 9)

    return word[i]