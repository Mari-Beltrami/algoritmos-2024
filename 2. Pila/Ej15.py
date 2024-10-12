#Realizar el algoritmo de ordenamiento quicksort de manera que funcione iterativamente.

from pila import Stack

def particionar(arr, inicio, fin):
    # Usamos el último elemento como pivote
    pivote = arr[fin]
    i = inicio - 1  # Índice del elemento más pequeño

    for j in range(inicio, fin):
        if arr[j] <= pivote:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]  # Intercambiar elementos

    # Colocar el pivote en la posición correcta
    arr[i + 1], arr[fin] = arr[fin], arr[i + 1]
    return i + 1  # Retornar la posición del pivote

def quicksort_iterativo(arr):
    # Crear una pila para almacenar los índices de los subarreglos
    pila = Stack()

    # Empujar el rango inicial del arreglo completo
    pila.push((0, len(arr) - 1))

    # Mientras la pila no esté vacía
    while pila.size() > 0:
        # Obtener el rango superior de la pila
        inicio, fin = pila.pop()

        if inicio < fin:
            # Particionar el arreglo y obtener la posición del pivote
            pivote = particionar(arr, inicio, fin)

            # Empujar los subarreglos izquierdo y derecho en la pila
            pila.push((inicio, pivote - 1))  # Subarreglo izquierdo
            pila.push((pivote + 1, fin))     # Subarreglo derecho

# Ejemplo de uso
arreglo = [23, 45, 16, 37, 3, 99, 22, 12]
quicksort_iterativo(arreglo)
print("Arreglo ordenado:", arreglo)
