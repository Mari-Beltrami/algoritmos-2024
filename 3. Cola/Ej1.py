# Eliminar de una cola de caracteres todas las vocales que aparecen.
from cola import Queue

#Función que elimina las vocales de la cola

def eliminar_vocales(queue):
    #Identificar cuales son las vocales con la lista
    vocales = ["a", "e", "i", "o", "u"]
    #Cola auxiliar que almacenará los caracteres sin vocales.
    cola_aux = Queue()
    
    while queue.size() > 0:
        #Obtener el elemento en el frente de la cola usando attention().
        char = queue.attention()
        #Verificar que el caracter no está en la lista de vocales. Y si no es una vocal, se agrega a la nueva cola usando arrive().
        if char.lower() not in vocales:
            cola_aux.arrive(char)
    #Retorna la nueva cola que contiene los caracteres sin vocales   
    return cola_aux

#Crear cola de caracteres.
my_queue = Queue()
my_queue.arrive('H')
my_queue.arrive('o')
my_queue.arrive('l')
my_queue.arrive('a')

#Eliminar las vocales de la cola.
cola_aux = eliminar_vocales(my_queue);

#Imprimir elementos de la nueva cola
while cola_aux.size() > 0:
    print(cola_aux.attention(), end="")


