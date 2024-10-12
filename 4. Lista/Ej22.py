# Se dispone de una lista de todos los Jedi, de cada uno de estos se conoce su nombre, maestros,
# colores de sable de luz usados y especie. implementar las funciones necesarias para resolver las
# actividades enumeradas a continuación:
# a. listado ordenado por nombre y por especie;
# b. mostrar toda la información de Ahsoka Tano y Kit Fisto;
# c. mostrar todos los padawan de Yoda y Luke Skywalker, es decir sus aprendices;
# d. mostrar los Jedi de especie humana y twi'lek;
# e. listar todos los Jedi que comienzan con A;
# f. mostrar los Jedi que usaron sable de luz de más de un color;
# g. indicar los Jedi que utilizaron sable de luz amarillo o violeta;
# h. indicar los nombre de los padawans de Qui-Gon Jin y Mace Windu, si los tuvieron

from lista import sort_list, display_list, search

def ejercicio_jedi():
    # Lista de Jedis, cada Jedi es un diccionario con nombre, maestros, colores de sable, y especie
    jedis = [
        {'nombre': 'Luke Skywalker', 'maestros': ['Yoda', 'Obi-Wan'], 'colores_sable': ['verde'], 'especie': 'Humano'},
        {'nombre': 'Ahsoka Tano', 'maestros': ['Anakin Skywalker'], 'colores_sable': ['blanco'], 'especie': 'Togruta'},
        {'nombre': 'Kit Fisto', 'maestros': ['Yoda'], 'colores_sable': ['verde'], 'especie': 'Nautolano'},
        {'nombre': 'Yoda', 'maestros': [], 'colores_sable': ['verde'], 'especie': 'Desconocida'},
        {'nombre': 'Qui-Gon Jinn', 'maestros': ['Dooku'], 'colores_sable': ['verde'], 'especie': 'Humano'},
        {'nombre': 'Mace Windu', 'maestros': [], 'colores_sable': ['violeta'], 'especie': 'Humano'},
        {'nombre': 'Obi-Wan Kenobi', 'maestros': ['Qui-Gon Jinn'], 'colores_sable': ['azul'], 'especie': 'Humano'},
        {'nombre': 'Anakin Skywalker', 'maestros': ['Obi-Wan Kenobi'], 'colores_sable': ['azul'], 'especie': 'Humano'},
    ]

    # a. Listado ordenado por nombre y por especie
    sort_list(jedis, 'nombre')
    print("Listado ordenado por nombre y especie:")
    display_list(jedis)

    # b. Mostrar toda la información de Ahsoka Tano y Kit Fisto
    print("\nInformación de Ahsoka Tano y Kit Fisto:")
    for jedi_name in ['Ahsoka Tano', 'Kit Fisto']:
        index = search(jedis, 'nombre', jedi_name)
        if index is not None:
            print(jedis[index])

    # c. Mostrar todos los padawan de Yoda y Luke Skywalker
    print("\nPadawans de Yoda y Luke Skywalker:")
    for jedi in jedis:
        if 'Yoda' in jedi['maestros'] or 'Luke Skywalker' in jedi['maestros']:
            print(jedi['nombre'])

    # d. Mostrar los Jedi de especie humana y twi'lek
    print("\nJedis de especie humana y twi'lek:")
    for jedi in jedis:
        if jedi['especie'] in ['Humano', "Twi'lek"]:
            print(jedi['nombre'])

    # e. Listar todos los Jedi que comienzan con A
    print("\nJedis que comienzan con A:")
    for jedi in jedis:
        if jedi['nombre'].startswith('A'):
            print(jedi['nombre'])

    # f. Mostrar los Jedi que usaron sable de luz de más de un color
    print("\nJedis que usaron sable de luz de más de un color:")
    for jedi in jedis:
        if len(jedi['colores_sable']) > 1:
            print(jedi['nombre'])

    # g. Indicar los Jedi que utilizaron sable de luz amarillo o violeta
    print("\nJedis que usaron sable de luz amarillo o violeta:")
    for jedi in jedis:
        if 'amarillo' in jedi['colores_sable'] or 'violeta' in jedi['colores_sable']:
            print(jedi['nombre'])

    # h. Indicar los nombres de los padawans de Qui-Gon Jinn y Mace Windu, si los tuvieron
    print("\nPadawans de Qui-Gon Jinn y Mace Windu:")
    for jedi in jedis:
        if 'Qui-Gon Jinn' in jedi['maestros'] or 'Mace Windu' in jedi['maestros']:
            print(jedi['nombre'])

# Llamar a la función del ejercicio
if __name__ == "__main__":
    ejercicio_jedi()