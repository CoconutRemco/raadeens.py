from functions import getFromListByKeyIs

thingsList = [
    {
        'name' : 'Pie',
        'tasty' : True,
        'round' : True
    },{
        'name' : 'Fries',
        'tasty' : True,
        'round' : False
    },{
        'name' : 'Soccerball',
        'tasty' : False,
        'round' : True
    }
]

result1 = [{
        'name' : 'Pie',
        'tasty' : True,
        'round' : True
    }, {
        'name' : 'Soccerball',
        'tasty' : False,
        'round' : True
    }]

if getFromListByKeyIs(thingsList, 'round', True) != result1:
    print('Test 1 is False')
else:
    print('Test 1 is correct')


result2 = [{
        'name' : 'Pie',
        'tasty' : True,
        'round' : True
    },{
        'name' : 'Fries',
        'tasty' : True,
        'round' : False
    }]

if getFromListByKeyIs(thingsList, 'tasty', True) != result2:
    print('Test 2 is False')
else:
    print('Test 2 is correct')

result3 = [{
        'name' : 'Fries',
        'tasty' : True,
        'round' : False
    }]

if getFromListByKeyIs(thingsList, 'round', False) != result3:
    print('Test 3 is False')
else:
    print('Test 3 is correct')