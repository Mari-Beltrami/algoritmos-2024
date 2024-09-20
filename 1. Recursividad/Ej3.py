#Implementar una función para calcular el producto de dos números enteros dados

def calcular_producto (n1, n2):
    #caso base
    if n1==0 or n2==0:
        return 0
    #llamada recursiva
    else:
        return n1 + calcular_producto(n1, n2-1)
    
n1 = int(input("Ingrese el primer número: "))   
n2 = int(input("Ingrese el segundo número: "))
resultado = calcular_producto(n1,n2)
print (f"El resultado del producto entre {n1} y {n2} es: {resultado}")
        
        