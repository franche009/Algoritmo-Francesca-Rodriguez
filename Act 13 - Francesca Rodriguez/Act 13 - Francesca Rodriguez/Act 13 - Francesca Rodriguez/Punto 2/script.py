#2. En un banco se procesan datos de las cuentas corrientes de sus clientes. De cada cuenta corriente se conoce: número de cuenta y saldo actual. El ingreso de datos debe finalizar al ingresar un valor negativo en el número de cuenta. Se pide confeccionar un programa que lea los datos de las cuentas corrientes e informe:
#● a) De cada cuenta: número de cuenta y estado de la cuenta según su saldo, sabiendo que:
#○ Estado de la cuenta:
#○ "Deudor" si el saldo es < 0
#○ “Acreedor” si el saldo es &gt; 0.
#○ “Nulo” si el saldo es = 0.
#● b) La suma total de los saldos acreedores.

sumaAcreedores=0

numeroCuenta=int(input("Ingrese numero de cuenta (ingresar un valor negativo para finalizar): "))

while numeroCuenta>0:
    saldo= int(input("Ingrese el saldo de la cuenta: "))
    if saldo>0:
        print(f"Cuenta: {numeroCuenta} es acreedor")
        sumaAcreedores= sumaAcreedores + saldo
    else:
        if saldo<0:
            print(f"Cuenta: {numeroCuenta} es deudor")
        else:
            print(f"Cueta: {numeroCuenta} es nulo")
    numeroCuenta=int(input("Ingrese numero de cuenta (ingresar un valor negativo para finalizar): "))

print(f"Suma total de saldos acreedores: {sumaAcreedores}")
