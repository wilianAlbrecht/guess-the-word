from words import word_EN
import os

def game_EN():

    os.system("cls")

    print("you chose english.")
    secret_word = word_EN.word_selection()

    print("How to play")
    print("1- The computer will choose a random word ")
    print("2- You will try guess the letters of the word ")
    print("3- If you now what is the word, type [res] to answer ")
    print("4- You have no limits on attempts to get it right")
    print("Good luck...")

    input("The word already drawn, press any key... ")

    user_word = "{}".format("-" *len(secret_word))
    user_att = 0

    while True:
        os.system("cls")

        print("type the letter \n\n")
        print(user_word)

        op = input()

        user_att += 1

        if op.lower() == "res":
            user_try = input("What is the word? ")
            if user_try == secret_word:
                win(secret_word, user_att)
                break
            else:
                print("You missed ")
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

    print('congratulations you hit "{}" with {} attempts. \n\n'.format(secret_word, user_att))
    again = input("Play again?[Y] ")

    if again.lower() == "y":
        game_EN()
    else:  
        os.system("cls")
        print("Thank you for played :) \n\n")

