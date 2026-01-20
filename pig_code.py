import random
win = 100

def dice():
    random.randint(1,6)

def turn():
    turn_count = 0
    while True:
        roll = dice()
        print("You rolled a " + roll)
        if roll == 1:
            print("You busted! Back to 0")
            
            turn_count +=