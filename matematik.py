#https://discuss.codecademy.com/t/how-to-go-back-to-the-beginning-of-an-if-elif-statement/416536


import math



while True:
    handling = input("Hvilken handling vil du udføre?(a: Sidelægnde  b: Vinkelsum)").lower()
    if handling == "a":
        print("A Godkendt")
    elif handling == "b":
        print("B Godkendt")
    else:
        print("Ugyldig tast. Prøv igen")


    if handling == "a":

      while True:
        retvinkel = input("Hvilken trekant er det?(a: Retvinklet  b: Vilkårlig trekant)").lower()
        if retvinkel == "a":
            print("Trekant er retvinklet")
            #Spørger om sider og bruger dem i pythagoras for at finde side længder.
            while True:
                kendteSider = int(input("Hvor mange sider i trekanten kender du?(0 , 1 , 2)"))
                if kendteSider == 2:
                    print("Du kender 2 sider")

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

                    if ukendteSide == "a":
                        print("du kender side b og c")
                        kendteSideNavn1 = "b"
                        kendteSideNavn2 = "c"

                        print("Hvor lang er ", kendteSideNavn1, "?")
                        kendteside1 = int(input(""))

                        print("Hvor lang er ", kendteSideNavn2, "?")
                        kendteside2 = int(input(""))

                        print("Udregner c^2-b^2=a^2")
                        print(math.sqrt((kendteside2 ** 2) - (kendteside1 ** 2)))
                        break

                    elif ukendteSide == "b":
                        print("du kender ikke side a og c")
                        kendteSideNavn1 = "a"
                        kendteSideNavn2 = "c"

                        print("Hvor lang er ", kendteSideNavn1, "?")
                        kendteside1 = int(input(""))

                        print("Hvor lang er ", kendteSideNavn2, "?")
                        kendteside2 = int(input(""))

                        print("Udregner c^2-a^2=b^2")
                        print(math.sqrt((kendteside2 ** 2) - (kendteside1 ** 2)))
                        break

                    elif ukendteSide == "c":
                        print("du kender ikke side b og c")
                        kendteSideNavn1 = "a"
                        kendteSideNavn2 = "b"

                        print("Hvor lang er ", kendteSideNavn1, "?")
                        kendteside1 = int(input(""))

                        print("Hvor lang er ", kendteSideNavn2, "?")
                        kendteside2 = int(input(""))

                        print("Udregner a^2 + b^2 = c^2")
                        print(math.sqrt((kendteside1 ** 2) + (kendteside2 ** 2)))
                        break



                elif kendteSider == 1 or 0:
                    print("Hvor mange vinkler i trekanten kender du?(0 , 1 , 2)(Udover den rettevinkel)")
                    kendteVinkler = int(input())
                    if kendteVinkler == 1 and kendteSider == 1:
                        kendteVinkelPos = input("Hvilken vinkel kender du? (a, b)").lower()
                        if kendteVinkelPos  == "a":
                            math.acos()


                        #TODO: Udregn med cosinus eller sinus
                    break
                else:
                    continue

        elif retvinkel == "b":
            # TODO: Gør vilkårlig trekants beregner funktionel
            print( "Trekant er vilkårlig")
            print( "       C ")
            print( "        ..   ")
            print( "       .  .   ")
            print( "    b .    .  a")
            print( "     .      .   ")
            print( "    .        .  ")
            print( "   .          . ")
            print( "A .............. B")
            print( "       c")

        else:
            print("Ugyldig tast. Prøv igen")



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