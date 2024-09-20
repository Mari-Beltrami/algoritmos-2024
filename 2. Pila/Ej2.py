# Eliminar de una pila todos los elementos impares, es decir que en la misma solo queden nú-
# meros pares.

from pila import Stack

def pila_pares (pila):
    pila_aux=Stack()
    
    while pila.size() > 0:
        num = pila.pop()
        if num % 2 == 0:
            pila_aux.push(num)
    
    while pila_aux.size():
        pila.push(pila_aux.pop())
        
    return pila
    
pila = Stack()
pila.push(1)
pila.push(2)
pila.push(3)
pila.push(2)
pila.push(1)    

pila_pares(pila)

pares = []
while pila.size() > 0:  
    pares.append(pila.pop())
print(f"Los números pares son: {pares}")