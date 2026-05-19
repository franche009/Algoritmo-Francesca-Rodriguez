"""
3. Se registran los nombres de 5 atletas y sus tiempos (en segundos) en una
carrera de 100 metros. El programa debe cargar los datos en dos vectores
paralelos, calcular y mostrar el promedio de los tiempos, mostrar el nombre del
atleta con mejor y peor tiempo, y mostrar los nombres de quienes superaron el
promedio.
"""

nombres=[]
tiempos=[]
suma=0
promedio=0

for x in range(5):
    nombre=input(f"Ingrese el nombre del atleta n°{x}: ")
    nombres.append(nombre)
    tiempo=float(input(f"Ingrese el tiempo de {nombres[x]}: "))
    tiempos.append(tiempo)
    suma=suma+tiempo

promedio=suma/5
aux1=0
aux2=0

for k in range(4):
    for i in range(4-k):
        if tiempos[i]<tiempos[i+1]:
            aux1=tiempos[i]
            tiempos[i]=tiempos[i+1]
            tiempos[i+1]=aux1
            aux2=nombres[i]
            nombres[i]=nombres[i+1]
            nombres[i+1]=aux2

print(f"El promedio de tiempo entre todos los jugadores para la carrera es {promedio}")
print(f"El jugador con mejor tiempo es {nombres[4]}")
print(f"El jugador con el peor tiempo es {nombres[0]}")
print("Los jugadores que superaron el promedio son: ")
for l in range(5):
    if tiempos[l]<promedio:
        print(nombres[l])