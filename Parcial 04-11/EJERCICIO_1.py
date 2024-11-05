# Se tiene datos de los Pokémons de las 8 generaciones cargados de manera desordenada de los cuales se conoce su nombre, número, tipo/tipos para el cual debemos construir tres árboles para acceder de manera eficiente a los datos, contemplando lo siguiente: 
# a) los índices de cada uno de los árboles deben ser nombre, número y tipo; 
# b) mostrar todos los datos de un Pokémon a partir de su número y nombre –para este
# último, la búsqueda debe ser por proximidad, es decir si busco “bul” se deben mostrar todos los Pokémons cuyos nombres comiencen o contengan dichos caracteres–; 
# c) mostrar todos los nombres de todos los Pokémons de un determinado tipo agua, fuego, planta y eléctrico; 
# d) realizar un listado en orden ascendente por número y nombre de Pokémon, y además un listado por nivel por nombre; 
# e) mostrar todos los datos de los Pokémons: Jolteon, Lycanroc y Tyrantrum; 
# f) Determina cuantos Pokémons hay de tipo eléctrico y acero. 

from datos_pokemon import pokemones  
from arbol import ArbolBinario  
from arbol_avl import ArbolAVL  

#se crean los tres arboles
arbol_nombre = ArbolAVL()  
arbol_numero = ArbolBinario()
arbol_tipo = ArbolBinario()

# pto a. indice de los árboles
for pokemon in pokemones:   
    arbol_nombre.insertar_nodo(pokemon["nombre"], pokemon)  
    
    arbol_numero.insertar_nodo(pokemon["numero"], pokemon)
    
    for tipo in pokemon["tipos"]:
        arbol_tipo.insertar_nodo(tipo, pokemon)

# pto b. mostrar datos del pokemon a partir de su núm y nombre
def buscar_por_numero(numero):
    resultado = arbol_numero.buscar(numero)
    if resultado:
        print(f"b. Datos del Pokémon con número {numero}: {resultado.otro_valor}")
    else:
        print(f"b. Pokémon con número {numero} no encontrado.")

def buscar_por_nombre_proximidad(nombre_parcial):
    print(f"b. Resultados para búsqueda por proximidad '{nombre_parcial}':")
    arbol_nombre.busqueda_aproximada(nombre_parcial)

buscar_por_numero(135)  
buscar_por_nombre_proximidad("bul")

# pto c. mostrar nombres de pokemons de tipos específicos
def mostrar_pokemones_por_tipo(tipo):
    print(f"c. Pokémon de tipo {tipo}:")
    pokemones_encontrados = []

    def __mostrar_en_tipo(nodo, tipo):
        if nodo is not None:
            __mostrar_en_tipo(nodo.izquierdo, tipo)
            if tipo in nodo.otro_valor["tipos"]:
                pokemones_encontrados.append(f" - {nodo.otro_valor['nombre']} (#{nodo.otro_valor['numero']})")
            __mostrar_en_tipo(nodo.derecho, tipo)

    __mostrar_en_tipo(arbol_nombre.raiz, tipo)
    if pokemones_encontrados:
        print("\n".join(pokemones_encontrados))
    else:
        print(" No se encontraron Pokémon de este tipo.")

mostrar_pokemones_por_tipo("Agua")
mostrar_pokemones_por_tipo("Fuego")
mostrar_pokemones_por_tipo("Planta")
mostrar_pokemones_por_tipo("Eléctrico")

# pto d. listado en orden ascendente por número y nombre de Pokémon y por nivel por nombre
print("\nd. Listado:")

print("En orden ascendente por número:")
arbol_numero.inorden()

print("\nEn orden ascendente por nombre:")
arbol_nombre.inorden()

print("\nPor nivel por nombre:")
arbol_nombre.por_nivel()

# pto e. datos de Jolteon, Lycanroc y Tyrantrum
def mostrar_datos_pokemon_especifico(nombres):
    for nombre in nombres:
        resultado = arbol_nombre.buscar(nombre)
        if resultado:
            print(f"e. Datos de {nombre}: {resultado.otro_valor}")
        else:
            print(f"e. Pokémon {nombre} no encontrado.")

mostrar_datos_pokemon_especifico(["Jolteon", "Lycanroc", "Tyrantrum"])

# pto f. cuántos eléctricos y acero hay
def contar_por_tipo(tipo):
    contador = 0

    def contar_en_arbol(nodo):
        nonlocal contador
        if nodo is not None:
            if tipo in nodo.otro_valor["tipos"]:
                contador += 1
            contar_en_arbol(nodo.izquierdo)
            contar_en_arbol(nodo.derecho)
    
    contar_en_arbol(arbol_tipo.raiz)
    print(f"f. Cantidad de Pokémon de tipo {tipo}: {contador}")

contar_por_tipo("Eléctrico")
contar_por_tipo("Acero")