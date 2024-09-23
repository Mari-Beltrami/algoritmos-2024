# Reemplazar todas las ocurrencias de un determinado elemento en una pila   
from pila import Stack
pila_aux= Stack()
def reemplazo (pila, elemento):
    pila_aux = Stack()
    reemplazo=54
    while pila.size() > 0:
        ocurrencia_elemento = pila.pop()
        if ocurrencia_elemento == elemento:
            pila_aux.push(reemplazo)
        else:
            pila_aux.push(ocurrencia_elemento)
    
    while pila_aux.size() > 0:
        pila.push(pila_aux.pop())
        
    return pila

pila = Stack()
pila.push(1)
pila.push(2)
pila.push(3)
pila.push(2)
pila.push(1) 

elemento=int(input("INGRESE EL ELEMENTO QUE DESEA REEMPLAZAR:"))
reemplazada = reemplazo(pila,elemento)

pila_resultante = []
while pila.size() > 0:
    pila_resultante.append(pila.pop())
print(f"El elemento {elemento} fue reemplazado por 54. La pila queda de la siguiente forma: {pila_resultante}")