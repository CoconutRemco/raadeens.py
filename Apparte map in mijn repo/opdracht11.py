import fruitmand
rond = 0
nietrond = 0
colors = []
for j in range(len(fruitmand.fruitmand)):
    if fruitmand.fruitmand[j]['color'] not in colors:
        colors.append(fruitmand.fruitmand[j]['color'])
print(colors)
kleur = input('Welke kleur wilt u? ').lower()
if kleur in colors:
    pass
else:
    print('HEY ' +kleur+ ' IS GEEN KLEUR UIT DE LIJSTTT')

kleuren = sorted(fruitmand.fruitmand, key=lambda x: x['color'], reverse = True)
for i in kleuren:
    if i['color'] == kleur:
      if i['round'] == True:
        rond += 1
      else:
        nietrond += 1
if rond > nietrond:
    print('Wow er zijn'+ str(rond-nietrond) + 'meer ronde dan niet ronde fruitsoorten van deze kleur')
elif rond == nietrond:
    print("Wow er zijn evenveel ronde " +str(rond)+ " als niet ronde "+str(nietrond)+ " van deze kleur!")
elif rond < nietrond:
    print("Wow er zijn "+ str(nietrond-rond) + "meer niet ronde dan ronde van deze kleur!")
    