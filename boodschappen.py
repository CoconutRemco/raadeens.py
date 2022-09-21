boodschappen = {}
for i in range(10):
        boodschap = input("Wat voor boodschappen wilt u in uw mandje doen?").lower()
        aantal = int(input("Hoevaak wilt u dit item in uw mandje?"))
        if  boodschap in boodschappen.keys():
            boodschappen[boodschap] += (aantal)
        else:
            boodschappen[boodschap] = aantal
        print(boodschappen)

        door = input("Wilt u nog meer toevoegen? 1 ja 2 nee")
        if door > '1':
            print("Oke dan zijn dit uw boodschappen." + str(boodschappen))

