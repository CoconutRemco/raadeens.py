import fruitmand
langstefruit = {"name":""}
for f in fruitmand.fruitmand:
    if len(langstefruit["name"]) < len(f['name']):
        langstefruit = f
naamlangstefruit = langstefruit['name']
gewichtlangstefruit = langstefruit['weight']/1000
kleurlangstefruit = langstefruit['color']
lengtenaamlangstefruit= len(langstefruit['name'])
if kleurlangstefruit == 'orange':
    kleurlangstefruit = 'oranje'
elif kleurlangstefruit == 'brown':
    kleurlangstefruit = 'bruin'
elif kleurlangstefruit == 'green':
    kleurlangstefruit = 'groen'
elif kleurlangstefruit == 'red':
    kleurlangstefruit = 'red'
else:
    kleurlangstefruit = 'yellow'
print("De " + naamlangstefruit + " ("+ str(lengtenaamlangstefruit) + " Letters) Heeft een " + kleurlangstefruit + " kleur en een gewicht van " + str(gewichtlangstefruit) + "KG")