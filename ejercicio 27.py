num1 = float(input("enter your first number: "))
num2 = float(input("enter your second number: "))
operation = (input("what operation do you want?: "))

if operation == "sum" or operation == "SUM":
    print(num1 + num2)
elif operation == "subtract" or operation == "SUBTRACT":
    print(num1 - num2)
elif operation == "multiplication" or operation == "MULTIPLICATION":
    print(num1 * num2)
elif operation == "division" or operation == "DIVISION": 
    print(num1 // num2)
else: 
    print("no numbers")