"""
3. Confeccionar un programa que permita:
1) Cargar una lista de 10 elementos enteros.
2) Generar dos listas a partir de la primera. En una guardar los valores
positivos y en otra los negativos.
3) Imprimir las dos listas generadas.
"""

def programa (lista1, lista2, lista3):
    for x in range (10):
        valor1=int(input("ingrese un numero entero: "))
        lista1.append(valor1)

    for x in range (10):
        if lista1[x] > 0:
            lista2.append(list[x])

        elif lista1[x] < 0:
            lista3.append(list[x])

    print(f"lista original: {lista1}")
    print(f"lista de numeros positivos: {lista2}")
    print(f"lista de numeros negativos: {lista3}")


numeros=[]
listaP=[]
listaN=[]
programa(numeros, listaP, listaN)

