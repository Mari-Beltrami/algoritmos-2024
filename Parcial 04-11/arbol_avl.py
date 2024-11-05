from cola import Queue  # Importa la clase Cola para realizar recorridos por niveles en el árbol

# Clase ArbolAVL
class ArbolAVL:

    # Clase interna Nodo
    class __Nodo:
        def __init__(self, valor, izquierdo=None, derecho=None, otro_valor=None):
            self.valor = valor  # Valor principal del nodo
            self.izquierdo = izquierdo  # Referencia al nodo izquierdo
            self.derecho = derecho  # Referencia al nodo derecho
            self.otro_valor = otro_valor  # Información adicional del nodo
            self.altura = 0  # Altura del nodo, utilizada para balanceo

    def __init__(self):
        self.raiz = None  # Inicializa el árbol AVL con la raíz vacía

    # Obtiene la altura de un nodo dado
    def altura(self, nodo):
        if nodo is None:
            return -1
        else:
            return nodo.altura

    # Actualiza la altura de un nodo basándose en las alturas de sus hijos
    def actualizar_altura(self, nodo):
        if nodo is not None:
            altura_izq = self.altura(nodo.izquierdo)
            altura_der = self.altura(nodo.derecho)
            nodo.altura = max(altura_izq, altura_der) + 1

    # Realiza una rotación simple (izquierda o derecha)
    def rotacion_simple(self, nodo, es_izquierda):
        if es_izquierda:
            auxiliar = nodo.izquierdo
            nodo.izquierdo = auxiliar.derecho
            auxiliar.derecho = nodo
        else:
            auxiliar = nodo.derecho
            nodo.derecho = auxiliar.izquierdo
            auxiliar.izquierdo = nodo
        self.actualizar_altura(nodo)
        self.actualizar_altura(auxiliar)
        nodo = auxiliar
        return nodo

    # Realiza una rotación doble (izquierda-derecha o derecha-izquierda)
    def rotacion_doble(self, nodo, es_izquierda):
        if es_izquierda:
            nodo.izquierdo = self.rotacion_simple(nodo.izquierdo, False)
            nodo = self.rotacion_simple(nodo, True)
        else:
            nodo.derecho = self.rotacion_simple(nodo.derecho, True)
            nodo = self.rotacion_simple(nodo, False)
        return nodo

    # Balancea el árbol en torno a un nodo específico
    def balancear(self, nodo):
        if nodo is not None:
            if self.altura(nodo.izquierdo) - self.altura(nodo.derecho) == 2:
                if self.altura(nodo.izquierdo.izquierdo) >= self.altura(nodo.izquierdo.derecho):
                    nodo = self.rotacion_simple(nodo, True)
                else:
                    nodo = self.rotacion_doble(nodo, True)
            elif self.altura(nodo.derecho) - self.altura(nodo.izquierdo) == 2:
                if self.altura(nodo.derecho.derecho) >= self.altura(nodo.derecho.izquierdo):
                    nodo = self.rotacion_simple(nodo, False)
                else:
                    nodo = self.rotacion_doble(nodo, False)
        return nodo

    # Inserta un nodo en el árbol AVL
    def insertar_nodo(self, valor, otro_valor=None):
        def __insertar(raiz, valor, otro_valor=None):
            if raiz is None:
                return ArbolAVL.__Nodo(valor, otro_valor=otro_valor)
            elif valor < raiz.valor:
                raiz.izquierdo = __insertar(raiz.izquierdo, valor, otro_valor)
            else:
                raiz.derecho = __insertar(raiz.derecho, valor, otro_valor)
            raiz = self.balancear(raiz)
            self.actualizar_altura(raiz)
            return raiz

        self.raiz = __insertar(self.raiz, valor, otro_valor)

    # Busca un nodo con un valor específico en el árbol AVL
    def buscar(self, clave):
        def __buscar(raiz, clave):
            if raiz is not None:
                if raiz.valor == clave:
                    return raiz
                elif clave < raiz.valor:
                    return __buscar(raiz.izquierdo, clave)
                else:
                    return __buscar(raiz.derecho, clave)
        aux = None
        if self.raiz is not None:
            aux = __buscar(self.raiz, clave)
        return aux

    # Recorrido en preorden del árbol AVL
    def preorden(self):
        def __preorden(raiz):
            if raiz is not None:
                print(raiz.valor)
                __preorden(raiz.izquierdo)
                __preorden(raiz.derecho)

        if self.raiz is not None:
            __preorden(self.raiz)

    # Contar nodos en el árbol con el atributo 'es_heroe' igual a True
    def contar_super_heroes(self):
        def __contar_super_heroes(raiz):
            contador = 0
            if raiz is not None:
                if raiz.otro_valor.get('es_heroe') is True:
                    contador = 1
                contador += __contar_super_heroes(raiz.izquierdo)
                contador += __contar_super_heroes(raiz.derecho)
            return contador

        return __contar_super_heroes(self.raiz)

    # Recorrido en inorden del árbol AVL
    def inorden(self):
        def __inorden(raiz):
            if raiz is not None:
                __inorden(raiz.izquierdo)
                print(raiz.valor)
                __inorden(raiz.derecho)

        if self.raiz is not None:
            __inorden(self.raiz)

    # Recorrido en postorden del árbol AVL
    def postorden(self):
        def __postorden(raiz):
            if raiz is not None:
                __postorden(raiz.derecho)
                print(raiz.valor)
                __postorden(raiz.izquierdo)

        if self.raiz is not None:
            __postorden(self.raiz)

    # Recorrido en inorden mostrando solo los nodos villanos (no héroes)
    def inorden_villanos(self):
        def __inorden_villanos(raiz):
            if raiz is not None:
                __inorden_villanos(raiz.izquierdo)
                if raiz.otro_valor.get('es_heroe') is not True:
                    print(raiz.valor)
                __inorden_villanos(raiz.derecho)

        if self.raiz is not None:
            __inorden_villanos(self.raiz)

    # Recorrido en inorden mostrando solo los héroes cuyo nombre empieza con una letra específica
    def inorden_superheroes_comienzan_con(self, inicio):
        def __inorden_superheroes_comienzan_con(raiz, inicio):
            if raiz is not None:
                __inorden_superheroes_comienzan_con(raiz.izquierdo, inicio)
                if raiz.otro_valor.get('es_heroe') is True and raiz.valor.startswith(inicio):
                    print(raiz.valor)
                __inorden_superheroes_comienzan_con(raiz.derecho, inicio)

        if self.raiz is not None:
            __inorden_superheroes_comienzan_con(self.raiz, inicio)

