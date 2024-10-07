import random

odpoved = random.randint(0, 4)
odpovedi = ["1", "2", "3", "4", "5"]
odpovedi_dana = ["1","1", "2", "3", "4",]

otazka = input("Jak se volas? \n")
if otazka == "dana":
    odpoved = random.randint(0, 4)
    print(odpovedi_dana[odpoved])
else:
    odpoved = random.randint(0, 4)
    print(odpovedi[odpoved])