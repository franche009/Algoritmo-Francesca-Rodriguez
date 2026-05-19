"""
5. Crear y cargar en un lista los nombres de 5 países y en otra lista paralela
la cantidad de habitantes del mismo. Ordenar alfabéticamente e imprimir
los resultados. Por último ordenar con respecto a la cantidad de habitantes
(de mayor a menor) e imprimir nuevamente.
"""
paises=[]
habitantes=[]
aux=0

for x in range(5):
    pais=input(f"Ingrese el nombre del pais n°{x}: ")
    paises.append(pais)
    habitante=int(input(f"Ingrese la cantidad de habitantes de {paises[x]}: "))
    habitantes.append(habitante)

for i in range(4):
    for j in range(4):
        if paises[j]>paises[j+1]:
            aux=paises[j]
            paises[j]=paises[j+1]
            paises[j+1]=aux

print("La lista ordenada alfabeticamente es: ")
for n in range(5):
    print(f"{paises[n]} - {habitantes[n]}")


for i in range(4):
    for j in range(4):
        if habitantes[j]<habitantes[j+1]:
            aux=habitantes[j]
            habitantes[j]=habitantes[j+1]
            habitantes[j+1]=aux

print("La lista ordenada en función a la cantidad de habitantes (de mayor a menor) es: ")
for m in range(5):
    print(f"{paises[m]} - {habitantes[m]}")