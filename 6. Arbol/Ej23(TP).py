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

# Implementación de un árbol binario para resolver el ejercicio sobre criaturas mitológicas

class Nodo:
    def __init__(self, nombre, derrotado_por=None):
        """Clase Nodo que representa cada criatura del árbol."""
        self.nombre = nombre  # Nombre de la criatura
        self.derrotado_por = derrotado_por  # Nombre del héroe o dios que la derrotó
        self.capturada = None  # Nombre del héroe o dios que la capturó
        self.descripcion = ""  # Breve descripción de la criatura
        self.izquierdo = None  # Hijo izquierdo
        self.derecho = None  # Hijo derecho

class ArbolBinario:
    def __init__(self):
        """Clase que representa el árbol binario."""
        self.raiz = None  # Inicialmente el árbol está vacío

    def insertar(self, nombre, derrotado_por=None):
        """Inserta un nodo en el árbol."""
        if self.raiz is None:
            self.raiz = Nodo(nombre, derrotado_por)
        else:
            self._insertar_recursivo(self.raiz, nombre, derrotado_por)

    def _insertar_recursivo(self, nodo, nombre, derrotado_por):
        """Inserta un nodo de manera recursiva en el árbol."""
        if nombre < nodo.nombre:
            if nodo.izquierdo is None:
                nodo.izquierdo = Nodo(nombre, derrotado_por)
            else:
                self._insertar_recursivo(nodo.izquierdo, nombre, derrotado_por)
        else:
            if nodo.derecho is None:
                nodo.derecho = Nodo(nombre, derrotado_por)
            else:
                self._insertar_recursivo(nodo.derecho, nombre, derrotado_por)

    def inorden(self, nodo):
        """Recorrido inorden del árbol para listar las criaturas y sus derrotadores."""
        if nodo is not None:
            self.inorden(nodo.izquierdo)
            print(f"Criatura: {nodo.nombre}, Derrotado por: {nodo.derrotado_por}")
            self.inorden(nodo.derecho)

    def cargar_descripcion(self, nombre, descripcion):
        """Carga una breve descripción sobre una criatura específica."""
        nodo = self.buscar(self.raiz, nombre)
        if nodo:
            nodo.descripcion = descripcion

    def buscar(self, nodo, nombre):
        """Busca un nodo específico en el árbol."""
        if nodo is None or nodo.nombre == nombre:
            return nodo
        elif nombre < nodo.nombre:
            return self.buscar(nodo.izquierdo, nombre)
        else:
            return self.buscar(nodo.derecho, nombre)

    def mostrar_informacion(self, nombre):
        """Muestra toda la información de una criatura específica."""
        nodo = self.buscar(self.raiz, nombre)
        if nodo:
            print(f"Nombre: {nodo.nombre}, Derrotado por: {nodo.derrotado_por}, Capturado por: {nodo.capturada}, Descripción: {nodo.descripcion}")
        else:
            print(f"La criatura {nombre} no se encuentra en el árbol.")

    def contar_derrotas(self):
        """Cuenta cuántas criaturas ha derrotado cada héroe o dios."""
        conteo = {}
        self._contar_derrotas_recursivo(self.raiz, conteo)
        return sorted(conteo.items(), key=lambda x: x[1], reverse=True)[:3]

    def _contar_derrotas_recursivo(self, nodo, conteo):
        if nodo is not None:
            if nodo.derrotado_por:
                if nodo.derrotado_por in conteo:
                    conteo[nodo.derrotado_por] += 1
                else:
                    conteo[nodo.derrotado_por] = 1
            self._contar_derrotas_recursivo(nodo.izquierdo, conteo)
            self._contar_derrotas_recursivo(nodo.derecho, conteo)

    def listar_criaturas_derrotadas_por(self, heroe):
        """Lista las criaturas derrotadas por un héroe específico."""
        self._listar_derrotadas_recursivo(self.raiz, heroe)

    def _listar_derrotadas_recursivo(self, nodo, heroe):
        if nodo is not None:
            if nodo.derrotado_por == heroe:
                print(nodo.nombre)
            self._listar_derrotadas_recursivo(nodo.izquierdo, heroe)
            self._listar_derrotadas_recursivo(nodo.derecho, heroe)

    def listar_criaturas_no_derrotadas(self):
        """Lista las criaturas que no han sido derrotadas."""
        self._listar_no_derrotadas_recursivo(self.raiz)

    def _listar_no_derrotadas_recursivo(self, nodo):
        if nodo is not None:
            if nodo.derrotado_por is None:
                print(nodo.nombre)
            self._listar_no_derrotadas_recursivo(nodo.izquierdo)
            self._listar_no_derrotadas_recursivo(nodo.derecho)

    def modificar_captura(self, nombre, capturado_por):
        """Modifica el campo capturado por de un nodo específico."""
        nodo = self.buscar(self.raiz, nombre)
        if nodo:
            nodo.capturada = capturado_por

    def modificar_nombre(self, nombre_actual, nombre_nuevo):
        """Modifica el nombre de una criatura."""
        nodo = self.buscar(self.raiz, nombre_actual)
        if nodo:
            nodo.nombre = nombre_nuevo

    def eliminar(self, nombre):
        """Elimina un nodo del árbol."""
        self.raiz = self._eliminar_recursivo(self.raiz, nombre)

    def _eliminar_recursivo(self, nodo, nombre):
        if nodo is None:
            return nodo
        if nombre < nodo.nombre:
            nodo.izquierdo = self._eliminar_recursivo(nodo.izquierdo, nombre)
        elif nombre > nodo.nombre:
            nodo.derecho = self._eliminar_recursivo(nodo.derecho, nombre)
        else:
            if nodo.izquierdo is None:
                return nodo.derecho
            elif nodo.derecho is None:
                return nodo.izquierdo
            temp = self._min_value_node(nodo.derecho)
            nodo.nombre = temp.nombre
            nodo.derrotado_por = temp.derrotado_por
            nodo.capturada = temp.capturada
            nodo.descripcion = temp.descripcion
            nodo.derecho = self._eliminar_recursivo(nodo.derecho, temp.nombre)
        return nodo

    def _min_value_node(self, nodo):
        actual = nodo
        while actual.izquierdo is not None:
            actual = actual.izquierdo
        return actual

    def recorrido_por_niveles(self):
        """Realiza un recorrido por niveles del árbol."""
        if self.raiz is None:
            return
        cola = [self.raiz]
        while cola:
            nodo = cola.pop(0)
            print(f"Criatura: {nodo.nombre}, Derrotado por: {nodo.derrotado_por}, Capturado por: {nodo.capturada}")
            if nodo.izquierdo:
                cola.append(nodo.izquierdo)
            if nodo.derecho:
                cola.append(nodo.derecho)

