class Stack:

#Pila vacia
    def __init__(self):
        self.__elements = []

#Agregar el elemento sobre la cima de la pila
    def push(self, element):
        self.__elements.append(element)

#Elimina y devuelve el elemento almacenado en la cima de la pila
    def pop(self):
        if len(self.__elements) > 0:
            return self.__elements.pop()
        else:
            return None

#Devuelve el valor del elemento que está almacenado encima de la pila pero sin eliminarlo
    def on_top(self):
        if len(self.__elements) > 0:
            return self.__elements[-1]
        else:
            return None

#Devuelve la cantidad de elementos en la pila
    def size(self):
        return len(self.__elements)