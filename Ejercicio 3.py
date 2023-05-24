# Diseñe un algoritmo que guarde el nombre del aprendiz, nombre del curso, 
# nota definitiva, el nro de clases en el semestre y el número de las fallas. En el 
# caso de que las fallas superen el 30% del número de clases se debe mostrar 
# la nota que no aprobó y se calificara cero(0)

Name = str(input("enter your name: "))
course = str(input("enter the name of the course: "))
Notes1 =float(input("ingresas las notas"))
Notes2 =float(input("ingresas las notas"))
Notes3 =float(input("ingresas las notas"))
grade_points_average = (Notes1 + Notes2 + Notes3) / 3
Classes = float(input("enter the number of assistances "))
Faults = float(input(" enter the faults: "))

Not_aproved = Classes > (Faults * 0.3)

if Not_aproved is True: 
    print("Aprove")
else: 
    print("Not aprove")
print(f"Your name is {Name}, your course is {course} and your notes is {Notes1, Notes2, Notes3} \n your avarage is {grade_points_average}")


