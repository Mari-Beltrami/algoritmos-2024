# Implementar sobre un grafo no dirigido los algoritmos necesario para dar solución a las si-
# guientes tareas:
# a. cada vértice representar un ambiente de una casa: cocina, comedor, cochera, quincho,
# baño 1, baño 2, habitación 1, habitación 2, sala de estar, terraza, patio;
# b. cargar al menos tres aristas a cada vértice, y a dos de estas cárguele cinco, el peso de la aris-
# ta es la distancia entre los ambientes, se debe cargar en metros;
# c. obtener el árbol de expansión mínima y determine cuantos metros de cables se necesitan
# para conectar todos los ambientes;
# d. determinar cuál es el camino más corto desde la habitación 1 hasta la sala de estar para
# determinar cuántos metros de cable de red se necesitan para conectar el router con el
# Smart Tv.

from grafo import Grafo

casa_grafo = Grafo(dirigido=False)

ambientes = [
    "cocina", "comedor", "cochera", "quincho", "baño 1", "baño 2",
    "habitación 1", "habitación 2", "sala de estar", "terraza", "patio"
]

for ambiente in ambientes:
    casa_grafo.insertar_vertice(ambiente)

aristas = [
    ("cocina", "comedor", 5),
    ("cocina", "baño 1", 3),
    ("comedor", "patio", 4),
    ("cochera", "patio", 5),
    ("quincho", "patio", 4),
    ("baño 1", "habitación 1", 4),
    ("baño 2", "habitación 2", 4),
    ("patio", "terraza", 5),
    ("cochera", "habitación 2", 6),
    ("sala de estar", "terraza", 7)
]

for origen, destino, peso in aristas:
    casa_grafo.insertar_arista(origen, destino, peso)

print("\nc) Árbol de expansión mínima para conectar los ambientes:")
arbol_minimo = casa_grafo.kruskal()
for arista in arbol_minimo:
    print(f"    {arista}")

total_distancia = sum(int(arista.split("-")[-1].split(";")[-1]) for arista in arbol_minimo if arista.split("-")[-1].split(";")[-1].isdigit())
print(f"Total de metros de cable necesarios: {total_distancia} m")

print("\nd) Camino más corto desde 'habitación 1' hasta 'sala de estar':")
camino_mas_corto = casa_grafo.dijkstra("habitación 1")

camino = []
while camino_mas_corto.size() > 0:
    paso = camino_mas_corto.pop()
    nodo, nodo_info, anterior = paso[1][0], paso[1][1], paso[1][2]
    if anterior:
        camino.append(f"{anterior} -> {nodo} (Distancia acumulada: {paso[0]} m)")
    else:
        camino.append(f"{nodo} (Inicio)")

for paso in reversed(camino):
    print(f"    {paso}")
