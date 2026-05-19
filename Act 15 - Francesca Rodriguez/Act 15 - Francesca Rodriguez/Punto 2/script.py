"""
2. Realizar un programa que pida la carga de dos listas numéricas enteras
de 4 elementos cada una. Generar una tercera lista que surja de la suma
de los elementos de la misma posición de cada lista. Mostrar esta tercera
lista.
"""

lista1=[]
lista2=[]
lista3=[]
aux=0

for x in range(4):
    num1=int(input(f"Ingrese la posicion n°{x} de la lista n°1: "))
    lista1.append(num1)

for i in range(4):
    num2=int(input(f"Ingrese la posicion n°{i} de la lista n°2: "))
    lista2.append(num2)

for j in range(4):
    aux=lista1[j]+lista2[j]
    lista3.append(aux)

print(f"La tercera lista, con la suma es: {lista3}")