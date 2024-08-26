# Desarrollar una función que permita convertir un número romano en un número decimal.

def romano_a_decimal(romano):
    valores_romanos = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    
    if len(romano)==0:
        return 0
    
    if len(romano)==1:
        return valores_romanos[romano]
    
    if valores_romanos[romano[0]] < valores_romanos[romano[1]]:
        return valores_romanos[romano[1]] - valores_romanos[romano[0]] + romano_a_decimal(romano[2:])
    else:
        return valores_romanos[romano[0]] + romano_a_decimal(romano[1:])
    
numero_romano = "IV"
print("Número romano:", numero_romano)
print("Número decimal:", romano_a_decimal(numero_romano))


