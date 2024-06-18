
import random
import time
from getch import getch

# welcome them to the game of Gibblegorp!
# explain the rules of Gibblegorp! 
# random time delay for printing Gibblegorp!
ROUNDS = 5
MAX_NUMBER = 1000 # ONE THOUSAND
STRSTAR = "* "
GIBBLEGORPE_NUMS_DELETE = 10
P1_NUMS = GIBBLEGORPE_NUMS_DELETE
P2_NUMS = GIBBLEGORPE_NUMS_DELETE


DELAY = 1
COUNTDOWN_TIME = 5
COUNTER = 5


def main():

    welcome_message()
    start_or_help()

    rand_max = random.randint(1,MAX_NUMBER)
    print(rand_max)
    print("The number is set between 1 &", MAX_NUMBER)

    for i in range(ROUNDS):
        if rand_max <= 0:
            break

        print("*** Round",i+1,"***")
        print("")

        star_count = len(str(rand_max))
        print("Number of digits to remove from Gibblegorpe!")
        print(star_count * STRSTAR)
        print("")


        # player 1 check
        subtract_player_1 = int(input("Player one, place your number:"))
        print("")
        while subtract_player_1 <= 0 or subtract_player_1 >= MAX_NUMBER:
            subtract_player_1 = int(input("Player one, place your number:"))
            print("")

        rand_max = rand_max - subtract_player_1
        if rand_max <= 0: 
            print("PLAYER 2 WINS")

            print("  _____ _ _     _     _       _____                       _ ")
            print(" / ____(_) |   | |   | |     / ____|                     | |")
            print("| |  __ _| |__ | |__ | | ___| |  __  ___  _ __ _ __  ___ | |")
            print("| | |_ | | '_ \| '_ \| |/ _ \ | |_ |/ _ \| '__| '_ \/ _ \| |")
            print("| |__| | | |_) | |_) | |  __/ |__| | (_) | |  | |_)   __/|_|")
            print(" \_____|_|_.__/|_.__/|_|\___|\_____|\___/|_|  | .__/\___|(_)")
            print("                                              | |           ")
            print("                                              |_|           ") 
            print("Game is done!")
            break

        # player 2 check 
        subtract_player_2 = int(input("Player two, place your number:"))
        print("")
        while subtract_player_2 <= 0 or subtract_player_2 >= MAX_NUMBER:
            subtract_player_2 = int(input("Player one, place your number:"))
            print("")
            
        rand_max = rand_max - subtract_player_2
        if rand_max <= 0: 
            print("PLAYER 1 WINS")
            
            print("  _____ _ _     _     _       _____                       _ ")
            print(" / ____(_) |   | |   | |     / ____|                     | |")
            print("| |  __ _| |__ | |__ | | ___| |  __  ___  _ __ _ __  ___ | |")
            print("| | |_ | | '_ \| '_ \| |/ _ \ | |_ |/ _ \| '__| '_ \/ _ \| |")
            print("| |__| | | |_) | |_) | |  __/ |__| | (_) | |  | |_)   __/|_|")
            print(" \_____|_|_.__/|_.__/|_|\___|\_____|\___/|_|  | .__/\___|(_)")
            print("                                              | |           ")
            print("                                              |_|           ")  
            print("Game is done!")

    if rand_max>= 1:
        print ("player 1 press: 'a'")
        time.sleep(DELAY) 
        print ("player 2 press: 'l'")
        
        for i in range(COUNTDOWN_TIME):
            print(COUNTER)
            time.sleep(DELAY) 
            COUNTER -= 1
        
        char = getch() # also displayed on the screen
        if char == "a":
            print("player 1 wins")
        if char == "l":  
            print("player 2 wins")
        

    

def gibblegorpe_rules():
    print("Gibblegorpe is a game based on random number generation!")
    print("1. A random number is generated")
    print("2. Players need to reduce the number ")
    print("3. If you reduce the number to low you lose")
    print("4. If neither player lowers the generated number bith face-off in GIBBLEGORPE!\n")

def welcome_message():
    print("Welcome to GibbleGorpe! \nThe most intense PvP game ever created!\n")
  
def start_or_help():
    intro_input = input("Press 'enter' to start. Type 'rules' for how to play! ")
    if intro_input != "rules":
        print("")
    if intro_input == "rules":
        gibblegorpe_rules()

if __name__ == "__main__":
    main()

