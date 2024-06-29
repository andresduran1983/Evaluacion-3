import random
from funciones_vehiculos import grabar_vehiculos,buscar_vehiculos,imprimir_certificados,salir,menu
lista_vehículos=[]

def main():
    while True:
        menu()
        op=int(input("Ingrese su opción: [1/2/3/4]: "))
        if op==1:
            grabar_vehiculos()
        elif op==2:
            buscar_vehiculos()
        elif op==3:
            imprimir_certificados()
        elif op==4:
            salir()
            break
        else:
            input("Por favor ingrese una opción válida. Presione enter para continuar...")

main()