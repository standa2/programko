import random
import tkinter as tk

root = tk.Tk()
root.title = ("nas oblibeny ucitel honzik")
root.geometry("400x300")

entry = tk.Entry()
entry.pack()

odpovedi = ["1", "2", "3", "4", "5"]
odpovedi_dana = ["1","1", "2", "3", "4",]

def on_click():
    if entry.get() == "dana":
        odpoved = random.randint(0, 4)
        label.config(text = odpovedi_dana[odpoved])
    else:
        odpoved = random.randint(0, 4)
        label.config(text = odpovedi[odpoved])


button = tk.Button(root, text = "známka pro tebe", command = on_click)
button.pack()

label = tk.Label(root, text = "ZNÁMKA")
label.pack()

root.mainloop()



