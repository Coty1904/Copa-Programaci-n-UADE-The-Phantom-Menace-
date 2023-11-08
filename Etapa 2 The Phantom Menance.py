"""
---------------------------------------------------------------------------------------------------------------------
                                                    ETAPA-02
                                            COPA UADE DE ALGORITMIA
                                                   25-05-2023

Facundo Jonas (1175315)
Carracedo Constantino (1170700)
---------------------------------------------------------------------------------------------------------------------
"""

import csv
import random
import os

def verificarSiExiste(datosElecciones, dato, i):
    '''Devuelve False si el dato es duplicado, devuelve True si no es duplicado'''
    for elemento in datosElecciones:
        if elemento[i] == dato:
            return False
        
    return True

def ingresoDeDatos(datosElecciones):
    '''Ingreso de datos para crear archivos'''
    #Titulo e Instrucción de la función.
    print(f"{'':_^100} \n" )
    print("INGRESO DE PARTIDOS POLÍTICOS".center(100))
    print(f"{'':_^100} \n")
    print("Ingrese FIN en nombre del partido para cargar datos. \n".center(100))
    
    partidoPolitico = 'BLANCO'
    abreviatura = 'BLANCO'
    numeroDeLista = 0
    datosElecciones.append([partidoPolitico, abreviatura, numeroDeLista]) #Cargar una lista en forma de matriz     

    while True:
        while True:
            partidoPolitico = 'BLANCO'

            partidoPolitico = input("Ingrese un partido político: ").upper() 
            if verificarSiExiste(datosElecciones, partidoPolitico, 0) == True:
                break
            else:
                print("Nombre del partido político duplicado.")
        
        if partidoPolitico == "FIN" or partidoPolitico == " ":
            break
        

        while True:
            abreviatura = input("Ingrese la abreviatura del partido político: ").upper()   #Ingresar abreviatura del partido politico
            if abreviatura.isalnum() == False:  #Verificamos si la abreviatura no es alfanumérica
                while True:
                    print("ERROR. Únicamente se admiten valores alfanuméricos. \n")
                    abreviatura = input("Ingrese la abreviatura del partido político: ").upper()  #Volvemos a pedir una abreviatura valida y alfanumerica
                    if abreviatura.isalnum() == True:
                        break
            if verificarSiExiste(datosElecciones, abreviatura, 1) == True:
                break
            else:
                print("Abreviatura del partido político duplicado, ingrese una nueva abreviatura válida. \n")
        
        while True:
            try:
                numeroDeLista = int(input("Ingrese el número de lista del partido: "))
                while numeroDeLista == 0:
                    print("0 no es un valor válido. \n")
                    numeroDeLista = int(input("Ingrese el número de lista del partido: "))

                if verificarSiExiste(datosElecciones, numeroDeLista, 2) == True:
                    break
                print("El número de lista ingresado ya es utilizado.")

            except ValueError:
                print("No ha ingresado un valor númerico.")
            
        datosElecciones.append([partidoPolitico, abreviatura, numeroDeLista]) #Cargar una lista en forma de matriz     
        
    try:
        archivo = open("partidos.csv", "w")
        for dato in datosElecciones:
            linea = dato[0] + ";" + dato[1] + ";" + str(dato[2]) + "\n"
            archivo.write(linea)
            print("¡Carga éxitosa de datos!")

        archivo.close()
        
        archivo = open("partidos.csv", "r")
        lineas = archivo.readlines()
        

    except IOError:
        print("No se pudo crear el archivo.")
    except OSError:
        print("No se pudo cerrar el archivo.")
    
    return datosElecciones

def imprimirPartidos(datosElecciones):
    print(f"{'':_^100}\n")
    print("PARTIDOS POLÍTICOS".center(100))
    print(f"{'':_^100}")
    print(f"{'NOMBRE'}{'ABREVIATURA'.center(90)}{'LISTA'}")
    for dato in datosElecciones:
        nombre = dato[0]
        abreviatura = dato[1]
        lista = str(dato[2])
        if len(abreviatura) == 1:
            print(f"{nombre:<49}{abreviatura}{lista:>49}")
        else:
            print(f"{nombre:<48}{abreviatura}{lista:>48}")

