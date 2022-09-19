import random
num1 = random.randint(1,1000)

print(num1)

guess1 = input("Raad het nummer van 1 tm 1000")
if int(guess1) == num1:
    print("wow u heeft het nummer geraden!")
elif abs(num1 - int(guess1)) <= 50:
    print("U zit warm!")
elif abs(num1 - int(guess1)) <= 20:
    print("U zit erg warm!")
else:
    print("Ooh nee probeer het nog een keer")