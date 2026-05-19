#4. Cargar por teclado y almacenar en una lista las alturas de 5 personas (valores float) Obtener el promedio de las mismas. Contar cuántas personas son más altas que el promedio y cuántas más bajas.

medidas=[]
suma=0
x=0
promedio=0
contadorAltos=0
contadorBajos=0

while x<5:
    valor=float(input(f"Ingrese la altura de la persona n°{x}: "))
    medidas.append(valor)
    suma=suma+valor
    x=x+1

promedio=suma/5

i=0
for i in range(5):
    if medidas[i]>promedio:
        contadorAltos=contadorAltos+1
    else:
        contadorBajos=contadorBajos+1

print(f"La cantidad de personas que son más altas que el promedio son {contadorAltos}")
print(f"La cantidad de personas que son más bajas que el promedio son {contadorBajos}")