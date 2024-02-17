Highest_bid = 100
Running_bid = "True"



#A
new_bid = int(input(F"THE CURRENT HIGHEST BID IS {Highest_bid}\n"
                    F"what would you like to bid?\n"
                    F"> "))
if new_bid == -1:
    Running_bid = "False"
elif new_bid >= Highest_bid:
    Highest_bid = new_bid



#B
def newbid(high):
    global Highest_bid
    global Running_bid

    new_bid = int(input(F"THE CURRENT HIGHEST BID IS {high}\n"
                        F"what would you like to bid?\n"
                        F"> "))
    if new_bid == -1:
        Running_bid = "False"
    elif new_bid >= (high):
        Highest_bid = new_bid

newbid(Highest_bid)



print (Highest_bid)