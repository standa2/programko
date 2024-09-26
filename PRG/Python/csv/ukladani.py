cesta = "H:\\WET\\PRG\\Python\\csv\\data.txt"
with open(cesta, "r") as file :
    print(file.read())

with open(cesta, "w") as file :
    text = "JABA DABA DOOOO"
    file.write(text)

with open(cesta, "a") as file :
    text = "\nJABA DABA DOOOO"
    file.write(text)

