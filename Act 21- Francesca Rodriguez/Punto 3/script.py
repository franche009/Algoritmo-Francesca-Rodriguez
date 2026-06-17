"""
3-Almacenar en una lista 5 empleados, cada elemento de la lista es una sub lista
con el nombre del empleado junto a sus últimos tres sueldos (estos tres valores en
una tupla)
El programa debe tener las siguientes funciones:
1)Carga de los nombres de empleados y sus últimos tres sueldos.
2)Imprimir el monto total cobrado por cada empleado.
3)Imprimir los nombres de empleados que tuvieron un ingreso trimestral mayor a
10000 en los últimos tres meses.
Tener en cuenta que la estructura de datos si se carga por asignación debería ser
similar a:
empleados = [['juan',(2000,3000,4233)] , ['ana',(3444,1000,5333)] , etc. ]"""

def cargarEmpleados():
    empleados = []
    for numeroEmpleado in range(5):
        nombre = input(f"Ingrese el nombre del empleado n{numeroEmpleado +1}: ")
        sueldo1 = int(input("Ingrese sueldo del primer mes: "))
        sueldo2 = int(input("Ingrese sueldo del segundo mes: "))
        sueldo3 = int(input("Ingrese sueldo del tercer mes: "))
        empleados.append([nombre, (sueldo1, sueldo2, sueldo3)])
    return empleados

def totalCobrado(empleados):
    print("El total de cobrado por cada empleado:")
    for empleado in empleados:
        nombre = empleado[0]
        total = sum(empleado[1])
        print(nombre, "cobró", total)


def mayores10000(empleados):
    print("Los empleados con ingreso trimestral mayor a 10000 son:")
    for empleado in empleados:
        nombre = empleado[0]
        total = sum(empleado[1])
        if total > 10000:
            print(nombre)

empleados = cargarEmpleados()
totalCobrado(empleados)
mayores10000(empleados)