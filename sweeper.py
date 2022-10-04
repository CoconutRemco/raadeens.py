import random


play = True
x =1
bomb = random.randint(1,10)
score = 0
while play == True:
    print('Het is ronde! ' + str(x))
    x += 1
    print(bomb)
    getal = input('Op welk getal denk je dat de bom ligt? 1tm10')
    if int(getal) == bomb:
        play = False
        print("Boem! Game over")
    else:
        score += x*x
        n1k = input('wilt u naar ronde '+ str(x) + ' Y/N ?').lower()
        if n1k == 'n':
            play = False
print('Uw score is ' + str(score))

    



    


