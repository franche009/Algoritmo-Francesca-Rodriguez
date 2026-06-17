"""
4-Se tiene que cargar los votos obtenidos por tres candidatos a una elección.
En una lista cargar en el primer componente el nombre del candidato y en la
segunda componente cargar una lista con componentes de tipo tupla con el
nombre de la provincia y la cantidad de votos obtenidos en dicha provincia.
Se deben cargar los datos por teclado.
1) Función para cargar todos los candidatos, sus nombres y las provincias con los
votos obtenidos.
2) Imprimir el nombre del candidato y la cantidad total de votos obtenidos en todas
las provincias."""

def cargarCandidatos():
    candidatos = []
    for numeroCandidato in range(3):
        nombreCandidato = input(f"Ingrese el nombre del candidato n{numeroCandidato +1}: ")
        provincias = []
        cantidadProvincias = int(input("¿Cuántas provincias desea cargar?: "))
        for numeroProvincia in range(cantidadProvincias):
            nombreProvincia = input(f"Ingrese el nombre de la provincia n{numeroProvincia +1}: ")
            votos = int(input("Ingrese la cantidad de votos: "))
            provincias.append((nombreProvincia, votos))
        candidatos.append([nombreCandidato, provincias])
    return candidatos

def totalVotos(candidatos):
    print("El total de votos por candidato:")
    for candidato in candidatos:
        nombreCandidato = candidato[0]
        provincias = candidato[1]
        total = 0
        for provincia in provincias:
            total = total + provincia[1]
        print(nombreCandidato, "obtuvo", total, "votos")

candidatos = cargarCandidatos()
totalVotos(candidatos)