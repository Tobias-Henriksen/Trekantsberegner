#https://discuss.codecademy.com/t/how-to-go-back-to-the-beginning-of-an-if-elif-statement/416536


import math


while True:
    handling = input("Hvilken handling vil du udføre?(a: Pythagoras  b: Vinkelsum)").lower()
    if handling == "a":
        print("A Godkendt")
    elif handling == "b":
        print("B Godkendt")
    else:
        print("Ugyldig tast. Prøv igen")

    if handling == "a":

      retvinkel = input("Hvilken trekant er det?(a: Retvinklet  b: Vilkårlig trekant)").lower()
      #TODO: Gør det funktionelt

      print("        b    ")
      print("   ___________")
      print("  |__________/")
      print("  |_________/")
      print("  |________/")
      print("  |_______/")
      print("a |______/ c")
      print("  |_____/")
      print("  |____/")
      print("  |___/")
      print("  |__/")
      print("  |_/")
      print("  |/")


      ukendteSide = input("Hvilken side kender du ikke? (a,b,c)")
      print("Du kender ikke side ", ukendteSide)


      if ukendteSide=="a":
        print("du kender side b og c")
        kendteSideNavn1 = "b"
        kendteSideNavn2 = "c"


      elif ukendteSide=="b":
        print("du kender ikke side a og c")
        kendteSideNavn1 = "a"
        kendteSideNavn2 = "c"



      elif ukendteSide=="c":
        print("du kender ikke side b og c")
        kendteSideNavn1 = "a"
        kendteSideNavn2 = "b"

      print("Hvor lang er ",kendteSideNavn1,"?")
      kendteside1 = int(input(""))

      print("Hvor lang er ",kendteSideNavn2,"?")
      kendteside2 = int(input(""))

      if ukendteSide=="c":
        print("Udregner a^2 + b^2 = c^2")
        print(math.sqrt((kendteside1**2) + (kendteside2**2)))

      elif ukendteSide=="b":
        print("Udregner c^2-a^2=b^2")
        print(math.sqrt((kendteside2**2) - (kendteside1**2)))

      elif ukendteSide=="a":
        print("Udregner c^2-b^2=a^2")
        print(math.sqrt((kendteside2**2) - (kendteside1**2)))

    elif handling=="b":
      print("Du har valgt beregning af vinkel summen")

      #Kører et tjek på om vinklerne er gyldige og om de er inden for vinkelsummen.
      while True:
        vinkel1 = int(input("Hvor stor er den første vinkel?"))
        vinkel2 = int(input("Hvor stor er den anden vinkel?"))

        if vinkel1 + vinkel2 > 180:
          print("Ugyldige vinkler")
        elif vinkel1 + vinkel2 < 180:
          print("Gyldige vinkler")

          ukendteVinkel = 180 - (vinkel1 + vinkel2)
          print("Den sidste vinkel i trekanten er:")
          print(ukendteVinkel)

          break
        else:
          print("Ugyldigt input")


      exit()