import tkinter as tk
import random
root = tk.Tk()
root.title = ("nas oblibeny ucitel honzik")
root.geometry("400x300")

label = tk.Label(root, text = "JMENO")
label.pack()

label2 = tk.Label(root, text = "PRIJMENI")
label2.pack()

seznam = ["vasek", "jakub", "ema", "laura", "krop", "ombre", "maja", "klara", "honzik", "sofia", "monique", "kacka", "kaja", "anez", "dondadell", "ztracený syn zdena", "ha ha ha hanna", "julia", "dianna", "jess", "pablo"]
seznam2 = ["vasekovic", "jakubic", "emadic", "lauranic", "kropic", "ombreic", "majaic", "klaraic", "honzikic", "sofiaic", "moniqueic", "kackaic", "kajaic", "anezic", "gay", "juliaic", "diannaic", "jessic", "pabloic"]

def on_click1():
    vyber = random.randint(0, 20)
    jmeno = seznam[vyber]
    label.config(text = jmeno)
    label3.config(text = f"{jmeno}  bez k tabuli!!!!!")
def on_click2():
    vyber = random.randint(0, 20)
    prijmeni = seznam2[vyber]
    label2.config(text = prijmeni)
    label3.config(text = f" {prijmeni} bez k tabuli!!!!!")

    
button = tk.Button(root, text = "JMENO", command = on_click1)
button.pack()

button2 = tk.Button(root, text = "PRIJMENI", command = on_click2)
button2.pack()

label3 = tk.Label(root, text = f"ty debile bez k tabuli!!!!!")
label3.pack()




root.mainloop()