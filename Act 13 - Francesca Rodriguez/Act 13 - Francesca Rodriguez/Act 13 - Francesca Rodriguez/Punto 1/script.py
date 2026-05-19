#1. En una empresa trabajan n empleados cuyos sueldos oscilan entre $100 y $500, realizar un programa que lea los sueldos que cobra cada empleado e informe cuántos empleados cobran entre $100 y $300 y cuántos cobran más de $300. Además el programa deberá informar el importe que gasta la empresa en sueldos al personal.

n= int(input("Ingrese cuantos empleados trabajan: "))
sueldosEntre=0
sueldosMas=0
sueldoTotal=0
x=1

while x<=n:
    sueldo=int(input("Ingrese el sueldo del emepleado: "))
    if sueldo>=100 and sueldo<=300:
        sueldosEntre= sueldosEntre+1
    else:
        if sueldo>300:
            sueldosMas= sueldosMas+1
    sueldoTotal= sueldoTotal + sueldo
    x=x+1
print("La cantitad de empleados que cobran entre 100 y 300 son: ")
print(sueldosEntre)
print("La cantitad de empleados que cobran mas de 300 son: ")
print(sueldosMas)
print("El importe que gasta la empresa en sueldos es: ")
print(sueldoTotal)