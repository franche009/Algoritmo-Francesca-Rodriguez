"""
2-Confeccionar un programa con las siguientes funciones:
1)Cargar el nombre de un empleado y su sueldo. Retornar una tupla con dichos
valores
2)Una función que reciba como parámetro dos tuplas con los nombres y sueldos
de empleados y muestre el nombre del empleado con sueldo mayor.
En el bloque principal del programa llamar dos veces a la función de carga y
seguidamente llamar a la función que muestra el nombre de empleado con sueldo
mayor.
# bloque principal
empleado1=cargar_empleado()
empleado2=cargar_empleado()
mayor_sueldo(empleado1,empleado2)def cargar_empleado():
    nombre = input("Ingrese el nombre del empleado: ")
    sueldo = int(input(f"Ingrese el sueldo de {nombre}: "))
    return (nombre, sueldo)

def mayor_sueldo(emp1, emp2):
    if emp1[1] > emp2[1]:
        print("Empleado con mayor sueldo:", emp1[0])
    elif emp2[1] > emp1[1]:
        print("Empleado con mayor sueldo:", emp2[0])

empleado1 = cargar_empleado()
empleado2 = cargar_empleado()
mayor_sueldo(empleado1, empleado2)"""

def cargar_empleados():

    empleados = []

    for x in range(5):

        nombre = input("Ingrese el nombre del empleado: ")

        sueldo1 = float(input("Ingrese sueldo del primer mes: "))
        sueldo2 = float(input("Ingrese sueldo del segundo mes: "))
        sueldo3 = float(input("Ingrese sueldo del tercer mes: "))

        empleados.append([nombre, (sueldo1, sueldo2, sueldo3)])

    return empleados


# Función para imprimir el total cobrado por cada empleado
def total_cobrado(empleados):

    print("\nTotal cobrado por cada empleado:")

    for empleado in empleados:

        nombre = empleado[0]
        total = sum(empleado[1])

        print(nombre, "cobró", total)


# Función para mostrar empleados con ingreso trimestral mayor a 10000
def mayores_a_10000(empleados):

    print("\nEmpleados con ingreso trimestral mayor a 10000:")

    for empleado in empleados:

        nombre = empleado[0]
        total = sum(empleado[1])

        if total > 10000:
            print(nombre)


# Bloque principal
empleados = cargar_empleados()

total_cobrado(empleados)

mayores_a_10000(empleados)