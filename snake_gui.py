import tkinter as tk
from tkinter import font
import random

#declare some constatnts

WIDTH = 800
HEIGHT = WIDTH * 0.75
PLAYER_SIZE = 30
ENEMY_SIZE = 20
TEXT_SIZE = 50
BIGONE_SIZE = 60

BAR_WIDTH = 150
BAR_SPEED = 12

#declare variable

alive = True
score = 0
game_state = "start"
next_event_score = 250


#build window

root = tk.Tk()
root.title("Dodger")

canvas = tk.Canvas(root, width=WIDTH, height=HEIGHT, bg="black")
canvas.pack()

player = None
score_text = None
enemies = []
bigones = []
bars = []
warnings = []

#start screen

def show_start_screen():
    canvas.delete("all")
    canvas.create_text(WIDTH//2, HEIGHT//2 - 50, text="DODGER", fill="white", font=("Arial",60,"bold"))
    canvas.create_text(WIDTH//2,HEIGHT//2+50, text= "Press SPACE to Start", fill="white",font=("Arial",30))

#game over screen

def show_game_over_screen():
    canvas.delete("all")
    canvas.create_text(WIDTH//2,HEIGHT//2-50,text="YOU DIED",fill="#5C0606",font=("Arial",60,"bold"))
    canvas.create_text(WIDTH//2,HEIGHT//2+50,text="Press SPACE to Restart",fill="white",font=("Arial",30))

#game start(kind og)

def start_game(event=None):
    global alive, score, enemies, bigones, bars, warnings
    global player, score_text, game_state, next_event_score

    game_state = "running"
    alive = True
    score = 0
    enemies = []
    bigones = []
    bars = []
    warnings = []
    next_event_score = 250
    canvas.delete("all")

    player = canvas.create_rectangle(WIDTH/2-(PLAYER_SIZE/2), HEIGHT/2-(PLAYER_SIZE/2), WIDTH/2+(PLAYER_SIZE/2), HEIGHT/2+(PLAYER_SIZE/2), fill="#00FF37")
    score_text = canvas.create_text(70, 30, text="0", fill="white", font=("Arial",24))
    run_game()


#movemenet function
def move_left(event):
    x1,y1,x2,y2 = canvas.bbox(player)
    if x1>0:
        canvas.move(player, -20, 0)
def move_right(event):
    x1,y1,x2,y2 = canvas.bbox(player)
    if x2 < WIDTH:
        canvas.move(player, 20, 0)
def move_up(event):
    x1,y1,x2,y2 = canvas.bbox(player)
    if y1>0:
        canvas.move(player, 0, -20)
def move_down(event):
    x1,y1,x2,y2 = canvas.bbox(player)
    if y2 < HEIGHT:
        canvas.move(player, 0, 20)

#binding buttons
root.bind("a",move_left)
root.bind("d",move_right)
root.bind("w",move_up)
root.bind("s",move_down)
root.bind("<space>", start_game)
#bad guys



def spawn_enemy():
    x = random.randint(0, WIDTH-ENEMY_SIZE)
    enemy = canvas.create_rectangle(x, 0, x+ENEMY_SIZE, ENEMY_SIZE, fill = "#FF0000")
    enemies.append(enemy)

def spawn_bigone():
    x = random.randint(0, WIDTH - BIGONE_SIZE)
    enemy = canvas.create_rectangle(x, 0, x + BIGONE_SIZE, BIGONE_SIZE, fill="#8B0000")
    bigones.append(enemy)
    
def trigger_specical_event():
    x = random.randint(0, WIDTH - BAR_WIDTH)
    flash_warning(x)

def flash_warning(x, flashes = 6):
    warning = canvas.create_rectangle(x, 0, x + BAR_WIDTH, 20, fill="yellow")
    warnings.append(warning)

    def animate(count):
        if count == 0:
            if warning in warnings:
                canvas.delete(warning)
                warnings.remove(warning)
            spawn_bar(x)
            return
        current = canvas.itemcget(warning, "fill")
        new = "" if current == "yellow" else "yellow"
        canvas.itemconfig(warning, fill = new)

        root.after(100, lambda: animate(count-1))
    animate(flashes)

def spawn_bar(x):
    bar = canvas.create_rectangle(x, 0, x + BAR_WIDTH, 40, fill="#AA0000")
    bars.append(bar)

#run game
def run_game():
    global alive, score, game_state, next_event_score
    if game_state != "running":
        return
    if not alive:
        game_state = "game over"
        show_game_over_screen()
        return
        

    if random.randint(1,10)==1:
        spawn_enemy()
    if random.randint(1,120)==1:
        spawn_bigone()

    for enemy in enemies:
        canvas.move(enemy, 0, 10)
        ex1,ey1,ex2,ey2 = canvas.bbox(enemy)

        if ey2 > HEIGHT:
            score += 1
            canvas.itemconfig(score_text,text=f"{score}")
            if score >= next_event_score:
                trigger_specical_event()
                next_event_score += 250
            canvas.delete(enemy)
            enemies.remove(enemy)
            continue
        if canvas.bbox(enemy) and canvas.bbox(player):
            px1,py1,px2,py2 = canvas.bbox(player)

            if ex1 < px2 and ex2 > px1 and ey1 < py2 and ey2 > py1:
                alive = False
    
    for enemy in bigones:
        canvas.move(enemy, 0, 7)
        ex1, ey1, ex2, ey2 = canvas.bbox(enemy)

        if ey2 > HEIGHT:
            score += 5
            canvas.itemconfig(score_text, text=f"{score}")
            if score >= next_event_score:
                trigger_specical_event()
                next_event_score+= 250
            canvas.delete(enemy)
            bigones.remove(enemy)
            continue

        if canvas.bbox(enemy) and canvas.bbox(player):
            px1,py1,px2,py2 = canvas.bbox(player)

            if ex1 < px2 and ex2 > px1 and ey1 < py2 and ey2 > py1:
                alive = False

    for bar in bars[:]:
        canvas.move(bar, 0, BAR_SPEED)
        bx1, by1, bx2, by2 = canvas.bbox(bar)
        if by2 > HEIGHT:
            canvas.delete(bar)
            bars.remove(bar)
            continue

        px1, py1, px2, py2 = canvas.bbox(player)
        if bx1 < px2 and bx2 > px1 and by1 < py2 and by2 > py1:
            alive = False

        

    root.after(40, run_game)


#main loop
show_start_screen()
root.mainloop()

