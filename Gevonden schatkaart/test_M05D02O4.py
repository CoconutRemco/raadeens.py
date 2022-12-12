from functions import getJourneyFoodCostsInGold

if getJourneyFoodCostsInGold(1,1) != 1.54:
    print('Test 1 is False')
else:
    print('Test 1 is correct')

if getJourneyFoodCostsInGold(12,3) != 12.54:
    print('Test 2 is False')
else:
    print('Test 2 is correct')

if getJourneyFoodCostsInGold(24,11) != 28.38:
    print('Test 3 is False')
else:
    print('Test 3 is correct')

if getJourneyFoodCostsInGold(0,0) != 0.0:
    print('Test 4 is False')
else:
    print('Test 4 is correct')

if getJourneyFoodCostsInGold(10,10) != 15.4:
    print('Test 5 is False')
else:
    print('Test 5 is correct')