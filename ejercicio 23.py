day = input("what day you are going to buy: ")
bought = input("are you going to buy something: ")
if day == "saturday" or day == "SATURDAY" and bought == "yes" or bought == "YES":
    discount = 1000 * .18 
    total = 1000 - discount
    print(f"your motocycle with discount {total}")
elif day == "tuesday" or day == "TUESDAY" and bought == "yes" or bought == "YES":
    discount = 1000 * .10
    total = 1000 - discount
    print(f"your motocycle with discount {total}")
else: 
    print("excuse me?")

