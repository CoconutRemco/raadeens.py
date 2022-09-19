import random
import sys
for j in range(20):
    num1 = random.randint(1,1000)
    print(num1)
    score = 0
    ronde = 0
    ronde += 1
    for i in range(10):
        guess1 = input("Raad het nummer van 1 tm 1000")
        if int(guess1) == num1:
            score += 1
            print("wow u heeft het nummer geraden!")
            print("Ronde " + str(ronde) + " is afgelopen score= " + str(score))
            spelen = input("Nog een keer spelen? 1 ja 2 nee")
            if int(spelen) > 1:
                print("Oke tot de volgende keer!" + sys.exit())
            else:
                print("Suc6 in de volgende ronde!")

        elif abs(num1 - int(guess1)) <= 20:
            print("U zit erg warm!")
        elif abs(num1 - int(guess1)) <= 50:
            print("U zit warm!")
        else:
            print("Ooh nee probeer het nog een keer")
    
        print("Ronde " + str(ronde) + " is afgelopen score= " + str(score))
        spelen = input("Nog een keer spelen? 1 ja 2 nee")
        if int(spelen) > 1:
            print("Oke tot de volgende keer!" + sys.exit())
        else:
            print("Suc6 in de volgende ronde!")


