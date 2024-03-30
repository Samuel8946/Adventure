import random
import time
import os


def main():
    # Create the adventure
    adventure(player())










def adventure(commands):
    # Location is Giffildore
    adventure = input("You are trap in a cave with no end in sight, Suddenly you spot 2 items on the ground which one will you pick, left or right? ").lower()
    while True:
        if "left" != adventure != "right":
            adventure = input("Adventure type left or right: ")
        elif adventure == "left":
            print("You Died! From a poisonous snake ")
            quit()
        elif adventure == "right":
            os.system('cls')
            print(f"You picked up poop -_-")
            {time.sleep(2)}            
            print("annnnnnnnnddd your face is filled with disgust")
            time.sleep(2)
            os.system('cls')
            break
    
    adventure = input("You graze your DISGUSTING hand against the wall trying to find a way out, then 3 path ways appeared, Where will you go? left, right or straight: ").lower()

    while True:
        if "left" != adventure != "right" and adventure != "straight":
            adventure = input("Adventure type left, right or straight: ")
        elif adventure == "right":
            os.system('cls')
            print("You Fell into a trap and Died! Bones broken, head crushed, body twitching, truly an awful death :) ")
            quit()
        elif adventure == "left":
            os.system('cls')
            print(f"You find a bunch of man eating dog and died")
            time.sleep(2)            
            adventure = input("Will you play again? Yes or No, I'm trash :( ").lower()
            while True:
                if "yes" != adventure != "no":
                    print("Ok since you wont type what I want you to type, START OVER")
                    quit()
                elif adventure == "yes":
                    break
                elif adventure == "no":
                    print("Well bye-bye :)")
            
        elif adventure == "straight":
            input("YOU LIVE but your determination slowly diminishes more and more. WIll anything be remained? ")
            print("I don't care about your answer :). You'll die if you don't keep moving.")
            time.sleep(2)
            os.system('cls')
            break

    print("Finally you feel like you are near you journey, but there is one last thing you must do")
    time.sleep(2)
    adventure = input("left or right: ").lower()
    while True:
        if "left" != adventure != "right":
            adventure = input("Done with games left or right: ")
        elif adventure == "left" or adventure =="right":
            os.system('cls')
            print("You ESCAPED THE CAVE CONGRATS :)")
            time.sleep(1)
            print("YOU WIN")
            os.system('pause')
            break


def player():
    # Ask player for name
    playerName = input("What is your name Great Adventurer? ").title().strip()
    name_length = len(playerName)

    while True:
        if name_length == 0: 
            print("Adventurer you forgot to add your name")
            playerName = input("What is your name Great Adventurer? ").title().strip()
            name_length = len(playerName)
            continue      
        else:
            print(f"What a unique name you have. {playerName}")
            break
    
    # Player's gender and age
    playerGender = input("Now are you a Boy or a Girl? ").lower()
    playerAge = ""
        
    while True:
        if playerGender == "boy" or playerGender == "girl":
            if playerGender != "boy":
                playerAge = int(input(f"Ok Miss {playerName}, how old are you. "))
            elif playerGender == "boy":
                playerAge = int(input(f"Ok Mister {playerName}, how old are you. "))
        else:
            playerGender = input("No No No. Adventurer, I am asking if you are a boy or a girl? ").lower()
            continue
    
        if playerAge < 18:
            print("Oh no adventurer! It seems you are too young to play this game. Come back when you're older. I will be waiting.")
            quit()
        else:
            print(f"Manificent {playerName}. Welcome to the world of GIFFILDORE!! A wonderful adventure awaits.")
            time.sleep(3) 
            os.system("cls")
            print("loading...")
            time.sleep(4)
            os.system("cls")
            break 

main()

