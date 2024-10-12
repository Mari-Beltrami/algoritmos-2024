# Dado un árbol con los nombre de los superhéroes y villanos de la saga Marvel Cinematic Univer-
# se (MCU), desarrollar un algoritmo que contemple lo siguiente:
# a. además del nombre del superhéroe, en cada nodo del árbol se almacenará un campo boo-
# leano que indica si es un héroe o un villano, True y False respectivamente;
# b. listar los villanos ordenados alfabéticamente;
# c. mostrar todos los superhéroes que empiezan con C;
# d. determinar cuántos superhéroes hay el árbol;
# e. Doctor Strange en realidad está mal cargado. Utilice una búsqueda por proximidad para
# encontrarlo en el árbol y modificar su nombre;
# f. listar los superhéroes ordenados de manera descendente;
# g. generar un bosque a partir de este árbol, un árbol debe contener a los superhéroes y otro a
# los villanos, luego resolver las siguiente tareas:
# I. determinar cuántos nodos tiene cada árbol;
# II. realizar un barrido ordenado alfabéticamente de cada árbol.

# Implementación de un árbol binario para resolver el ejercicio sobre los superhéroes y villanos de MCU

class Nodo:
    def __init__(self, nombre, es_heroe):
        """Clase Nodo que representa cada elemento del árbol."""
        self.nombre = nombre  # Nombre del superhéroe o villano
        self.es_heroe = es_heroe  # Booleano: True si es héroe, False si es villano
        self.izquierdo = None  # Hijo izquierdo
        self.derecho = None  # Hijo derecho

class ArbolBinario:
    def __init__(self):
        """Clase que representa el árbol binario."""
        self.raiz = None  # Inicialmente el árbol está vacío

    def insertar(self, nombre, es_heroe):
        """Inserta un nodo en el árbol."""
        # Si el árbol está vacío, el nodo será la raíz
        if self.raiz is None:
            self.raiz = Nodo(nombre, es_heroe)
        else:
            self._insertar_recursivo(self.raiz, nombre, es_heroe)

    def _insertar_recursivo(self, nodo, nombre, es_heroe):
        """Inserta un nodo de manera recursiva en el árbol."""
        # Compara el nombre para decidir dónde insertar el nuevo nodo
        if nombre < nodo.nombre:
            if nodo.izquierdo is None:
                nodo.izquierdo = Nodo(nombre, es_heroe)
            else:
                self._insertar_recursivo(nodo.izquierdo, nombre, es_heroe)
        else:
            if nodo.derecho is None:
                nodo.derecho = Nodo(nombre, es_heroe)
            else:
                self._insertar_recursivo(nodo.derecho, nombre, es_heroe)

    def inorden_villanos(self, nodo):
        """Lista los villanos de manera ordenada alfabéticamente."""
        if nodo is not None:
            self.inorden_villanos(nodo.izquierdo)
            if not nodo.es_heroe:
                print(nodo.nombre)
            self.inorden_villanos(nodo.derecho)

    def listar_heroes_con_c(self, nodo):
        """Muestra todos los superhéroes cuyo nombre comienza con 'C'."""
        if nodo is not None:
            self.listar_heroes_con_c(nodo.izquierdo)
            if nodo.es_heroe and nodo.nombre.startswith('C'):
                print(nodo.nombre)
            self.listar_heroes_con_c(nodo.derecho)

    def contar_heroes(self, nodo):
        """Cuenta cuántos superhéroes hay en el árbol."""
        if nodo is None:
            return 0
        else:
            cuenta = 1 if nodo.es_heroe else 0
            return cuenta + self.contar_heroes(nodo.izquierdo) + self.contar_heroes(nodo.derecho)

    def buscar_y_modificar(self, nodo, nombre_actual, nombre_nuevo):
        """Busca un nodo por proximidad y modifica su nombre si lo encuentra."""
        if nodo is not None:
            if nombre_actual.lower() in nodo.nombre.lower():
                nodo.nombre = nombre_nuevo
                return True
            return self.buscar_y_modificar(nodo.izquierdo, nombre_actual, nombre_nuevo) or \
                   self.buscar_y_modificar(nodo.derecho, nombre_actual, nombre_nuevo)
        return False

    def inorden_heroes_descendente(self, nodo):
        """Lista los superhéroes de manera descendente."""
        if nodo is not None:
            self.inorden_heroes_descendente(nodo.derecho)
            if nodo.es_heroe:
                print(nodo.nombre)
            self.inorden_heroes_descendente(nodo.izquierdo)

    def generar_bosque(self, nodo, arbol_heroes, arbol_villanos):
        """Genera un bosque dividiendo los héroes y villanos en dos árboles separados."""
        if nodo is not None:
            if nodo.es_heroe:
                arbol_heroes.insertar(nodo.nombre, nodo.es_heroe)
            else:
                arbol_villanos.insertar(nodo.nombre, nodo.es_heroe)
            self.generar_bosque(nodo.izquierdo, arbol_heroes, arbol_villanos)
            self.generar_bosque(nodo.derecho, arbol_heroes, arbol_villanos)

    def contar_nodos(self, nodo):
        """Cuenta cuántos nodos tiene el árbol."""
        if nodo is None:
            return 0
        return 1 + self.contar_nodos(nodo.izquierdo) + self.contar_nodos(nodo.derecho)

