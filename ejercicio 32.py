gender = str(input("Enter your gender: "))
height = float(input("Enter your heigth: "))
age = float(input("Enter your age: "))
maritalStatus = str(input("Enter your marital status: "))

if gender.upper() =="WOMAN":
    if height > 1.60 and age >= 20 and age <= 25 and maritalStatus.upper() == "SINGLE": 
        print("welcome to the navy ")
    else:
        print("you could not enter the army ")
elif gender.upper() == "MAN":
    if height > 1.65 and age >= 18 and age <= 24 and maritalStatus.upper() == "SINGLE": 
        print("welcome to the navy ")
    else:
        print("you could not enter the army ")
else:
    print("Enter a valid gender")