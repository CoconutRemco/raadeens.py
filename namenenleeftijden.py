listnamenenleeftijden = []
leeftijden = []
def namenenleeftijden_func():
    namenenleeftijden = {}
    naam = input("Wat is uw naam?")
    leeftijd = input("Wat is uw leeftijd?")
    leeftijden.append(leeftijd)     
    namenenleeftijden[naam] = leeftijd
    return namenenleeftijden
var1 = True
while var1 == True:
    dict1=namenenleeftijden_func()

    if "stop" in dict1:
        var1 = False
    else:
        listnamenenleeftijden.append(dict1)
for i in range(len(listnamenenleeftijden)):
    for keys in listnamenenleeftijden[i]:
        print(keys + " is " + leeftijden[i] + " jaar")

        
    
        

       
        
            
        


