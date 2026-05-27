"""
2. Se desea saber la temperatura media trimestral de cuatro países. Para ello se
tiene como dato las temperaturas medias mensuales de dichos países. Se debe
ingresar el nombre del país y seguidamente las tres temperaturas medias
mensuales.
Seleccionar las estructuras de datos adecuadas para el almacenamiento de los
datos en memoria.

● Cargar por teclado los nombres de los países y las temperaturas
medias mensuales.
● Imprimir los nombres de los países y las temperaturas medias
mensuales de las mismas.
● Calcular la temperatura media trimestral de cada país.
● Imprimir los nombres de los países y las temperaturas medias
trimestrales.
● Imprimir el nombre del país con la temperatura media trimestral
mayor."""

"""12 - 17.7 - 12.1 - 2.5"""

paises=[]
temperaturas=[]
temperaturasTri=[]
mayor=0
posMayor=0

for x in range (4):
    pais=input(f"Ingrese el nombre del país n°{x}: ")
    paises.append(pais)
    tempMensual1=float(input(f"Ingrese la temperatura mensual n°1 de {paises[x]}: "))
    tempMensual2=float(input(f"Ingrese la temperatura mensual n°2 de {paises[x]}: "))
    tempMensual3=float(input(f"Ingrese la temperatura mensual n°3 de {paises[x]}: "))
    temperaturas.append([tempMensual1, tempMensual2, tempMensual3])

for j in range(4):
    print(f"{paises[j]} - mes 1: {temperaturas[j][0]} - mes 2: {temperaturas[j][1]}  - mes 3: {temperaturas[j][2]}")


for i in range(4):
    total=temperaturas[i][0]+temperaturas[i][1]+temperaturas[i][2]
    total=total/3
    temperaturasTri.append(total)

print("--------")

for f in range(4):
    print(f"{paises[f]} - Temperatura trimestral: {temperaturasTri[f]}")
h=0

while h<4:
    mayor=temperaturasTri[0]
    if temperaturasTri[h]>mayor:
        mayor=temperaturasTri[h]
        posMayor=h
    h=h+1

print(f"El país con mayor temperatura trimestral es {paises[posMayor]}")