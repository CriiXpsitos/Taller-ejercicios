money = int(input("how many hours I work: "))

if money <= 20:
    total = 10000 * money
    print(f"your minimum salary is {total}")
elif money > 20: 
    total = 35000 * money 
    print(f"your minimum salary is {total}")
