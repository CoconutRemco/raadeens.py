import random
var2 = True
var1 = True
loodjes = {}
names = []
print('voer 3 unieke namen in!')
for i in range(3):
    name = input("Voer een unieke naam in")
    if name not in names:
        names.append(name)
    else:
        print("HOO IS EVEN ER IS EEN DUBBELE NAAM IN GEVULD GEKKIE")
    if len(names) == 3:
        while var1 == True:
            ja = input('Nog een naam toevoegen? 1 ja 2 nee')
            if ja == '1':
                name = input("Voer een unieke naam in")
                if name not in names:
                    names.append(name)
                else:
                    print("HOO IS EVEN ER IS EEN DUBBELE NAAM IN GEVULD GEKKIE")
            else:
                var1 = False
            namenloodjes = names.copy()
            random.shuffle(namenloodjes)
            while var2 == True:
                for x in names:
                    loodjes[x] = namenloodjes.pop(0)
                var2 = False
                for key in loodjes:
                    if loodjes[key] == key:
                        var2 == True

           
print(loodjes)
    