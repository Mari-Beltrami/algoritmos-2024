#determinar el numero de ocurrencias de un determinado elemento de una pila
"""
from pila import Stack
pila = Stack()

for i in range(1, 11):
    if i % 2 == 0:
        pila.push(i)

print(pila.on_top())
"""

from random import randint
from pila import Stack
pila = Stack()
lista = [] #borrar

for i in range(10):
    azar = randint(1, 5)
    pila.push(azar)
    lista.append(azar) #borrar
    
print(lista)

def ocurrencias(pila, elemento):
    pila_aux = Stack()
    numeros_2 = 0
    for i in range(pila.size()):
        
        if pila.on_top() == elemento:
            numeros_2 += 1
        
        pila_aux.push(pila.pop())
    for i in range(pila_aux.size()):
        pila.push(pila_aux.pop())
    
    return numeros_2

print(ocurrencias(pila, 2))