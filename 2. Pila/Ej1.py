#determinar el numero de ocurrencias de un determinado elemento de una pila
from pila import Stack

pila_aux= Stack()

def ocurrencias(pila, elemento):
    contador = 0
    
    while pila.size() > 0:
        elemento_arriba = pila.pop()
        if elemento_arriba  == elemento:
            contador += 1
        pila_aux.push(elemento_arriba)
        
    while pila_aux.size() > 0:
        pila.push(pila_aux.pop())
        
    return contador

pila = Stack()
pila.push(1)
pila.push(2)
pila.push(3)
pila.push(2)
pila.push(1)

elemento_buscado = 1
num_ocurrencias = ocurrencias(pila, elemento_buscado)
print(f"El elemento {elemento_buscado} aparece {num_ocurrencias} veces en la pila.")
