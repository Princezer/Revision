sub_1s = []
list = [1, 2, 3, 40, 0, 1, 0]
Output = []
people = ["he", "me", "ta", "no", "bo", "chadrick", "jord", 'Zach']


list.append(int(input("enter a number: ")))

for location, value in enumerate(list):
    if value < 5:
        sub_1s.append(location)

print("Indices of items less than 5:", sub_1s)

for item in (sub_1s):
    Output.append(people[item])

print (Output)





