# Dada una lista de valores ordenadas, desarrollar un algoritmo que modifique el método de
# búsqueda binaria para que funcione de forma recursiva, y permita determinar si un valor dado
# está o no en dicha lista.

#!Búsqueda binaria: Si tenemos una lista ordenada de menor a mayor, en lugar de buscar el valor uno por uno (que sería una búsqueda lineal y muy lenta si la lista es grande), la búsqueda binaria se enfoca en reducir el tamaño del área de búsqueda dividiendo la lista a la mitad en cada paso. Así con cada comparación se pueden descartar la mitad de los elementos.
#!Para que la búsqueda binaria funcione, la lista debe estar ordenada. Si no está ordenada, este método no sirve, ya que se basa en la idea de descartar mitades del rango de búsqueda.

# def busqueda_binaria(lista,valor):
    # inicio = 0
    # fin = len(lista) - 1
    
    # while inicio <= fin:
        #Encontrar el punto medio del rango actual
        #medio = (inicio + fin) // 2
        
        # #Caso en el que encontramos el valor
        # if lista[medio] == valor:
            # return True
        
        # #Si el valor es menor que el valor en el medio, buscamos en la mitad izquierda
        # elif valor < lista[medio]:
            # fin = medio - 1
            
        # #Si el valor es mayor que el valor en el medio, buscamos en la mitad derecha
        # else:
            # inicio = medio + 1
    
    # #Si salimos del ciclo, el valor no está en la lista
    # return False

# #Ejemplo
# lista_ordenada = [1, 3, 5, 7, 9, 11, 13, 15]
# valor_a_buscar = 9
# resultado = busqueda_binaria(lista_ordenada, valor_a_buscar)

# if resultado:
    # print(f"El valor {valor_a_buscar} está en la lista.")
# else:
    # print(f"El valor {valor_a_buscar} no está en la lista.")
        
#!Búsqueda binaria recursiva
def busqueda_binaria(lista,valor,inicio,fin):
    # Caso base: si el inicio supera al final, significa que el valor no está en la lista.
    if inicio > fin:
        return False
    
    # Encontrar el punto medio del rango actual
    medio = (inicio + fin) // 2

    # Caso base: si el valor en la posición 'medio' es igual al valor buscado, se encontró
    if lista[medio] == valor:
        return True

    # Si el valor es menor que el valor en la posición 'medio', buscamos en la mitad izquierda
    elif valor < lista[medio]:
        return busqueda_binaria(lista, valor, inicio, medio - 1)

    # Si el valor es mayor que el valor en la posición 'medio', buscamos en la mitad derecha
    else:
        return busqueda_binaria(lista, valor, medio + 1, fin)

# Ejemplo de uso
lista_ordenada = [1, 3, 5, 7, 9, 11, 13, 15]
valor_a_buscar = 7
resultado = busqueda_binaria(lista_ordenada, valor_a_buscar, 0, len(lista_ordenada) - 1)

if resultado:
    print(f"El valor {valor_a_buscar} está en la lista.")
else:
    print(f"El valor {valor_a_buscar} no está en la lista.")