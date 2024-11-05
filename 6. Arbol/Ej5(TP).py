# Dado un árbol con los nombre de los superhéroes y villanos de la saga Marvel Cinematic Univer-
# se (MCU), desarrollar un algoritmo que contemple lo siguiente:
# a. además del nombre del superhéroe, en cada nodo del árbol se almacenará un campo boo-
# leano que indica si es un héroe o un villano, True y False respectivamente;
# b. listar los villanos ordenados alfabéticamente;
# c. mostrar todos los superhéroes que empiezan con C;
# d. determinar cuántos superhéroes hay el árbol;
# e. Doctor Strange en realidad está mal cargado. Utilice una búsqueda por proximidad para
# encontrarlo en el árbol y modificar su nombre;
# f. listar los superhéroes ordenados de manera descendente;
# g. generar un bosque a partir de este árbol, un árbol debe contener a los superhéroes y otro a
# los villanos, luego resolver las siguiente tareas:
# I. determinar cuántos nodos tiene cada árbol;
# II. realizar un barrido ordenado alfabéticamente de cada árbol.

from arbol_avl import ArbolAVL

arbol_personajes = ArbolAVL()

personajes_mcu = [
    {"nombre": "Iron Man", "es_heroe": True},
    {"nombre": "Thanos", "es_heroe": False},
    {"nombre": "Captain America", "es_heroe": True},
    {"nombre": "Doctor Strange", "es_heroe": True},
    {"nombre": "Loki", "es_heroe": False},
    {"nombre": "Black Widow", "es_heroe": True},
    {"nombre": "Green Goblin", "es_heroe": False},
    {"nombre": "Hawkeye", "es_heroe": True},
    {"nombre": "Scarlet Witch", "es_heroe": True},
    {"nombre": "Vision", "es_heroe": True},
    {"nombre": "Ultron", "es_heroe": False},
    {"nombre": "Spider-Man", "es_heroe": True},
]

for personaje in personajes_mcu:
    arbol_personajes.insertar_nodo(personaje["nombre"], personaje)

print("Villanos ordenados alfabéticamente:")
arbol_personajes.inorden_villanos()

print("\nSuperhéroes que empiezan con C:")
arbol_personajes.inorden_superheroes_comienzan_con("C")

cantidad_heroes = arbol_personajes.contar_super_heroes()
print("\nCantidad de superhéroes en el árbol:", cantidad_heroes)

print("\nModificando el nombre de Doctor Strange:")
arbol_personajes.busqueda_aproximada("Doctor")

print("\nSuperhéroes en orden descendente:")
arbol_personajes.postorden()

arbol_heroes = ArbolAVL()
arbol_villanos = ArbolAVL()

for personaje in personajes_mcu:
    if personaje["es_heroe"]:
        arbol_heroes.insertar_nodo(personaje["nombre"], personaje)
    else:
        arbol_villanos.insertar_nodo(personaje["nombre"], personaje)

cantidad_heroes_bosque = arbol_heroes.contar_super_heroes()
cantidad_villanos_bosque = arbol_villanos.contar_super_heroes()
print("\nCantidad de nodos en el árbol de héroes:", cantidad_heroes_bosque)
print("Cantidad de nodos en el árbol de villanos:", cantidad_villanos_bosque)

print("\nBarrido alfabético del árbol de héroes:")
arbol_heroes.inorden()

print("\nBarrido alfabético del árbol de villanos:")
arbol_villanos.inorden()
