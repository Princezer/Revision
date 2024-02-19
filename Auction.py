Highest_bid = 1
where_to = "blank"
items = ["table", "chair", "house", "chuck noris", "your mother", "wall"]
End = "no"
Add = "blank"
Running_bid = "false"
new_bid = 0
Retun_to_Menu = "anything"

def newbid(high):
    global Running_bid
    global Highest_bid

    new_bid = int(input(F"THE CURRENT HIGHEST BID IS {high}\n"
                        F"what would you like to bid?\n"
                        F"> "))
    if new_bid == -1:
        Running_bid = "False"
    elif new_bid >= (high):
        Highest_bid = new_bid


#Start Code

while End == "no":
    where_to = input("============================================================\n"
                     "WELCOME TO BUYING STUFF, BUT FAST AND STRESSFULL!\n"
                     "what would you like to do?\n"
                     "Add item to Auction list,  1\n"
                     "Chose an item to Acution,  2\n"
                     "Join current Auction,      3\n"
                     "End script,                4\n"
                     "> ")


    if where_to == "1":
        Add = input("What would you like to add to your Auction list?\n"
                    "> ").lower()
        items.append(Add)

        Retun_to_Menu = input("ENTER ANYTHING TO RETURN TO MENU\n"
                              "> ")


    elif where_to == "2":
        if Running_bid != "True":
            Item = input(f"What item would you like to Auction off?\n"
                         f"the avalible items to auction are:\n"
                         f"{items}\n"
                         f"pls enter full word\n"
                         f"> ").lower()
            items.remove(Item)
            Highest_bid = int(input("What would you like to make the starting bid?\n"
                                    ">$ "))
            Running_bid = ("True")

            Retun_to_Menu = input("ENTER ANYTHING TO RETURN TO MENU\n"
                                  "> ")
        else:
            Retun_to_Menu = input("Sorry, there is a bid running atm,\n"
                                  "to start a new auction you must end runnign one.\n"
                                  "enter anything to return to menu\n"
                                  "> ")


    elif where_to == "3":
        if Running_bid == "True":
            print (f"=========================================================\n"
                   f"WELCOME TO THE BIDDING!\n"
                   f"YOU ARE BIDDING FOR {Item}\n"
                   f"inter -1 to end bidding")
            while Running_bid == "True":
                newbid(Highest_bid)

            Retun_to_Menu = input("ENTER ANYTHING TO RETURN TO MENU\n"
                                  "> ")

        else:
            Retun_to_Menu = input("Sorry, There is no bid running at ths time.\n"
                                  "ENTER ANYTHING TO RETURN TO MENU\n"
                                  "> ")

    elif where_to == "4":
        End = "yes"



print ("Thank you for using BUYING STUFF, BUT FAST AND STRESSFUL\n"
       "Return Soon :] ")
