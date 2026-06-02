"""1. Desarrollar un programa que solicite la carga de tres valores y muestre el
menor. Desde el bloque principal del programa llamar 2 veces a dicha
función (sin utilizar una estructura repetitiva)"""


def numero_menor(num1, num2, num3):
    if num1<num2 and num1<num3:
        menor = num1
    elif num2<num1 and num2<num3:
        menor = num2
    elif num3<num1 and num3<num2:
        menor = num3
    return menor

def solicitar():
    num1= int(input("Ingrese su primer numero: "))
    num2= int(input("Ingrese su segundo numero: "))
    num3= int(input("Ingrese su tercer numero: "))

    menor=numero_menor(num1, num2, num3)
    print(menor)

solicitar()


