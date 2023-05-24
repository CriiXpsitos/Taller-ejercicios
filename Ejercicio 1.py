# Diseñe un algoritmo que capture dos números, y que realice la suma de
# dichos números, y mostrar los datos si es el resultado no es negativo
Note1 = float(input("Enter the first note : "))
Note2 = float(input("Enter the second note: "))

addition = Note1 + Note2

if addition > 0:
    print(f"the addition of {Note1} and {Note2} is {addition}")
else:
    print(f"{addition} juas juas, the addition is minor that zero")