"""
1. Se desea desarrollar un programa que permita registrar los nombres y las
calificaciones de 6 estudiantes. Luego de cargar los datos, se debe mostrar el
nombre del estudiante con la nota más alta, junto con su nota. Al igual que el
estudiante con la nota más baja. Informar si hay estudiantes con la misma nota
máxima o mínima.
"""

nombres=[]
notas=[]
alumnosMayor=0
alumnosMenor=0
notaMayor=0
notaMenor=0
contadorMayor=0
contadorMenor=0

for x in range (6):
    nombre=input(f"Ingrese el nombre del estudiante n°{x}: ")
    nombres.append(nombre)
    nota=int(input(f"Ingrese la nota de {nombres[x]}: "))
    notas.append(nota)

aux1=0
aux2=0

for k in range(5):
    for i in range(5-k):
        if notas[i]<notas[i+1]:
            aux1=notas[i]
            notas[i]=notas[i+1]
            notas[i+1]=aux1
            aux2=nombres[i]
            nombres[i]=nombres[i+1]
            nombres[i+1]=aux2


alumnosMayor=nombres[0]
notaMayor=notas[0]
alumnosMenor=nombres[5]
notaMenor=notas[5]

for n in range(6):
    if notaMayor==notas[n]:
        contadorMayor=contadorMayor+1
    if notaMenor==notas[n]:
        contadorMenor=contadorMenor+1

print(f"El alumno con la nota más alta es {alumnosMayor} con una nota de {notaMayor}")
print(f"La cantidad de Estudiantes con la misma nota mayor son {contadorMayor}")
print(f"El alumno con la nota más baja es {alumnosMenor} con una nota de {notaMenor}")
print(f"La cantidad de Estudiantes con la misma nota menor son {contadorMenor}")
