import  csv
cesta = "H:\\WET\\PRG\\Python\\gule\\srackanaukol.csv"
def main():
    gule = {}
    nacist_data(gule)
    print("zdar")
    print("vyber")
    print("vsechno = 1")
    print("jeden zmrd = 2")
    print("pridat = 3")
    print("vzit = 4")
    print("zmrd roku = 5")
    print("pridej zmrda = 6")

    zvolene = int(input())

    match zvolene:
      case 1:
        vypisGulePro(gule)
      case 2:
        vypisVse(gule)
      case 3:
        pridejGule(gule)
      case 4:
        odeberGule(gule)
      case 5:
        nejvetsiGule(gule)
      case 6:
        novaGule(gule)
      case _:
        print("nedbud kokot")







def vypisGulePro(gule):
  jmeno = input("Koho chces vedet pocet gulí?").capitalize()
  if jmeno in gule:
    print(jmeno, gule[jmeno])




def vypisVse(gule):
  for vseci in gule:
    print(vseci, gule[vseci])





def pridejGule(gule):
  jmeno = input("Komu chces pridat guli?").capitalize()
  if jmeno in gule:
    print(jmeno, gule[jmeno] + 1)





def odeberGule(gule):
  jmeno = input("Komu chces odebrat guli?").capitalize()
  if jmeno in gule:
    print(jmeno, gule[jmeno] - 1)





def novaGule(gule):
  jmeno = input("Komu chces pridat guli?").capitalize()
  pocet = int(input("kolik uz ma gulí?"))
  gule[jmeno] = pocet
  print(jmeno, gule[jmeno])





def nejvetsiGule(gule):
  gulusmaximus = max(gule.values())
  gulusgigantos = [typek for typek, value in gule.items() if value == gulusmaximus]
  print("Nejvíc gulí má:", gulusgigantos[0], gulusmaximus)





def ulozit_data(gule):
  with open(cesta, "w") as file:
    writer = csv.writer(file, delimiter=";")
    for meno, value in gule.items():
      writer.writerow([meno, value])




def nacist_data(gule):
  with open(cesta, "r", newline="") as file:
    reader = csv.reader(file, delimiter=";")
    for row in reader:
      gule[row[0]] = int(row[1])

main()