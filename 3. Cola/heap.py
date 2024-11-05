class MonticuloMax:
    """Clase que representa un Montículo Máximo"""

    def __init__(self):
        """Inicializa el montículo vacío"""
        self.elementos = []

    def agregar(self, valor):
        """Añade un valor al montículo y ajusta la posición para mantener la propiedad del montículo"""
        self.elementos.append(valor)
        self.elevar(len(self.elementos) - 1)

    def eliminar(self):
        """Elimina el elemento de mayor prioridad (la raíz del montículo)"""
        if len(self.elementos) > 0:
            self.intercambiar(0, len(self.elementos) - 1)
            valor = self.elementos.pop()
            self.hundir(0)
            return valor
        else:
            return None

    def intercambiar(self, indice_1, indice_2):
        """Intercambia dos elementos del montículo"""
        self.elementos[indice_1], self.elementos[indice_2] = self.elementos[indice_2], self.elementos[indice_1]

    def elevar(self, indice):
        """Hace que un elemento suba hasta su posición correcta en el montículo"""
        padre = (indice - 1) // 2
        while indice > 0 and self.elementos[indice][0] > self.elementos[padre][0]:
            self.intercambiar(indice, padre)
            indice = padre
            padre = (indice - 1) // 2

    def hundir(self, indice):
        """Hace que un elemento baje hasta su posición correcta en el montículo"""
        hijo_izq = (indice * 2) + 1
        control = True
        while control and hijo_izq < len(self.elementos):
            hijo_der = (indice * 2) + 2
            hijo_mayor = hijo_izq
            if hijo_der < len(self.elementos) and self.elementos[hijo_der][0] > self.elementos[hijo_izq][0]:
                hijo_mayor = hijo_der
            if self.elementos[indice][0] < self.elementos[hijo_mayor][0]:
                self.intercambiar(indice, hijo_mayor)
                indice = hijo_mayor
                hijo_izq = (indice * 2) + 1
            else:
                control = False

    def construir_monticulo(self, elementos):
        """Construye un montículo a partir de una lista de elementos"""
        self.elementos = elementos
        for i in range(len(self.elementos)):
            self.elevar(i)

    def ordenar(self):
        """Ordena los elementos del montículo en orden descendente"""
        resultado = []
        cantidad_elementos = len(self.elementos)
        for i in range(cantidad_elementos):
            valor = self.eliminar()
            resultado.append(valor)
        return resultado

    def buscar(self, valor):
        """Busca un valor en el montículo y devuelve su índice"""
        for indice, elemento in enumerate(self.elementos):
            if elemento[1][0] == valor:
                return indice

    def agregar_operacion(self, valor, prioridad):
        """Agrega una operación con una prioridad específica"""
        self.agregar([prioridad, valor])

    def atender(self):
        """Atiende la operación de mayor prioridad"""
        return self.eliminar()

    def cambiar_prioridad(self, indice, nueva_prioridad):
        """Cambia la prioridad de un elemento y ajusta su posición en el montículo"""
        if indice < len(self.elementos):
            prioridad_anterior = self.elementos[indice][0]
            self.elementos[indice][0] = nueva_prioridad
            if nueva_prioridad > prioridad_anterior:
                self.elevar(indice)
            elif nueva_prioridad < prioridad_anterior:
                self.hundir(indice)


class MonticuloMin:
    """Clase que representa un Montículo Mínimo"""

    def __init__(self):
        """Inicializa el montículo vacío"""
        self.elementos = []

    def agregar(self, valor):
        """Añade un valor al montículo y ajusta su posición para mantener la propiedad del montículo"""
        self.elementos.append(valor)
        self.elevar(len(self.elementos) - 1)

    def eliminar(self):
        """Elimina el elemento de menor prioridad (la raíz del montículo)"""
        if len(self.elementos) > 0:
            self.intercambiar(0, len(self.elementos) - 1)
            valor = self.elementos.pop()
            self.hundir(0)
            return valor
        else:
            return None

    def intercambiar(self, indice_1, indice_2):
        """Intercambia dos elementos del montículo"""
        self.elementos[indice_1], self.elementos[indice_2] = self.elementos[indice_2], self.elementos[indice_1]

    def elevar(self, indice):
        """Hace que un elemento suba hasta su posición correcta en el montículo"""
        padre = (indice - 1) // 2
        while indice > 0 and self.elementos[indice] < self.elementos[padre]:
            self.intercambiar(indice, padre)
            indice = padre
            padre = (indice - 1) // 2

    def hundir(self, indice):
        """Hace que un elemento baje hasta su posición correcta en el montículo"""
        hijo_izq = (indice * 2) + 1
        control = True
        while control and hijo_izq < len(self.elementos):
            hijo_der = (indice * 2) + 2
            hijo_menor = hijo_izq
            if hijo_der < len(self.elementos) and self.elementos[hijo_der] < self.elementos[hijo_izq]:
                hijo_menor = hijo_der
            if self.elementos[indice] > self.elementos[hijo_menor]:
                self.intercambiar(indice, hijo_menor)
                indice = hijo_menor
                hijo_izq = (indice * 2) + 1
            else:
                control = False

    def construir_monticulo(self, elementos):
        """Construye un montículo a partir de una lista de elementos"""
        self.elementos = elementos
        for i in range(len(self.elementos)):
            self.elevar(i)

    def ordenar(self):
        """Ordena los elementos del montículo en orden ascendente"""
        resultado = []
        cantidad_elementos = len(self.elementos)
        for i in range(cantidad_elementos):
            valor = self.eliminar()
            resultado.append(valor)
        return resultado

    def buscar(self, valor):
        """Busca un valor en el montículo y devuelve su índice"""
        for indice, elemento in enumerate(self.elementos):
            if elemento[1][0] == valor:
                return indice

    def agregar_operacion(self, valor, prioridad):
        """Agrega una operación con una prioridad específica"""
        self.agregar([prioridad, valor])

    def atender(self):
        """Atiende la operación de menor prioridad"""
        return self.eliminar()

    def cambiar_prioridad(self, indice, nueva_prioridad):
        """Cambia la prioridad de un elemento y ajusta su posición en el montículo"""
        if indice < len(self.elementos):
            prioridad_anterior = self.elementos[indice][0]
            self.elementos[indice][0] = nueva_prioridad
            if nueva_prioridad < prioridad_anterior:
                self.elevar(indice)
            elif nueva_prioridad > prioridad_anterior:
                self.hundir(indice)
