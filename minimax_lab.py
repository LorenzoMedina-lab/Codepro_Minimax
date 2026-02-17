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
            juego["tablero"][f][c] = "-"        #Bucle anidado

    #Agrego a los jugadores al tablero
    gato_fila, gato_columna = juego["gato"]
    raton_fila, raton_columna = juego["raton"]
    juego["tablero"][gato_fila][gato_columna] = "G"
    juego["tablero"][raton_fila][raton_columna] = "R"

    # Se imprime el tablero
    print("\--Minimax Raton y Gato IA--")
    for fila in juego["tablero"]:
        print("|".join(fila))   #Aqui utilizo el separador de fila y columna
        print("-" * (juego["columnas"] *2))
    # Movimiento 
def movimiento_jugadores(juego, personaje, direccion):
     #Verifica el moviento para evitar que choque con los limetes del tablero
    if personaje == "raton":
        pos = juego["raton"]
    else:
        pos = juego["gato"]
        #calculo la nueva posicion 
    nueva_fila, nueva_columna = pos[0], pos[1]

    if direccion == "arriba": nueva_fila -= 1
    elif direccion == "abajo": nueva_fila += 1
    elif direccion == "izquierda": nueva_columna -= 1
    elif direccion == "derecha": nueva_columna += 1
    #Verifica que no salga del mapa
    if 0 <= nueva_fila < juego["filas"] and 0 <= nueva_columna < juego["columnas"]:
        #Si el movimiento es valido, actualiza la posicion actual
        if personaje == "raton":
            juego["raton"] = [nueva_fila, nueva_columna]
        else:
                juego["gato"] = [nueva_fila, nueva_columna]
        return True # Movimiento correcto
        
    return False # Movimiento fallido 

# Minimax
# --- 4. CEREBRO IA (MINIMAX) ---
def obtener_distancia(juego):
    #Calcula cuántos pasos hay entre el Gato y el Ratón (Manhattan).
    dist_vertical = abs(juego["gato"][0] - juego["raton"][0])
    dist_horizontal = abs(juego["gato"][1] - juego["raton"][1])
    return dist_vertical + dist_horizontal

def minimax(juego, profundidad, es_turno_raton):    #Caso Base
    if profundidad == 0 or juego["gato"] == juego["raton"]:
        return obtener_distancia(juego)
    
    direcciones = ["arriba", "abajo", "izquierda", "derecha"]
    
    if es_turno_raton:   #El gato quiere Maximizar su distancia del gato
        mejor_valor = -float("inf")  # El peor valor posible infinito negativo
        for direc in direcciones:
            copia = copy.deepcopy(juego)   #Se crea un universo paralelo
            if movimiento_jugadores(copia, "raton", direc):
                #Analiza si me muevo aqui, que hara el gato despues
                valor = minimax(copia, profundidad -1 False)
                mejor_valor = max(mejor_valor, valor)
        return mejor_valor

    else: #El gato quiere Minimizar su distancia del raton 
        mejor_valor = float("inf")   #El peor valor posible infinito positivo
        for direc in direcciones:
            copia = copy.deepcopy(juego) #Se crea un universo paralelo
            if movimiento_jugadores(copia, "gato", direc):
                #Analiza si se mueve aqui que hara el raton despues
                valor = minimax(copia, profundidad - 1, True)
                mejor_valor = min(mejor_valor, valor)
        return mejor_valor
    