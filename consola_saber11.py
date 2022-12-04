"""
Ejercicio nivel 4: Prueba ICFES Saber 11 en Colombia
Interfaz basada en consola para la interaccion con el usuario.

@author: Cupi2
"""

import saber11 as s11
import pandas as pd

def ejecutar_cargar_datos() -> pd.DataFrame:
    """Solicita al usuario que ingrese el nombre de un archivo CSV con los datos de las pruebas saber 11 en Colombia.
    Retorno: dict
        El diccionario de clubes con la informaciÃ³n de los jugadores en el archivo
    """
    datos = None
    archivo = input("Por favor ingrese el nombre del archivo CSV con la informacion de las pruebas saber 11: ")
    datos = s11.cargar_datos(archivo)
    if len(datos) == 0:
        print("El archivo seleccionado no es valido. No se pudo cargar la informacion.")
    else:
        print("Se cargaron los siguientes datos a partir del archivo csv: ")
        print(datos)
    return datos

def ejecutar_piechart_genero(dataframe: pd.DataFrame)->None:
    """Ejecuta la opcion de hacer una gráfica de pie sobre la distribución 
    del género de los colegios.
    """
    s11.piechart_genero(dataframe)
    print("Se graficó la distribución del género de los colegios éxitosamente!!!")
    
def ejecutar_top10_departamentos(dataframe: pd.DataFrame) -> None:
    """Ejecuta la opcion de hacer una grafica de barras del top 10 de departamentos 
    que tuvieron mejor resultado en una categoría dada por el usuario en las pruebas 
    Saber 11.
    """
    categoria = input("Ingrese la categoria del examen de la cual se quiere conocer el top 10: ")
    s11.top10_departamentos(dataframe, categoria)
    print("Se graficó el top 10 departamentos con mejor resultado en las pruebas Saber 11 en la categoria", categoria, " éxitosamente!!!")

def ejecutar_categorias_evaluacion(dataframe: pd.DataFrame) -> None:
    """Ejecuta la opcion que hace un diagrama de caja y bigotes de la distribución 
    de los puntajes por categoría de las pruebas Saber 11. 
    """
    s11.categorias_evaluacion(dataframe)
    print("Se graficó el diagrama de caja y bigotes de la distribución de los puntajes de las pruebas Saber 11 éxitosamente!!!")

def ejecutar_crear_matriz(dataframe: pd.DataFrame) -> tuple:
    """Ejecuta la opcion que construye la matriz de Departamento vs Número de hogares
    que tienen un equipo/electrodoméstico/servicio determinado.
    """
    matriz = s11.crear_matriz(dataframe)
    print("La matriz armada de Departamento vs. Numero de hogares con un servicio/electrodomestico/equipo es:")
    print(matriz)
    return matriz

def ejecutar_depto_mas_electrodomesticos(matriz:tuple) -> None:
    """Ejecuta la opcion que encuentra el departamento con mayor cantidad de 
    electrodomésticos (lavadora y microondas). El mensaje que se le muestra al usuario
    debe tener el siguiente formato:
        'El departamento con mayor cantidad de electrodomesticos es (departamento)'.
    """
    mayor = s11.depto_mas_electrodomesticos(matriz)
    print("El departamento con mayor cantidad de electrodomesticos es", mayor)
    
def ejecutar_cantidad_equipos_electrodomesticos(matriz:tuple) -> None:
    """Ejecuta la opcion que cuenta la cantidad de estudiantes con un 
    equipo/electrodoméstico/servicio dado en el país. El mensaje que se le muestra
    al usuario debe tener el siguiente formato:
        'Hay (cantidad) de personas con el equipo/servicio/electrodomestico (equipo) en el pais.'
    """
    equipo = input("Ingrese el equipo/servicio/electrodoméstico para el cual desea obtener su cantidad total: ")
    cantidad = s11.cantidad_equipos_electrodomesticos(matriz, equipo)
    print("Hay", cantidad, "de personas con el equipo/servicio/electrodomestico", equipo)

def ejecutar_ICV_depto(matriz:tuple) -> None:
    """Ejecuta la opcion que calcula el Índice de Calidad de Vida (ICV) de un departamento dado.
    El mensaje que se le muestra al usuario debe tener el siguiente formato:
        'El Indice de Calidad de Vida (ICV) del departamento (departamento) es (indice)'
    """
    departamento = input("Ingrese el departamento del cual desea conocer el Indice de Calidad de Vida: ")
    ICV = s11.ICV_depto(matriz, departamento)
    print("El Indice de Calidad de Vida (ICV) del departamento", departamento, "es", ICV)
    
def mostrar_menu():
    """Imprime las opciones de ejecucion disponibles para el usuario.
    """
    print("\nOpciones")
    print("1. Cargar datos de las pruebas Saber 11 calendario A 2020 en Colombia.")
    print("2. Consultar distribucion de los estudiantes en los diferentes generos de los colegios")
    print("3. Consultar el top 10 departamentos en las pruebas Saber 11 en una categoria determinada.")
    print("4. Consultar la distribucion de los puntajes por categoria de las pruebas Saber 11.")
    print("5. Construccion de la matriz de Departamentos vs. Numero de hogares que tienen un equipo/electrodomestico/servicio determinado.")
    print("6. Consultar departamento con mayor cantidad de electrodomesticos.")
    print("7. Consultar la cantidad de estudiantes en el pais que cuentan con un equipo/servicio/electrodomestico determinado. ")
    print("8. Consultar el Indice de Calidad de Vida de un departamento dado.")    
    print("9. Salir.") 

def iniciar_aplicacion():
    """Ejecuta el programa para el usuario."""
    continuar = True
    datos = None
    matriz = None
    while continuar:
        mostrar_menu()
        opcion_seleccionada = int(input("Por favor seleccione una opcion: "))
        if opcion_seleccionada == 1:
            datos = ejecutar_cargar_datos()
        elif opcion_seleccionada ==2:
            ejecutar_piechart_genero(datos)
        elif opcion_seleccionada ==3:
            ejecutar_top10_departamentos(datos)
        elif opcion_seleccionada ==4:
            ejecutar_categorias_evaluacion(datos)
        elif opcion_seleccionada ==5:
            matriz = ejecutar_crear_matriz(datos)
        elif opcion_seleccionada ==6:
            ejecutar_depto_mas_electrodomesticos(matriz)
        elif opcion_seleccionada ==7:
            ejecutar_cantidad_equipos_electrodomesticos(matriz)
        elif opcion_seleccionada ==8:
            ejecutar_ICV_depto(matriz)
        elif opcion_seleccionada ==9:
            continuar = False
        else:
            print("Por favor seleccione una opcion valida.")


#PROGRAMA PRINCIPAL
iniciar_aplicacion()


