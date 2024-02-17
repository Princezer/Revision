Doing = "Nothing"
Child = "nothing"
childroll =[]
offedchild = "gone"
time = 0

#PROGRAM STARTS

while Doing != "x":
    Doing = input("Do you want to pick up or drop off a child?\n"
                  "press 'P' for pick up and 'D' for drop off\n"
                  "> ").lower()

    if Doing == "d":
        Child = input("What is your childs name?")
        childroll.append(Child)
        print(childroll)

    elif Doing == "p":
        offedchild = input("child name? ")
        childroll.remove(offedchild)

        time=int(input("How long was your child at daycare?\n"
                       "> "))
        print(f"In that case, you owe us ${time*12}.\n"
              f"thanks :]")


print("Thank you for using satans child care")