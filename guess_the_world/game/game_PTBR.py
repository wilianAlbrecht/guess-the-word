from words import word_PTBR
import os

def game_PTBR():

    os.system("cls")

    print("Você escolheu português.\n")
    secret_word = word_PTBR.word_selection()

    print("como jogar: ")
    print("1- O computador ira escolher uma palavra aleatoria ")
    print("2- voce terá que advinhar quais são as letras da palavra ate completa-la ")
    print("3- Se você já souber a palavra digite [res] para responder qual a palavra completa ")
    print("4- você não tem limites de tentativas para acertar ")
    print("5- As palavras não contém acentuação para facilitar")
    print("Bom jogo... \n")

    input("Palavra já sorteada, precione qualquer tecla para continuar. ")

    user_word = "{}".format("-" *len(secret_word))
    user_att = 0

    while True:
        os.system("cls")

        print("Digite uma letra \n\n")
        print(user_word)

        op = input()

        user_att += 1

        if op.lower() == "res":
            user_try = input("Qual é a palavra? ")
            if user_try == secret_word:
                win(secret_word, user_att)
                break
            else:
                print("Resposta incorreta ")
                input()

        else:

            user_word = validation(secret_word, op,user_word)

            if "-" not in user_word:
                os.system("cls")
                win(secret_word, user_att)
                break

        os.system("cls")


def validation(secret_word, op, user_word):
    user_response = ""

    index = 0

    while index < len(user_word):
        if secret_word[index] == op or secret_word[index] == user_word[index]:
            user_response += secret_word[index]
        else:
            user_response += "-"

        index += 1

    user_word = user_response

    return user_word

        

def win(secret_word, user_att):

    print('Parabéns você acertou a palavra "{}" com {} tentativas. \n\n'.format(secret_word, user_att))
    again = input("Jogar novamente?[Y] ")

    if again.lower() == "y":
        game_PTBR()
    else:  
        os.system("cls")
        print("Obrigado por jogar :) \n\n")

