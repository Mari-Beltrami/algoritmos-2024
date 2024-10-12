# El general Hux es la persona encargada de administrar todas las operaciones de la base Starki-
# ller, para lo cual nos solicita desarrollar un algoritmo que permita controlar las actividades que
# se realizan, contemplando lo siguiente:
# a. debe contemplar distintas prioridades para el control de operaciones de acuerdo al siguien-
# te criterio: pedidos de líder supremo Snoke y de Kylo Ren nivel tres, de capitán Phasma
# nivel dos y el resto de las operaciones nivel a cargo de los generales de la base de nivel uno;
# b. de cada actividad se conoce quien es el encargado, una descripción, la hora y opcional-
# mente la cantidad de Stormtroopers requeridos;
# c. utilizar una cola de prioridad para administrar las distintas operaciones, debe cargar al
# menos ocho: dos de nivel tres, cuatro de nivel dos y cuatro de nivel uno;
# d. opcionalmente se podrán agregar operaciones luego de atender una;
# e. realizar la atención de las operaciones de la cola;
# f. luego de atender la quinta operación, agregar una operación solicitada por capitán Phasma
# para revisión de intrusos en el hangar B7 que requiere 25 Stormstroopers;
# g. luego de atender la sexta operación, agregar una operación solicitada por el líder supremo
# Snoke para destruir el planeta Takodana.

class HeapMax:
    def __init__(self):
        self.elements = []

    def add(self, value):
        """Añade una operación al montículo y mantiene la propiedad del montículo."""
        self.elements.append(value)
        self.float(len(self.elements) - 1)

    def remove(self):
        """Elimina la operación con mayor prioridad (raíz del montículo)."""
        if len(self.elements) > 0:
            self.interchange(0, len(self.elements) - 1)
            value = self.elements.pop()
            self.sink(0)
            return value
        else:
            return None

    def interchange(self, index_1, index_2):
        """Intercambia dos elementos del montículo."""
        self.elements[index_1], self.elements[index_2] = self.elements[index_2], self.elements[index_1]

    def float(self, index):
        """Hace que un elemento suba hasta su posición correcta."""
        father = (index - 1) // 2
        while index > 0 and self.elements[index][0] > self.elements[father][0]:
            self.interchange(index, father)
            index = father
            father = (index - 1) // 2

    def sink(self, index):
        """Hace que un elemento baje hasta su posición correcta."""
        left_child = (index * 2) + 1
        control = True
        while control and left_child < len(self.elements):
            right_child = (index * 2) + 2
            max_child = left_child
            if right_child < len(self.elements) and self.elements[right_child][0] > self.elements[left_child][0]:
                max_child = right_child
            if self.elements[index][0] < self.elements[max_child][0]:
                self.interchange(index, max_child)
                index = max_child
                left_child = (index * 2) + 1
            else:
                control = False

    def is_empty(self):
        """Verifica si el montículo está vacío."""
        return len(self.elements) == 0

# Definir las prioridades de las actividades
PRIORIDAD_SNOKE_KYLO = 3  # Nivel tres para Snoke y Kylo Ren
PRIORIDAD_PHASMA = 2  # Nivel dos para el capitán Phasma
PRIORIDAD_GENERALES = 1  # Nivel uno para el resto de los generales

# Inicializar el montículo
cola_prioridad = HeapMax()

# a. Cargar las operaciones
# Nivel 3 (Snoke y Kylo Ren)
cola_prioridad.add((PRIORIDAD_SNOKE_KYLO, 'Kylo Ren', 'Entrenar en el uso del sable de luz', '08:00', None))
cola_prioridad.add((PRIORIDAD_SNOKE_KYLO, 'Líder Supremo Snoke', 'Revisión de estrategias de ataque', '09:00', None))

# Nivel 2 (Capitán Phasma)
cola_prioridad.add((PRIORIDAD_PHASMA, 'Capitán Phasma', 'Patrullaje de las instalaciones', '10:00', 10))
cola_prioridad.add((PRIORIDAD_PHASMA, 'Capitán Phasma', 'Revisión de seguridad en sector C', '11:00', 15))
cola_prioridad.add((PRIORIDAD_PHASMA, 'Capitán Phasma', 'Entrenamiento de Stormtroopers', '12:00', 20))
cola_prioridad.add((PRIORIDAD_PHASMA, 'Capitán Phasma', 'Inspección de vehículos en el hangar', '13:00', None))

# Nivel 1 (Generales)
cola_prioridad.add((PRIORIDAD_GENERALES, 'General Hux', 'Mantenimiento de la base Starkiller', '14:00', None))
cola_prioridad.add((PRIORIDAD_GENERALES, 'General Mitaka', 'Supervisión de la producción de energía', '15:00', None))
cola_prioridad.add((PRIORIDAD_GENERALES, 'General Quinn', 'Revisión de comunicaciones intergalácticas', '16:00', None))
cola_prioridad.add((PRIORIDAD_GENERALES, 'General Hux', 'Planificación de misiones futuras', '17:00', None))

# e. Atender las operaciones de la cola
print("Atendiendo operaciones de la cola de prioridad:")
atendidas = 0
while not cola_prioridad.is_empty() and atendidas < 10:
    operacion = cola_prioridad.remove()
    print(f"Atendiendo operación: Encargado: {operacion[1]}, Descripción: {operacion[2]}, Hora: {operacion[3]}, Stormtroopers requeridos: {operacion[4]}")
    atendidas += 1
    
    # f. Luego de atender la quinta operación, agregar la operación de revisión de intrusos
    if atendidas == 5:
        cola_prioridad.add((PRIORIDAD_PHASMA, 'Capitán Phasma', 'Revisión de intrusos en el hangar B7', '18:00', 25))
        print("Agregando operación de revisión de intrusos solicitada por Capitán Phasma.")
    
    # g. Luego de atender la sexta operación, agregar la operación solicitada por Snoke
    if atendidas == 6:
        cola_prioridad.add((PRIORIDAD_SNOKE_KYLO, 'Líder Supremo Snoke', 'Destruir el planeta Takodana', '19:00', None))
        print("Agregando operación para destruir el planeta Takodana solicitada por Líder Supremo Snoke.")