# Búsqueda aproximada de nodos cuyos valores comiencen con un texto específico
    def busqueda_aproximada(self, valor_busqueda):
        def __busqueda_aproximada(raiz, valor_busqueda):
            if raiz is not None:
                __busqueda_aproximada(raiz.izquierdo, valor_busqueda)
                if raiz.valor.lower().startswith(valor_busqueda.lower()):
                    # Muestra el nombre y otros datos del Pokémon
                    print(f"Nombre: {raiz.valor}, Datos: {raiz.otro_valor}")
                __busqueda_aproximada(raiz.derecho, valor_busqueda)

        if self.raiz is not None:
            __busqueda_aproximada(self.raiz, valor_busqueda)

    # Recorrido por niveles del árbol usando una cola
    def por_nivel(self):
        pendientes = Queue()
        if self.raiz is not None:
            pendientes.arrive(self.raiz)

        while pendientes.size() > 0:
            nodo = pendientes.attention()
            print(f"nivel {nodo.altura}", nodo.valor)
            if nodo.izquierdo is not None:
                pendientes.arrive(nodo.izquierdo)
            if nodo.derecho is not None:
                pendientes.arrive(nodo.derecho)

    # Elimina un nodo del árbol AVL
    def eliminar_nodo(self, valor):
        def __reemplazar(raiz):
            if raiz.derecho is None:
                return raiz.izquierdo, raiz
            else:
                raiz.derecho, nodo_reemplazo = __reemplazar(raiz.derecho)
                return raiz, nodo_reemplazo

        def __eliminar(raiz, valor):
            valor_eliminado = None
            otro_valor_eliminado = None
            if raiz is not None:
                if raiz.valor > valor:
                    raiz.izquierdo, valor_eliminado, otro_valor_eliminado = __eliminar(raiz.izquierdo, valor)
                elif raiz.valor < valor:
                    raiz.derecho, valor_eliminado, otro_valor_eliminado = __eliminar(raiz.derecho, valor)
                else:
                    valor_eliminado = raiz.valor
                    otro_valor_eliminado = raiz.otro_valor
                    if raiz.izquierdo is None:
                        return raiz.derecho, valor_eliminado, otro_valor_eliminado
                    elif raiz.derecho is None:
                        return raiz.izquierdo, valor_eliminado, otro_valor_eliminado
                    else:
                        raiz.izquierdo, nodo_reemplazo = __reemplazar(raiz.izquierdo)
                        raiz.valor = nodo_reemplazo.valor
                        raiz.otro_valor = nodo_reemplazo.otro_valor
                    raiz = self.balancear(raiz)
                    self.actualizar_altura(raiz)
            return raiz, valor_eliminado, otro_valor_eliminado

        valor_eliminado = None
        otro_valor_eliminado = None
        if self.raiz is not None:
            self.raiz, valor_eliminado, otro_valor_eliminado = __eliminar(self.raiz, valor)
        return valor_eliminado, otro_valor_eliminado
