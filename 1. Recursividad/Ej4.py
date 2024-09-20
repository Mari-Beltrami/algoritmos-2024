# Implementar una función para calcular la potencia dado dos números enteros, el primero re-
# presenta la base y segundo el exponente.

def calcular_potencia (n1, n2):
    #caso base
    if n2 == 0:
        return 1
    #llamada recursiva
    else: 
        return n1 * calcular_potencia (n1, n2-1)
    
n1 = int(input("Ingrese el primer número:"))
n2 = int(input("Ingrese el segundo número:"))
resultado = calcular_potencia(n1,n2)
print (f"La potencia de {n1} sobre {n2} es: {resultado}")