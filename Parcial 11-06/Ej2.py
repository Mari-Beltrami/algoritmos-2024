from pila import Stack
from dino import dinosaurios

def contar_especies(dinosaurios):
    especies_pila = Stack()
    for dino in dinosaurios:
        especie_ya_contada = False
        lista_temporal = []
        while especies_pila.size() > 0:
            especie = especies_pila.pop()
            lista_temporal.append(especie)
            if especie == dino['especie']:
                especie_ya_contada = True
        for elemento in reversed(lista_temporal):
            especies_pila.push(elemento)
        if not especie_ya_contada:
            especies_pila.push(dino['especie'])
    return especies_pila.size()

def contar_descubridores(dinosaurios):
    descubridores_pila = Stack()
    for dino in dinosaurios:
        descubridor_ya_contado = False
        lista_temporal = []
        while descubridores_pila.size() > 0:
            descubridor = descubridores_pila.pop()
            lista_temporal.append(descubridor)
            if descubridor == dino['descubridor']:
                descubridor_ya_contado = True
        for elemento in reversed(lista_temporal):
            descubridores_pila.push(elemento)
        if not descubridor_ya_contado:
            descubridores_pila.push(dino['descubridor'])
    return descubridores_pila.size()

def dinosaurios_con_t(dinosaurios):
    dinos_t = [dino for dino in dinosaurios if dino['nombre'].startswith('T')]
    return dinos_t

def dinosaurios_menos_275kg(dinosaurios):
    dinos_ligeros = [dino for dino in dinosaurios if float(dino['peso'].replace(' kg', '')) < 275]
    return dinos_ligeros

def dinosaurios_iniciales(dinosaurios):
    pila_iniciales = Stack()
    for dino in dinosaurios:
        if dino['nombre'].startswith(('A', 'Q', 'S')):
            pila_iniciales.push(dino)
    return pila_iniciales

especies_totales = contar_especies(dinosaurios)
print(f"Cantidad de especies: {especies_totales}")

descubridores_totales = contar_descubridores(dinosaurios)
print(f"Cantidad de descubridores distintos: {descubridores_totales}")

dinos_t = dinosaurios_con_t(dinosaurios)
print("Dinosaurios que empiezan con T:")
for dino in dinos_t:
    print(dino['nombre'])

dinos_ligeros = dinosaurios_menos_275kg(dinosaurios)
print("Dinosaurios que pesan menos de 275 Kg:")
for dino in dinos_ligeros:
    print(f"{dino['nombre']}: {dino['peso']}")

pila_iniciales = dinosaurios_iniciales(dinosaurios)
print("Dinosaurios que empiezan con A, Q o S:")
while pila_iniciales.size() > 0:
    dino = pila_iniciales.pop()
    print(dino['nombre'])
