import fruitmand
weight = 0
watermeloen ={"name":"watermeloen","weight":"2000","color":"green","round":True}
fruitmand.fruitmand.append(watermeloen)
for i in range(8):
    weight += int(fruitmand.fruitmand[i]['weight'])
print(weight)
    
