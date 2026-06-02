"""
3. Confeccionar una funciÃ³n que calcule la superficie de un rectÃ¡ngulo y la
retorne, la funciÃ³n recibe como parÃ¡metros los valores de dos de sus lados:
def retornar_superficie(lado1,lado2):
En el bloque principal del programa cargar los lados de dos rectÃ¡ngulos y
luego mostrar cuÃ¡l de los dos tiene una superficie mayor.
"""

def calculo():
    base=int(input("ingrese la base del rectangulo: "))
    altura=int(input("ingrese la altura del rectangulo: "))
    resultado = base * altura
    return resultado

def respuesta():

    resultado= calculo()
    print(f"la superficie del rectangulo es de {resultado}")


respuesta()