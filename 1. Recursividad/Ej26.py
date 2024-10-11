#Resuelva el problema de colocar las 8 reinas sobre un tablero de ajedrez sin que las mismas
#se amenacen

#!Backtracking es una técnica de fuerza bruta optimizada que consiste en explorar todas las posibles soluciones de un problema, pero retrocediendo ("backtracking") si se determina que una posible solución no lleva al resultado deseado. En el caso de las 8 reinas, intentamos colocar las reinas una por una y retrocedemos si no es posible completar la colocación.

N = 8  # Tamaño del tablero (8x8)

def es_seguro(tablero, fila, columna):
    # Verificar si hay una reina en la misma columna
    for i in range(fila):
        if tablero[i] == columna:
            return False

    # Verificar la diagonal superior izquierda
    for i, j in zip(range(fila - 1, -1, -1), range(columna - 1, -1, -1)):
        if tablero[i] == j:
            return False

    # Verificar la diagonal superior derecha
    for i, j in zip(range(fila - 1, -1, -1), range(columna + 1, N)):
        if tablero[i] == j:
            return False

    # Si pasa todas las verificaciones, es seguro colocar la reina aquí
    return True

def resolver_8_reinas(tablero, fila):
    # Si todas las reinas han sido colocadas, imprimimos el tablero
    if fila == N:
        imprimir_tablero(tablero)
        return True

    # Intentar colocar una reina en cada columna de la fila actual
    for columna in range(N):
        if es_seguro(tablero, fila, columna):
            tablero[fila] = columna  # Colocar la reina en la posición segura
            # Llamada recursiva para colocar la siguiente reina
            if resolver_8_reinas(tablero, fila + 1):
                return True

            # Backtracking: eliminar la reina si no se encuentra una solución
            tablero[fila] = -1

    # Si no se puede colocar una reina en esta fila, devolvemos False
    return False

def imprimir_tablero(tablero):
    for i in range(N):
        fila = ['.'] * N
        if tablero[i] != -1:
            fila[tablero[i]] = 'Q'
        print(' '.join(fila))
    print("\n")

# Inicializar el tablero con todas las reinas fuera del tablero
tablero = [-1] * N

# Llamar a la función para resolver el problema de las 8 reinas
resolver_8_reinas(tablero, 0)

#!zip() es una función incorporada que se usa para emparejar elementos de dos o más listas, tuplas u otros iterables. La función toma dos o más iterables y devuelve un iterador de tuplas, donde cada tupla contiene elementos que ocupan la misma posición en cada uno de los iterables.

# Explicación del Uso de zip() en este ejercicio:

# Queremos verificar la diagonal superior izquierda desde la posición de la reina.
# # Usamos range(fila - 1, -1, -1) para ir moviéndonos hacia arriba, es decir, desde la fila actual hasta la primera fila (-1 significa hasta el comienzo).
# # Usamos range(columna - 1, -1, -1) para movernos hacia la izquierda, es decir, desde la columna actual hacia la primera columna.
# # zip() combina ambos range() para recorrer simultáneamente ambas dimensiones (fila y columna), lo que nos permite verificar todas las posiciones a lo largo de la diagonal.