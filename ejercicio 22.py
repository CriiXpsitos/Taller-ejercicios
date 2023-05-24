salary = int(input("enter your salary: "))
if salary <= 1000000: 
    discount = salary * .4 
    total = salary - discount
    print(f"your salary with discount is {total}")
elif salary >= 1000000 or salary <= 2000000: 
    discount = salary * .7 
    total = salary - discount
    print(f"your salary with discount is {total}")
elif salary > 2000000:
    discount = salary * .8
    total = salary - discount
    print(f"your salary with discount is {total}")
else: 
    print("your salary is what?")
