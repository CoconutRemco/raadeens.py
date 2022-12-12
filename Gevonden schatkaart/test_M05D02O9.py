from functions import getTotalInvestorsCosts

testInverstorsList1 = [{
    'profitReturn' : 5,
    'adventuring' : True
}]

testGearList1 = [{
    'amount' : 3,
    'price' : {
        'amount' : 1,
        'type' : 'gold'
    }
}]

if getTotalInvestorsCosts(testInverstorsList1, testGearList1) != 21.54:
    print('Test 1 is False')
else:
    print('Test 1 is correct')

testGearList2 = [{
    'amount' : 3,
    'price' : {
        'amount' : 3,
        'type' : 'copper'
    }
},{
    'amount' : 1,
    'price' : {
        'amount' : 10,
        'type' : 'silver'
    }
}]

if getTotalInvestorsCosts(testInverstorsList1, testGearList2) != 20.72:
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

if getTotalInvestorsCosts(testInverstorsList2, testGearList2) != 20.72:
    print('Test 3 is False')
else:
    print('Test 3 is correct')


testGearList3 = [{
    'amount' : 1,
    'price' : {
        'amount' : 2,
        'type' : 'platinum'
    }
},{
    'amount' : 5,
    'price' : {
        'amount' : 7,
        'type' : 'silver'
    }
},{
    'amount' : 19,
    'price' : {
        'amount' : 10,
        'type' : 'copper'
    }
}]

if getTotalInvestorsCosts(testInverstorsList1, testGearList3) != 79.34:
    print('Test 4 is False')
else:
    print('Test 4 is correct')


testInverstorsList3 = [{
    'profitReturn' : 5,
    'adventuring' : True
},{
    'profitReturn' : 9,
    'adventuring' : True
},{
    'profitReturn' : 1,
    'adventuring' : False
}]

if getTotalInvestorsCosts(testInverstorsList3, testGearList3) != 158.68:
    print('Test 5 is False')
else:
    print('Test 5 is correct')