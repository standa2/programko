import random
odpoved = random.randint(1, 5)

""""
if budoucnost == 1:
  print("ano")
elif budoucnost == 2:
  print("ne")
elif budoucnost == 3:
  print("urcite")
elif budoucnost == 4:
  print("nevim")
elif budoucnost == 5:
  print("50/50")
"""
odpovedi = ["ano", "ne", "urcite", "nevim", "50/50"]

while True:
  otazka = input("Mas nejaku otazku o sve budoucnosti?\n")
  if otazka == "konec":
    break
  odpoved = random.randint(1, 5)
  print(odpovedi[odpoved])
