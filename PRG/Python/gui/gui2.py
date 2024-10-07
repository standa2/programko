import random
import tkinter as tk
import csv

root = tk.Tk()
root.title = ("nas oblibeny ucitel honzik")
root.geometry("400x300")
entry = tk.Entry()
entry.pack()

odpovedi = [1,2,3,4,5]
odpovedi_dana = [1,1,2,3,4]
pocet1 = 0
pocet2 = 0

root.configure(bg='white')

cesta = "H:\\WET\\PRG\\Python\\gui\\data.csv"
new_avarage = {}

with open(cesta, "r") as file:
    reader = csv.reader(file, delimiter=";")
    for x in reader:
        new_avarage[x[0]] = float(x[1])

prumer = new_avarage["dsadas"]

def on_click():
    global pocet1
    global pocet2
    global prumer


    if entry.get() == "dana":
        odpoved = random.randint(0, 4)

        znamka = odpovedi_dana[odpoved]
        pocet1 = pocet1 + znamka
        pocet2 = pocet2 + 1
        prumer = pocet1 / pocet2
        label1.config(text = znamka)
        label2.config(text = prumer)

        if znamka == 1 :
            root.configure(bg='green')
        if znamka == 2 :
            root.configure(bg='lightblue')
        if znamka == 3 :
            root.configure(bg='yellow')
        if znamka == 4 :
            root.configure(bg='orange')
        if znamka == 5 :
            root.configure(bg='red')

        with open(cesta, "w", newline="") as file:
            jmeno = entry.get() 
            avarage = prumer
            writer = csv.writer(file, delimiter=";")
            writer.writerow([jmeno, avarage])

            

    else:
        odpoved = random.randint(0, 4)
        znamka2 = odpovedi[odpoved]
        pocet1 = pocet1 + znamka2
        pocet2 = pocet2 + 1
        prumer = pocet1 / pocet2
        label1.config(text = znamka2)
        label2.config(text = prumer)

        if znamka2 == 1 :
            root.configure(bg='green')
        if znamka2 == 2 :
            root.configure(bg='lightblue')
        if znamka2 == 3 :
            root.configure(bg='yellow')
        if znamka2 == 4 :
            root.configure(bg='orange')
        if znamka2 == 5 :
            root.configure(bg='red')

        with open(cesta, "w", newline="") as file:
            jmeno = entry.get() 
            avarage = prumer
            writer = csv.writer(file, delimiter=";")
            writer.writerow([jmeno, avarage])




button = tk.Button(root, text = "známka pro tebe", command = on_click)
button.pack()


label1 = tk.Label(root, text = "ZNÁMKA")
label1.pack()

label2 = tk.Label(root, text = "PRUMER")
label2.pack()



root.mainloop()



