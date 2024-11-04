""" El problema de la mochila Jedi. Suponga que un Jedi (Luke Skywalker, Obi-Wan Kenobi, Rey u
otro, el que más le guste) está atrapado, pero muy cerca está su mochila que contiene muchos
objetos. Implementar una función recursiva llamada “usar la fuerza” que le permita al Jedi “con
ayuda de la fuerza” realizar las siguientes actividades:
a. sacar los objetos de la mochila de a uno a la vez hasta encontrar un sable de luz o que no
queden más objetos en la mochila;

b. determinar si la mochila contiene un sable de luz y cuantos objetos fueron necesarios sa-
car para encontrarlo;

c. Utilizar un vector para representar la mochila. """

def usar_la_fuerza (mochila, cantidad_objetos=0):

    if not mochila:
        return (False, cantidad_objetos)

    objeto = mochila[0]
    print("Luke encontró:", objeto, "en la mochila.")

    if objeto == "sable de luz":
        return (True, cantidad_objetos + 1) 
    else:
        return usar_la_fuerza(mochila[1:], cantidad_objetos + 1)
    
#prueba
mochila = ["comida", "agua", "mapa", "sable de luz", "ropa"]
tiene_sable, cantidad_objetos = usar_la_fuerza(mochila)
if tiene_sable:
    print("Luke encontró un sable de luz después de", cantidad_objetos, "objetos.")
else:
    print("Luke no encontró un sable de luz en la mochila.")
        
    