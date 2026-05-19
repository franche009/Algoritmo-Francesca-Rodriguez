"""
2. Una empresa registra los nombres de sus 5 vendedores y el total de ventas
realizadas por cada uno en un mes. Cargar los nombres y ventas en dos
vectores paralelos, ordenar los datos de mayor a menor según las ventas,
imprimir la lista ordenada con nombre y monto de la venta, e informar quien fue
el que menos vendió de los 5 empleados.
"""

nombres=[]
ventas=[]

for x in range(5):
    nombre=input(f"Ingrese el nombre del vendedor n°{x}: ")
    nombres.append(nombre)
    venta=int(input(f"Ingrese la cantidad de ventas de {nombres[x]}: "))
    ventas.append(venta)

aux1=0
aux2=0

for k in range(4):
    for i in range(4-k):
        if ventas[i]<ventas[i+1]:
            aux1=ventas[i]
            ventas[i]=ventas[i+1]
            ventas[i+1]=aux1
            aux2=nombres[i]
            nombres[i]=nombres[i+1]
            nombres[i+1]=aux2

for n in range(5):
    print(f"{nombres[n]} - {ventas[n]}")

print(f"La persona que vendió menos fue {nombres[4]}")