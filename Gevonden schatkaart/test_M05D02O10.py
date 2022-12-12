from functions import getMaxAmountOfNightsInInn, getJourneyInnCostsInGold

if getMaxAmountOfNightsInInn(0, 1, 1) != 0:
    print('Test 1 is False')
else:
    print('Test 1 is correct')

if getMaxAmountOfNightsInInn(1, 1, 1) != 1:
    print('Test 2 is False')
else:
    print('Test 2 is correct')

if getMaxAmountOfNightsInInn(10, 2, 1) != 7:
    print('Test 3 is False')
else:
    print('Test 3 is correct')

if getMaxAmountOfNightsInInn(5, 100, 100) != 0:
    print('Test 4 is False')
else:
    print('Test 4 is correct')

if getMaxAmountOfNightsInInn(5, 2, 2) != 3:
    print('Test 5 is False')
else:
    print('Test 5 is correct')

if getJourneyInnCostsInGold(1,1,1) != 0.68:
    print('Test 6 is False')
else:
    print('Test 6 is correct')

if getJourneyInnCostsInGold(0,10,10) != 0:
    print('Test 7 is False')
else:
    print('Test 7 is correct')

if getJourneyInnCostsInGold(3,12,4) != 22.56:
    print('Test 8 is False')
else:
    print('Test 8 is correct')

if getJourneyInnCostsInGold(10,0,0) != 0.0:
    print('Test 9 is False')
else:
    print('Test 9 is correct')

if getJourneyInnCostsInGold(123,421,124) != 32289.96:
    print('Test 10 is False')
else:
    print('Test 10 is correct')
