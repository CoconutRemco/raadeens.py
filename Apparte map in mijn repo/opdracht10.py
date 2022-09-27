import fruitmand


names = sorted(fruitmand.fruitmand, key=lambda x: x['weight'], reverse = True)
for i in names:
    print(i['name'])



