Number1 = 0
number2 = 0

print("Here is how it works.\n"
        "You will put in two numbers,\n"
        "I will pick the bigger one.\n")
number1 = input("Put in your first number\n>")
number2 = input("Put in your second number\n>")

while number1 == number2:
    print("OI!\n"
          "you sneeky bugger!\n"
          "dont try breaking my code")
    number2 = input("Now\n"
                    "Put in a DIFFERENT number this time.")

if number1 >= number2:
    print("your first number Was bigger")
else :
    print("your second number Was bigger")


Numeral = 20
Sum = 0

while Numeral <= 25:
    print (Numeral)
    Sum += Numeral
    Numeral += 1

print ("The Sum of these numbers is", Sum)


Building_Type = "o"
Depth = 0
NS_length = 0
EW_length = 0
Repeat = 0
Volume = 0

while Building_Type != "R" and Building_Type != "C":
    if Repeat <= 1:
        print("Tht is an incorect option")
    elif Repeat <= 5:
        print("Honesty man ITS NOT A HARD QUESTION")
    else:
        print("What type of building would you like?")
    Building_Type = input("Resedential or Commersial?\n"
                          "For Resedential enter 'R'\n"
                          "For Commersial enter 'C'\n"
                          ">").upper()
    Repeat += 1
if Building_Type == "C":
    Depth = .5
else:
    Depth = .25

NS_length =int(input("What is the length of the foundation from North to South in m?\n"
                 ">"))
EW_length =int(input("What is the length of the foundation from East to West in m?\n"
                 ">"))
Volume = Depth * NS_length * EW_length

print("The Volume you need for your foundation is", Volume,"M^3")


