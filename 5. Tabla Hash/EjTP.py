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

class TablaHash:
    def __init__(self, tamaño):
        self.tamaño = tamaño
        self.tabla = [None] * tamaño

    def insertar(self, clave, dato):
        indice = clave % self.tamaño
        if not self.tabla[indice]:
            self.tabla[indice] = Nodo(dato)
        else:
            actual = self.tabla[indice]
            while actual.siguiente:
                actual = actual.siguiente
            actual.siguiente = Nodo(dato)

    def buscar(self, clave):
        indice = clave % self.tamaño
        actual = self.tabla[indice]
        resultado = []  
        while actual:
            if clave == actual.dato['numero'] % self.tamaño:
                resultado.append(actual.dato)
            actual = actual.siguiente
        return resultado

    def mostrar_todos(self, condicion):
        resultado = []  
        for cubeta in self.tabla:
            actual = cubeta
            while actual:
                if condicion(actual.dato):
                    resultado.append(actual.dato)
                actual = actual.siguiente
        return resultado

def hash_tipo(tipo):
    return sum(ord(c) for c in tipo) % 10  

def hash_numero(numero):
    return numero % 10  

def hash_nivel(nivel):
    return nivel // 10  

tabla_tipo = TablaHash(10)
tabla_numero = TablaHash(10)
tabla_nivel = TablaHash(10)

def ingresar_datos():
    pokemones = []  
    while True:
        numero = int(input("Ingrese el número del Pokémon (o -1 para terminar): "))
        if numero == -1:
            break  
        nombre = input("Ingrese el nombre del Pokémon: ")  
        tipos = input("Ingrese los tipos de Pokémon separados por coma: ").split(',')
        nivel = int(input("Ingrese el nivel del Pokémon: "))  
        pokemones.append({'numero': numero, 'nombre': nombre, 'tipos': tipos, 'nivel': nivel})
    return pokemones  

pokemones = ingresar_datos()

for pokemon in pokemones:
    for tipo in pokemon['tipos']:
        tabla_tipo.insertar(hash_tipo(tipo.strip()), pokemon)
    tabla_numero.insertar(hash_numero(pokemon['numero']), pokemon)
    tabla_nivel.insertar(hash_nivel(pokemon['nivel']), pokemon)

numeros_terminan_3_7_9 = tabla_numero.mostrar_todos(lambda p: p['numero'] % 10 in [3, 7, 9])
print("Pokémons cuyos números terminan en 3, 7 y 9:", numeros_terminan_3_7_9)

niveles_multiplos_2_5_10 = tabla_nivel.mostrar_todos(lambda p: p['nivel'] % 2 == 0 or p['nivel'] % 5 == 0)
print("Pokémons cuyos niveles son múltiplos de 2, 5 y 10:", niveles_multiplos_2_5_10)

tipos_especificos = ['Acero', 'Fuego', 'Eléctrico', 'Hielo']
pokemones_tipos_especificos = []

for tipo in tipos_especificos:
    pokemones_tipos_especificos.extend(tabla_tipo.mostrar_todos(lambda p: tipo in p['tipos']))
print("Pokémons de tipos específicos (Acero, Fuego, Eléctrico, Hielo):", pokemones_tipos_especificos)

print()  

