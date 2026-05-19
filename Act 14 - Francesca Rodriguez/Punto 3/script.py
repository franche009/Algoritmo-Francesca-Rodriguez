#3. Cargar una lista con 5 elementos enteros. Imprimir el mayor y un mensaje si se repite dentro de la lista (es decir si dicho valor se encuentra en 2 o más posiciones en la lista) 

lista=[]

#1 2 3 4 5
i=0
contador=0
while i<5:
    valor=(int(input(f"Ingrese el valor n°{i}: ")))
    lista.append(valor)
    i=i+1

mayor=lista[0]
x=0
while x<5:
    if lista[x]>mayor:
        mayor=lista[x]
    x=x+1

for f in range (5):
    if mayor==lista[f]:
        contador=contador+1

print(f"El número mayor es {mayor}")
if contador>=2:
    print(f"Este número se encuentra un total de {contador} veces en la lista")