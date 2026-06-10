"""4. Confeccionar una función que reciba una serie de edades y me retorne la
cantidad que son mayores o iguales a 18 (como mínimo se envía un entero
a la función)"""


def edades(le):
    con=0
    for x in range(len(le)):
        if le[x] >= 18:
            con=con+1
    return con

edad=[20,15,17,19,18,20]

print(f"hay {edades(edad)} numeros mayores o con 18")