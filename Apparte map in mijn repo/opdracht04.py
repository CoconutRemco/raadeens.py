import random
import fruitmand

aantal = input('Wat is het aantal?')
i = random.randint(0,7)
for j in range(int(aantal)):
    print(fruitmand.fruitmand[i]['name'])