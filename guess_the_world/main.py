"""

faça um jogo que o usuario tente advinhar qual é a palavra secreta, o usuario podera digitar apenas uma letra por vez, o jogo acaba qunado o usuario completa a a palavra.
por fim mostre na tela a palavra correta e a quantidade de vezes tentada

"""
from game import game_PTBR
from game import game_EN

print("1- Português")
print("2- English")

lang = input("")

if lang == "1":
    game_PTBR.game_PTBR()
    print("Desenvolvido por WIlian Albrecht")
elif lang == "2":
    game_EN.game_EN()
    print("Developed by Wilian Albrecht")

