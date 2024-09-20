#Implementar una función que calcule la suma de todos los números enteros comprendidos entre cero y un número entero positivo dado
numero = input("Introduce un número entero");
enteros = int(numero)
def suma_enteros (enteros):
    if enteros == 0:
        return 0
    else:
        return enteros + suma_enteros (enteros-1)
        
resultado = suma_enteros(enteros)
print (f"La suma de todos los números entre 0 y {enteros} es: {resultado}")