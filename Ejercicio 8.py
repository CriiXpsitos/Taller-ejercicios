name = str(input("enter your name: "))
incomes = float(input("how much is your income: "))
expenditures = float(input("how much is your expenditure: "))

Total = incomes - expenditures

if Total <= 2000: 
    print(f"{name} you have to work harder, lazybones, your numbers are in the red. ")
elif Total <= 3000:
    print(f"{name} you are doing well :3")
elif Total > 3000: 
    print(f"{name} oh my goodness, what a good state they financed ")