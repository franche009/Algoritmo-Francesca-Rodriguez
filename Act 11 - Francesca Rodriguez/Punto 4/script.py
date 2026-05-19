#4. Se ingresa por teclado un número positivo de uno o dos dígitos (1..99) mostrar un mensaje indicando si el número tiene uno o dos dígitos. (Tener en cuenta que condición debe cumplirse para tener dos dígitos un número entero)

num = int(input("Ingrese un numero positivo de una o dos cifras: "))

if num>0 and num<10:  
    print(num)
    print("Su numero es de una cifra")

else:   
    if num>=10 and num<100:
        print(num)
        print("Su numero es de dos cifras")