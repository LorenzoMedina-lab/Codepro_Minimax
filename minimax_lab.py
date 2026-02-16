#Importo las librerias a utilizar
import random
import copy
# Primero creo el tablero (Matrix)
def crear_tablero(filas,columnas):
    tablero = [] #Lista principal contiene el tablero

    for _ in range(filas):
        fila = [] #Aqui creo una fila vacia para empezar
        for _ in range(columnas):
            fila.append("-")  #Aqui agrego el macador a la fila actual
        tablero.append(fila)
    return tablero

#Iniciar juego define el estado inicial del juego
def iniciar_juego(filas,columnas):
    matriz_tablero = crear_tablero(filas,columnas)
    return {
        "filas":filas,
        "columnas": columnas,
        "raton": [filas -1, columnas -1],  #P.del raton esquina inferior derecha
        "gato": [0,0],                    #P del gaton esquina superior izquierda
        "tablero": matriz_tablero
    }

# Esta funcion muestra mi tablero

def mostrar_tablero(matriz):
    for fila in matriz:
        print("|".join(fila))

mi_tablero = crear_tablero(5, 5)
mostrar_tablero(mi_tablero)
