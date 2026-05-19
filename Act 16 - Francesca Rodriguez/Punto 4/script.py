"""
4. Se realiza una evaluación a 6 docentes por parte de sus alumnos. Se registran
sus nombres y puntajes promedio obtenidos (de 1 a 10).
Cargar sus datos en vectores paralelos, mostrar docente con calificación más
alta y más baja, ordenar los vectores de mayor a menor de acuerdo con la
calificación y mostrar en pantalla la cantidad de docentes que aprobaron y
desaprobaron (tomando como base que se aprueba con una nota mayor o
igual a 6)
"""

nombres=[]
notas=[]
contadorMayor=0
contadorMenor=0
for x in range(6):
    nombre=input(f"Ingrese el nombre del docente n°{x}: ")
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

for l in range(6):
    if notas[l]>=6:
        contadorMayor=contadorMayor+1
    else:
        contadorMenor=contadorMenor+1

print(f"El docente con mayor calificacion es {nombres[0]}")
print(f"El docente con menor calificacion es {nombres[5]}")
print(f"La cantidad de docentes que aprobaron es {contadorMayor}")
print(f"La cantidad de docentes que desaprobaron es {contadorMenor}")