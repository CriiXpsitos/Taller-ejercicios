num1 = float(input("enter your first number: "))
num2 = float(input("enter your second number: "))
num3 = float(input("enter your first number: "))

if num1 <= num2 and num1 <= num3:
    menor = num1 
elif num2 <= num1 and num2 <= num3:
    menor = num2
else:
    menor = num3 
print(f"the minor number is {menor}")