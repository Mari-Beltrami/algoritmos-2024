"""Dada una lista de superhéroes de comics, de los cuales se conoce su nombre, año aparición,
casa de comic a la que pertenece (Marvel o DC) y biografía, implementar la funciones necesa-
rias para poder realizar las siguientes actividades:
a. eliminar el nodo que contiene la información de Linterna Verde;
b. mostrar el año de aparición de Wolverine;
c. cambiar la casa de Dr. Strange a Marvel;
d. mostrar el nombre de aquellos superhéroes que en su biografía menciona la palabra
“traje” o “armadura”;
e. mostrar el nombre y la casa de los superhéroes cuya fecha de aparición
sea anterior a 1963;
f. mostrar la casa a la que pertenece Capitana Marvel y Mujer Maravilla;
g. mostrar toda la información de Flash y Star-Lord;
h. listar los superhéroes que comienzan con la letra B, M y S;
i. determinar cuántos superhéroes hay de cada casa de comic."""

from lista import remove, search, show_list
from lista_superheroes import super_heroes

def eliminar_superheroe(lista, nombre):
    remove(lista, 'nombre', nombre)

def mostrar_anio_aparicion(lista, nombre):
    index = search(lista, 'nombre', nombre)
    if index is not None:
        print(f"Año de aparición de {nombre}: {lista[index]['año_aparicion']}")

def cambiar_casa(lista, nombre, nueva_casa):
    index = search(lista, 'nombre', nombre)
    if index is not None:
        lista[index]['casa'] = nueva_casa

def mostrar_superheroes_con_palabras(lista, palabras):
    for super_heroes in lista:
        if any(palabra in super_heroes['biografia'] for palabra in palabras):
            print(f"Superhéroe con {' o '.join(palabras)} en su biografía: {super_heroes['nombre']}")

def mostrar_heroes_anteriores_a(lista, anio):
    for super_heroes in lista:
        if super_heroes['año_aparicion'] < anio:
            print(f"Superhéroe anterior a {anio}: {super_heroes['nombre']}, Casa: {super_heroes['casa_comic']}")

def mostrar_casa_heroes(lista, nombres):
    for nombre in nombres:
        index = search(lista, 'nombre', nombre)
        if index is not None:
            print(f"Casa de {nombre}: {lista[index]['casa_comic']}")

def mostrar_info_heroes(lista, nombres):
    for nombre in nombres:
        index = search(lista, 'nombre', nombre)
        if index is not None:
            info = lista[index]
            print(f"Información de {nombre}: Nombre: {info['nombre']}, Año: {info['año_aparicion']}, Casa: {info['casa_comic']}, Biografía: {info['biografia']}")

def listar_heroes_por_letra(lista, letras):
    for superheroe in lista:
        if superheroe['nombre'][0] in letras:
            print(f"Superhéroe que comienza con {', '.join(letras)}: {superheroe['nombre']}")

def contar_heroes_por_casa(lista):
    marvel_count = 0
    dc_count = 0
    for super_heroes in lista:
        if super_heroes['casa_comic'] == "Marvel":
            marvel_count += 1
        elif super_heroes['casa_comic'] == "DC":
            dc_count += 1
    print(f"Cantidad de superhéroes de Marvel: {marvel_count}")
    print(f"Cantidad de superhéroes de DC: {dc_count}")

eliminar_superheroe(super_heroes, "Linterna Verde")
mostrar_anio_aparicion(super_heroes, "Wolverine")
cambiar_casa(super_heroes, "Dr. Strange", "Marvel")
mostrar_superheroes_con_palabras(super_heroes, ["traje", "armadura"])
mostrar_heroes_anteriores_a(super_heroes, 1963)
mostrar_casa_heroes(super_heroes, ["Capitana Marvel", "Mujer Maravilla"])
mostrar_info_heroes(super_heroes, ["Flash", "Star-Lord"])
listar_heroes_por_letra(super_heroes, ["B", "M", "S"])
contar_heroes_por_casa(super_heroes)

show_list("Lista de Superhéroes", super_heroes)
