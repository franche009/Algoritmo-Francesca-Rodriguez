"""
4. Cargar una lista con 5 elementos enteros. Ordenar de menor a mayor y
mostrarla por pantalla, luego ordenar de mayor a menor e imprimir
nuevamente.
"""

lista=[]
aux=0

for x in range(5):
    num=int(input(f"Ingrese la posición n°{x} de la lista: "))
    lista.append(num)

for i in range(4):
    for j in range(4):
        if lista[j]>lista[j+1]:
            aux=lista[j]
            lista[j]=lista[j+1]
            lista[j+1]=aux

print(f"La lista ordenada de menor a mayor es: {lista}")

for i in range(4):
    for j in range(4):
        if lista[j]<lista[j+1]:
            aux=lista[j]
            lista[j]=lista[j+1]
            lista[j+1]=aux

print(f"La lista ordenada de mayor a menor es: {lista}")