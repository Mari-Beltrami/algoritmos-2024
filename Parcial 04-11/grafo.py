from cola import Queue  # Importa la clase Cola para realizar recorridos por amplitud
from heap import HeapMin  # Importa el montículo mínimo para Dijkstra y Kruskal
from pila import Stack  # Importa la clase Pila para almacenar caminos en Dijkstra

# Clase Grafo
class Grafo:
    def __init__(self, dirigido=True):
        """Inicializa el grafo, que puede ser dirigido o no."""
        self.elementos = []  # Lista de nodos (vértices) del grafo
        self.dirigido = dirigido  # Indica si el grafo es dirigido

    def mostrar_grafo(self):
        """Muestra el grafo con sus nodos y aristas."""
        print("\nNodos")
        for indice, nodo in enumerate(self.elementos):
            print(nodo['valor'])
            print(f"    Aristas")
            for indice_arista, arista in enumerate(nodo['aristas']):
                print(f'    destino {arista["valor"]} peso: {arista["peso"]}')
        print()

    def buscar(self, valor):
        """Busca un nodo en el grafo y devuelve su índice si existe."""
        for indice, elemento in enumerate(self.elementos):
            if elemento['valor'] == valor:
                return indice
        return None

    def buscar_arista(self, valor_origen, valor_destino):
        """Busca una arista entre dos nodos específicos."""
        pos_origen = self.buscar(valor_origen)
        if pos_origen is not None:
            for indice, arista in enumerate(self.elementos[pos_origen]['aristas']):
                if arista['valor'] == valor_destino:
                    return pos_origen, indice
        return None

    def insertar_vertice(self, valor):
        """Inserta un nuevo vértice en el grafo."""
        nodo = {
            'valor': valor,
            'aristas': [],  # Lista de aristas para este nodo
            'visitado': False,  # Marca de visitado para recorridos
        }
        self.elementos.append(nodo)

    def insertar_arista(self, origen, destino, peso):
        """Inserta una arista entre dos nodos del grafo con un peso."""
        pos_origen = self.buscar(origen)
        pos_destino = self.buscar(destino)
        if pos_origen is not None and pos_destino is not None:
            arista = {
                'valor': destino,
                'peso': peso  # Peso de la arista
            }
            self.elementos[pos_origen]['aristas'].append(arista)
            # Si el grafo no es dirigido, también añade la arista inversa
            if not self.dirigido:
                arista = {
                    'valor': origen,
                    'peso': peso
                }
                self.elementos[pos_destino]['aristas'].append(arista)

    def eliminar_arista(self, origen, destino):
        """Elimina una arista entre dos nodos especificados."""
        resultado = self.buscar_arista(origen, destino)
        if resultado:
            pos_vertice, pos_arista = resultado
            self.elementos[pos_vertice]['aristas'].pop(pos_arista)
            if not self.dirigido:
                # Elimina la arista inversa si el grafo no es dirigido
                resultado = self.buscar_arista(destino, origen)
                if resultado:
                    pos_vertice, pos_arista = resultado
                    self.elementos[pos_vertice]['aristas'].pop(pos_arista)

    def eliminar_vertice(self, valor):
        """Elimina un nodo y todas sus aristas en el grafo."""
        pos_vertice = self.buscar(valor)
        if pos_vertice is not None:
            self.elementos.pop(pos_vertice)
            # Elimina todas las aristas que apuntan a este nodo
            for nodo in self.elementos:
                self.eliminar_arista(nodo['valor'], valor)

    def marcar_no_visitado(self):
        """Marca todos los nodos del grafo como no visitados."""
        for nodo in self.elementos:
            nodo['visitado'] = False

    def recorrido_profundidad(self, origen):
        """Realiza un recorrido en profundidad a partir de un nodo inicial."""
        def __recorrido_profundidad(grafo, origen):
            pos_vertice = grafo.buscar(origen)
            if pos_vertice is not None:
                if not grafo.elementos[pos_vertice]['visitado']:
                    grafo.elementos[pos_vertice]['visitado'] = True
                    print(grafo.elementos[pos_vertice]['valor'])
                    adyacentes = grafo.elementos[pos_vertice]['aristas']
                    for adyacente in adyacentes:
                        __recorrido_profundidad(grafo, adyacente['valor'])
        
        self.marcar_no_visitado()
        __recorrido_profundidad(self, origen)

    def recorrido_amplitud(self, origen):
        """Realiza un recorrido en amplitud a partir de un nodo inicial."""
        self.marcar_no_visitado()
        cola = Queue()  # Usa una cola para gestionar los nodos por visitar
        pos_vertice = self.buscar(origen)
        if pos_vertice is not None:
            cola.arrive(self.elementos[pos_vertice])
            while cola.size() > 0:
                nodo = cola.attention()
                nodo['visitado'] = True
                print(nodo['valor'])
                adyacentes = nodo['aristas']
                for adyacente in adyacentes:
                    pos_adyacente = self.buscar(adyacente['valor'])
                    if not self.elementos[pos_adyacente]['visitado']:
                        cola.arrive(self.elementos[pos_adyacente])

    def existe_camino(self, origen, destino):
        """Determina si existe un camino entre dos nodos."""
        def __existe_camino(grafo, origen, destino):
            result = False
            pos_vertice = grafo.buscar(origen)
            if pos_vertice is not None:
                if not grafo.elementos[pos_vertice]['visitado']:
                    grafo.elementos[pos_vertice]['visitado'] = True
                    if grafo.elementos[pos_vertice]['valor'] == destino:
                        return True
                    else:
                        adyacentes = grafo.elementos[pos_vertice]['aristas']
                        for adyacente in adyacentes:
                            result = __existe_camino(grafo, adyacente['valor'], destino)
                            if result:
                                break
            return result
        
        self.marcar_no_visitado()
        return __existe_camino(self, origen, destino)

    def dijkstra(self, origen):
        """Aplica el algoritmo de Dijkstra para encontrar el camino más corto desde un nodo."""
        from math import inf
        no_visitados = HeapMin()  # Usa un montículo para gestionar los nodos no visitados
        camino = Stack()  # Pila para almacenar el camino
        for nodo in self.elementos:
            distancia = 0 if nodo['valor'] == origen else inf
            no_visitados.arrive([nodo['valor'], nodo, None], distancia)
        while len(no_visitados.elements) > 0:
            nodo_actual = no_visitados.atention()
            costo_nodo_actual = nodo_actual[0]
            camino.push(nodo_actual)
            adyacentes = nodo_actual[1][1]['aristas']
            for adyacente in adyacentes:
                pos = no_visitados.search(adyacente['valor'])
                if pos is not None:
                    if costo_nodo_actual + adyacente['peso'] < no_visitados.elements[pos][0]:
                        no_visitados.elements[pos][1][2] = nodo_actual[1][0]
                        no_visitados.change_proirity(pos, costo_nodo_actual + adyacente['peso'])
        return camino

    def kruskal(self):
        """Aplica el algoritmo de Kruskal para encontrar el árbol de expansión mínima."""
        def buscar_en_bosque(bosque, buscado):
            for index, arbol in enumerate(bosque):
                if buscado in arbol:
                    return index

        bosque = []
        aristas = HeapMin()  # Montículo para gestionar las aristas por peso
        for nodo in self.elementos:
            bosque.append(nodo['valor'])
            adyacentes = nodo['aristas']
            for adyacente in adyacentes:
                aristas.arrive([nodo['valor'], adyacente['valor']], adyacente['peso'])

        while len(bosque) > 1 and len(aristas.elements) > 0:
            arista = aristas.atention()
            origen = buscar_en_bosque(bosque, arista[1][0])
            destino = buscar_en_bosque(bosque, arista[1][1])
            if origen is not None and destino is not None:
                if origen != destino:
                    if origen > destino:
                        vertice_ori = bosque.pop(origen)
                        vertice_des = bosque.pop(destino)
                    else:
                        vertice_des = bosque.pop(destino)
                        vertice_ori = bosque.pop(origen)

                    if '-' not in vertice_ori and '-' not in vertice_des:
                        bosque.append(f'{vertice_ori}-{vertice_des}-{arista[0]}')
                    elif '-' not in vertice_des:
                        bosque.append(vertice_ori+';'+f'{arista[1][0]}-{vertice_des}-{arista[0]}')
                    elif '-' not in vertice_ori:
                        bosque.append(vertice_des+';'+f'{vertice_ori}-{arista[1][1]}-{arista[0]}')
                    else:
                        bosque.append(vertice_ori+';'+vertice_des+';'+f'{arista[1][0]}-{arista[1][1]}-{arista[0]}')
        return bosque
