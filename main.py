#!/usr/bin/python3
# Repositorio en GitHub: https://github.com/rulerdo/buscador_ciudades_dev
# Clonar repo: git clone git@github.com:rulerdo/buscador_ciudades_dev.git
# Datos descargados del sitio: https://worldpopulationreview.com/world-cities
# Repositorio script terminado: https://github.com/rulerdo/buscador_ciudades

import csv, json, sys
from tabulate import tabulate

def buscar_ciudades(pais,archivo):

    ciudades = list()

    try:

        if 'csv' in archivo:

            with open(archivo,'r') as c:

                lector_csv = csv.reader(c,delimiter=',')
                ciudades.append(next(lector_csv))
                for linea in lector_csv:
                    if pais in linea[2]:
                        ciudades.append(linea)


        elif 'json' in archivo:

            with open(archivo,'r') as j:

                lector_json = json.load(j)
                ciudades.append(list(lector_json[0].keys()))
                for dict_ciudad in lector_json:
                    if pais in dict_ciudad['Country']:
                        ciudades.append(list(dict_ciudad.values()))

        else:
            raise IndexError

    except (IndexError,FileNotFoundError):

        print(f'Archivo {archivo} no encontrado o en formato no soportado')
        sys.exit(0)

    return ciudades


def imprimir_busqueda(ciudades):

    ciudades[0][0] = 'Rank'

    total_ciudades = len(ciudades) - 1
    print('Ciudades encontradas:',total_ciudades)

    if total_ciudades > 0:
        print(tabulate(ciudades,headers='firstrow',tablefmt='grid'))

    return total_ciudades


def guardar_busqueda(pais,ciudades):

    formato = input('Escribe csv o json para guardar en ese formato, o cualquier otra cosa para salir: ')
    archivo_pais = pais + '.' + formato
    respuesta = f'Archivo guardado como: {archivo_pais}'

    if formato == 'csv':

        with open(archivo_pais,'w') as f:

            escritor_csv = csv.writer(f,delimiter=',')
            for ciudad in ciudades:
                escritor_csv.writerow(ciudad)


    elif formato == 'json':

        lista_ciudades = list()
        llaves = ciudades.pop(0)

        for valores in ciudades:
            dict_ciudad = dict(zip(llaves,valores))
            lista_ciudades.append(dict_ciudad)

        with open(archivo_pais,'w') as f:

            json.dump(lista_ciudades,f,indent=4)

    else:
        respuesta = 'Archivo NO guardado... adios!'

    print(respuesta)


if __name__ == '__main__':

    archivo = input('Archivo origen: ')
    pais = input('Pais a buscar: ')
    ciudades = buscar_ciudades(pais,archivo)
    total_ciudades = imprimir_busqueda(ciudades)

    '''
    RAYOS! Olvide evaluar si total_ciudades era mayor a 0
    antes de ejecutar la funcion de guardar

    Por favor consideren este update menor en sus codigos
    Aca la version ya corregida!

    Gracias!
    '''
    if total_ciudades > 0: # Esta linea es la que me falto!!!
        guardar_busqueda(pais,ciudades)
