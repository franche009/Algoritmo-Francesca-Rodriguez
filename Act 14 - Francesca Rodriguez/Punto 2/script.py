#2. Una empresa tiene dos turnos (mañana y tarde) en los que trabajan 8 empleados (4 por la mañana y 4 por la tarde) Confeccionar un programa que permita almacenar los sueldos de los empleados agrupados en dos listas. Imprimir las dos listas de sueldos.

sueldosMañana=[]
sueldosTarde=[]
x=0
xx=0

while x<4:
    sueldo=int(input(f"Ingrese el sueldo del empleado de la mañana n°{x}: "))
    sueldosMañana.append(sueldo)
    x=x+1

while xx<4:
    sueldoT=int(input(f"Ingrese el sueldo del empleado de la tarde n°{xx}: "))
    sueldosTarde.append(sueldoT)
    xx=xx+1

print("Lista de sueldos de los empleados de la mañana:")
print(sueldosMañana)
print("Lista de sueldos de los empleados de la tarde:")
print(sueldosTarde)