import tkinter as tk

root = tk.Tk()
root.title = ("DI DO CHUJE")
root.geometry("400x300")

label = tk.Label(root, text = "ZAŽIJEŠ AMERIKU TY ZMRDE")
label.pack()

def on_click():
    label.config(text = "TY DEBILEEEE")
button = tk.Button(root, text = "KLIKNI ME TY DEŽO", command = on_click)
button.pack()
root.mainloop()