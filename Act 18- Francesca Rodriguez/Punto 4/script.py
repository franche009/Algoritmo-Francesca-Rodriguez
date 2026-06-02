"""4. Plantear una función que reciba un string en mayúsculas o minúsculas y
retorne la cantidad de letras 'a' o 'A'."""


def cantidad(p):
    
    cantM=0
    cantm=0
    
    
    cantM= p.count("A")

    
    cantm= p.count("a")

    print(f"cantidad de letras 'A': {cantM}")
    print(f"cantidad de letras 'a': {cantm}")

def texto():
    p=str(input("Ingrese un texto: "))

    cantidad(p)
    

texto()