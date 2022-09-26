import random


mydeck = ["2","3","4","5","6","7","8","9","10","Aas","Boer","Vrouw","Heer",]
mycards = ["Harten","Schoppen","Klaveren","Ruiten"]
mymadedeck = []
mymadedeck.append("Joker")
mymadedeck.append("Joker")
for j in mycards:
    for i in mydeck:
        mymadedeck.insert(1,j+i)
        print(len(mymadedeck))
    mymadedeck = mymadedeck[:54]
    random.shuffle(mymadedeck)
    for i in range(7):
        i+=1
        print("Kaart " +str(i) + ": " + str( mymadedeck[int(i)]))
    print("deck (47 kaarten)" + str(mymadedeck[7:54]))
    print(len(mymadedeck))
