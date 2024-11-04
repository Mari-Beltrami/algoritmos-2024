"""Se cuenta con una lista de entrenadores Pokémon. De cada uno de estos se conoce: nombre, can-
tidad de torneos ganados, cantidad de batallas perdidas y cantidad de batallas ganadas. Y ade-
más la lista de sus Pokémons, de los cuales se sabe: nombre, nivel, tipo y subtipo. Se pide resolver
las siguientes actividades utilizando lista de lista implementando las funciones necesarias:
a. obtener la cantidad de Pokémons de un determinado entrenador;
b. listar los entrenadores que hayan ganado más de tres torneos;
c. el Pokémon de mayor nivel del entrenador con mayor cantidad de torneos ganados;
d. mostrar todos los datos de un entrenador y sus Pokémos;
e. mostrar los entrenadores cuyo porcentaje de batallas ganados sea mayor al 79 %;
f. los entrenadores que tengan Pokémons de tipo fuego y planta o agua/volador
(tipo y subtipo);
g. el promedio de nivel de los Pokémons de un determinado entrenador;
h. determinar cuántos entrenadores tienen a un determinado Pokémon;
i. mostrar los entrenadores que tienen Pokémons repetidos;
j. determinar los entrenadores que tengan uno de los siguientes Pokémons: Tyrantrum, Te-
rrakion o Wingull;
k. determinar si un entrenador “X” tiene al Pokémon “Y”, tanto el nombre del entrenador
como del Pokémon deben ser ingresados; además si el entrenador tiene al Pokémon se
deberán mostrar los datos de ambos;"""

import random
from lista import remove, search, show_list
from entrenadores_pokemon import entrenadores
from pokemones import pokemons

def asignar_pokemons_aleatorios(entrenadores, pokemons, min_pokemons=1, max_pokemons=3):
    for entrenador in entrenadores:
        num_pokemons = random.randint(min_pokemons, max_pokemons)
        entrenador['pokemons'] = random.sample(pokemons, num_pokemons)

asignar_pokemons_aleatorios(entrenadores, pokemons)

def cantidad_pokemons_de_entrenador(lista, nombre_entrenador):
    index = search(lista, 'nombre', nombre_entrenador)
    if index is not None:
        if 'pokemons' in lista[index]:
            cantidad_pokemons = len(lista[index]['pokemons'])
            print(f"Cantidad de Pokémons de {nombre_entrenador}: {cantidad_pokemons}")
        else:
            print(f"{nombre_entrenador} no tiene Pokémons.")
    else:
        print(f"Entrenador {nombre_entrenador} no encontrado.")

def listar_entrenadores_mas_de_tres_torneos(lista):
    for entrenador in lista:
        if entrenador['torneos_ganados'] > 3:
            print(f"Entrenador con más de 3 torneos ganados: {entrenador['nombre']}")

def obtener_entrenador_con_mas_torneos(lista):
    if not lista:
        return None
    mejor_entrenador = lista[0]
    for entrenador in lista[1:]:
        if entrenador['torneos_ganados'] > mejor_entrenador['torneos_ganados']:
            mejor_entrenador = entrenador
    return mejor_entrenador

def obtener_pokemon_de_mayor_nivel(pokemons):
    if not pokemons:
        return None
    mejor_pokemon = pokemons[0]
    for pokemon in pokemons[1:]:
        if pokemon['nivel'] > mejor_pokemon['nivel']:
            mejor_pokemon = pokemon
    return mejor_pokemon

def pokemon_mayor_nivel_del_mejor_entrenador(lista):
    mejor_entrenador = obtener_entrenador_con_mas_torneos(lista)
    if mejor_entrenador:
        if 'pokemons' in mejor_entrenador:
            mejor_pokemon = obtener_pokemon_de_mayor_nivel(mejor_entrenador['pokemons'])
            if mejor_pokemon:
                print(f"Pokémon de mayor nivel de {mejor_entrenador['nombre']}: {mejor_pokemon['nombre']}, Nivel: {mejor_pokemon['nivel']}")
            else:
                print(f"{mejor_entrenador['nombre']} no tiene Pokémons.")
        else:
            print(f"{mejor_entrenador['nombre']} no tiene Pokémons.")
    else:
        print("No hay entrenadores en la lista.")

def mostrar_datos_entrenador(lista, nombre_entrenador):
    index = search(lista, 'nombre', nombre_entrenador)
    if index is not None:
        entrenador = lista[index]
        print(f"Datos del entrenador {nombre_entrenador}:")
        print(entrenador)
        if 'pokemons' in entrenador:
            print("Pokémons:")
            for pokemon in entrenador['pokemons']:
                print(pokemon)
        else:
            print(f"{nombre_entrenador} no tiene Pokémons.")
    else:
        print(f"Entrenador {nombre_entrenador} no encontrado.")

