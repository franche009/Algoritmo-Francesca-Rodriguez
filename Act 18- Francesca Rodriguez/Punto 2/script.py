"""2. Confeccionar una función que reciba tres enteros y los muestre ordenados
de menor a mayor. En otra función solicitar la carga de 3 enteros por
teclado y proceder a llamar a la primer función definida."""


def ordenados (num1, num2, num3):
    if num1<num2 and num1<num3 and num2< num3:
        print(num1, num2, num3)
    elif num1<num2 and num1<num3 and num2> num3:
        print(num1, num3, num2)
    elif num2<num1 and num2<num3 and num1<num3:
        print(num2, num1, num3)
    elif num2<num1 and num2<num3 and num1>num3:
        print(num2, num3, num1)
    elif num3<num1 and num3<num2 and num1<num2:
        print(num3,num1,num2)
    elif num3<num1 and num3<num2 and num1>num2:
        print(num3,num2,num1)
        
    

def solicitar():
    num1= int(input("Ingrese su primer numero: "))
    num2= int(input("Ingrese su segundo numero: "))
    num3= int(input("Ingrese su tercer numero: "))

    ordenados (num1, num2, num3)

solicitar()

