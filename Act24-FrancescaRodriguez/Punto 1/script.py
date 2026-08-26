"""Una ciudad inteligente cuenta con sensores que miden las partículas contaminantes de
dióxido de carbono (CO2) en diferentes puntos geográficos.
 Crear un diccionario donde la Clave sea el nombre del barrio o estación de
monitoreo (ej: "San Telmo") y el Valor sea una lista de flotantes que represente
las últimas 3 lecturas de contaminación tomadas en el día.
Desarrollar las siguientes funciones:
1. Cargar sensores: Ingresar por teclado 3 estaciones de monitoreo y, para cada
una, solicitar las 3 lecturas consecutivas de CO2 (en partes por millón - ppm).
2. Reportar promedios: Calcular y mostrar el promedio de contaminación de cada
barrio.
3. Alerta ambiental: Mostrar en pantalla una alerta roja de &quot;Protocolo de
Emergencia&quot; únicamente para las estaciones cuyo promedio de contaminación
supere las 400 ppm.
"""

def cargar():
    lista={}
    codigo="s"
    numero=[]
    prom=0
  
    while codigo == "s":
            barrio=(input("ingrese el nombre de su barrio: "))
            for x in range (3):
                num=int(input(f"ingrese la lectura n° {x} de contaminacion de {barrio} en ppm: "))
                numero.append(num)
                lista[barrio]=numero
                prom= prom + num /3
            promedio.append(prom)
            prom=0


            codigo=input("desea agregar otro barrio? (s/n): ")
            numero=[]


    return lista


def ingreso(lista):
    print("TODOS LOS DATOS INGRESADOS: ")
    print(lista)
    print("PROMEDIOS DE CADA BARRIO: ")
    print(promedio)
    for x in range(len(lista)):
        if promedio[x] > 400:
            print(f"el barrio {x+1} tiene un promedio de mas de 400 CO2 ppm")
    

    return



promedio=[]
lista=cargar()
ingreso(lista)