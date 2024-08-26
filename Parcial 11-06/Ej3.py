from Jedi import jedis
from pila import Stack

def listar_jedis_por_name(jedis):
    return sorted(jedis, key=lambda jedi: jedi['name'])

def listar_jedis_por_species(jedis):
    return sorted(filter(lambda x: x['species'] is not None, jedis), key=lambda jedi: jedi['species'])

def mostrar_info_jedis(jedis, names):
    return [jedi for jedi in jedis if jedi['name'] in names]

def mostrar_padawans(jedis, masters):
    padawans = []
    for jedi in jedis:
        if jedi['master'] and any(master in jedi['master'] for master in masters):
            padawans.append(jedi['name'])
    return padawans

def mostrar_jedis_humanos_twilek(jedis):
    return [jedi for jedi in jedis if jedi['species'] in ['Human', 'Twi\'lek']]

def listar_jedis_con_a(jedis):
    return [jedi for jedi in jedis if jedi['name'].startswith('A')]

def jedis_con_varios_sables(jedis):
    return [jedi for jedi in jedis if jedi.get('lightsaber_color') is not None and '/' in jedi['lightsaber_color']]

def jedis_con_sables_amarillo_violeta(jedis):
    return [jedi for jedi in jedis if jedi.get('lightsaber_color') is not None and ('Yellow' in jedi['lightsaber_color'] or 'Purple' in jedi['lightsaber_color'])]

def padawans_de_masters(jedis, masters):
    padawans = []
    for jedi in jedis:
        if jedi['master'] and any(master in jedi['master'] for master in masters):
            padawans.append(jedi['name'])
    return padawans

def jedis_con_rango_grand_master(jedis):
    return [jedi for jedi in jedis if jedi['rank'] == 'Grand Master']


jedis_por_name = listar_jedis_por_name(jedis)
jedis_por_species = listar_jedis_por_species(jedis)

print("Listado ordenado por nombre:")
for jedi in jedis_por_name:
    print(jedi['name'])

print("\nListado ordenado por especies:")
for jedi in jedis_por_species:
    print(jedi['species'], jedi['name'])

info_ahsoka_kit = mostrar_info_jedis(jedis, ["Ahsoka Tano", "Kit Fisto"])
print("\nInformación de Ahsoka Tano y Kit Fisto:")
for jedi in info_ahsoka_kit:
    print(jedi)

padawans_yoda_luke = mostrar_padawans(jedis, ["Yoda", "Luke Skywalker"])
print("\nPadawans de Yoda y Luke Skywalker:", padawans_yoda_luke)

jedis_humanos_twilek = mostrar_jedis_humanos_twilek(jedis)
print("\nJedis humanos y twi'lek:")
for jedi in jedis_humanos_twilek:
    print(jedi['name'], "-", jedi['species'])

jedis_con_a = listar_jedis_con_a(jedis)
print("\nJedis que comienzan con A:")
for jedi in jedis_con_a:
    print(jedi['name'])

jedis_varios_sables = jedis_con_varios_sables(jedis)
print("\nJedis que usaron sable de luz de más de un color:")
for jedi in jedis_varios_sables:
    print(jedi['name'], "-", jedi['lightsaber_color'])

jedis_amarillo_violeta = jedis_con_sables_amarillo_violeta(jedis)
print("\nJedis que usaron sable de luz amarillo o violeta:")
for jedi in jedis_amarillo_violeta:
    print(jedi['name'], "-", jedi['lightsaber_color'])

padawans_quigon_mace = padawans_de_masters(jedis, ["Qui-Gon Jinn", "Mace Windu"])
print("\nPadawans de Qui-Gon Jinn y Mace Windu:", padawans_quigon_mace)

jedis_grand_master = jedis_con_rango_grand_master(jedis)
print("\nJedis con rango de Grand Master:")
for jedi in jedis_grand_master:
    print(jedi['name'])
