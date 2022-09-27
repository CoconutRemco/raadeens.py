import fruitmand
weight = 0
kleur = input('Welke kleur wilt u? yellow, green, orange, red, brown? ').lower()

kleuren = sorted(fruitmand.fruitmand, key=lambda x: x['color'], reverse = True)
for i in kleuren:
    if i['color'] == kleur:
        weight += (i)['weight']
print(weight)
    