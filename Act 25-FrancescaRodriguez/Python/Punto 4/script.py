"""
4-
Un comercio de tecnología necesita administrar el stock de sus 5 componentes clave de
hardware.
 Crear una lista donde cada elemento sea una tupla de tres elementos que
represente: (nombre_articulo, precio, stock).
Desarrollar las siguientes funciones:
1. Cargar inventario: Ingresar por teclado los datos de los 5 componentes para
armar las tuplas correspondientes.
2. Imprimir listado: Mostrar por pantalla los nombres, precios y stock de todos los
artículos desempaquetando la tupla de manera directa en el bucle for.
3. Valor del Inventario: Calcular e informar el valor total de la mercadería en el local
(sumando el resultado de precio * stock de cada uno de los componentes).
4. Alerta de Reposición: Imprimir el nombre de todos aquellos artículos cuyo stock
sea menor o igual a 10 unidades para emitir un aviso de compra urgente.
"""

def cargar():
    lista = []
    for x in range(5):
        nombre = input("Ingrese el nombre del artículo: ")
        precio = float(input("Ingrese el precio: "))
        stock = int(input("Ingrese el stock: "))
        articulo = (nombre, precio, stock)
        lista.append(articulo)

    return lista


def imprimir(inventario):
    print("-- INVENTARIO --")
    for nombre, precio, stock in inventario:
        print("Artículo:", nombre)
        print("Precio:", precio)
        print("Stock:", stock)


def valor(inventario):
    total = 0
    for nombre, precio, stock in inventario:
        total = total + precio * stock
    print("El valor total del inventario es:", total)


def alerta(inventario):
    for nombre, precio, stock in inventario:
        if stock<=10:
            print("Es necesario reponer:", nombre)


inventario = cargar()
imprimir(inventario)
valor(inventario)
alerta(inventario)