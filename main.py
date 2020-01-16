from Model.messageModel import *
from View.messageView import *
import os

if __name__ == "__main__":
    show = View()
    show.show_message()
    User_choice = ""

    while User_choice != "q":
        User_choice = input("Voir(v), Ecrire(w) et Quitter(q) :")
        Choice = Model()
        if User_choice == "v":
            show.show_message()

        if User_choice == "w":
            author = input ("Veuillez entrer votre nom : ")
            content = input ("Quel est votre message : ")
            Choice.write_message(content, author)

        if User_choice == "q":
            print ("Nous vous souhaitons une bonne journée. ")
            exit()
