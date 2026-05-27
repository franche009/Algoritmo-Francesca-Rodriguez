"""
4. Crear dos listas paralelas. En la primera ingresar los nombres de empleados y
en la segunda los sueldos de cada empleado.
Ingresar por teclado cuando inicia el programa la cantidad de empleados de la
empresa.
Borrar luego todos los empleados que tienen un sueldo mayor a 10000 (tanto el
sueldo como su nombre)
"""

nombres=[]
sueldos=[]
empleados=0

empleados=int(input("Ingrese la cantidad de empleados que va a nombrar: "))

for x in range(empleados):
    nombre=input(f"Ingrese el nombre del empleado n°{x}: ")
    nombres.append(nombre)
    sueldo=int(input(f"Ingrese el sueldo de {nombres[x]}: "))
    sueldos.append(sueldo)

i=0

while i<len(sueldos):
    if sueldos[i]>10000:
        nombres.pop(i)
        sueldos.pop(i)
    else:
          i=i+1
        

print(f"Empleados con sueldos menores a 10000: {nombres}")