def entrenadores_con_porcentaje_batallas(lista, porcentaje):
    for entrenador in lista:
        batallas_totales = entrenador['batallas_ganadas'] + entrenador['batallas_perdidas']
        if batallas_totales > 0:
            porcentaje_ganadas = (entrenador['batallas_ganadas'] / batallas_totales) * 100
            if porcentaje_ganadas > porcentaje:
                print(f"Entrenador con más del {porcentaje}% de batallas ganadas: {entrenador['nombre']}")

def entrenadores_con_pokemons_tipo(lista, tipos):
    for entrenador in lista:
        if 'pokemons' in entrenador:
            for pokemon in entrenador['pokemons']:
                if (pokemon['tipo'], pokemon['subtipo']) in tipos:
                    print(f"Entrenador con Pokémon de tipo {pokemon['tipo']} y subtipo {pokemon['subtipo']}: {entrenador['nombre']}")
                    break

def promedio_nivel_pokemons(lista, nombre_entrenador):
    index = search(lista, 'nombre', nombre_entrenador)
    if index is not None:
        if 'pokemons' in lista[index]:
            pokemons = lista[index]['pokemons']
            if pokemons:
                promedio_nivel = sum(pokemon['nivel'] for pokemon in pokemons) / len(pokemons)
                print(f"Promedio de nivel de los Pokémons de {nombre_entrenador}: {promedio_nivel:.2f}")
            else:
                print(f"{nombre_entrenador} no tiene Pokémons.")
        else:
            print(f"{nombre_entrenador} no tiene Pokémons.")
    else:
        print(f"Entrenador {nombre_entrenador} no encontrado.")

def entrenadores_con_pokemon(lista, nombre_pokemon):
    contador = 0
    for entrenador in lista:
        if 'pokemons' in entrenador:
            for pokemon in entrenador['pokemons']:
                if pokemon['nombre'] == nombre_pokemon:
                    contador += 1
                    break
    print(f"Cantidad de entrenadores con el Pokémon {nombre_pokemon}: {contador}")

def entrenadores_con_pokemons_repetidos(lista):
    for entrenador in lista:
        if 'pokemons' in entrenador:
            nombres_pokemons = [pokemon['nombre'] for pokemon in entrenador['pokemons']]
            if len(nombres_pokemons) != len(set(nombres_pokemons)):
                print(f"Entrenador con Pokémons repetidos: {entrenador['nombre']}")

def entrenadores_con_pokemons_especificos(lista, nombres_pokemons):
    for entrenador in lista:
        if 'pokemons' in entrenador:
            for pokemon in entrenador['pokemons']:
                if pokemon['nombre'] in nombres_pokemons:
                    print(f"Entrenador con uno de los Pokémons específicos ({', '.join(nombres_pokemons)}): {entrenador['nombre']}")
                    break

def entrenador_con_pokemon(lista, nombre_entrenador, nombre_pokemon):
    index = search(lista, 'nombre', nombre_entrenador)
    if index is not None:
        entrenador = lista[index]
        if 'pokemons' in entrenador:
            for pokemon in entrenador['pokemons']:
                if pokemon['nombre'] == nombre_pokemon:
                    print(f"Entrenador {nombre_entrenador} tiene al Pokémon {nombre_pokemon}.")
                    print(f"Datos del entrenador: {entrenador}")
                    print(f"Datos del Pokémon: {pokemon}")
                    return
            print(f"Entrenador {nombre_entrenador} no tiene al Pokémon {nombre_pokemon}.")
        else:
            print(f"{nombre_entrenador} no tiene Pokémons.")
    else:
        print(f"Entrenador {nombre_entrenador} no encontrado.")

cantidad_pokemons_de_entrenador(entrenadores, "Ash Ketchum")
listar_entrenadores_mas_de_tres_torneos(entrenadores)
pokemon_mayor_nivel_del_mejor_entrenador(entrenadores)
mostrar_datos_entrenador(entrenadores, "Misty")
entrenadores_con_porcentaje_batallas(entrenadores, 79)
entrenadores_con_pokemons_tipo(entrenadores, [("Fuego", "Planta"), ("Agua", "Volador")])
promedio_nivel_pokemons(entrenadores, "Brock")
entrenadores_con_pokemon(entrenadores, "Pikachu")
entrenadores_con_pokemons_repetidos(entrenadores)
entrenadores_con_pokemons_especificos(entrenadores, ["Charmander", "Bulbasaur", "Squirtle"])
entrenador_con_pokemon(entrenadores, "Ash Ketchum", "Pikachu")