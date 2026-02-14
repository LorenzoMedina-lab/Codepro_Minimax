# Primero creo el tablero (Matrix)
def crear_tablero(filas,columnas):
    tablero = [] #Lista principal contiene el tablero

    for _ in range(filas):
        fila = [] #Aqui creo una fila vacia para empezar
        for _ in range(columnas):
            fila.append("-")  #Aqui agrego el macador a la fila actual
        tablero.append(fila)
    return tablero


# Esta funcion muestra mi tablero

def mostrar_tablero(matriz):
    for fila in matriz:
        print("|".join(fila))

mi_tablero = crear_tablero(5, 5)
mostrar_tablero(mi_tablero)