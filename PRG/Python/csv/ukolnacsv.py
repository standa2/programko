import csv
def main() :
  gule = {"Božetěch": 1,"Želmíra": 3,"Andělín": 4,"Hvězdoslava": 1,}
  cesta = "H:\\WET\\PRG\\Python\\data.csv"
  ulozit_data(cesta, gule)

def ulozit_data(cesta, gule):
    with open(cesta, "r") as file:
   reader = csv.reader(file, delimiter=";")
   for x in reader:
       print(x)


if __name__ == "__main__":
  main()