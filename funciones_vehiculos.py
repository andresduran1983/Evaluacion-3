lista_vehículos =[]

def grabar_vehiculos():
    vehiculos={}
    try:
        while True:
            patente=str(input("Ingrese el patente con dígito verificador: (Ejemplo: 1011-2): "))
            if patente[-2]=="-" and (len(patente)==5 or len(patente)==4): #Verificación patente correcto
                break
            else:
                print("ERROR: patente ingresado de manera incorrecta.")
        while True:
            Tipo=str(input("Ingrese el tipo: "))
            if len(Tipo)>0: #Verificación Tipo correcto
                break
            else:
                print("ERROR: Por favor ingrese un Tipo")
        while True:
            marca=str(input("Ingrese el marca: "))
            if len(marca)>0: #Verificación marca correcto
                break
            else:
                print("ERROR: Por favor ingrese marca")
        while True:
            precio=int(input("Ingerse precio: "))
            if precio>=5000000: #Verificación mayor de $5.000.000
                break
            else:
                print("ERROR: El precio debe ser mayor a (+$5.000.000)")
        while True:
             fecha_registro_vehículo=input("Ingrese la fecha de registro de Vehiculo (formato: DD/MM/AAAA ej: 04/09/2022): ")
             if fecha_registro_vehículo[2]=="/" and fecha_registro_vehículo[5]=="/" and len()==10: #Verificación fecha correcta
                break
             else:
                print("ERROR: Fecha ingresada de forma errónea.")
        #Asignación de variables a diccionario
        vehiculos['patente']=patente
        vehiculos['Tipo']=Tipo
        vehiculos['marca']=marca
        vehiculos['precio']=precio
        vehiculos['fecha_registro_vehiculo']=fecha_registro_vehículo
        lista_vehículos.append(vehiculos)
        input("\nVehiculo añadido con éxito, presione enter para continuar...")

    except (ValueError,TypeError):
        input("ERROR: Ingreso inválido, presione enter para volver al menú principal")

def buscar_vehiculos():
    try:
        while True:
            patente_busqueda=input("Ingrese la patente que desea consultar,con dígito verificador (Ejemplo: 1011-2)")
            if patente_busqueda[-2]=="-" and (len(patente_busqueda)==5 or len(patente_busqueda)==4): #Verificación patente correcta
                resultado_busqueda=False #Si no ha encontrado la patente
                for vehiculos in lista_vehículos:
                    if vehiculos['patente']==patente_busqueda:
                        print(f"***Búsqueda patente {patente_busqueda} exitosa, imprimiendo información: ")
                        print(f"tipo: {vehiculos['tipo']} {vehiculos['apellido']}")
                        print(f"marca: {vehiculos['marca']}")
                        print(f"Fecha_registro_vehiculo: {vehiculos['fecha_registro_vehiculo']}")
                        print("***\n")
                        resultado_busqueda=True #Si se ha encontrado la patente
                if not resultado_busqueda: #Si no se encontró la patente, imprimir aviso
                    input(f"\nPATENTE {patente_busqueda} No se encuentra en nuestros registros. Presione enter para continuar...")
                break
            else: 
                input("ERROR: La patente ingresada de manera incorrecta. Presione enter para continuar...") 
    except (ValueError,TypeError):
        input("ERROR: Ingreso inválido, presione enter para volver al menú principal")


def imprimir_certificados():
    try:
        import random
        valores=["$1.500","$3.500"]#Posibles opciones de valor
        if len(lista_vehículos)>0: #Verifica si hay lista de vehiculos
            for vehiculos in lista_vehículos:
                valor_certificado=valores[(random.randint(0,1))] #Asigna aleatoriamente un valor u otro
                print("-----------------------------------------------------------------------")
                print("\nAuto Seguro\n")
                print("\t\t CERTIFICADO DE VEHICULOS\n")
                print(f"Auto seguro, certifica que el {(vehiculos['patente'])}")
                print(f"tipo: {vehiculos['tipo']} marca {vehiculos['marca']} ")
                print(f"registra un contrato vigente desde {vehiculos['fecha_registro_vehiculo']}.")
                print(f"\nValor certificado: {valor_certificado}\n")     
                print(f"\t\t CERTIFICADO INTERNET N°{random.randint(1,999999)}\n")
                print("\n-----------------------------------------------------------------------\n")
                input("Impresión exitosa, presione enter para continuar...")
        else:
            input("\nNo hay Vehiculos para mostrar. Presione enter para continuar...")
    except (ValueError,TypeError):
        input("ERROR: Ingreso inválido, presione enter para volver al menú principal")


def salir():
    print("Saliendo del programa")
   

    
def menu():
    print("\n\n***  REGISTRO AUTO SEGURO  ***")
    print("1.- Grabar")
    print("2.- Buscar")
    print("3.- Imprimir certificados")
    print("4.- Salir")
    print("----------------------------------------")