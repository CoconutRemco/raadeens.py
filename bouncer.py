leeftijd = input("Wat is uw leeftijd?")
bandje = 0
sticker = 0
if int(leeftijd) > 17:
    print("U mag naar binnen!")
    naam = input("Wat is uw naam?")
    if int(leeftijd) < 21:
        bandje = 1
        if naam == "Rudi"or naam == "Arnold"or naam =="Jeroen"or naam =="Kjeld":
            print("U krijgt een sticker!")
            sticker = 1
        else:
            print("U krijgt geen bandje!")
    else:
        bandje = 2
        print("U krijgt een bandje!")
    drinken = input("Wat wilt u drinken? A) Bier 1.50 B) Cola 1.00")
    if drinken == "A":
        if bandje == 2:
            print("Oke geniet van uw Bier")
        else:
            print("U bent te jong om bier te bestellen!")
    if drinken == "B":
        if sticker == 1:
            print("U krijgt de cola gratis!")
        else:
            print("Oke geniet van uw Cola")
else:
    print("Helaas u word niet toegelaten!")