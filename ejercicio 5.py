investment = float(input("Enter your initial investment: "))
interest = float(input("Enter the interest rate: "))

reinvestment = investment * interest

if investment <= 7000:
    finalInvestment = investment + reinvestment
    print(f"The final amount of money in your account is {finalInvestment}")

else:
    finalInvestment = investment + 7000
    print(f"The final amount of money in your account is {finalInvestment}")