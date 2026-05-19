"""
3. Solicitar por teclado la cantidad de empleados que tiene la empresa. Crear
y cargar una lista con todos los sueldos de dichos empleados. Imprimir la
lista de sueldos ordenamos de menor a mayor.
"""
cantEmpleados=0
sueldos=[]
aux=0

cantEmpleados=int(input("Ingrese la cantidad de empleados que tiene la empresa: "))
x=0
while x<cantEmpleados:
    sueldo=int(input(f"Ingrese el sueldo del empleado n°{x}: "))
    sueldos.append(sueldo)
    x=x+1

for i in range(cantEmpleados-1):
    for j in range(cantEmpleados-1):
        if sueldos[j]>sueldos[j+1]:
            aux=sueldos[j]
            sueldos[j]=sueldos[j+1]
            sueldos[j+1]=aux

print("Lista de sueldos ordenada:")
print(sueldos)