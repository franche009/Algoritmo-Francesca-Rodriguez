#1. Escribir un programa que solicite ingresar 10 notas de alumnos y nos informe cuántos tienen notas mayores o iguales a 7 y cuántos menores.

contadorMayor=0
contadorMenor=0

for i in range(10):
    nota=int(input("Ingrese la nota de los alumnos: "))
    if nota>=7:
        contadorMayor= contadorMayor +1    
    else:
        contadorMenor= contadorMenor +1
print("La cantidad de alumnos con nota mayor o igual a 7 son: ")
print(contadorMayor)
print("La cantidad de alumnos con nota menor a 7 son: ")
print(contadorMenor)
