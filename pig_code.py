import random
win = 100

def dice():
    return random.randint(1,6)

def turn():
    turn_score = 0
    while True:
        roll = dice()
        print("You rolled a " + str(roll))
        if roll == 1:
            print("You busted! Back to 0")
            return 0
        turn_score += roll
        print("Turn total: " + str(turn_score))
        
        choice = input("Would you like to roll or stay (r/s)?")
        if choice == "s":
            print("You have chosen to stay, your total for this turn is " + str(turn_score))
            return turn_score

def play_game():
    