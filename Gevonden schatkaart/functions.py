import time

from data import (COST_FOOD_HORSE_COPPER_PER_DAY,
                  COST_FOOD_HUMAN_COPPER_PER_DAY, JOURNEY_IN_DAYS)
from termcolor import colored

##################### M04.D02.O2 #####################

def copper2silver(amount:int) -> float:
    return amount/10

def silver2gold(amount:int) -> float:
    return amount/5

def copper2gold(amount:int) -> float:
    num = copper2silver(amount)
    return silver2gold(num)

def platinum2gold(amount:int) -> float:
    return amount*25

def getPersonCashInGold(personCash:dict) -> float:
    num1 = copper2silver(personCash['copper'])
    num2 = silver2gold(personCash['silver'])
    num3 = platinum2gold(personCash['platinum'])
    geheel = num1+num2+num3
    return geheel
    

##################### M04.D02.O4 #####################

def getJourneyFoodCostsInGold(people:int, horses:int) -> float:
    bedragdagpersoon = people*COST_FOOD_HUMAN_COPPER_PER_DAY
    bedragdagpaard = horses*COST_FOOD_HORSE_COPPER_PER_DAY
    totaal = bedragdagpersoon+bedragdagpaard
    totaal*JOURNEY_IN_DAYS
    num1 = copper2silver(totaal)
    num2 = silver2gold(num1)
    return num2

##################### M04.D02.O5 #####################

def getFromListByKeyIs(list:list, key:str, value:any) -> list:
    personlist= []
    for i in list:
        if i[key] == value:
            personlist.append(i)
        
    return personlist

def getAdventuringPeople(people:list) -> list:
    var1 =getFromListByKeyIs(people, 'shareWith', True)
    return var1

def getShareWithFriends(friends:list) -> int:
    var1 = getFromListByKeyIs(friends, 'adventuring', True)
    return var1

def getAdventuringFriends(friends:list) -> list:
    var1=getAdventuringPeople(friends)
    var2=getShareWithFriends(friends)
    list1 = var1+var2
    return list1

##################### M04.D02.O6 #####################

def getNumberOfHorsesNeeded(people:int) -> int:
    pass

def getNumberOfTentsNeeded(people:int) -> int:
    pass

def getTotalRentalCost(horses:int, tents:int) -> float:
    pass

##################### M04.D02.O7 #####################

def getItemsAsText(items:list) -> str:
    pass

def getItemsValueInGold(items:list) -> float:
    pass

##################### M04.D02.O8 #####################

def getCashInGoldFromPeople(people:list) -> float:
    pass

##################### M04.D02.O9 #####################

def getInterestingInvestors(investors:list) -> list:
    pass

def getAdventuringInvestors(investors:list) -> list:
    pass

def getTotalInvestorsCosts(investors:list, gear:list) -> float:
    pass

##################### M04.D02.O10 #####################

def getMaxAmountOfNightsInInn(leftoverGold:float, people:int, horses:int) -> int:
    pass

def getJourneyInnCostsInGold(nightsInInn:int, people:int, horses:int) -> float:
    pass

##################### M04.D02.O12 #####################

def getInvestorsCuts(profitGold:float, investors:list) -> list:
    pass

def getAdventurerCut(profitGold:float, investorsCuts:list, fellowship:list) -> float:
    pass

##################### M04.D02.O13 #####################

def getEarnigs(profitGold:float, mainCharacter:dict, friends:list, investors:list) -> list:
    pass

##################### view functions #####################
def print_colorvars(txt:str='{}', vars:list=[], color:str='yellow') -> None:
    vars = map(lambda string, color=color: colored(str(string), color, attrs=['bold']) ,vars)
    print(txt.format(*vars))

def print_title(name:str) -> None:
    print_colorvars(vars=['=== [ {} ] ==='.format(name)], color='green')

def print_chapter(number:int, name:str) -> None:
    nextStep(2)
    print_colorvars(vars=['- CHAPTER {}: {} -'.format(number, name)], color='magenta')

def nextStep(secwait:int=1) -> None:
    print('')
    time.sleep(secwait)

def ifOne(amount:int, yes:str, no:str, single='een') -> str:
    text = yes if amount == 1 else no
    amount = single if amount == 1 else amount
    return '{} {}'.format(amount, text).lstrip()