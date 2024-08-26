""" Dada una pila de personajes de Marvel Cinematic Universe (MCU), de los cuales se dispone de su nombre y la cantidad de películas de la saga en la que participó, implementar las funciones necesarias para resolver las siguientes actividades:
a. determinar en qué posición se encuentran Rocket Raccoon y Groot, tomando como posición uno la cima de la pila;
b. determinar los personajes que participaron en más de 5 películas de la saga, además indicar la cantidad de películas en la que aparece;
c. determinar en cuantas películas participo la Viuda Negra (Black Widow);
d. mostrar todos los personajes cuyos nombre empiezan con C, D y G. """

from pila import Stack

def encontrar_posiciones(stack, nombres):
    temp_stack = Stack()
    posiciones = {}
    posicion = 1

    while stack.size() > 0:
        personaje = stack.pop()
        temp_stack.push(personaje)
        if personaje["nombre"] in nombres:
            posiciones[personaje["nombre"]] = posicion
        posicion += 1

    while temp_stack.size() > 0:
        stack.push(temp_stack.pop())

    return posiciones
def mas_de_5_peliculas(stack):
    temp_stack = Stack()
    resultado = []

    while stack.size() > 0:
        personaje = stack.pop()
        temp_stack.push(personaje)
        if personaje["peliculas"] > 5:
            resultado.append((personaje["nombre"], personaje["peliculas"]))

    while temp_stack.size() > 0:
        stack.push(temp_stack.pop())

    return resultado
def black_widow_peliculas(stack):
    temp_stack = Stack()
    black_widow_contador = 0

    while stack.size() > 0:
        personaje = stack.pop()
        temp_stack.push(personaje)
        if personaje["nombre"] == "Black Widow":
            black_widow_contador = personaje["peliculas"]

    while temp_stack.size() > 0:
        stack.push(temp_stack.pop())

    return black_widow_contador
def personajes_comienzan_con(stack, iniciales):
    temp_stack = Stack()
    resultado = []

    while stack.size() > 0:
        personaje = stack.pop()
        temp_stack.push(personaje)
        if personaje["nombre"][0] in iniciales:
            resultado.append(personaje["nombre"])

    while temp_stack.size() > 0:
        stack.push(temp_stack.pop())

    return resultado
MCU_stack = Stack()
MCU_stack.push({"nombre": "Iron Man", "peliculas": 10})
MCU_stack.push({"nombre": "Captain America", "peliculas": 9})
MCU_stack.push({"nombre": "Rocket Raccoon", "peliculas": 5})
MCU_stack.push({"nombre": "Groot", "peliculas": 4})
MCU_stack.push({"nombre": "Black Widow", "peliculas": 7})
MCU_stack.push({"nombre": "Doctor Strange", "peliculas": 3})

# a. Determinar en qué posición se encuentran Rocket Raccoon y Groot
posiciones = encontrar_posiciones(MCU_stack, ["Rocket Raccoon", "Groot"])
print("Posiciones:", posiciones)

# b. Determinar los personajes que participaron en más de 5 películas
mas_de_5 = mas_de_5_peliculas(MCU_stack)
print("Personajes en más de 5 películas:", mas_de_5)

# c. Determinar en cuántas películas participó Black Widow
black_widow_contador = black_widow_peliculas(MCU_stack)
print("Black Widow participó en", black_widow_contador, "películas")

# d. Mostrar todos los personajes cuyos nombres empiezan con C, D y G
caracteres_c_d_g = personajes_comienzan_con(MCU_stack, {'C', 'D', 'G'})
print("Personajes que empiezan con C, D, G:", caracteres_c_d_g)