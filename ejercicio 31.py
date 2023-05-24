payForHour = float(input("Enter the hourly rate: "))
hours = float(input("Enter the number of hours worked: "))
print("Categories: A,B,C or D")
category = str(input("Enter your category: "))

if category == "A" or category == "a":
    salary = payForHour * hours
    increment = salary * .1
    newSalary = salary + increment
    print(f"Your salary will be ${newSalary}, with a increment of 10%")
elif category == "B" or category == "b":
    salary = payForHour * hours
    increment = salary * .15
    newSalary = salary + increment
    print(f"Your salary will be ${newSalary}, with a increment of 15%")
elif category == "C" or category == "c":
    salary = payForHour * hours
    increment = salary * .23
    newSalary = salary + increment
    print(f"Your salary will be ${newSalary}, with a increment of 23%") 
elif category == "D" or category == "d":
    salary = payForHour * hours
    increment = salary * .25
    newSalary = salary + increment
    print(f"Your salary will be ${newSalary}, with a increment of 25%")
else:
    print("Enter a valid category")    