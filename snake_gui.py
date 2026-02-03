import tkinter as tk
from tkinter import font
import random

#declare some constatnts

WIDTH = 800
HEIGHT = WIDTH * 0.75
PLAYER_SIZE = 30
ENEMY_SIZE = 20

#build window

root = tk.Tk()
root.title("Dodger")

canvas = tk.Canvas(root, width=WIDTH, height=HEIGHT, bg="black")
canvas.pack()

#build player
player = canvas.create_rectangle(WIDTH/2-(PLAYER_SIZE/2), HEIGHT/2-(PLAYER_SIZE/2), WIDTH/2+(PLAYER_SIZE/2), HEIGHT/2+(PLAYER_SIZE/2), fill="#00FF37")

#make alive bool
alive = True

#movemenet function
def move_left(event):
    canvas.move(player, -20, 0)
def move_right(event):
    canvas.move(player, 20, 0)
def move_up(event):
    canvas.move(player, 0, -20)
def move_down(event):
    canvas.move(player, 0, 20)

#binding buttons
root.bind("a",move_left)
root.bind("d",move_right)
root.bind("w",move_up)
root.bind("s",move_down)
#bad guys

enemies = []

def spawn_enemy():
    x = random.randint(0, WIDTH-ENEMY_SIZE)
    enemy = canvas.create_rectangle(x, 0, x+ENEMY_SIZE, ENEMY_SIZE, fill = "#FF0000")
    enemies.append(enemy)




#run game
def run_game():
    global alive
    if not alive:
        canvas.delete("all")
        canvas.create_text(WIDTH//2,HEIGHT//2, text="YOU DIED",fill="#5C0606", font=("Arial", 48, "bold"))
        

    if random.randint(1,20)==1:
        spawn_enemy()

    for enemy in enemies:
        canvas.move(enemy, 0, 10)
        
        if canvas.bbox(enemy) and canvas.bbox(player):
            ex1,ey1,ex2,ey2 = canvas.bbox(enemy)
            px1,py1,px2,py2 = canvas.bbox(player)

            if ex1 < px2 and ex2 > px1 and ey1 < py2 and ey2 > py1:
                alive = False


    root.after(50, run_game)


#main loop
run_game()
root.mainloop()

