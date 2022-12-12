from functions import getCashInGoldFromPeople

testList1 = [{
    'cash' : {
        'platinum' : 1,
        'gold' : 2,
        'silver' : 3,
        'copper' : 12
    }
}]

if getCashInGoldFromPeople(testList1) != 27.84:
    print('Test 1 is False')
else:
    print('Test 1 is correct')

testList2 = [{
    'cash' : {
        'platinum' : 2,
        'gold' : 231,
        'silver' : 33,
        'copper' : 66
    }
},{
    'cash' : {
        'platinum' : 0,
        'gold' : 11,
        'silver' : 6,
        'copper' : 2
    }
}]

if getCashInGoldFromPeople(testList2) != 301.16:
    print('Test 2 is False')
else:
    print('Test 2 is correct')

testList3 = [{
    'cash' : {
        'platinum' : 0,
        'gold' : 0,
        'silver' : 0,
        'copper' : 0
    }
},{
    'cash' : {
        'platinum' : 0,
        'gold' : 0,
        'silver' : 0,
        'copper' : 0
    }
},{
    'cash' : {
        'platinum' : 0,
        'gold' : 0,
        'silver' : 0,
        'copper' : 0
    }
}]

if getCashInGoldFromPeople(testList3) != 0:
    print('Test 3 is False')
else:
    print('Test 3 is correct')