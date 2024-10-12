# Implementar una tabla hash para almacenar la información de todos los Jedi, de los cuales se
# conoce su nombre y quien fue su maestro –este último puede ser más de uno o desconocido–
# contemplando las siguientes requerimientos:
# a. la tabla debe ser de 15 posiciones;
# b. debe poder manejar las colisiones que se produzcan dependiendo del tipo
# de tabla utilizado;
# c. cargar al menos 30 Jedi;
# d. determinar si están cargados los Jedi: Yoda, Luke Skywalker y Ahsoka Tano.
# Si no están, agregarlos;
# e. crear una función que permita determinar el factor de carga de la tabla, dependiendo del
# tipo utilizado;
# f. mostrar toda la información de Ahsoka Tano, Obi-Wan Kenobi y Qui-Gon Jin;
# g. mostrar los maestros y aprendices (padawan) de Yoda y Luke Skywalker; los aprendices no
# son parte de la información, debe determinarlos a partir del campo maestro de cada Jedi.

# Definición de la Tabla Hash para los Jedi

class TablaHash:
    def __init__(self, tamano=15):
        self.tamano = tamano  # Tamaño de la tabla
        self.tabla = [[] for _ in range(tamano)]  # Inicializar la tabla con listas vacías (encadenamiento)

    def funcion_hash(self, clave):
        """Función hash para convertir la clave en un índice de la tabla."""
        return hash(clave) % self.tamano

    def insertar(self, clave, valor):
        """Inserta un elemento en la tabla hash."""
        indice = self.funcion_hash(clave)
        for i, (k, v) in enumerate(self.tabla[indice]):
            if k == clave:
                self.tabla[indice][i] = (clave, valor)  # Reemplazar si la clave ya existe
                return
        self.tabla[indice].append((clave, valor))  # Si no existe, agregarlo al final de la lista

    def buscar(self, clave):
        """Busca un elemento en la tabla hash y devuelve el valor."""
        indice = self.funcion_hash(clave)
        for k, v in self.tabla[indice]:
            if k == clave:
                return v
        return None

    def eliminar(self, clave):
        """Elimina un elemento de la tabla hash."""
        indice = self.funcion_hash(clave)
        for i, (k, v) in enumerate(self.tabla[indice]):
            if k == clave:
                del self.tabla[indice][i]
                return True
        return False

    def mostrar(self):
        """Muestra todos los elementos de la tabla hash."""
        for i, lista in enumerate(self.tabla):
            if lista:
                print(f"Índice {i}: {lista}")

    def factor_carga(self):
        """Calcula el factor de carga de la tabla hash."""
        elementos_totales = sum(len(lista) for lista in self.tabla)
        return elementos_totales / self.tamano


# Lista de Jedis para cargar en la tabla hash
jedis = [
    {'nombre': 'Luke Skywalker', 'maestros': ['Yoda', 'Obi-Wan']},
    {'nombre': 'Ahsoka Tano', 'maestros': ['Anakin Skywalker']},
    {'nombre': 'Kit Fisto', 'maestros': ['Yoda']},
    {'nombre': 'Yoda', 'maestros': []},
    {'nombre': 'Qui-Gon Jinn', 'maestros': ['Dooku']},
    {'nombre': 'Mace Windu', 'maestros': []},
    {'nombre': 'Obi-Wan Kenobi', 'maestros': ['Qui-Gon Jinn']},
    {'nombre': 'Anakin Skywalker', 'maestros': ['Obi-Wan Kenobi']},
    {'nombre': 'Leia Organa', 'maestros': ['Luke Skywalker']},
    {'nombre': 'Rey', 'maestros': ['Leia Organa', 'Luke Skywalker']},
    # Agregamos más Jedis para completar los 30
    {'nombre': 'Luminara Unduli', 'maestros': []},
    {'nombre': 'Barriss Offee', 'maestros': ['Luminara Unduli']},
    {'nombre': 'Plo Koon', 'maestros': []},
    {'nombre': 'Shaak Ti', 'maestros': []},
    {'nombre': 'Eeth Koth', 'maestros': []},
    {'nombre': 'Adi Gallia', 'maestros': []},
    {'nombre': 'Depa Billaba', 'maestros': ['Mace Windu']},
    {'nombre': 'Cere Junda', 'maestros': []},
    {'nombre': 'Cal Kestis', 'maestros': ['Cere Junda']},
    {'nombre': 'Aayla Secura', 'maestros': ['Quinlan Vos']},
    {'nombre': 'Quinlan Vos', 'maestros': []},
    {'nombre': 'Jocasta Nu', 'maestros': []},
    {'nombre': 'Stass Allie', 'maestros': []},
    {'nombre': 'Eeth Koth', 'maestros': []},
    {'nombre': 'Agen Kolar', 'maestros': []},
    {'nombre': 'Saesee Tiin', 'maestros': []},
    {'nombre': 'Yaddle', 'maestros': []},
    {'nombre': 'Even Piell', 'maestros': []},
    {'nombre': 'Oppo Rancisis', 'maestros': []},
    {'nombre': 'Coleman Trebor', 'maestros': []},
]

# Inicializar la tabla hash y cargar los Jedi
tabla_jedis = TablaHash()
for jedi in jedis:
    tabla_jedis.insertar(jedi['nombre'], jedi)

# d. Determinar si están cargados los Jedi Yoda, Luke Skywalker y Ahsoka Tano. Si no están, agregarlos.
for nombre in ['Yoda', 'Luke Skywalker', 'Ahsoka Tano']:
    if tabla_jedis.buscar(nombre) is None:
        print(f"{nombre} no estaba en la tabla. Agregándolo...")
        tabla_jedis.insertar(nombre, {'nombre': nombre, 'maestros': []})

# e. Calcular el factor de carga
print(f"Factor de carga: {tabla_jedis.factor_carga():.2f}")

# f. Mostrar la información de Ahsoka Tano, Obi-Wan Kenobi y Qui-Gon Jinn
for nombre in ['Ahsoka Tano', 'Obi-Wan Kenobi', 'Qui-Gon Jinn']:
    jedi = tabla_jedis.buscar(nombre)
    if jedi:
        print(f"Información de {nombre}: {jedi}")

# g. Mostrar maestros y aprendices de Yoda y Luke Skywalker
print("\nMaestros y aprendices de Yoda y Luke Skywalker:")
for nombre in ['Yoda', 'Luke Skywalker']:
    print(f"\nAprendices de {nombre}:")
    for jedi in jedis:
        if nombre in jedi['maestros']:
            print(f"- {jedi['nombre']}")