def ingresoDeProvincia( provincias, listaProvincias):
    '''Ingreso de datos para crear archivos'''
    #Titulo e Instrucción de la función.
    print(f"{'':_^100} \n" )
    print("INGRESO DE REGIONES GEOGRÁFICAS".center(100))
    print(f"{'':_^100} \n")
    print("Ingrese FIN en nombre de la región geográfica para cargar datos. \n".center(100))

    provincias = []
    while True:
        nombreProvincias = input("Ingrese el nombre de la región geográfica: ").upper()
        if nombreProvincias == "FIN":
            break
        if nombreProvincias not in provincias and nombreProvincias in listaProvincias:
            provincias.append(nombreProvincias)
        elif nombreProvincias not in listaProvincias:
            print("La provincia ingresada no es una provincia válida.")
        elif nombreProvincias in provincias:
            print("La provincia ya fue ingresada.")
    
    #Guardar los datos en un archivo CSV
    Lista_Provincias = "provincias.csv"
    try:
        with open(Lista_Provincias, "w", newline="") as archivo:
            escribir_csv = csv.writer(archivo, delimiter=";")
            for i, nombreProvincias in enumerate(provincias, start=1):
                escribir_csv.writerow([nombreProvincias, i])

        if nombreProvincias in listaProvincias:
            print("Valor(es) cargado(s).")
        else:
            print("Nombre de región geográfica inválida.")

    except IOError:
        print("No se pudo crear el archivo")
    return provincias

def imprimirProvincias():
    print(f"{'':_^100}\n")
    print("REGIONES GEOGRÁFICAS".center(100))
    print(f"{'':_^100}")
    print(f"{'NOMBRE':<50}{'CÓDIGO':>50}")

    Lista_Provincias = "provincias.csv"
    try:
        with open(Lista_Provincias, "r") as archivo:
            leer_csv = csv.reader(archivo, delimiter=";")
            for fila in leer_csv:
                nombre = fila[0]
                codigo = fila[1]
                print(f"{nombre:<48}{codigo:>48}")

    except IOError:
        print("No se pudo leer el archivo")

def agregarProvincias(listaProvincias):
    '''Agregar Provincias permitidas en caso de ser necesario.'''

    print(f"{'':_^100} \n" )
    print("AGREGAR REGIONES GEOGRÁFICAS".center(100))
    print(f"{'':_^100} \n")
    print("Ingrese FIN en nombre de la región geográfica para cargar datos. \n".center(100))

    while True:
        agregar = input("Ingrese la región geográfica que quiera agregar: ").upper()
        if agregar == "FIN":
            break
        if agregar not in listaProvincias:
            listaProvincias.append(agregar)
            print("\nLista de Regiones Geográficas actualizada.")

        else:
            print("La región ya fue establecida.")

def quitarProvinciaArchivo(provincia, archivo_provincias):
    '''Quita una provincia del archivo "provincias.csv"'''
    filas = []
    with open(archivo_provincias, 'r') as archivo_csv:
        lector_csv = csv.reader(archivo_csv)
        for fila in lector_csv:
            if fila[0] != provincia:  # Verifica si el nombre de la provincia no coincide
                filas.append(fila)

    with open(archivo_provincias, 'w', newline='') as archivo_csv:
        escritor_csv = csv.writer(archivo_csv)
        escritor_csv.writerows(filas)

