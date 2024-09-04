import tkinter as tk
import random

root = tk.Tk()
root.title("WHACK EVERY MOLE !!!")
score = 0
current_mole = None
moles = []

def choose_mole():
    global moles, current_mole
    current_mole = random.choice(moles)
    current_mole.config(bg = "red")
def whack(event):
    global score, current_mole
    if event.widget == current_mole:
        score += 1
        print("preco???")
        print(score)
        score_label.config(text=f"SCORE : {score}")

def create_grid():
    for x in range(3):
        for y in range(3):
            mole = tk.Button(root, text="", width = 12, height = 5, bg = "green")
            mole.bind("<Button-1>", whack)
            mole.grid(row = x, column = y)
            moles.append(moles)

score_label = tk.Label(root, text = f"SCORE : {score}")
score_label.grid(row = 4, column= 0)
create_grid()
choose_mole()
root.mainloop