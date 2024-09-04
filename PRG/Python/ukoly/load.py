#############################################################
import csv
def main():
  gule = {
      "Božetěch": 1,
      "Želmíra": 3,
      "Andělín": 4,
      "Hvězdoslava": 1,
  }
  cesta = "H:\WET\PRG\Python\ukoly\srackanaukol.csv"
  ulozit_data(cesta, gule)

def ulozit_data(cesta, gule):
  with open(cesta, "w") as file:
    writer = csv.writer(file, delimiter=";")
    for meno, value in gule.items():
      writer.writerow([meno, value])

if __name__ == "__main__":
  main()
#############################################################
import csv
def main():
  gule = []
  cesta = "H:\WET\PRG\Python\ukoly\srackanaukol.csv"
  ulozit_data(cesta, gule)

def ulozit_data(cesta, gule):
  with open(cesta, "r", newline="") as file:
    reader = csv.reader(file, delimiter=";")
    for row in reader:
      gule.append(row)
  for row in gule:
    print(f"{row[0]};{int(row[1])}")

if __name__ == "__main__":
  main()