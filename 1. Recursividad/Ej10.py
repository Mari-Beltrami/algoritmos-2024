# Desarrollar un algoritmo que cuente la cantidad de dígitos de un número entero

def cantidad_digitos (n):
    if n < 10:
        return 1
    else: 
        return 1 + cantidad_digitos (n // 10)
    
n = int(input("Ingrese un número entero: ")) 
resultado = cantidad_digitos(n)
print (f"La cantidad de dígitos que tiene {n} es de: {resultado}")