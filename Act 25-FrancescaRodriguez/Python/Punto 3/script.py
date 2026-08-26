"""
3-
Un equipo de Fórmula 1 registra los nombres de sus 4 pilotos junto con los tiempos (en
segundos) obtenidos en sus últimas 3 vueltas de clasificación.
 La estructura de datos debe ser una lista general. Cada elemento de la lista será
una sublista que contenga en el primer componente el nombre del piloto (cadena
de caracteres) y en el segundo componente una tupla con sus 3 tiempos
(flotantes).
 Sugerencia de estructura interna si se cargara por asignación:
pilotos = [ [&quot;Franco&quot;, (78.5, 77.2, 79.1)], [&quot;Lewis&quot;, (77.9, 78.1, 77.4)], ... ]
Desarrollar las siguientes funciones:
1. Cargar pilotos: Solicitar por teclado el nombre de cada uno de los 4 pilotos y sus
3 mejores tiempos para estructurar la lista y las tuplas correspondientes.
2. Calcular Promedios: Recorrer la estructura de datos, calcular el tiempo promedio
de cada piloto en sus 3 vueltas e imprimir su nombre junto a dicho promedio.
3. Mejor Vuelta: Recorrer la estructura para buscar y mostrar la vuelta más rápida de
toda la clasificación (el tiempo individual más bajo dentro de cualquier tupla),
detallando a qué piloto le pertenece.
"""

def cargar():
    lista = []
    for x in range(4):
        nombre = input("Ingrese el nombre del piloto: ")
        val1 = float(input("Ingrese el tiempo de la vuelta 1: "))
        val2 = float(input("Ingrese el tiempo de la vuelta 2: "))
        val3 = float(input("Ingrese el tiempo de la vuelta 3: "))
        tiempos = (val1, val2, val3)
        lista.append([nombre, tiempos])

    return lista


def promedios(pilotos):
    for nombre, tiempos in pilotos:
        promedio = (tiempos[0] + tiempos[1] + tiempos[2]) / 3
        print("Piloto:", nombre, "Promedio:", promedio)


def mejor(pilotos):
    mejor=pilotos[0][1][0]
    piloto_mejor=pilotos[0][0]

    for nombre, tiempos in pilotos:
        for tiempo in tiempos:
            if tiempo < mejor:
                mejor = tiempo
                piloto_mejor = nombre

    print("La mejor vuelta fue:", mejor, "segundos")
    print("Pertenece al piloto:", piloto_mejor)


pilotos = cargar()
promedios(pilotos)
mejor(pilotos)