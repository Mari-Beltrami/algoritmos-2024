"""Escribir un algoritmo que permita utilizar tres tablas hash para guardar los datos de Pokémons,
que contemple las siguientes actividades: 
a. en la primera tabla hash la función hash debe ser sobre el tipo de Pokémon, en la segunda
tabla la función hash deberá utilizar el ultimo dígito del número del Pokémon como clave y la tercera sera en base  a su nivel repartiéndolos en 10 posiciones dentro de la tabla; 
b. debe utilizar tablas hash abiertas con listas como estructura secundaria;
c. si el Pokémon es de más de un tipo deberá cargarlo en cada uno de las tabla que indiquen estos tipos;
d. deberá permitir cargar Pokémons de los cuales se dispone de su número, nombre, tipo/s, nivel.
e. mostrar todos los Pokémons cuyos numeros terminan en 3, 7 y 9;
f. mostrar todos los Pokémons cuyos niveles son multiplos de 2, 5 y 10;
g. mostrar todos los Pokémons de los siguientes tipo: Acero, Fuego, Electrifico, Hielo"""

class Nodo:
    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None

class HashTable:
    def __init__(self, size):
        self.size = size
        self.table = [None] * size

    def insertar(self, key, dato):
        index = key % self.size
        if not self.table[index]:
            self.table[index] = Nodo(dato)
        else:
            current = self.table[index]
            while current.siguiente:
                current = current.siguiente
            current.siguiente = Nodo(dato)

    def buscar(self, key):
        index = key % self.size
        current = self.table[index]
        result = []
        while current:
            if key == current.dato['numero'] % self.size:
                result.append(current.dato)
            current = current.siguiente
        return result

    def mostrar_todos(self, condition):
        result = []
        for bucket in self.table:
            current = bucket
            while current:
                if condition(current.dato):
                    result.append(current.dato)
                current = current.siguiente
        return result

def hash_tipo(tipo):
    return sum(ord(c) for c in tipo) % 10

def hash_numero(numero):
    return numero % 10

def hash_nivel(nivel):
    return nivel // 10

tabla_tipo = HashTable(10)
tabla_numero = HashTable(10)
tabla_nivel = HashTable(10)

def ingresar_datos():
    pokemons = []
    while True:
        numero = int(input("Ingrese el número del Pokémon (o -1 para terminar): "))
        if numero == -1:
            break
        nombre = input("Ingrese el nombre del Pokémon: ")
        tipos = input("Ingrese los tipos de Pokémon separados por coma: ").split(',')
        nivel = int(input("Ingrese el nivel del Pokémon: "))
        pokemons.append({'numero': numero, 'nombre': nombre, 'tipos': tipos, 'nivel': nivel})
    return pokemons

pokemons = ingresar_datos()
for pokemon in pokemons:
    for tipo in pokemon['tipos']:
        tabla_tipo.insertar(hash_tipo(tipo.strip()), pokemon)
    tabla_numero.insertar(hash_numero(pokemon['numero']), pokemon)
    tabla_nivel.insertar(hash_nivel(pokemon['nivel']), pokemon)

numeros_terminan_3_7_9 = tabla_numero.mostrar_todos(lambda p: p['numero'] % 10 in [3, 7, 9])
print("Pokémons cuyos números terminan en 3, 7 y 9:", numeros_terminan_3_7_9)

niveles_multiplos_2_5_10 = tabla_nivel.mostrar_todos(lambda p: p['nivel'] % 2 == 0 or p['nivel'] % 5 == 0)
print("Pokémons cuyos niveles son múltiplos de 2, 5 y 10:", niveles_multiplos_2_5_10)

tipos_especificos = ['Acero', 'Fuego', 'Eléctrico', 'Hielo']
pokemons_tipos_especificos = []
for tipo in tipos_especificos:
    pokemons_tipos_especificos.extend(tabla_tipo.mostrar_todos(lambda p: tipo in p['tipos']))
print("Pokémons de tipos específicos (Acero, Fuego, Eléctrico, Hielo):", pokemons_tipos_especificos)




print ()

