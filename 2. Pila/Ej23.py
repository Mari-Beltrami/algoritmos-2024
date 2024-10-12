# Dada una pila con los valores promedio de temperatura ambiente de cada día del mes de abril,
# obtener la siguiente información sin perder los datos:
# a. determinar el rango de temperatura del mes, temperatura mínima y máxima;
# b. calcular el promedio de temperatura (o media) del total de valores;
# c. determinar la cantidad de valores por encima y por debajo de la media.

from pila import Stack

def analizar_temperaturas (pila_temperaturas):
    #Crear una copia de la pila para no perder los datos originales
    pila_auxiliar = Stack()
    pila_temperaturas_copia = Stack()
    
    #Pasar los elementos de la pila original a la copia
    while pila_temperaturas.size() > 0:
        valor = pila_temperaturas.pop()
        pila_temperaturas_copia.push(valor)
        pila_auxiliar.push(valor)
        
    #Inicializar las variables para cálculo
    temperatura_min = float ('inf')
    temperatura_max = float('-inf')
    suma_temperaturas = 0
    total_dias = pila_auxiliar.size()
    
    #Recorrer la pila auxiliar para calcular temperatura mínima, máxima y suma
    while pila_auxiliar.size() > 0:
        temperatura = pila_auxiliar.pop()
        
        #Determinar temperatura mínima y máxima 
        if temperatura < temperatura_min:
            temperatura_min = temperatura
            
        if temperatura > temperatura_max:
            temperatura_max = temperatura
            
        #Calcular la suma de temperaturas
        suma_temperaturas += temperatura
    
    #Calcular promedio de temperatura    
    promedio_temperatura = suma_temperaturas / total_dias
    
    #Inicializar contadores para temperaturas por encima y por debajo de la media
    dias_por_encima = 0 
    dias_por_debajo = 0
    
    # Recorrer la pila copia para contar temperaturas por encima y por debajo del promedio
    while pila_temperaturas_copia.size() > 0:
        temperatura = pila_temperaturas_copia.pop()

        if temperatura > promedio_temperatura:
            dias_por_encima += 1
        elif temperatura < promedio_temperatura:
            dias_por_debajo += 1

    # Mostrar resultados
    print(f"Temperatura mínima del mes: {temperatura_min}°C")
    print(f"Temperatura máxima del mes: {temperatura_max}°C")
    print(f"Promedio de temperatura del mes: {promedio_temperatura:.2f}°C")
    print(f"Días con temperatura por encima del promedio: {dias_por_encima}")
    print(f"Días con temperatura por debajo del promedio: {dias_por_debajo}")

# Crear una pila con las temperaturas del mes de abril
temperaturas_abril = Stack()
valores_temperatura = [22, 25, 19, 23, 21, 24, 26, 28, 27, 25, 22, 23, 24, 26, 19, 20, 21, 22, 23, 24, 25, 27, 28, 29, 30, 21, 20, 19, 18, 22]
for valor in valores_temperatura:
    temperaturas_abril.push(valor)

# Llamar a la función para analizar las temperaturas
analizar_temperaturas(temperaturas_abril)