"""
1. En un curso de 4 alumnos se registraron las notas de sus exámenes y se
deben procesar de acuerdo a lo siguiente:
a. Ingresar nombre y nota de cada alumno (almacenar los datos en
dos listas paralelas)
b. Realizar un listado que muestre los nombres, notas y condición del
alumno. En la condición, colocar "Muy Bueno" si la nota es mayor o
igual a 8, "Bueno" si la nota está entre 4 y 7, y colocar "Insuficiente"
si la nota es inferior a 4.
c. Imprimir cuántos alumnos tienen la leyenda “Muy Bueno”.
"""

notas=[]
alumnos=[]
contador=0

for x in range(4):
    alumno=input(f"Ingrese el nombre del alumno n°{x}: ")
    alumnos.append(alumno)
    nota=int(input(f"Ingrese la nota del alumno n°{x}: "))
    notas.append(nota)

for i in range(4):
    if notas[i]>=8 and notas[i]<=10:
        print(f"{alumnos[i]} - {notas[i]} - Muy Bueno")
        contador=contador+1
    else:
        if notas[i]<8 and notas[i]>=4:
            print(f"{alumnos[i]} - {notas[i]} - Bueno")
        else:
            if notas[i]>0 and notas[i]<4:
                print(f"{alumnos[i]} - {notas[i]} - Insuficiente")

print(f"La cantidad de alumnos que se sacaron -Muy Bueno- son {contador}")