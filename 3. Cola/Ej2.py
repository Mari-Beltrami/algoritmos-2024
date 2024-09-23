#Utilizando operaciones de cola y pila, invertir el contenido de una cola.
from pila import Stack
from cola import Queue

cola = Queue()

#Cola ejemplo
cola.arrive(1)
cola.arrive(2)
cola.arrive(3)
cola.arrive(4)

def invertir_cola (cola, pila):
    while cola.size() > 0:
        pila.push(cola.attention()) #Sacar de la cola y agregar a la pila
        
    while pila.size() > 0:
        cola.arrive(pila.pop()) #Sacar de la pila y agregar a la cola

pila = Stack()

invertir_cola(cola, pila)

resultado = []
while cola.size() > 0:
    resultado.append(cola.attention()) #Dentro del bucle, se extrae el primer elemento de la cola utilizando attention() (que debería eliminar el elemento de la cola) y se añade a la lista resultado. Esto se repite hasta que la cola esté vacía.
    
print (f"Ahora la cola está invertida: {resultado}")