# Crear el árbol binario y cargar los datos de los personajes MCU
arbol = ArbolBinario()
arbol.insertar('Iron Man', True)
arbol.insertar('Doctor Strange', True)
arbol.insertar('Thanos', False)
arbol.insertar('Captain America', True)
arbol.insertar('Red Skull', False)
arbol.insertar('Thor', True)
arbol.insertar('Loki', False)
arbol.insertar('Hulk', True)
arbol.insertar('Ultron', False)
arbol.insertar('Black Widow', True)

# a. Listar los villanos ordenados alfabéticamente
print("Villanos ordenados alfabéticamente:")
arbol.inorden_villanos(arbol.raiz)

# b. Mostrar todos los superhéroes que empiezan con 'C'
print("\nSuperhéroes que comienzan con 'C':")
arbol.listar_heroes_con_c(arbol.raiz)

# c. Determinar cuántos superhéroes hay en el árbol
cantidad_heroes = arbol.contar_heroes(arbol.raiz)
print(f"\nCantidad de superhéroes en el árbol: {cantidad_heroes}")

# d. Modificar el nombre de Doctor Strange usando una búsqueda por proximidad
print("\nModificando 'Doctor Strange' a 'Doctor Stephen Strange'...")
arbol.buscar_y_modificar(arbol.raiz, 'Doctor Strange', 'Doctor Stephen Strange')

# e. Listar los superhéroes ordenados de manera descendente
print("\nSuperhéroes ordenados de manera descendente:")
arbol.inorden_heroes_descendente(arbol.raiz)

# f. Generar un bosque (dos árboles: héroes y villanos)
arbol_heroes = ArbolBinario()
arbol_villanos = ArbolBinario()
arbol.generar_bosque(arbol.raiz, arbol_heroes, arbol_villanos)

# f.I. Determinar cuántos nodos tiene cada árbol
print(f"\nCantidad de nodos en el árbol de héroes: {arbol_heroes.contar_nodos(arbol_heroes.raiz)}")
print(f"Cantidad de nodos en el árbol de villanos: {arbol_villanos.contar_nodos(arbol_villanos.raiz)}")

# f.II. Barrido ordenado alfabéticamente de cada árbol
print("\nHéroes ordenados alfabéticamente:")
arbol_heroes.inorden_villanos(arbol_heroes.raiz)
print("\nVillanos ordenados alfabéticamente:")
arbol_villanos.inorden_villanos(arbol_villanos.raiz)