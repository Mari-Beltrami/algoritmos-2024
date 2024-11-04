# Se tienen una cola con personajes de Marvel Cinematic Universe (MCU), de los cuales se cono-
# ce el nombre del personaje, el nombre del superhéroe y su género (Masculino M y Femenino
# F) –por ejemplo {Tony Stark, Iron Man, M}, {Steve Rogers, Capitán América, M}, {Natasha Ro-
# manoff, Black Widow, F}, etc., desarrollar un algoritmo que resuelva las siguientes actividades:
#     a. determinar el nombre del personaje de la superhéroe Capitana Marvel;
#     b. mostrar los nombre de los superhéroes femeninos;
#     c. mostrar los nombres de los personajes masculinos;
#     d. determinar el nombre del superhéroe del personaje Scott Lang;
#     e. mostrar todos datos de los superhéroes o personaje cuyos nombres comienzan
#     con la letra S;
#     f. determinar si el personaje Carol Danvers se encuentra en la cola e indicar su nombre
#     de superhéroes.

from cola import Queue

cola_personajes = Queue()
cola_personajes.arrive({"nombre": "Tony Stark", "superheroe": "Iron Man", "genero": "M"})
cola_personajes.arrive({"nombre": "Steve Rogers", "superheroe": "Capitán América", "genero": "M"})
cola_personajes.arrive({"nombre": "Carol Danvers", "superheroe": "Capitana Marvel", "genero": "F"})
cola_personajes.arrive({"nombre": "Natasha Romanoff", "superheroe": "Black Widow", "genero": "F"})
cola_personajes.arrive({"nombre": "Scott Lang", "superheroe": "Ant-Man", "genero": "M"})

def encontrar_capitana_marvel(cola):
    for _ in range(cola.size()):
        personaje = cola.attention()
        if personaje["superheroe"] == "Capitana Marvel":
            print(f"El nombre del personaje de Capitana Marvel es {personaje['nombre']}")
        cola.arrive(personaje)

def superheroinas(cola):
    for _ in range(cola.size()):
        personaje = cola.attention()
        if personaje["genero"] == "F":
            print(f"Superheroína: {personaje['superheroe']}")
        cola.arrive(personaje)

def personajes_masculinos(cola):
    for _ in range(cola.size()):
        personaje = cola.attention()
        if personaje["genero"] == "M":
            print(f"Personaje masculino: {personaje['nombre']}")
        cola.arrive(personaje)

def superheroe_scott_lang(cola):
    for _ in range(cola.size()):
        personaje = cola.attention()
        if personaje["nombre"] == "Scott Lang":
            print(f"El superhéroe de Scott Lang es {personaje['superheroe']}")
        cola.arrive(personaje)

def personajes_con_s(cola):
    for _ in range(cola.size()):
        personaje = cola.attention()
        if personaje["nombre"].startswith("S") or personaje["superheroe"].startswith("S"):
            print(f"Personaje: {personaje['nombre']}, Superhéroe: {personaje['superheroe']}, Género: {personaje['genero']}")
        cola.arrive(personaje)

def encontrar_carol_danvers(cola):
    encontrado = False
    for _ in range(cola.size()):
        personaje = cola.attention()
        if personaje["nombre"] == "Carol Danvers":
            print(f"Carol Danvers es {personaje['superheroe']}")
            encontrado = True
        cola.arrive(personaje)
    if not encontrado:
        print("Carol Danvers no se encuentra en la cola.")

# prueba
encontrar_capitana_marvel(cola_personajes)
superheroinas(cola_personajes)
personajes_masculinos(cola_personajes)
superheroe_scott_lang(cola_personajes)
personajes_con_s(cola_personajes)
encontrar_carol_danvers(cola_personajes)
