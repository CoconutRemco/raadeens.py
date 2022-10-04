import random
var2 = False
var1 = True
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
        while var1 == True:
            ja = input('Nog een naam toevoegen? 1 ja 2 nee')
            if ja == '1':
                name = input("Voer een unieke naam in")
                if name not in names:
                    names.append(name)
                    namenloodjes.append(name)
                else:
                    print("HOO IS EVEN ER IS EEN DUBBELE NAAM IN GEVULD GEKKIE")
            else:
                var1 = False
        for i in range(len(names)):
            randomname=random.choice(namenloodjes)
            loodje=random.choice(names)
            if loodje == randomname:
                var2 = True
                while var2 == True:
                    randomname=random.choice(namenloodjes)
                    loodje=random.choice(names)
                    if loodje != randomname:
                        var2 = False
                        names.remove(loodje)
                        namenloodjes.remove(randomname)
                        loodjes[randomname]=loodje

            else:
                names.remove(loodje)
                namenloodjes.remove(randomname)
                loodjes[randomname]=loodje
        print(loodjes)
    
    