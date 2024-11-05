from cola import Queue  # Importa la clase Cola para realizar recorridos por niveles en el árbol

# Clase Árbol Binario
class ArbolBinario:
    
    # Clase interna Nodo
    class __Nodo:
        def __init__(self, valor, izquierdo=None, derecho=None, otro_valor=None):
            self.valor = valor  # Valor principal del nodo
            self.izquierdo = izquierdo  # Referencia al nodo izquierdo
            self.derecho = derecho  # Referencia al nodo derecho
            self.otro_valor = otro_valor  # Valor adicional, puede contener información extra

    def __init__(self):
        self.raiz = None  # Inicializa el árbol con la raíz vacía

    # Inserta un nuevo nodo en el árbol
    def insertar_nodo(self, valor, otro_valor=None):
        def __insertar(raiz, valor, otro_valor=None):
            if raiz is None:
                return ArbolBinario.__Nodo(valor, otro_valor=otro_valor)
            elif valor < raiz.valor:
                raiz.izquierdo = __insertar(raiz.izquierdo, valor, otro_valor)
            else:
                raiz.derecho = __insertar(raiz.derecho, valor, otro_valor)
            return raiz

        self.raiz = __insertar(self.raiz, valor, otro_valor)

    # Busca un nodo en el árbol por su valor
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

    # Recorre el árbol en preorden
    def preorden(self):
        def __preorden(raiz):
            if raiz is not None:
                print(raiz.valor)
                __preorden(raiz.izquierdo)
                __preorden(raiz.derecho)

        if self.raiz is not None:
            __preorden(self.raiz)

    # Cuenta los nodos que son superhéroes
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

    # Recorre el árbol en inorden
    def inorden(self):
        def __inorden(raiz):
            if raiz is not None:
                __inorden(raiz.izquierdo)
                print(raiz.valor)
                __inorden(raiz.derecho)

        if self.raiz is not None:
            __inorden(self.raiz)

    # Recorre el árbol en postorden
    def postorden(self):
        def __postorden(raiz):
            if raiz is not None:
                __postorden(raiz.derecho)
                print(raiz.valor)
                __postorden(raiz.izquierdo)

        if self.raiz is not None:
            __postorden(self.raiz)

    # Recorre el árbol en inorden, mostrando solo los villanos
    def inorden_villanos(self):
        def __inorden_villanos(raiz):
            if raiz is not None:
                __inorden_villanos(raiz.izquierdo)
                if raiz.otro_valor.get('es_heroe') is not True:
                    print(raiz.valor)
                __inorden_villanos(raiz.derecho)

        if self.raiz is not None:
            __inorden_villanos(self.raiz)

    # Muestra los superhéroes cuyo nombre empieza con una letra específica
    def inorden_superheroes_comienzan_con(self, inicio):
        def __inorden_superheroes_comienzan_con(raiz, inicio):
            if raiz is not None:
                __inorden_superheroes_comienzan_con(raiz.izquierdo, inicio)
                if raiz.otro_valor.get('es_heroe') is True and raiz.valor.startswith(inicio):
                    print(raiz.valor)
                __inorden_superheroes_comienzan_con(raiz.derecho, inicio)

        if self.raiz is not None:
            __inorden_superheroes_comienzan_con(self.raiz, inicio)

    # Recorre el árbol por niveles usando una cola
    def por_nivel(self):
        pendientes = Queue()
        if self.raiz is not None:
            pendientes.arrive(self.raiz)

        while pendientes.size() > 0:
            nodo = pendientes.attention()
            print(nodo.valor)
            if nodo.izquierdo is not None:
                pendientes.arrive(nodo.izquierdo)
            if nodo.derecho is not None:
                pendientes.arrive(nodo.derecho)

    # Elimina un nodo por su valor
    def eliminar_nodo(self, valor):
        def __reemplazar(raiz):
            if raiz.derecho is None:
                return raiz.izquierdo, raiz
            else:
                raiz.derecho, nodo_reemplazo = __reemplazar(raiz.derecho)
                return raiz, nodo_reemplazo

        def __eliminar(raiz, valor):
            valor_eliminado = None
            if raiz is not None:
                if raiz.valor > valor:
                    raiz.izquierdo, valor_eliminado = __eliminar(raiz.izquierdo, valor)
                elif raiz.valor < valor:
                    raiz.derecho, valor_eliminado = __eliminar(raiz.derecho, valor)
                else:
                    valor_eliminado = raiz.valor
                    if raiz.izquierdo is None:
                        return raiz.derecho, valor_eliminado
                    elif raiz.derecho is None:
                        return raiz.izquierdo, valor_eliminado
                    else:
                        raiz.izquierdo, nodo_reemplazo = __reemplazar(raiz.izquierdo)
                        raiz.valor = nodo_reemplazo.valor
                        return raiz, valor_eliminado
                
            return raiz, valor_eliminado

        valor_eliminado = None
        if self.raiz is not None:
            self.raiz, valor_eliminado = __eliminar(self.raiz, valor)
        return valor_eliminado
