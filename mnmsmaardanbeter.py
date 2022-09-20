import random


kleuren = ["rood","geel","groen","bruin","blauw"]
aantal = input("Hoeveel mnms wilt u in de zak?")

rood = random.randint(0,int(aantal))
overige1 = int(aantal)-int(rood)
blauw = random.randint(0,int(overige1))
overige2 = int(overige1)-int(blauw)
groen = random.randint(0,int(overige2))
overige3 = int(overige2)-int(groen)
bruin = random.randint(0,int(overige3))
overige4 = int(overige3)-int(bruin)
geel = overige4

zak = {}


if rood > 0:
    zak['rood']= rood
if blauw > 0:
    zak['blauw']= blauw
if groen > 0:
    zak['groen']= groen
if bruin > 0:
    zak['bruin']= bruin
if geel > 0:
    zak['geel']= geel

print(zak)
