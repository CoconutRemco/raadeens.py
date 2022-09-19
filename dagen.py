
def Reverse(mytuple):
    new_tup = mytuple[::-1]
    return new_tup
mytuple = ("Maandag","Dinsdag","Woensdag","Donderdag","Vrijdag","Zaterdag","Zondag")


print(mytuple)
print(mytuple[0:5])
print(mytuple[5:7])
print(Reverse(mytuple))
print(Reverse(mytuple[0:5]))
print(Reverse(mytuple[5:7]))

