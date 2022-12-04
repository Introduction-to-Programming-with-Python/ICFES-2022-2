#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Ejercicio nivel 4: Prueba ICFES Saber 11 en Colombia
Modulo de funciones.

@author: Cupi2
"""
import pandas as pd
from pandas.core.frame import DataFrame
import matplotlib.pyplot as plt
from operator import itemgetter

# PARTE 1----------------------------------------------------------------------------

# Requerimiento 0

def cargar_datos(nombre_archivo:str)->DataFrame:

    """

    Cargar los datos de un archivo csv a un DataFrame.
    
    Parameters
    ----------
    nombre_archivo : str
        Nombre del archivo que contiene la informacion de la prueba ICFES Saber 11.

    Returns
    -------
    DataFrame
        Informacion del archivo CSV como DataFrame.

    """

    archivo = pd.read_csv(nombre_archivo)

    return archivo

# PARTE 2----------------------------------------------------------------------------

# Requerimiento 1

def crear_matriz(dataframe: pd.DataFrame) -> tuple:

    """

    Construir una matriz que cruce el departamento y el número de hogares que
    poseen equipos tecnológicos/electrodomésticos/servicios.
    
    Parameters
    ----------
    dataframe: DataFrame
        Informacion del archivo CSV como DataFrame.

    Returns
    -------
    tuple
        Tupla que contiene la matriz creada y los diccionarios de filas y 
        columnas en el siguiente formato (matriz, dict_columnas, dict_filas).

    """

    servicios_equipos = sorted(
        [
            "internet",
            "tv", 
            "computador",
            "microondas",
            "carro",
            "lavadora",
            "moto",
            "videojuegos"
        ]
    )
    servicios_equipos_dict = dict(list(enumerate(servicios_equipos)))
    deptos =  sorted(dataframe["dpto"].unique())
    dept_dict = dict(list(enumerate(deptos)))
    
    dic_groupby = {}
    for serv in servicios_equipos:
        group = dataframe.groupby("dpto")[serv].sum()
        dic_groupby[serv] = group
    
    matriz =[]
    for i in dept_dict:
        departamento = dept_dict[i]
        fila = []
        for j in servicios_equipos_dict:
            serv_eq = dic_groupby[servicios_equipos_dict[j]][departamento]
            fila.append(serv_eq)
        matriz.append(fila)

    return (matriz, servicios_equipos_dict, dept_dict)

# Requerimiento 2

def depto_mas_electrodomesticos(datos: tuple) -> str:

    """

    Encontrar el departamento que ha registrado la mayor cantidad de
    electrodomésticos (lavadora y microondas).
    
    Parameters
    ----------
    datos: tuple
        Tupla que contiene la matriz creada en el requerimiento 1 y los
        diccionarios de filas y columnas en el siguiente formato (matriz,
        dict_columnas, dict_filas).

    Returns
    -------
    str
         Nombre del departamento con mayor número de electrodomésticos.

    """

    conteo = {}
    for i in datos[2].keys():
        conteo[datos[2][i]] = 0
        conteo[datos[2][i]] += datos[0][i][3]
        conteo[datos[2][i]] += datos[0][i][4]

    departamento = ""
    mayor = 0
    for i in range(0, len(datos[2].values())):
        if conteo[datos[2][i]] > mayor:
            mayor = conteo[datos[2][i]]
            departamento = datos[2][i]

    return departamento.lower().capitalize()

# Requerimiento 3

def cantidad_equipos_electrodomesticos(datos: tuple, equipo:str) -> int:

    """

    Calcular el número total de un servicio/electrodoméstico/equipo
    tecnológico en todo el país. 
    
    Parameters
    ----------
    datos: tuple
        Tupla que contiene la matriz creada en el requerimiento 1 y los
        diccionarios de filas y columnas en el siguiente formato (matriz,
        dict_columnas, dict_filas).

    Returns
    -------
    int
        Entero que represente la cantidad de la categoría ingresada en el país. 

    """

    equipo = equipo.lower()
    posicion = 0
    for i in range(0, len(datos[1].values())):
        if datos[1][i] == equipo:
            posicion = i

    conteo = 0
    for i in datos[0]:
        conteo += i[posicion]

    return conteo

# Requerimiento 4

def ICV_depto(datos: tuple, departamento:str) -> float:

    """

    Determinar el Índice de Calidad de Vida de un departamento.
    
    Parameters
    ----------
    datos: tuple
        Tupla que contiene la matriz creada en el requerimiento 1 y los
        diccionarios de filas y columnas en el siguiente formato (matriz,
        dict_columnas, dict_filas).
    departamento: str
        Departamento a consultar

    Returns
    -------
    float
         Redondeado a 2 cifras decimales que represente el ICV del departamento
         dado por el usuario.

    """

    departamento = departamento.upper()
    posicion = 0
    for i in range(0, len(datos[2].values())):
        if datos[2][i] == departamento:
            posicion = i

    pesos = {
        "carro": 0.2,
        "computador": 0.09,
        "internet": 0.09,
        "lavadora": 0.07,
        "microondas": 0.08,
        "moto": 0.16,
        "tv": 0.13,
        "videojuegos": 0.18
    }
    ICV = 0
    posicion_columna = 0
    for i in datos[0][posicion]:
        ICV += i*pesos[datos[1][posicion_columna]]
        posicion_columna += 1

    return round(ICV/10, 2)

# PARTE 3----------------------------------------------------------------------------

# Requerimiento 5

def piechart_genero(dataframe: DataFrame) -> None:

    """

    Conocer la distribución de los estudiantes en los diferentes géneros de los colegios. 
    
    Parameters
    ----------
    dataframe: DataFrame
        Informacion del archivo CSV como DataFrame.

    Returns
    -------
    None

    """

    cant_total = dataframe.shape[0]
    cant_mas = (dataframe.loc[dataframe["genero_col"] == "MASCULINO"]).shape[0]
    cant_fem = (dataframe.loc[dataframe["genero_col"] == "FEMENINO"]).shape[0]
    cant_mix = (dataframe.loc[dataframe["genero_col"] == "MIXTO"]).shape[0]

    porcentaje_mas = (cant_mas*100)/cant_total
    porcentaje_fem = (cant_fem*100)/cant_total
    porcentaje_mix = (cant_mix*100)/cant_total

    labels = 'FEMENINO', 'MASCULINO', "MIXTO"
    sizes = [porcentaje_fem, porcentaje_mas, porcentaje_mix]
    plt.title("Distribución porcentual según género del colegio")
    plt.pie(sizes, labels=labels, autopct='%1.1f%%')
    plt.show() 
    plt.show()

# Requerimiento 6

def top10_departamentos(dataframe: DataFrame, categoria: str) -> None:

    """

    Conocer el top 10 departamentos que tuvieron mejor resultado en una categoría 
    dada por el usuario en las pruebas Saber 11. 
    
    Parameters
    ----------
    dataframe: DataFrame
        Informacion del archivo CSV como DataFrame.
    categoria: str
        Categoris de calificación ingresada por el usuario.

    Returns
    -------
    None

    """

    departamentos = list((dataframe.iloc[:, 1].unique()))
    departamentos.sort()

    top = {}
    for i in departamentos:
        filtered_rows = dataframe.loc[dataframe["dpto"] == i]
        filtered_columns = filtered_rows.filter(items=[categoria.lower()])
        promedio = filtered_columns.mean()
        top[i] = float(promedio)

    top = dict(sorted(top.items(), key=itemgetter(1)))
    departamentos = list(top.keys())
    departamentos.reverse()
    puntajes = list(top.values())
    puntajes.reverse()

    plt.bar(departamentos[0:10], puntajes[0:10])
    plt.title(f"Top 10 departamentos con mejor puntajes en la categoria {categoria.lower()} en las pruebas saber 11")
    plt.xlabel("Promedio de puntaje obtenido")
    plt.ylabel("Departamento")
    plt.show()

# Requerimiento 7

def categorias_evaluacion(dataframe: DataFrame) -> None:

    """

    Mostrar la distribución de los puntajes por categoría de las pruebas Saber 11. 
    
    Parameters
    ----------
    dataframe: DataFrame
        Informacion del archivo CSV como DataFrame.

    Returns
    -------
    None

    """

    datos = {
        "categoria": [],
        "puntaje": []
        }
    for registro in dataframe.itertuples():
        datos["categoria"].append("lectura_critica")
        datos["puntaje"].append(registro.lectura_critica)
        datos["categoria"].append("matematicas")
        datos["puntaje"].append(registro.matematicas)
        datos["categoria"].append("ciencias")
        datos["puntaje"].append(registro.ciencias)
        datos["categoria"].append("sociales")
        datos["puntaje"].append(registro.sociales)
        datos["categoria"].append("ingles")
        datos["puntaje"].append(registro.ingles)

    datos = pd.DataFrame(datos)
    datos = datos.loc[:, ["categoria", "puntaje"]].boxplot(by="categoria", rot=90,figsize=(15,10))  
    plt.title("Puntaje por categoría de evaluación")
    plt.xlabel("Categoria")
    plt.ylabel("Puntaje")
    plt.show()