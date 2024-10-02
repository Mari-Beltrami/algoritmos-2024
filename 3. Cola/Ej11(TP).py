# Dada una cola con personajes de la saga Star Wars, de los cuales se conoce su nombre y planeta
# de origen. Desarrollar las funciones necesarias para resolver las siguientes actividades:
#     a. mostrar los personajes del planeta Alderaan, Endor y Tatooine
#     b. indicar el plantea natal de Luke Skywalker y Han Solo
#     c. insertar un nuevo personaje antes del maestro Yoda
#     d. eliminar el personaje ubicado después de Jar Jar Binks

from cola import Queue

cola_personajes = Queue()
cola_planeta = Queue()
cola_aux = Queue()
cola_eliminar = Queue()

def mostrar_personajes (cola):
    while cola.size () > 0:
        personaje = cola.attention()
        if personaje["planeta"] in ["Alderaan", "Endor", "Tatooine"]:
            print (f"Personaje: {personaje['nombre']}, Planeta: {personaje['planeta']}")
        cola_personajes.arrive(personaje)
    
    while cola_personajes.size() > 0:
        cola.arrive(cola_personajes.attention())
        
def indicar_planeta (cola):
    while cola.size() > 0:
        personaje = cola.attention()
        if personaje["nombre"] in ["Luke Skywalker" , "Han Solo"]:
            print(f"El planeta natal de {personaje['nombre']} es {personaje['planeta']}")
        cola_planeta.arrive(personaje)
        
    while cola_planeta.size():
        cola.arrive(cola_planeta.attention())
            
def insertar_personaje(cola):
    personaje_insertado = False
    while cola.size() > 0:
        personaje = cola.attention()
        if personaje["nombre"] == "Yoda" and not personaje_insertado: 
            nuevo_personaje = {"nombre": "Ahsoka Tano", "planeta": "Shili"}
            cola_aux.arrive(nuevo_personaje)
            personaje_insertado = True
            print (f"Se agregó al personaje {nuevo_personaje['nombre']} de {nuevo_personaje['planeta']}")
        cola_aux.arrive(personaje)
        
    while cola_aux.size() > 0:
        cola.arrive(cola_aux.attention())      

def eliminar_personaje(cola):
    eliminar_siguiente = False
    personaje_eliminado = None
    
    while cola.size() > 0:
        personaje = cola.attention()
        if eliminar_siguiente:
            personaje_eliminado = personaje
            eliminar_siguiente = False
        else:
            cola_eliminar.arrive(personaje)
        if personaje['nombre'] == "Jar Jar Binks":
            eliminar_siguiente = True
            
    while cola_eliminar.size() > 0:
        cola.arrive(cola_eliminar.attention())
        
    if personaje_eliminado:
        print(f"El personaje eliminado es: {personaje_eliminado['nombre']} de {personaje_eliminado['planeta']}")
    else:
        print("No se eliminó ningún personaje")
        
        
cola = Queue()
cola.arrive({"nombre": "Luke Skywalker", "planeta": "Tatooine"})
cola.arrive({"nombre": "Leia Organa", "planeta": "Alderaan"})
cola.arrive({"nombre": "Han Solo", "planeta": "Corellia"})
cola.arrive({"nombre": "Yoda", "planeta": "Dagobah"})
cola.arrive({"nombre": "Darth Vader", "planeta": "Tatooine"})
cola.arrive({"nombre": "Obi-Wan Kenobi", "planeta": "Stewjon"})
cola.arrive({"nombre": "Chewbacca", "planeta": "Kashyyyk"})
cola.arrive({"nombre": "Jar Jar Binks", "planeta": "Naboo"})
cola.arrive({"nombre": "Anakin Skywalker", "planeta": "Tatooine"})
cola.arrive({"nombre": "Wicket W. Warrick", "planeta": "Endor"})
cola.arrive({"nombre": "Boba Fett", "planeta": "Kamino"})

mostrar_personajes(cola)
indicar_planeta(cola)
insertar_personaje(cola)
eliminar_personaje(cola)