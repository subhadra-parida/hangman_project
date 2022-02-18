# from dataclasses import field
import random
def hangman():
    list_of_word=["python","hangman","indexing"]
    word=random.choice(list_of_word)
    chance=10
    guessing=" "
    letters=set("abcdefghijklmnopqrstuvwxyz")
    while True:
        first_word=0
        cancle=0
        for letter in word:
            if letter in guessing:
                first_word=first_word+letter
        if first_word==word:
            print(first_word)
            print("Congratulation!!! You win.")
            break
            print("Guess the word",first_word)
        guess=input("Enter anything")
        if guess in letter:
            guess=guessing+guess
        else:
            print("Enter any valid letter")
            guess=input("Enter anything")
        if guess not in word:
            chance=chance-1
            if chance==9:
                print("9 chance done.")
                print("_")
            if chance==8:
                print("8 chance done.")
                print("_")
                print("o")
            if chance==7:
                print("7 chance done.")
                print("_")
                print(" o ")
                print(" | ") 
            if chance==6:
                print("6 chance done.")
                print("_")
                print("  o  ")
                print("  |  ")
                print(" /   ")
            if chance==5:
                print("5 chance done.")
                print("_")
                print("  o  ")
                print("  |  ")
                print(" /   ")
            if chance==4:
                print("4 chance done.")
                print("_")
                print(" \o  ")
                print("  |  ")
                print(" /   ")
            if chance==3:
                print("3 chance done.")
                print("_")
                print(" \o ")
                print("  | ")
                print(" / \ ")
            if chance==2:
                print("2 chance done")
                print("_")
                print(" \o/|")
                print("  |  ")
                print(" / \ ")
            if chance==1:
                print("1 chance done")
                print("_")
                print(" \o/_| ")
                print("  |    ")
                print(" / \   ")
            if chance==0:
                print("Sorry You are fail.")
name=input("Enter your name=")
print("Welcome",name,"!!!")
print("Again try to do this chance.")
hangman()


            
            
