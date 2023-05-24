name = str(input("enter your name: "))
value = float(input("what is the valor for the matricule: "))
university = str(input("are you a graduate of the university? "))
value2 = value - (value * 0.3) 

if university == "YES" or university == "yes": 
    print(f"wow, {name} this is your discount in your matricule: {value2}")
else: 
    print(f"Sr {name} this is your value {value}")