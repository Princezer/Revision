Number = 0
Happy = ("NO")

while Number < 10:
    print (Number)
    Number += 1
print ("All done!")


while Happy == "NO" or Happy == "N":
    Happy = input("are you happy?").upper()
    print (Happy)

print ("Good :]")