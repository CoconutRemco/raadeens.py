trueorfalse = False
keus = str(input("Wat wilt u doen? A) getallen optellen, B) getallen aftrekken, C) getallen vermenigvuldigen, D) getallen delen, E) getal ophogen, F) getal verlagen, G) getal verdubbelen of H) getal halveren?"))


n1 = int(input("Welk nummer wilt u"))
n2 = int(input("Welk nummer wilt u"))


def addition():
    ad = n1+n2
    return ad

var1=addition()

def substraction():
    su = n1-n2
    return su

var2=substraction()

def multiplication():
    mu = n1*n2
    return mu

var3=multiplication()

def division():
    di = n1/n2
    return di

var4=division()

def increment():
    inc = n1+1
    return inc

var5=increment()

def decrement():
    de = n1-1
    return de

var6=decrement()

def double():
    do = n1*2
    return do

var7=double()

def halve():
    ha = n1/2
    return ha

var8=halve()

if keus == "A":
    print(var1)
    keuze = var1
elif keus == "B":
    print(var2)
    keuze = var2
elif keus == "C":
    print(var3)
    keuze = var3
elif keus == "D":
    print(var4)
    keuze = var4
elif keus == "E":
    print(var5)
    keuze= var5
elif keus == "F":
    print(var6)
    keuze = var6
elif keus == "G":
    print(var7)
    keuze = var7
elif keus == "H":
    print(var8)
    keuze = var8

keus2 = input("Wil je wat met het antwoord " +str(keuze)+ " doen? A) iets optellen, B) iets aftrekken, C) met iets vermenigvuldigen, D) ergens door delen, E) ophogen, F) verlagen, G) verdubbelen, H) halveren of I) Nee?")
n3 = int(input("Welk nummer wilt u?"))
def addition():
    ad = int(keuze)+n3
    return ad

var1=addition()

def substraction():
    su = int(keuze)-n3
    return su

var2=substraction()

def multiplication():
    mu = int(keuze)*n3
    return mu

var3=multiplication()

def division():
    di = int(keuze)/n3
    return di

var4=division()

def increment():
    inc = int(keuze)+1
    return inc

var5=increment()

def decrement():
    de = int(keuze)-1
    return de

var6=decrement()

def double():
    do = int(keuze)*2
    return do

var7=double()

def halve():
    ha = int(keuze)/2
    return ha

var8=halve()

if keus2 == "A":
    print(var1)
    keuze = var1
elif keus2 == "B":
    print(var2)
    keuze = var2
elif keus2 == "C":
    print(var3)
    keuze = var3
elif keus2 == "D":
    print(var4)
    keuze = var4
elif keus2 == "E":
    print(var5)
    keuze= var5
elif keus2 == "F":
    print(var6)
    keuze = var6
elif keus2 == "G":
    print(var7)
    keuze = var7
elif keus2 == "H":
    print(var8)
    keuze = var8   
elif keus2 == "I":
    pass

