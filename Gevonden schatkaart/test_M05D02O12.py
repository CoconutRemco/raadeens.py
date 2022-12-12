from functions import getInvestorsCuts, getAdventurerCut
from random import randint

testInverstorsList1 = [{
    'profitReturn' : 5,
    'adventuring' : True
}]

if getInvestorsCuts(100, testInverstorsList1) != [5.0]:
    print('Test 1 is False')
else:
    print('Test 1 is correct')

if getInvestorsCuts(19.7, testInverstorsList1) != [0.98]:
    print('Test 2 is False')
else:
    print('Test 2 is correct')


testInverstorsList2 = [{
    'profitReturn' : 5,
    'adventuring' : True
},{
    'profitReturn' : 15,
    'adventuring' : True
},{
    'profitReturn' : 1,
    'adventuring' : False
}]

if getInvestorsCuts(50, testInverstorsList2) != [2.5, 0.5]:
    print('Test 3 is False')
else:
    print('Test 3 is correct')


testInverstorsList3 = [{
    'profitReturn' : 100,
    'adventuring' : True
},{
    'profitReturn' : 15,
    'adventuring' : True
},{
    'profitReturn' : 20,
    'adventuring' : False
}]

if getInvestorsCuts(randint(1,1000), testInverstorsList3) != []:
    print('Test 4 is False')
else:
    print('Test 4 is correct')


if getInvestorsCuts(randint(1,1000), []) != []:
    print('Test 5 is False')
else:
    print('Test 5 is correct')

if getAdventurerCut(100, [10.0, 10.0], 4) != 20.0:
    print('Test 6 is False')
else:
    print('Test 6 is correct')

if getAdventurerCut(100, [], 5) != 20.0:
    print('Test 7 is False')
else:
    print('Test 7 is correct')

if getAdventurerCut(150, [2.5, 1.9, 3.4, 12.3], 14) != 9.28:
    print('Test 8 is False')
else:
    print('Test 8 is correct')