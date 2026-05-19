#3. Realizar un programa que solicite la carga por teclado de dos números, si el primero es mayor al segundo informar su suma y diferencia, en caso contrario informar el producto y la división del primero respecto al segundo.

num1= int(input("Ingrese un numero: "))
num2= int(input("Ingrese otro numero: "))

if num1>num2:   
    suma = num1+num2
    print("La suma de los numeros es: ")
    print(suma)
    resta = num1-num2
    print("La resta de los numeros es: ")
    print(resta)
else:   
    producto = num2*num1
    print("El producto de los numeros es: ")
    print(producto)
    divison= num2/num1
    print("La division de los numeros es: ")
    print(divison)