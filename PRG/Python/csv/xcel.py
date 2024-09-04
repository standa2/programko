import csv
#cesta = "H:\\WET\\PRG\\Python\\data.csv"
#with open(cesta, "r") as file:
#    reader = csv.reader(file, delimiter=";")
#    for x in reader:
#        print(x)

cesta = "H:\\WET\\PRG\\Python\\data.csv"
with open(cesta, "w", newline="") as file:
    jmeno = input("Zadej meno: ")
    pocet = int(input("Zadej pocet: "))
    writer = csv.writer(file, delimiter=";")
    writer.writerow([jmeno, pocet])