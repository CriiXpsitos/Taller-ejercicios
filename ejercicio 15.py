shirts = int(input("----- welcome to our t-shirt store where we sell t-shirts ------ \n ----- each shirt is worth 25.000 ----- how many shirts will you buy?"))
if shirts >= 3: 
    total = 25000 * 0.15 
    print(f"the price to be paid is {total}")
elif shirts < 3: 
    total = 25000 * 0.5
    print(f"the price to be paid is {total}")