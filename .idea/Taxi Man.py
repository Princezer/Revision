Name = ""
Driving = "yes"
trips = 0
time = 0
Cost = 0

#start Code
Name = input("Hello Driver,\n"
             "Welcome to TaxiMan,\n"
             "Lets start with your name\n"
             ">")

while Driving == "yes" or Driving == "y" or trips >= 0:
    Driving = input("HAve you gone for a drive yet?\n"
                    "> ")
    if Driving == "yes" or Driving == "y":
        time = int(input("How long was the trip?\n"
                     "> "))
        Cost = time*2 + 10
        print (Cost)

    else:
        Driving = "no"

print ("thank you for using the TaxiMan service")