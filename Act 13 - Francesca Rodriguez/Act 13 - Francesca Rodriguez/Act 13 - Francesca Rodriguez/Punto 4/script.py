#4. Escribir un programa que pida ingresar coordenadas (x,y) que representan puntos en el plano. Informar cuántos puntos se han ingresado en el primer, segundo, tercer y cuarto cuadrante. Al comenzar el programa se pide que se ingrese la cantidad de puntos a procesar.

primer=0
segundo=0
tercer=0
cuarto=0
i=1
n=int(input("Ingrese la cantidad de puntos a procesar: "))

while i<=n:
    x=int(input("Ingrese el valor de la coordenada x: "))
    y=int(input("Ingrese el valor de la coordenada y: "))
    if x>0 and y>0:
        primer=primer+1
    else:
        if x<0 and y>0:
            segundo=segundo+1
        else:
            if x<0 and y<0:
                tercer= tercer +1
            else: 
                if x>0 and y<0:
                    cuarto= cuarto + 1
    i=i+1
print(f"se han ingresado {primer} coordenadas en el primer cuadrante")
print(f"se han ingresado {segundo} coordenadas en el segundo cuadrante")
print(f"se han ingresado {tercer} coordenadas en el tercer cuadrante")
print(f"se han ingresado {cuarto} coordenadas en el cuarto cuadrante")

