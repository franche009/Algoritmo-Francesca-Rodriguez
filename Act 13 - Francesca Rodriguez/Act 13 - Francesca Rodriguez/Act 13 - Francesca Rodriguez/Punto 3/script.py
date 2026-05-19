#3. Realizar un programa que permita cargar dos listas de 15 valores cada una. Informar con un mensaje cuál de las dos listas tiene un valor acumulado mayor (mensajes "Lista 1 mayor", "Lista 2 mayor", "Listas iguales") Tener en cuenta que puede haber dos o más estructuras repetitivas en un algoritmo.

sumaUno=0
sumaDos=0

for i in range(1,16):
    listaUno=int(input(f"Ingrese en la lista 1 en la posicion {i} un valor: "))
    sumaUno=sumaUno+listaUno


for i in range(1,16):
    listaDos=int(input(f"Ingrese en la lista 2 en la posicion {i} un valor: "))
    sumaDos=sumaDos+listaDos

if sumaUno>sumaDos:
    print("Lista 1 es mayor")
else:
    if sumaUno<sumaDos:
        print("Lista 2 es mayor")
    else:
        print("Las listas son iguales")