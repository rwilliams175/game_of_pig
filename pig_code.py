import random
win = 100

def dice():
    return random.randint(1,6)

def turn(player_name):
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
    scores = {"Player 1": 0, "Player 2": 0 }
    current_player = "Player 1"
    while True:
        print(current_player + "'s turn")
        print("Scores: " + scores)
        points = turn(current_player)
        scores(current_player) += points
        if scores >= win:
            print(current_player + " wins with the score of " + scores)
            break
        