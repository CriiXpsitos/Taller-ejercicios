num1 = int(input("enter your first number: "))
num2 = int(input("enter your second number: "))
num3 = int(input("enter your thirt number: "))

if num1 >= num2 and num1 >= num3:
    mayor = num1 
elif num2 >= num1 and num2 >= num3:
    mayor = num2
else:
    mayor = num3 
print(f"the mayor number is {mayor}")