#!/usr/bin/python3
# Datos descargados del sitio: https://worldpopulationreview.com/world-cities

from tabulate import tabulate
import json
import csv
import sys


def buscar_ciudades(pais,archivo):

    ciudades = list()

    try:

        if '.csv' in archivo:

            with open(archivo,'r') as c:
                lector_csv = csv.reader(c, delimiter=',')
                ciudades.append(next(lector_csv))
                for linea in lector_csv:
                    if pais in linea[2]:
                        ciudades.append(linea)

        elif '.json' in archivo:

            with open(archivo,'r') as j:
                lector_json = json.load(j)
                ciudades.append(list(lector_json[0].keys()))
                for dict_pais in lector_json:
                    if pais in dict_pais["Country"]:
                        ciudades.append(list(dict_pais.values()))

        else:
            raise IndexError

    except (FileNotFoundError,IndexError):

        print(f'Error: Archivo {archivo} no encontrado o formato no soportado!')
        sys.exit(0)

    return ciudades


def imprimir_busqueda(ciudades):
    
    total_ciudades = len(ciudades) - 1
    print(f'Ciudades encontradas:', total_ciudades)

    if total_ciudades > 0:
        ciudades[0][0] = 'Rank'
        print(tabulate(ciudades,headers="firstrow",tablefmt="grid"))
        print('\n')

    return total_ciudades


def guardar_busqueda(ciudades,pais):

    formato = input('Escribe csv o json para guardar la salida en ese formato o cualquier otro valor para salir sin guardar: ')

    archivo_ciudades = pais + '.' + formato
    respuesta = f'Archivo guardado como {archivo_ciudades}'

    if formato == 'csv':

        with open(archivo_ciudades,'w') as f:
            escritor_csv = csv.writer(f, delimiter=',')
            for ciudad in ciudades:
                escritor_csv.writerow(ciudad)
            
    elif formato == 'json':

        lista_ciudades = list()
        llaves = ciudades.pop(0)
        for valores in ciudades:
            diccionario_ciudad = dict(zip(llaves,valores))
            lista_ciudades.append(diccionario_ciudad)

        with open(archivo_ciudades,'w') as f:
            json.dump(lista_ciudades, f, indent=4)
                            
    else:

        respuesta = 'Archivo NO guardado'

    print(respuesta)


if __name__ == '__main__':

    archivo = input('Archivo origen: ')
    pais = input('Pais a buscar: ')

    ciudades = buscar_ciudades(pais,archivo)
    total_ciudades = imprimir_busqueda(ciudades)

    if total_ciudades > 0:
        
        guardar_busqueda(ciudades,pais)
