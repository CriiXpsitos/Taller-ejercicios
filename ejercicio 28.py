price = int(input("Enter the value of the purchase: "))
number = int(input("Enter how many smock you are going to buy: "))

if price > 40000:
    smock = str(input("Enter the color of the smoke: "))
    if smock.upper() == "RED":
        discount = price * .10
        discountNum = discount * number
        price = (price * number) - discountNum
        print(f"The price will be ${price} with a discount of ${discountNum}")
    elif smock.upper() == "WHITE":
        discount = price * .15
        discountNum = discount * number
        price = (price * number) - discountNum
        print(f"The price will be ${price} with a discount of ${discountNum}")
    elif smock.upper() == "BLACK":
        discount = price * .20
        discountNum = discount * number
        price = (price * number) - discountNum
        print(f"The price will be ${price} with a discount of ${discountNum}")
    elif smock.upper() == "YELLOW":
        discount = price * .20
        discountNum = discount * number
        price = (price * number) - discountNum
        print(f"The price will be ${price} with a discount of ${discountNum}")
    elif smock.upper() == "GREEN":
        discount = price * .30
        discountNum = discount * number
        price = (price * number) - discountNum
        print(f"The price will be ${price} with a discount of ${discountNum}")
    else:
        print("Enter a valid color...")
else:
    print(f"The price will be ${price} without any discount")