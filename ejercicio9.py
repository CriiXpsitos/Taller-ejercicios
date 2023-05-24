notes1 = float(input("enter your first note: "))
notes2 = float(input("enter your second note: "))
notes3 = float(input("enter your thirth note: "))
total = (notes1+ notes2+ notes3) / 3 
print(f"your final note is {total}")

if total >= 10: 
    print("your aprove")
else: 
    print("your not aprove")
