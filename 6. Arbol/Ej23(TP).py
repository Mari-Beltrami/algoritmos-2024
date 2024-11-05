# Implementar un algoritmo que permita generar un árbol con los datos de la siguiente tabla y
# resuelva las siguientes consultas:
# a. listado inorden de las criaturas y quienes la derrotaron;
# b. se debe permitir cargar una breve descripción sobre cada criatura;
# c. mostrar toda la información de la criatura Talos;
# d. determinar los 3 héroes o dioses que derrotaron mayor cantidad de criaturas;
# e. listar las criaturas derrotadas por Heracles;
# f. listar las criaturas que no han sido derrotadas;
# g. además cada nodo debe tener un campo “capturada” que almacenará el nombre del héroe
# o dios que la capturo;
# h. modifique los nodos de las criaturas Cerbero, Toro de Creta, Cierva Cerinea y Jabalí de
# Erimanto indicando que Heracles las atrapó;
# i. se debe permitir búsquedas por coincidencia;
# j. eliminar al Basilisco y a las Sirenas;
# k. modificar el nodo que contiene a las Aves del Estínfalo, agregando que Heracles
# derroto a varias;
# l. modifique el nombre de la criatura Ladón por Dragón Ladón;
# m. realizar un listado por nivel del árbol;
# n. muestre las criaturas capturadas por Heracles.

from arbol_avl import ArbolAVL

arbol_criaturas = ArbolAVL()

criaturas = [
    {"nombre": "Talos", "derrotado_por": ["Medea"], "capturada": None, "descripcion": ""},
    {"nombre": "Basilisco", "derrotado_por": [], "capturada": None, "descripcion": ""},
    {"nombre": "Cerbero", "derrotado_por": ["Heracles"], "capturada": None, "descripcion": ""},
    {"nombre": "Toro de Creta", "derrotado_por": ["Teseo"], "capturada": None, "descripcion": ""},
    {"nombre": "Aves del Estínfalo", "derrotado_por": ["Heracles"], "capturada": None, "descripcion": ""},
    {"nombre": "Ladón", "derrotado_por": ["Heracles"], "capturada": None, "descripcion": ""},
    {"nombre": "Sirenas", "derrotado_por": ["Odiseo"], "capturada": None, "descripcion": ""},
    {"nombre": "Cierva Cerinea", "derrotado_por": [], "capturada": None, "descripcion": ""},
    {"nombre": "Jabalí de Erimanto", "derrotado_por": ["Heracles"], "capturada": None, "descripcion": ""}
]

for criatura in criaturas:
    arbol_criaturas.insertar_nodo(criatura["nombre"], criatura)

print("Listado inorden de las criaturas y sus derrotadores:")
arbol_criaturas.inorden()

def agregar_descripcion(nombre_criatura, descripcion):
    nodo = arbol_criaturas.buscar(nombre_criatura)
    if nodo:
        nodo.otro_valor["descripcion"] = descripcion

print("\nInformación de la criatura Talos:")
nodo_talos = arbol_criaturas.buscar("Talos")
if nodo_talos:
    print(nodo_talos.otro_valor)

def top_derrotadores(arbol):
    derrotadores = {}
    def contar_derrotadores(nodo):
        if nodo:
            for heroe in nodo.otro_valor["derrotado_por"]:
                derrotadores[heroe] = derrotadores.get(heroe, 0) + 1
            contar_derrotadores(nodo.izquierdo)
            contar_derrotadores(nodo.derecho)
    contar_derrotadores(arbol.raiz)
    top_3 = sorted(derrotadores.items(), key=lambda x: x[1], reverse=True)[:3]
    return top_3

top_3_derrotadores = top_derrotadores(arbol_criaturas)
print("\nTop 3 héroes que derrotaron más criaturas:", top_3_derrotadores)

def criaturas_derrotadas_por(heroe, arbol):
    criaturas_derrotadas = []
    def buscar_criaturas(nodo):
        if nodo:
            if heroe in nodo.otro_valor["derrotado_por"]:
                criaturas_derrotadas.append(nodo.otro_valor["nombre"])
            buscar_criaturas(nodo.izquierdo)
            buscar_criaturas(nodo.derecho)
    buscar_criaturas(arbol.raiz)
    return criaturas_derrotadas

criaturas_heracles = criaturas_derrotadas_por("Heracles", arbol_criaturas)
print("\nCriaturas derrotadas por Heracles:", criaturas_heracles)

def criaturas_no_derrotadas(arbol):
    no_derrotadas = []
    def buscar_no_derrotadas(nodo):
        if nodo:
            if not nodo.otro_valor["derrotado_por"]:
                no_derrotadas.append(nodo.otro_valor["nombre"])
            buscar_no_derrotadas(nodo.izquierdo)
            buscar_no_derrotadas(nodo.derecho)
    buscar_no_derrotadas(arbol.raiz)
    return no_derrotadas

criaturas_no_vencidas = criaturas_no_derrotadas(arbol_criaturas)
print("\nCriaturas no derrotadas:", criaturas_no_vencidas)

for criatura in criaturas:
    arbol_criaturas.buscar(criatura["nombre"]).otro_valor["capturada"] = criatura["capturada"]

capturadas_por_heracles = ["Cerbero", "Toro de Creta", "Cierva Cerinea", "Jabalí de Erimanto"]
for criatura in capturadas_por_heracles:
    nodo = arbol_criaturas.buscar(criatura)
    if nodo:
        nodo.otro_valor["capturada"] = "Heracles"

print("\nBúsqueda por coincidencia ('Tor'):")
arbol_criaturas.busqueda_aproximada("Tor")

arbol_criaturas.eliminar_nodo("Basilisco")
arbol_criaturas.eliminar_nodo("Sirenas")

nodo_aves = arbol_criaturas.buscar("Aves del Estínfalo")
if nodo_aves:
    nodo_aves.otro_valor["derrotado_por"].append("Heracles derrotó a varias")

nodo_ladon = arbol_criaturas.buscar("Ladón")
if nodo_ladon:
    nodo_ladon.otro_valor["nombre"] = "Dragón Ladón"

print("\nListado por nivel del árbol:")
arbol_criaturas.por_nivel()

def criaturas_capturadas_por(heroe, arbol):
    capturadas = []
    def buscar_capturadas(nodo):
        if nodo:
            if nodo.otro_valor["capturada"] == heroe:
                capturadas.append(nodo.otro_valor["nombre"])
            buscar_capturadas(nodo.izquierdo)
            buscar_capturadas(nodo.derecho)
    buscar_capturadas(arbol.raiz)
    return capturadas

criaturas_capturadas_heracles = criaturas_capturadas_por("Heracles", arbol_criaturas)
print("\nCriaturas capturadas por Heracles:", criaturas_capturadas_heracles)
