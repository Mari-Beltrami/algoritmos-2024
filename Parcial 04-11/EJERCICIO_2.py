# Dado un grafo no dirigido con personajes de la saga Star Wars, implementar los algoritmos necesarios para resolver las siguientes tareas: 
# a) cada vértice debe almacenar el nombre de un personaje, las aristas representan la cantidad de episodios en los que aparecieron juntos ambos personajes que se relacionan; 
# b) hallar el árbol de expansión mínimo y determinar si contiene a Yoda; 
# c) determinar cuál es el número máximo de episodio que comparten dos personajes, y quienes son. 
# d) cargue al menos los siguientes personajes: Luke Skywalker, Darth Vader, Yoda, Boba Fett, C-3PO, Leia, Rey, Kylo Ren, Chewbacca, Han Solo, R2-D2, BB-8.

from grafo import Grafo  

star_wars_grafo = Grafo(dirigido=False)

#pto a. cada vértice almacena el nombre de un personaje
personajes = [
    "Luke Skywalker", "Darth Vader", "Yoda", "Boba Fett",
    "C-3PO", "Leia", "Rey", "Kylo Ren", "Chewbacca",
    "Han Solo", "R2-D2", "BB-8"
]

for personaje in personajes:
    star_wars_grafo.insertar_vertice(personaje)

# pto a. aristas entre personajes
star_wars_grafo.insertar_arista("Luke Skywalker", "Darth Vader", 3)
star_wars_grafo.insertar_arista("Luke Skywalker", "Leia", 5)
star_wars_grafo.insertar_arista("Luke Skywalker", "Han Solo", 4)
star_wars_grafo.insertar_arista("Luke Skywalker", "Yoda", 2)
star_wars_grafo.insertar_arista("Luke Skywalker", "R2-D2", 6)
star_wars_grafo.insertar_arista("Leia", "Darth Vader", 3)
star_wars_grafo.insertar_arista("Leia", "Chewbacca", 4)
star_wars_grafo.insertar_arista("Leia", "Han Solo", 5)
star_wars_grafo.insertar_arista("Leia", "C-3PO", 6)
star_wars_grafo.insertar_arista("Darth Vader", "Yoda", 1)
star_wars_grafo.insertar_arista("Han Solo", "Chewbacca", 5)
star_wars_grafo.insertar_arista("Han Solo", "R2-D2", 3)
star_wars_grafo.insertar_arista("Chewbacca", "R2-D2", 2)
star_wars_grafo.insertar_arista("Yoda", "R2-D2", 2)
star_wars_grafo.insertar_arista("Rey", "Kylo Ren", 3)
star_wars_grafo.insertar_arista("Rey", "BB-8", 2)
star_wars_grafo.insertar_arista("R2-D2", "C-3PO", 6)

# pto b. arbol de expansión mínima 
print("\nb. 1. El árbol de expansión mínima es:")
arbol_expansion_minima = star_wars_grafo.kruskal()  
contiene_yoda = False
for arista in arbol_expansion_minima:
    print("    ", arista)  
    # pto b. ver si contiene a Yoda
    if "Yoda" in arista:
        contiene_yoda = True

if contiene_yoda:
    print("b. 2. El árbol de expansión mínima contiene a Yoda.")
else:
    print("b. 2. El árbol de expansión mínima no contiene a Yoda.")

# pto c. número máx de episodios que comparte cada personaje y quienes son
max_episodios = 0
personajes_max_episodios = ("", "")

for nodo in star_wars_grafo.elementos:
    for arista in nodo["aristas"]:
        if arista["peso"] > max_episodios:
            max_episodios = arista["peso"]
            personajes_max_episodios = (nodo["valor"], arista["valor"])

print(f"\nc. El número máximo de episodios compartidos es {max_episodios}, entre {personajes_max_episodios[0]} y {personajes_max_episodios[1]}.")

# d) Mostrar el listado de personajes con sus respectivas conexiones
print("\nd. Lista de personajes con sus conexiones:")
star_wars_grafo.mostrar_grafo()  # Utilizamos la función mostrar_grafo() para listar conexiones
