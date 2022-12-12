from functions import getNumberOfHorsesNeeded, getNumberOfTentsNeeded, getTotalRentalCost

if getNumberOfHorsesNeeded(7) != 4:
    print('Test 1 is False')
else:
    print('Test 1 is correct')

if getNumberOfHorsesNeeded(4) != 2:
    print('Test 2 is False')
else:
    print('Test 2 is correct')

if getNumberOfTentsNeeded(7) != 3:
    print('Test 3 is False')
else:
    print('Test 3 is correct')

if getNumberOfTentsNeeded(8) != 3:
    print('Test 4 is False')
else:
    print('Test 4 is correct')

if getNumberOfTentsNeeded(6) != 2:
    print('Test 5 is False')
else:
    print('Test 5 is correct')

if getTotalRentalCost(1,2) != 23.0:
    print(f'Test 6 is False')
else:
    print('Test 6 is correct')

if getTotalRentalCost(5,2) != 67.0:
    print('Test 7 is False')
else:
    print('Test 7 is correct')

if getTotalRentalCost(3,11) != 99.0:
    print('Test 8 is False')
else:
    print('Test 8 is correct')