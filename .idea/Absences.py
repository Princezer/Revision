Employees = []
Employee = ""
Absenses = []
end = ""
Average = 0
Max = 0
Max_location = 0
Worst = ""
Sub_3s = []
location = 0
Value = 0
Bests = []

# start code

while Employee != "$":

    print("put name as '$' to get results")
    Employee = input("What is your employees name?\n"
                      "> ")
    Employees.append(Employee)

    if Employee != "$":
        Absenses.append(int(input(f"How many days was {Employees} absent?\n"
                            f"> ")))
#catorgorizes infomation

Average = sum(Absenses) / len(Absenses)
Max = max(Absenses)
Max_location = (Absenses.index(Max))
Worst = (Employees[Max_location])

for location, value in enumerate(Absenses):
    if value < 3:
        Sub_3s.append(location)

for item in Sub_3s:
    Bests.append(Employees[item])

print(f"===========================================================================\n"
      f"The average number of Absences was {Average} Days away.\n\n"
      f"The person with the most Absences was {Worst} with {Max} absences\n\n"
      f"the following people had less than 3 days absent:")
print(f"{Bests}")
print(f"with {Sub_3s} absences Respectivly")