#5. Se ingresa por teclado un valor entero, mostrar una leyenda que indique si el número es positivo, negativo o nulo (es decir cero)

num=int(input("Ingrese un numero: "))

if num<0:   
    print("Su numero es negativo")

else:   
    if num == 0:   
        print("Su numero es nulo")
    else: 
        print("Su numero es positivo")