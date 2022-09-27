import fruitmand


del fruitmand.fruitmand[4]
colors = []

for j in range(len(fruitmand.fruitmand)):
    if fruitmand.fruitmand[j]['color'] not in colors:
         colors.append(fruitmand.fruitmand[j]['color'])
print(colors)
    



