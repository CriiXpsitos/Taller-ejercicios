price = int(input("enter the price of the product: "))
number = int(input("enter a number random for a discount: "))
if number < 65:
    discount = price * .20 
    price -= discount
    print(f"The price will be {price} with a discount of {discount}")
else: 
    discount = price * .30 
    price -= discount
    print(f"congratulations you have a discount of 30%, this is your price {price}")