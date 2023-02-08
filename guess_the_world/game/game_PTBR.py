from words import word_PTBR
import os

#começa o jogo
def game_PTBR():

    os.system("cls")

    #escolhe a palavra usada
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

    #user_word é a palavra que aparecera na tela para o usuario, se o usuario acertar ira trocar o "-" pela a letra que ele digitou
    user_word = "{}".format("-" *len(secret_word))
    #user_att é a qunatidade de tentativas do usuario
    user_att = 0

    while True:
        os.system("cls")

        print("Digite uma letra \n\n")
        print(user_word)

        op = input()

        user_att += 1

        #nessa parte fara o tratamento se o usuario tentar acertar a palavra
        if op.lower() == "res":
            user_try = input("Qual é a palavra? ")
            if user_try == secret_word:
                #se acertar é levado a tela de vitoria
                win(secret_word, user_att)
                break
            else:
                #se errar o programa so continua
                print("Resposta incorreta ")
                input()

        else:
            #chama o metodo de validação da letra
            user_word = validation(secret_word, op,user_word)

            #verifica se o usuario já acertou todas as letras
            if "-" not in user_word:
                os.system("cls")
                win(secret_word, user_att)
                break

        os.system("cls")

#metodo que verifica se o usuario acertou a  letra digitada
def validation(secret_word, op, user_word):
    user_response = ""

    index = 0

    #percorre a palavra para descobrir se o usuario acertou e compara com as letras já reveladas a ele
    while index < len(user_word):
        if secret_word[index] == op or secret_word[index] == user_word[index]:
            user_response += secret_word[index]
        else:
            user_response += "-"

        index += 1

    user_word = user_response

    #retorna novas letras reveladas
    return user_word

        
#metodo que apresenta a vitoria
def win(secret_word, user_att):

    print('Parabéns você acertou a palavra "{}" com {} tentativas. \n\n'.format(secret_word, user_att))
    again = input("Jogar novamente?[Y] ")

    if again.lower() == "y":
        game_PTBR()
    else:  
        os.system("cls")
        print("Obrigado por jogar :) \n\n")

