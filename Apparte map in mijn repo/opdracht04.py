import random
import fruitmand

aantal = input('Wat is het aantal?')
i = random.randint(0,len(fruitmand.fruitmand))
for j in range(int(aantal)):
    print(fruitmand.fruitmand[i]['name'])