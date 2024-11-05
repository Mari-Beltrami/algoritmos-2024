# Se requiere implementar un grafo para almacenar las siete maravillas arquitectónicas moder-
# nas y naturales del mundo, para lo cual se deben tener en cuenta las siguientes actividades:
# a. de cada una de las maravillas se conoce su nombre, país de ubicación (puede ser más de
# uno en las naturales) y tipo (natural o arquitectónica);
# b. cada una debe estar relacionada con las otras seis de su tipo, para lo que se debe almacenar
# la distancia que las separa;
# c. hallar el árbol de expansión mínimo de cada tipo de las maravillas;
# d. determinar si existen países que dispongan de maravillas arquitectónicas y naturales;
# e. determinar si algún país tiene más de una maravilla del mismo tipo;
# f. deberá utilizar un grafo no dirigido.

from grafo import Grafo 

maravillas_grafo = Grafo(dirigido=False)

maravillas = [
    {"nombre": "Gran Muralla China", "pais": ["China"], "tipo": "arquitectonica"},
    {"nombre": "Petra", "pais": ["Jordania"], "tipo": "arquitectonica"},
    {"nombre": "Cristo Redentor", "pais": ["Brasil"], "tipo": "arquitectonica"},
    {"nombre": "Machu Picchu", "pais": ["Perú"], "tipo": "arquitectonica"},
    {"nombre": "Chichen Itza", "pais": ["México"], "tipo": "arquitectonica"},
    {"nombre": "Coliseo", "pais": ["Italia"], "tipo": "arquitectonica"},
    {"nombre": "Taj Mahal", "pais": ["India"], "tipo": "arquitectonica"},
    {"nombre": "Amazonas", "pais": ["Brasil", "Perú", "Colombia", "Venezuela"], "tipo": "natural"},
    {"nombre": "Bahía de Ha Long", "pais": ["Vietnam"], "tipo": "natural"},
    {"nombre": "Cataratas del Iguazú", "pais": ["Argentina", "Brasil"], "tipo": "natural"},
    {"nombre": "Isla Jeju", "pais": ["Corea del Sur"], "tipo": "natural"},
    {"nombre": "Parque Nacional de Komodo", "pais": ["Indonesia"], "tipo": "natural"},
    {"nombre": "Montaña de la Mesa", "pais": ["Sudáfrica"], "tipo": "natural"},
    {"nombre": "Río Subterráneo de Puerto Princesa", "pais": ["Filipinas"], "tipo": "natural"}
]

for maravilla in maravillas:
    maravillas_grafo.insertar_vertice_con_datos(maravilla["nombre"], otros_datos=maravilla) 

distancias_arquitectonicas = [
    ("Gran Muralla China", "Petra", 4500),
    ("Gran Muralla China", "Cristo Redentor", 17000),
    ("Gran Muralla China", "Machu Picchu", 17000),
    ("Gran Muralla China", "Chichen Itza", 15000),
    ("Gran Muralla China", "Coliseo", 8000),
    ("Gran Muralla China", "Taj Mahal", 4000),
    ("Petra", "Cristo Redentor", 12000),
    ("Petra", "Machu Picchu", 13000),
    ("Petra", "Chichen Itza", 12500),
    ("Petra", "Coliseo", 3000),
    ("Petra", "Taj Mahal", 5000),
]

distancias_naturales = [
    ("Amazonas", "Bahía de Ha Long", 17000),
    ("Amazonas", "Cataratas del Iguazú", 1500),
    ("Amazonas", "Isla Jeju", 19000),
    ("Amazonas", "Parque Nacional de Komodo", 18000),
    ("Amazonas", "Montaña de la Mesa", 12000),
    ("Amazonas", "Río Subterráneo de Puerto Princesa", 17000),
    ("Bahía de Ha Long", "Cataratas del Iguazú", 19000),
    ("Bahía de Ha Long", "Isla Jeju", 3000),
    ("Bahía de Ha Long", "Parque Nacional de Komodo", 3500),
    ("Bahía de Ha Long", "Montaña de la Mesa", 18000),
    ("Bahía de Ha Long", "Río Subterráneo de Puerto Princesa", 2000),
]

for origen, destino, distancia in distancias_arquitectonicas:
    maravillas_grafo.insertar_arista(origen, destino, distancia)

for origen, destino, distancia in distancias_naturales:
    maravillas_grafo.insertar_arista(origen, destino, distancia)

print("\nc) Árbol de expansión mínima para maravillas arquitectónicas:")
arbol_minimo_arquitectonico = maravillas_grafo.kruskal_con_filtro(filtro_tipo="arquitectonica")
for arista in arbol_minimo_arquitectonico:
    print("    ", arista)

print("\nc) Árbol de expansión mínima para maravillas naturales:")
arbol_minimo_natural = maravillas_grafo.kruskal_con_filtro(filtro_tipo="natural")
for arista in arbol_minimo_natural:
    print("    ", arista)

paises_maravillas = {}
for maravilla in maravillas:
    for pais in maravilla["pais"]:
        if pais not in paises_maravillas:
            paises_maravillas[pais] = {"arquitectonica": 0, "natural": 0}
        paises_maravillas[pais][maravilla["tipo"]] += 1

print("\nd) Países con maravillas de ambos tipos:")
for pais, tipos in paises_maravillas.items():
    if tipos["arquitectonica"] > 0 and tipos["natural"] > 0:
        print(f" - {pais} tiene maravillas arquitectónicas y naturales.")

print("\ne) Países con más de una maravilla del mismo tipo:")
for pais, tipos in paises_maravillas.items():
    if tipos["arquitectonica"] > 1:
        print(f" - {pais} tiene múltiples maravillas arquitectónicas.")
    if tipos["natural"] > 1:
        print(f" - {pais} tiene múltiples maravillas naturales.")
