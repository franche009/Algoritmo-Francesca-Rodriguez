"""
3. Definir una lista y almacenar los nombres de 3 empleados.
Por otro lado definir otra lista y almacenar en cada elemento una sublista con los
números de días del mes que el empleado faltó.
Imprimir los nombres de empleados y los días que faltó.
Mostrar los empleados con la cantidad de inasistencias.
Finalmente mostrar el nombre o los nombres de empleados que faltan menos
días.
"""

nombres=["Pepe", "Piolin", "Anacleta"]
faltas=[[14, 29, 15], [1, 2, 3, 4, 18, 23], [25]]
menor=0
posMenor=0
for x in range(3):
    print(f"{nombres[x]} - Faltas: {faltas[x]}")
    
print("------")

for i in range(3):
    print(f"{nombres[i]} - Cantidad de faltas: {len(faltas[i])}")

j=0

while j<3:
    menor=len(faltas[0])
    if len(faltas[i])<menor:
        menor=len(faltas[i])
        posMenor=j
    j=j+1

print(f"El empleado/s que falta/n menos es/son: {nombres[posMenor]}")