#5. Realizar un programa que lea los lados de n triángulos, e informar:

#a. De cada uno de ellos, qué tipo de triángulo es: equilátero (tres lados iguales), isósceles (dos lados iguales), o escaleno (ningún lado igual)
#b. Cantidad de triángulos de cada tipo.
equilatero=0
isoceles=0
escaleno=0
n=int(input("Cuantos triangulos va a ingresar:"))
x=1

while x<=n:
    ladoUno=int(input("Ingrese el valor del lado 1: "))
    ladoDos=int(input("Ingrese el valor del lado 2: "))
    ladoTres=int(input("Ingrese el valor del lado 3: "))
    if ladoUno==ladoDos and ladoUno==ladoTres:
        equilatero= equilatero+1
        print("Su tipo de triangulo es equilatero")
    else:
        if ladoUno==ladoDos or ladoDos==ladoTres or ladoUno==ladoTres:
            isoceles= isoceles+1
            print("Su tipo de triangulo es isoceles")
        else:
            print("Su tipo de triangulo es escaleno")
            escaleno= escaleno+1
    x=x+1
print("La cantidad de triangulos equilateros son: ")
print(equilatero)
print("La cantidad de de triangulos isoceles son: ")
print(isoceles)
print("La cantidad de triangulos escalenos son: ")
print(escaleno)