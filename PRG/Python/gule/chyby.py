import sys

def znamenko_hej(x):
        if x > 0 :
             print("broski jses kladas")
        elif x < 0 :
             print("broski jses zaporas")
        else :
              print("broski jses nulos")
while True:
      try:
          cislo = int(input("zadej numero broski:"))
          znamenko_hej(cislo)
      except KeyboardInterrupt:
          print("broski python ma padla")
          sys.exit()
      except ValueError:
          print("broski to neni numero to je textis zadavaj numero")
      else:
          print("broski jsi to dal")
          break
      finally:
          print("broski jsi neco zrobil co fakt nevim")


