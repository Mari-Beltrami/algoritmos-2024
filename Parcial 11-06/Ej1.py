import random

def listar_elementos(lista):
    if len(lista) == 0:
        return
    else:
        print(lista[-1])
        listar_elementos(lista[:-1])

numeros = [random.randint(0, 100) for _ in range(10)]

print("Lista original:", numeros)
print("Lista en orden inverso:")
listar_elementos(numeros)