# Crear el árbol binario y cargar los datos de las criaturas
arbol = ArbolBinario()
criaturas = [
    ('Ceto', None), ('Tifón', 'Zeus'), ('Equidna', 'Argos Panoptes'),
    ('Dino', None), ('Pefredo', None), ('Enio', None),
    ('Escila', None), ('Caribdis', None), ('Euríale', 'Átropos'),
    ('Medusa', 'Perseo'), ('Ladón', 'Heracles'), ('Quimera', 'Belerofonte'),
    ('Hidra de Lerna', 'Heracles'), ('León de Nemea', 'Heracles'),
    ('Esfinge', 'Edipo'), ('Cerda de Cromión', 'Teseo'),
    ('Toro de Creta', 'Teseo'), ('Jabalí de Calidón', 'Atalanta'),
    ('Carcinos', None), ('Gerión', 'Heracles'), ('Cloto', None),
    ('Láquesis', None), ('Minotauro de Creta', 'Teseo'),
    ('Harpías', None), ('Aves del Estínfalo', None),
    ('Talos', 'Medea'), ('Sirenas', None), ('Pitón', 'Apolo'),
    ('Cierva de Cerinea', None), ('Basilisco', None),
    ('Jabalí de Erimanto', None)
]
for criatura, derrotado_por in criaturas:
    arbol.insertar(criatura, derrotado_por)

# a. Listado inorden de las criaturas y quienes la derrotaron
print("Listado inorden de las criaturas y quienes la derrotaron:")
arbol.inorden(arbol.raiz)

# b. Cargar una breve descripción sobre cada criatura
arbol.cargar_descripcion('Talos', 'Talos era un autómata gigante de bronce en la mitología griega.')

# c. Mostrar toda la información de la criatura Talos
print("\nInformación de Talos:")
arbol.mostrar_informacion('Talos')

# d. Determinar los 3 héroes o dioses que derrotaron mayor cantidad de criaturas
print("\nLos 3 héroes o dioses que derrotaron mayor cantidad de criaturas:")
heroes_mas_derrotas = arbol.contar_derrotas()
for heroe, cantidad in heroes_mas_derrotas:
    print(f"{heroe}: {cantidad} criaturas derrotadas")

# e. Listar las criaturas derrotadas por Heracles
print("\nCriaturas derrotadas por Heracles:")
arbol.listar_criaturas_derrotadas_por('Heracles')

# f. Listar las criaturas que no han sido derrotadas
print("\nCriaturas no derrotadas:")
arbol.listar_criaturas_no_derrotadas()

# g. Modificar los nodos de las criaturas capturadas por Heracles
for criatura in ['Cerbero', 'Toro de Creta', 'Cierva de Cerinea', 'Jabalí de Erimanto']:
    arbol.modificar_captura(criatura, 'Heracles')

# h. Búsquedas por coincidencia
print("\nBúsqueda por coincidencia 'Talos':")
arbol.mostrar_informacion('Talos')

# i. Eliminar al Basilisco y a las Sirenas
arbol.eliminar('Basilisco')
arbol.eliminar('Sirenas')

# j. Modificar el nodo que contiene a las Aves del Estínfalo, agregando que Heracles derrotó a varias
arbol.modificar_captura('Aves del Estínfalo', 'Heracles')

# k. Modificar el nombre de la criatura Ladón por Dragón Ladón
arbol.modificar_nombre('Ladón', 'Dragón Ladón')

# l. Recorrido por niveles del árbol
print("\nRecorrido por niveles del árbol:")
arbol.recorrido_por_niveles()

# m. Mostrar las criaturas capturadas por Heracles
print("\nCriaturas capturadas por Heracles:")
arbol.listar_criaturas_derrotadas_por('Heracles')