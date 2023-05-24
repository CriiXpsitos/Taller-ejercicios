years = int(input("Enter a year: "))

if years % 100 == 0 and years % 400 == 0:
    print("is leap year ")
else: 
    print("This no leap year")