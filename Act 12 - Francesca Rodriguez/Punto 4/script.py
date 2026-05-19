#4. Se realiza la carga de 10 valores enteros por teclado. Se desea conocer:
#a. La cantidad de valores ingresados negativos.
#b. La cantidad de valores ingresados positivos.
#c. La cantidad de múltiplos de 15.
#d. El valor acumulado de los números ingresados que son pares.
cantidadNegativo=0
cantidadPositiva=0
multiplos=0
pares=0
for i in range(10):
    num=int(input("Ingrese 10 valores:"))
    if num<0:
        cantidadNegativo= cantidadNegativo+1
    else:
        if num>0:
         cantidadPositiva = cantidadPositiva+1
    if num%15==0 and num>0:
        multiplos=multiplos+1
    if num%2==0:
        pares=pares+num

print("La cantidad de valores negativos es: ")
print(cantidadNegativo)
print("La cantidad de valores positivos es: ")
print(cantidadPositiva)
print("La cantidad de multiplos de 15 es: ")
print(multiplos)
print("La suma de los valores pares es: ")
print(pares)
