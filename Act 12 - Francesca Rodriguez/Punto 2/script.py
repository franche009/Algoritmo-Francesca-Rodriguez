#2. Se ingresan un conjunto de n alturas de personas por teclado. Mostrar la altura promedio de las personas.

suma=0
per=int(input("Ingrese cuantas alturas de personas pondra: "))
x=1

while x<=per:
    valor=int(input("Ingrese la altura de la persona: "))
    suma=suma+valor
    x=x+1

promedio=suma/per
print("La altura promedio de las personas es: ")
print(promedio)