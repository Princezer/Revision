NUmbers = [1, 200, 3, 4, 50, 6, 7, 7, 9, 10, 0]
people = ["bob", "Dick", "harry", "steve"]

average = 0
Big = 0
Big_location = 0
worst = ""
#start code

average = sum(NUmbers) / len(NUmbers)
Big = max(NUmbers)

print(average, Big)

Big_location = (NUmbers.index(Big))
worst = (people[Big_location])

print (Big_location, worst)

zeros = []
for i, value in enumerate(NUmbers):
    if i <= 1:
       zeros.append(i)
    print (zeros)