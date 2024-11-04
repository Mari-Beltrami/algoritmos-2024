""" Se tienen dos pilas con personajes de Star Wars, en una los del episodio V de “The empire
strikes back” y la otra los del episodio VII “The force awakens”. Desarrollar un algoritmo que
permita obtener la intersección de ambas pilas, es decir los personajes que aparecen en am-
bos episodios. 
Luke Skywalker, Darth Vader, Han Solo, Leia Organa, Yoda 

Rey, Finn, Kylo Ren, Poe Dameron, BB-8"""

from pila import Stack

def interseccion(pilaV, pilaVII):
    pilaV_aux = Stack()
    pilaVII_aux = Stack()
    personajesV = []
    personajesVII = []
    interseccion = []
    
    for _ in range(pilaV.size()):
        personajesV.append(pilaV.pop())
        pilaV_aux.push(personajesV[-1])
    
    for _ in range(pilaV_aux.size()):
        pilaV.push(pilaV_aux.pop())

    for _ in range(pilaVII.size()):
            personajesVII.append(pilaVII.pop())
            pilaVII_aux.push(personajesVII[-1])
    
    for _ in range(pilaVII_aux.size()):
        pilaVII.push(pilaVII_aux.pop())

    for personaje in personajesV:
        if personaje in personajesVII:
            interseccion.append(personaje)
    
    for personaje in personajesVII:
        if personaje in personajesV and not personaje in interseccion:
            interseccion.append(personaje)
    
    return interseccion

pilaVII = Stack()
pilaV = Stack()

V = ['Luke Skywalker', 'Darth Vader', 'Han Solo', 'Leia Organa', 'Yoda']
VII = ['Rey', 'Luke Skywalker', 'Kylo Ren', 'Darth Vader', 'Poe Dameron', 'BB-8', 'Yoda']

for elemento in V:
    pilaV.push(elemento)
for elemento in VII:
    pilaVII.push(elemento)

pila = interseccion(pilaV, pilaVII)

print("Los personajes que estan en ambos episodios son:", pila)