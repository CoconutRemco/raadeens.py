mydeck = ["2","3","4","5","6","7","8","9","10","Aas","Boer","Vrouw","Heer","Joker"]
mycards = ["Harten","Schoppen","Klaveren","Ruiten"]
mymadedeck = []
for j in mycards:
    for i in mydeck:
        mymadedeck.insert(1,j+i)
        if len (mymadedeck)>54:
            mymadedeck = mymadedeck[:54]
            print(mymadedeck[0:7])
            input("Enter om uw volledige deck te zien")
            print(mymadedeck[7:54])
