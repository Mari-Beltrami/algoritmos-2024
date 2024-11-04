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

from heap import HeapMax

# Inicialización del heap para las operaciones de la base Starkiller
operaciones = HeapMax()

# a. Cargar operaciones con sus prioridades
operaciones.arrive({
    "encargado": "Líder Supremo Snoke",
    "descripción": "Revisión de sistemas",
    "hora": "08:00",
    "stormtroopers": 10
}, priority=3)

operaciones.arrive({
    "encargado": "Kylo Ren",
    "descripción": "Entrenamiento de combate",
    "hora": "09:00",
    "stormtroopers": 20
}, priority=3)

operaciones.arrive({
    "encargado": "Capitán Phasma",
    "descripción": "Control de patrullas",
    "hora": "10:00",
}, priority=2)

operaciones.arrive({
    "encargado": "Capitán Phasma",
    "descripción": "Revisión de arsenal",
    "hora": "11:00",
}, priority=2)

operaciones.arrive({
    "encargado": "General Hux",
    "descripción": "Planificación táctica",
    "hora": "12:00",
}, priority=1)

operaciones.arrive({
    "encargado": "General Hux",
    "descripción": "Mantenimiento de sistemas",
    "hora": "13:00",
}, priority=1)

operaciones.arrive({
    "encargado": "General Hux",
    "descripción": "Supervisión de entrenamiento",
    "hora": "14:00",
}, priority=1)

operaciones.arrive({
    "encargado": "General Hux",
    "descripción": "Gestión de suministros",
    "hora": "15:00",
}, priority=1)

# Función para atender y mostrar la operación actual
def atender_operacion(heap, contador):
    if contador == 5:
        # f. Luego de la quinta operación, agregar nueva operación de Phasma
        heap.arrive({
            "encargado": "Capitán Phasma",
            "descripción": "Revisión de intrusos en hangar B7",
            "hora": "16:00",
            "stormtroopers": 25
        }, priority=2)
        print("Operación añadida: Revisión de intrusos en hangar B7 por Capitán Phasma.")
    
    if contador == 6:
        # g. Luego de la sexta operación, agregar nueva operación de Snoke
        heap.arrive({
            "encargado": "Líder Supremo Snoke",
            "descripción": "Destrucción del planeta Takodana",
            "hora": "17:00",
        }, priority=3)
        print("Operación añadida: Destrucción del planeta Takodana por Líder Supremo Snoke.")

    # Atender la operación de mayor prioridad
    operacion = heap.atention()
    if operacion:
        print(f"Atendiendo operación: {operacion[1]['descripción']} a cargo de {operacion[1]['encargado']} con prioridad {operacion[0]}")

# Atender las operaciones secuencialmente
contador = 1
while operaciones.elements:
    atender_operacion(operaciones, contador)
    contador += 1
