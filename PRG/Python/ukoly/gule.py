#######################################################
def main():
  gule = {"Žitomír": 1, "Popokatepetl": 3, "Bohumil": 2, "Zdislava": 1}
  jmeno = input("Koho chces vedet pocet gulí?").capitalize()
  vypisGulePro(gule, jmeno)


def vypisGulePro(gule, jmeno):
  if jmeno in gule:
    print(jmeno, gule[jmeno])


if __name__ == "__main__":
  main()


#######################################################
def main():
  gule = {"Žitomír": 1, "Popokatepetl": 3, "Bohumil": 2, "Zdislava": 1}
  vypisVse(gule)


def vypisVse(gule):
  for vseci in gule:
    print(vseci, gule[vseci])


if __name__ == "__main__":
  main()


#######################################################
def main():
  gule = {"Žitomír": 1, "Popokatepetl": 3, "Bohumil": 2, "Zdislava": 1}
  jmeno = input("Komu chces pridat guli?").capitalize()
  pridejGule(gule, jmeno)


def pridejGule(gule, jmeno):
  if jmeno in gule:
    print(jmeno, gule[jmeno] + 1)


if __name__ == "__main__":
  main()


#######################################################
def main():
  gule = {"Žitomír": 1, "Popokatepetl": 3, "Bohumil": 2, "Zdislava": 1}
  jmeno = input("Komu chces odebrat guli?").capitalize()
  odeberGule(gule, jmeno)


def odeberGule(gule, jmeno):
  if jmeno in gule:
    print(jmeno, gule[jmeno] - 1)


if __name__ == "__main__":
  main()


#######################################################
def main():
  gule = {"Žitomír": 1, "Popokatepetl": 3, "Bohumil": 2, "Zdislava": 1}
  jmeno = input("Komu chces pridat guli?").capitalize()
  pocet = int(input("kolik uz ma gulí?"))
  novaGule(gule, jmeno, pocet)


def novaGule(gule, jmeno, pocet):
  gule[jmeno] = pocet
  print(jmeno, gule[jmeno])
  print(gule)


if __name__ == "__main__":
  main()


#######################################################
def main():
  gule = {"Žitomír": 1, "Popokatepetl": 3, "Bohumil": 2, "Zdislava": 1}
  gulusmaximus = max(gule.values())
  gulusgigantos = [
      typek for typek, value in gule.items() if value == gulusmaximus
  ]
  nejvetsiGule(gule, gulusgigantos, gulusmaximus)


def nejvetsiGule(gule, gulusgigantos, gulusmaximus):

  print("Nejvíc gulí má:", gulusgigantos[0], gulusmaximus)


if __name__ == "__main__":
  main()


