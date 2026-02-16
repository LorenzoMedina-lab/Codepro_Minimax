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
        "gato": [0,0],                    #P del gato esquina superior izquierda
        "tablero": matriz_tablero
    }

# Esta funcion muestra mi tablero

def mostrar_tablero(juego):
    for f in range(juego["filas"]):
        for c in range(juego["columnas"]):
            juego["tablero"][f][c] = "-"

    #Agrego a los jugadores al tablero
    gato_fila, gato_columna = juego["gato"]
    raton_fila, raton_columna = juego["raton"]
    juego["tablero"][gato_fila][gato_columna] = "G"
    juego["tablero"][raton_fila][raton_columna] = "R"

    # Se imprime el tablero
    print("\--Minimax Raton y Gato IA--")
    for fila in juego["tablero"]:
        print("|".join(fila))   #Aqui utilizo el separador de fila y columna
