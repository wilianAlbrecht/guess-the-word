from words import word_EN
import os

#start the game
def game_EN():

    os.system("cls")

    #choose the word 
    print("you chose english.")
    secret_word = word_EN.word_selection()

    print("How to play")
    print("1- The computer will choose a random word ")
    print("2- You will try guess the letters of the word ")
    print("3- If you now what is the word, type [res] to answer ")
    print("4- You have no limits on attempts to get it right")
    print("Good luck...")

    input("The word already drawn, press any key... ")

    #user_word is the word that will appear on the screen for the user, if the user hits it will change the "-" by the letter he typed
    user_word = "{}".format("-" *len(secret_word))
    #user_att is the amount of attempts
    user_att = 0

    while True:
        os.system("cls")

        print("type the letter \n\n")
        print(user_word)

        op = input()

        user_att += 1

        #if the user now what is the word will enter here
        if op.lower() == "res":
            user_try = input("What is the word? ")
            if user_try == secret_word:
                #if hit the word, will be directed to victory screen
                win(secret_word, user_att)
                break
            else:
                print("You missed ")
                input()

        else:
            
            #call a validation method of the letters
            user_word = validation(secret_word, op,user_word)

            #check if user hit all the letters
            if "-" not in user_word:
                os.system("cls")
                win(secret_word, user_att)
                break

        os.system("cls")

#letter check metod
def validation(secret_word, op, user_word):
    user_response = ""

    index = 0

    #check if the user hit any letter and compare with the letters already agreed
    while index < len(user_word):
        if secret_word[index] == op or secret_word[index] == user_word[index]:
            user_response += secret_word[index]
        else:
            user_response += "-"

        index += 1

    user_word = user_response

    #return the new word
    return user_word

        
#victory scream method
def win(secret_word, user_att):

    print('congratulations you hit "{}" with {} attempts. \n\n'.format(secret_word, user_att))
    again = input("Play again?[Y] ")

    if again.lower() == "y":
        game_EN()
    else:  
        os.system("cls")
        print("Thank you for played :) \n\n")

