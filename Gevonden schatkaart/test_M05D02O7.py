from functions import getItemsAsText, getItemsValueInGold

testList1 = [{
    'name' : 'Kaars',
    'amount' : 3,
    'unit' : 'x',
    'price' : {
        'amount' : 4,
        'type' : 'copper'
    }
}]

if getItemsAsText(testList1) != '3x Kaars':
    print('Test 1 is False')
else:
    print('Test 1 is correct')

if getItemsValueInGold(testList1) != 0.24:
    print('Test 2 is False')
else:
    print('Test 2 is correct')



testList2 = [{
    'name' : 'Voetbal',
    'amount' : 1,
    'unit' : ' ronde',
    'price' : {
        'amount' : 2,
        'type' : 'gold'
    }
},{
    'name' : 'Patat',
    'amount' : 11,
    'unit' : 'x',
    'price' : {
        'amount' : 4,
        'type' : 'silver'
    }
},{
    'name' : 'Cola',
    'amount' : 1,
    'unit' : 'l',
    'price' : {
        'amount' : 5,
        'type' : 'copper'
    }
},{
    'name' : 'Sinas',
    'amount' : 5,
    'unit' : 'dl',
    'price' : {
        'amount' : 12,
        'type' : 'copper'
    }
}]


if getItemsAsText(testList2) != '1 ronde Voetbal, 11x Patat, 1l Cola, 5dl Sinas':
    print('Test 3 is False')
else:
    print('Test 3 is correct')

if getItemsValueInGold(testList2) != 12.1:
    print('Test 4 is False')
else:
    print('Test 4 is correct')

testList3 = [{
    'name' : 'Diamand',
    'amount' : 1,
    'unit' : '',
    'price' : {
        'amount' : 7,
        'type' : 'platinum'
    }
}]

if getItemsAsText(testList3) != '1 Diamand':
    print('Test 5 is False')
else:
    print('Test 5 is correct')

if getItemsValueInGold(testList3) != 175:
    print('Test 6 is False')
else:
    print('Test 6 is correct')