def quitarProvincias(listaProvincias, provincias, archivo_provincias):
    '''Quitar Provincias permitidas en caso de ser necesario.'''
    
    print(f"{'':_^100} \n" )
    print("RETIRAR REGIONES GEOGRÁFICAS".center(100))
    print(f"{'':_^100} \n")
    print("Ingrese FIN en nombre de la región geográfica para cargar datos. \n".center(100))

    while True:
        quitar = input("Ingrese la región geográfica que desee quitar: ").upper()
        if quitar == "FIN":
            break
        if quitar in listaProvincias:
            listaProvincias.remove(quitar)
            print("\nLista de Regiones Geográficas actualizada.")
        else:
            print("La región ya fue eliminada.")
        if quitar in provincias:
            provincias.remove(quitar)
            print("\nLista de Regiones Geográficas actualizada.")
        else:
            print("La región ya fue eliminada.")
        
        quitarProvinciaArchivo(quitar, archivo_provincias)

def dni_aleatorio(dnis_generados):
    '''Devuelve un número de DNI de 8 dígitos que no esté en la lista de DNIs generados'''
    while True:
        dni = random.randint(10000000, 99999999)
        if dni not in dnis_generados:
            dnis_generados.append(dni)
            return dni

def cantidad_provincias(nombre_archivo):
    '''Devuelve la cantidad de provincias'''
    with open(nombre_archivo, 'r') as archivo:
        lector_csv = csv.reader(archivo)
        # Funcion len() para contar la cantidad de filas
        cantidad_filas = len(list(lector_csv))
        
        return cantidad_filas

def leer_abreviatura_partidos(nombre_archivo):
    '''Lee las abreviaturas de los partidos'''
    valor_numerico = {}
    contador = 1
    with open(nombre_archivo, 'r') as archivo:
        lector_csv = csv.reader(archivo, delimiter = ";")
        next(lector_csv)

        for fila in lector_csv:
            elemento = fila[1]

            if elemento not in valor_numerico:
                valor_numerico[elemento] = contador
                contador += 1

    return valor_numerico

def abreviatura_partidos(nombre_archivo):
    '''Devuelve una lista de las abreviaturas de los partidos políticos'''
    abreviaturas = []
    with open(nombre_archivo, 'r') as archivo:
        lector_csv = csv.reader(archivo, delimiter = ";")
        for fila in lector_csv:
            if len(fila) >= 2:
                abreviaturas.append(fila[1])

    return abreviaturas
    
def nombre_provincias(archivo_provincias):
    '''Devuelve una lista de nombres de la provincia'''
    nombres = []
    with open(archivo_provincias, "r") as archivo:
        lector_csv = csv.reader(archivo, delimiter = ";")
        for fila in lector_csv:
            nombres.append(fila[0])
        return nombres
    
def seleccion_partido(abreviatura):
    '''Devuelve una abreviatura de partido al azar'''
    aleatoreo = random.choice(abreviatura)
    return aleatoreo


def iniciar_programa(archivo):
    with open(archivo, 'w') as file:
        file.write('')  

