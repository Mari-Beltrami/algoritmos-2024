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

from heap import MonticuloMax

operaciones = MonticuloMax()

operaciones.agregar_operacion("Pedido del Líder Supremo Snoke", 3)
operaciones.agregar_operacion("Pedido de Kylo Ren", 3)
operaciones.agregar_operacion("Pedido del Capitán Phasma", 2)
operaciones.agregar_operacion("Pedido de inspección de equipo", 2)
operaciones.agregar_operacion("Mantenimiento del hangar principal", 2)
operaciones.agregar_operacion("Revisión de suministros", 2)
operaciones.agregar_operacion("Pedido del General Hux", 1)
operaciones.agregar_operacion("Revisión de seguridad", 1)

operaciones.agregar_operacion(("Capitán Phasma", "Inspección de intrusos en el hangar B7", "25 Stormtroopers requeridos"), 2)
operaciones.agregar_operacion(("Líder Supremo Snoke", "Destrucción del planeta Takodana"), 3)

print("\nAtención de operaciones en la base Starkiller:")
contador_atendidas = 0
while operaciones.elementos and contador_atendidas < 5:
    operacion = operaciones.atender()
    print("Atendiendo:", operacion)
    contador_atendidas += 1

if contador_atendidas == 5:
    operaciones.agregar_operacion(("Capitán Phasma", "Revisión de intrusos en el hangar B7", "25 Stormtroopers requeridos"), 2)
    print("\nAgregada operación después de la quinta atención.")

operacion = operaciones.atender()
contador_atendidas += 1
print("Atendiendo:", operacion)
if contador_atendidas == 6:
    operaciones.agregar_operacion(("Líder Supremo Snoke", "Destrucción del planeta Takodana"), 3)
    print("\nAgregada operación después de la sexta atención.")

print("\nAtención de operaciones restantes:")
while operaciones.elementos:
    operacion = operaciones.atender()
    print("Atendiendo:", operacion)

