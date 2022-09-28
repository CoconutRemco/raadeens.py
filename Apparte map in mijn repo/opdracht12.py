import fruitmand
colorst= {"pink" : "roze",
          "red" : "rood",
          "blue" : "blauw",
          "yellow" : "geel",
          "brown" : "bruin",
            "green" : "groen",
           "purple" : "paars",
           "orange" : "oranje"}

langstefruit = {"name":""}
for f in fruitmand.fruitmand:
    if len(langstefruit["name"]) < len(f['name']):
        langstefruit = f
naamlangstefruit = langstefruit['name']
gewichtlangstefruit = langstefruit['weight']/1000
kleurlangstefruit = langstefruit['color']
lengtenaamlangstefruit= len(langstefruit['name'])


print("De " + naamlangstefruit + " ("+ str(lengtenaamlangstefruit) + " Letters) Heeft een " + colorst[kleurlangstefruit] + " kleur en een gewicht van " + str(gewichtlangstefruit) + "KG")