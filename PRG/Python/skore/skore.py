## Vytváření proměnných
text = "What  is the answer to the ultimate question of life, the universe, and everythin"
cislo = 42

## Příklad podmínky
skore = input("Jaké je tvé skóre?")

if skore == 90:
  znamka = "Výborně"
elif skore == 80:
  znamka = "Chvalitebně"
else:
  znamka = "Nedostatečně"

## Příklad cyklu
skore2 = int(input("Jaké je tvé skóre?"))
while skore2 < 60:
  print("Snaž se víc")
  skore2 = int(input("Jaké je tvé skóre?"))
## int = cisla
## float = desetine
## string = text
## for
for i in range(0, 11):
  print(i)