def bucle_global(): 
    '''Lista que comprueba los DNI Duplicados'''
    dni_generado = []
    registros = []
    guardado_temporal = []
    '''Carga de archivos'''
    archivo_provincias = 'provincias.csv'
    archivo_partidos = 'partidos.csv'
    archivo_registros = 'registros.csv'
    '''Carga de funciones '''

    partidos = abreviatura_partidos(archivo_partidos) 
    provincias = cantidad_provincias(archivo_provincias)
    nombreProvincias = nombre_provincias(archivo_provincias)
    nombre = 0
    provincia = 1
    habitantes = 0
    elemento = 0
    '''Borrar lista para que no se agregen datos de una carga anterior'''
    iniciar_programa(archivo_registros)
    '''Inicio de bucle hasta que no haya más provincias'''
    if os.path.getsize(archivo_partidos) > 0 and os.path.getsize(archivo_provincias) > 0 :
        print("Tenga en cuenta que debe completar la información de partidos políticos y regiones geográficas para continuar")
        while provincia != provincias + 1:
            try:
                '''Ingreso de población de una provincia.'''
                poblacion = int(input(f"Ingrese el número de habitantes con la capacidad de votar en la provincia de {nombreProvincias[nombre]}: "))
                guardado_temporal.append(nombreProvincias[nombre])
                guardado_temporal.append(poblacion)
                if poblacion <=0:
                    while poblacion <=0:
                        poblacion = int(input(f"Ingrese el número de habitantes con la capacidad de votar en la provincia de {nombreProvincias[nombre]}: "))
                        habitantes = 0
                '''Inicio de bucle hasta que no haya mas población que contar en la provincia'''
                while poblacion != 0:
                    cargo = 1
                    habitantes += 1
                    dni = dni_aleatorio(dni_generado)
                    '''Inicio de bucle de los 4 cargos que se votan'''
                    while cargo != 5:
                        abreviatura = seleccion_partido(partidos)
                        registros.append([dni, provincia, cargo, abreviatura])
                        '''Cargar datos directamente en un archivo .csv'''
                        with open('registros.csv', 'a', newline='') as archivo:
                            escritor_csv = csv.writer(archivo, delimiter=';')
                            escritor_csv.writerow([dni, provincia, cargo, abreviatura])
                        cargo += 1
                    poblacion -= 1
                nombre += 1
                provincia +=1
            except ValueError:
                print("No se ingreso un valor numérico") 
        for i in range(0, len(guardado_temporal), 2):
            #Se realiza un bucle para traer la informacion de la lista creada anteriomente 
            elemento_actual = guardado_temporal[i]
            elemento_siguiente = guardado_temporal[i+1]
            print(f"La provincia {elemento_actual} tiene {elemento_siguiente} votos realizados")
        return registros
    else :
        print("No se poseen los datos nesesarios para continuar ")
    main()        
    bucle_global()
#Final del nuevo codigo 

def main():
    archivo_provincias = 'provincias.csv'
    lista =  ["BUENOS AIRES", "CIUDAD AUTÓNOMA DE BUENOS AIRES", "CATAMARCA", "SANTA FE", "CHACO", "CHUBUT", "CÓRDOBA", "CORRIENTES", "ENTRE RÍOS", "FORMOSA", "JUJUY", "LA PAMPA", "LA RIOJA", "MENDOZA", "MISIONES", "NEUQUÉN", "RÍO NEGRO", "SALTA", "SAN JUAN", "SAN LUIS", "SANTA CRUZ", "SANTIAGO DEL ESTERO", "TIERRA DEL FUEGO, ANTÁRTIDA E ISLAS ATLANTICO SUR", "TUCUMÁN"]
    datosElecciones = []
    provincias = []
    while True:
        while True:
            print()
            print(f"{'':_^100}\n")
            print("MENÚ DEL SISTEMA".center(100))
            print(f"{'':_^100}\n")
            print(f"{'1 - Cargar datos de partidos políticos':>47}")
            print(f"{'2 - Cargar datos de regiones geográficas':>49}")
            print(f"{'3 - Imprimir listados de partidos políticos y regiones geográficas':>75}")
            print(f"{'4 - Ingresar nuevas provincias':>39}")
            print(f"{'5 - Eliminar provincias existentes':>43}")
            print(f"{'6 - Simulacion de votacion':>35}")
            print(f"{'0 - Salir del programa':>31}")
            print(f"{'':_^100} \n")

            while True:
                try:
                    opcion = int(input("Ingrese una opción: "))
                    break
                except ValueError:
                    print("Ingresar un valor válido. \n")
                    continue
            if opcion in range(0, 7):
                break
            else:
                print()
                print(f"{'Ingrese un valor válido.'}".center(100))

        
        if opcion == 0:
            exit()
                 
        elif opcion == 1:
            ingresoDeDatos(datosElecciones)
        
        elif opcion == 2:
            ingresoDeProvincia(provincias, lista)

        elif opcion == 3:
            imprimirPartidos(datosElecciones)
            print("\n")
            imprimirProvincias()

        elif opcion == 4:
            agregarProvincias(lista)

        elif opcion == 5:
            quitarProvincias(lista, provincias, archivo_provincias)

        elif opcion == 6:
            bucle_global()
        print()
        input("Presione ENTER para continuar.")
        
main()


