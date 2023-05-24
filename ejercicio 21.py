print("Welcome to my store \n We sell different types of motorcycles ")
print("Honda brand motorcycles are discounted at of 4 discount off \nYamaha brand motorcycles are discounted at of 7 discount off \nsusuki brand motorcycles are discounted at of 15 discount off")
motos = input("which motorcycle are you going to buy?:  ")
Honda_discount = (100 * .4)
Honda_price = (100 - Honda_discount)
Susuki_discount = (100 * .15)
Susuki_price = (100 - Susuki_discount)
Yamaha_discount = (100 * .7)
Yamaha_price = (100 - Yamaha_discount)
if motos == "HONDA" or motos == "honda":
    print(f"your motocycle coust ${Honda_price}") 
elif motos == "SUSUKI" or motos == "susuki":
    print(f"your motocycle coust ${Susuki_price}")
elif motos == "YAMAHA" or motos == "yamaha":
    print(f"your motocycle coust {Yamaha_price}")
elif motos == "other" or motos == "OTHER":
    print("the other motos have discount 3%")
else: 
    print("excuse me")