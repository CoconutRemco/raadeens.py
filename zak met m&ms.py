import random


mylist = ("Oranje", "Blauw", "Groen", "Bruin")

hoeveelheid = input("Hoeveel m&ms moeten er in de zak?")

oranje = random.randint(0,int(hoeveelheid))
overige1 = int(hoeveelheid)-int(oranje)
blauw = random.randint(0,int(overige1))
overige2 = int(overige1)-int(blauw)
groen = random.randint(0,int(overige2))
overige3 = int(overige2)-int(groen)
bruin = overige3

mylist2 = []
mylist2.insert(1 , oranje)
mylist2.insert(1, blauw)
mylist2.insert(1, groen)
mylist2.insert(1, bruin)


print("Het totaal gekozen aantal is " + str(hoeveelheid))
if oranje > 0:
    print("Waarvan " + str(oranje) + " Oranje")
if blauw > 0:
    print("Waarvan " + str(blauw) + " Blauw")
if groen > 0:
    print("Waarvan " + str(groen) + " Groen")
if bruin > 0:
    print("Waarvan " + str(bruin) + " Bruin")
