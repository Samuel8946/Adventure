import random
import time
import os


def main():
    
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
            break
    #choice = input("You are trap in a cave with no end in sight, Suddenly you spot 2 items on the ground which one will you pick? ")
    

# Create the adventure


# Count how many times the player dies




# Decision: Left or Right? choose left you die from picking up a poisonous snake. right and you pick up pooop. your face is filled with disgust,
# You graze your DISGUSTING hand against the wall trying to find a way out, then 3 path ways appeared, Where will you go?
# Decision: Middle, Left or Right? Middle is Death from falling. Every bone in your body is fractured as you lose lots of blood slowly dying. Left, You find a bunch of man eating dog and die from heart attack. Right, you live but your determination slowly diminishes more and more. WIll anything be remained?
# While walking down the cave to see something shining in the distance, you run to it not knowing something is lurking behind you.
#   5 SECONDS TO TYPE DOCK, if failed they died from getting their head choped off else you docked and there is a weird deranged person with an axe in there hand will you fight or run? if they fight say "wow you fought bear handed against a man with an axe. what did you expect to happen." if they run "you decided to run and run and you see the light U HAVE ESCAPE THE CAVE."
# YOU WIN



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

    status = {
        "Name": playerName,
        "Age": playerAge,
        "Gender": playerGender,
        "HP": 10,
        "Lives": 3,
    }
    print("Your Stats")
    for stats in status:
        print(stats, status[stats], sep=": ")

    


main()

