print("what is your superheroe?")

skill1 = str(input("can he fly?: "))
skill2 = str(input("is he human?: "))
skill3 = str(input("has a mask ?: "))

if skill1.upper() == "YES" and skill2.upper() == "YES" and skill3.upper() == "YES":
    print("¿Your superhero is Iroman?")
elif skill1.upper() == "NO" and skill2.upper() == "YES" and skill3.upper() == "NO":
    print("Your superhero is spiderman?")
elif skill1.upper() == "YES" and skill2.upper() == "NO" and skill3.upper() == "NO":
    print("¿Your superhero is Thor?")
else:
    print("sorry, idk")