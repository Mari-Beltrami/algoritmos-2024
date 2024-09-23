

class Queue:

    def __init__(self):
        self.__elements = []

#Agrega el elemento al final de la cola
    def arrive(self, element):
        self.__elements.append(element)

#Elimina y devuelve el elemento almacenado en el frente de la cola
    def attention(self):
        if len(self.__elements) > 0:
            return self.__elements.pop(0)
        else:
            return None

#Determina la cantidad de elementos en la cola 
    def size(self):
        return len(self.__elements)

#Devuelve el valor del elemento que está almacenado en el frente de la cola sin eliminarlo
    def on_front(self):
        if len(self.__elements) > 0:
            return self.__elements[0]
        else:
            return None
    
#Elimina el elemento en el frente de la cola y lo inserta en el final de la misma
    def move_to_end(self):
        element = self.attention()
        if element is not None:
            self.arrive(element)
