import random

namenloodjes = []
loodjes = {}
names = []
print('voer 3 unieke namen in!')
for i in range(3):
    name = input("Voer een unieke naam in")
    if name not in names:
        names.append(name)
        namenloodjes.append(name)
    else:
        print("HOO IS EVEN ER IS EEN DUBBELE NAAM IN GEVULD GEKKIE")
    if len(names) == 3:
        for i in range(10):
            ja = input('Nog een naam toevoegen? 1 ja 2 nee')
            if ja == '1':
                name = input("Voer een unieke naam in")
                if name not in names:
                    names.append(name)
                    namenloodjes.append(name)
                else:
                    print("HOO IS EVEN ER IS EEN DUBBELE NAAM IN GEVULD GEKKIE")
            print(len(names))
        for i in range(len(names)):
            randomname=random.choice(namenloodjes)
            namenloodjes.remove(randomname)
            loodje=random.choice(names)
            names.remove(loodje)
            if loodje == randomname:
                pass
            else:
                loodjes[randomname]=loodje
        print(loodjes)
    
    