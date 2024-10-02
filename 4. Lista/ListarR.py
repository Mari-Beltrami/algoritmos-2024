def __agregar_random(lista, cantidad, seleccion = 0):
	from random import randint

	if cantidad == 0:
		return lista
	else:
		if seleccion == 0:
			seleccion = cantidad
		lista.append(randint(1, seleccion * 3))
		__agregar_random(lista, cantidad - 1, seleccion)

def __barrido_continuo(lista, indice = -1, indice_aux = -1):
	if indice == 0:
		print(lista[0], end=", ")
	else:
		if indice == -1:
			indice = len(lista) - 1
			indice_aux = indice
		__barrido_continuo(lista, indice - 1, indice_aux)
		print(lista[indice], end=".\n" if indice == indice_aux else "")
		if indice == indice_aux - 1:
			print(" y ", end="")
		elif indice != indice_aux:
			print(", ", end="")

def __filtrar_barrido(lista, *filtros, filtros_existentes = [], filtros_inexistentes = [], indice = -1, index = False):
	try:
		if not filtros_existentes:
			for filtro in filtros:
				if any(filtro in elemento for elemento in lista):
					filtros_existentes.append(filtro)
				else:
					filtros_inexistentes.append(filtro)
			if not filtros_existentes:
				print("La lista no posee ninguno de los filtros.")
			elif filtros_inexistentes:
				print(f"La lista no posee {"el filtro" if len(filtros_inexistentes) == 1 else "los filtros"} {', '.join(filtros_inexistentes)}.")
		if indice == 0:
			resultado = []
			for filtro in filtros:
				if filtro in filtros_existentes:
					if index:
						resultado.append("0")
					resultado.append(str(lista[0].get(filtro, "Desconocido")))
			print(", ".join(resultado))
		else:
			if indice == -1:
				indice = len(lista) - 1
			__filtrar_barrido(lista, *filtros, filtros_existentes = filtros_existentes, filtros_inexistentes = filtros_inexistentes, indice = indice - 1, index = index)

			resultado = []
			for filtro in filtros:
				if filtro in filtros_existentes:
					if index:
						resultado.append(str(indice))
					resultado.append(str(lista[indice].get(filtro, "Desconocido")))
			print(", ".join(resultado))
	except TypeError:
		print("La función sólo admite listas de diccionarios.")

def busqueda_simple(lista, elemento):
	if elemento in lista:
		print("Posición del elemento buscado:", lista.index(elemento), end=".\n")
	else:
		print("El elemento buscado no está en la lista.")

def busqueda_avanzada(lista, elemento):
	resultado = []
	for diccionario in lista:
		for item in diccionario.values():
			if isinstance(item, str) and elemento in item:
				resultado.append(str(lista.index(diccionario)))
	print("Posición" if len(resultado) == 1 else "Posiciones", "del elemento buscado:", ", ".join(resultado), end=".\n")
	if not resultado:
		print("El elemento buscado no está en la lista.")

def ordenar(lista, criterio, reverse = False):
	lista.sort(key = lambda item: item[criterio], reverse = reverse)

def ordenar_varios(lista, *criterios, reverse=False):
	criterios_validos = [criterio for criterio in criterios if criterio in lista[0]]
	if len(criterios_validos) == 0:
		print ("No existen criterios válidos para ordenar.")
		return
	lista.sort(key=lambda item: tuple(item[criterio] for criterio in criterios_validos), reverse=reverse)
	return lista

def mostrar_lista(lista, titulo):
	print(f"{titulo}:")
	for indice, diccionario in enumerate(lista):
		items = list(diccionario.items())
		print(f"{indice}->", end = " ")
		for elemento in items:
			print(f"{elemento[0]}: {elemento[1]}", end = " | " if items.index(elemento) < len(items) - 1 else "")
		print()

def mostrar_lista_sublista(lista, criterio, titulo, sublista, subtitulo):
	print(f"{titulo}:")
	for indice_1, diccionario in enumerate(lista):
		items = list(diccionario.items())
		print(f"{indice_1} {diccionario[criterio]}:")
		print(f"    {subtitulo}:")
		for indice_2, elemento in enumerate(diccionario[sublista]):
			print('      ', indice_2, elemento["nombre"])
	print()


personajes_star_wars = [
	{"nombre": "Luke Skywalker", "especie": "Humano", "altura": 172},
	{"nombre": "Princesa Leia", "especie": "Humano", "altura": 150},
	{"nombre": "Han Solo", "especie": "Humano", "altura": 180},
	{"nombre": "Darth Vader", "especie": "Humano", "altura": 202, "idioma": "Español"},
	{"nombre": "Yoda", "especie": "Desconocida", "altura": 66},
	{"nombre": "Obi-Wan Kenobi", "especie": "Humano", "altura": 182},
	{"nombre": "Chewbacca", "especie": "Wookiee", "altura": 228},
	{"nombre": "R2-D2", "especie": "Droide", "altura": 96, "idioma": "Robótico"},
	{"nombre": "C-3PO", "especie": "Droide", "altura": 167},
	{"nombre": "Padmé Amidala", "especie": "Humano", "altura": 165}
]

per_heroes = [
  {
	"nombre": "Linterna Verde",
	"año_aparicion": 1940,
	"casa_comic": "DC Comics",
	"biografia": "Miembro de la Tropa de Linternas Verdes, posee un anillo que le otorga poderes basados en la fuerza de voluntad."
  },
  {
	"nombre": "Wolverine",
	"año_aparicion": 1974,
	"casa_comic": "Marvel Comics",
	"biografia": "Mutante con garras retráctiles y habilidades regenerativas, miembro de los X-Men."
  },
  {
	"nombre": "Doctor Strange",
	"año_aparicion": 1963,
	"casa_comic": "Marvel Comics",
	"biografia": "Hechicero supremo del universo Marvel, maestro de las artes místicas y protector de la realidad."
  },
  {
	"nombre": "Capitana Marvel",
	"año_aparicion": 1968,
	"casa_comic": "Marvel Comics",
	"biografia": "Heroína cósmica con poderes de vuelo, fuerza sobrehumana y energía cósmica."
  },
  {
	"nombre": "Mujer Maravilla",
	"año_aparicion": 1941,
	"casa_comic": "DC Comics",
	"biografia": "Princesa amazona y una de las principales defensoras de la justicia y la igualdad en el Universo DC."
  },
  {
	"nombre": "Flash",
	"año_aparicion": 1940,
	"casa_comic": "DC Comics",
	"biografia": "Velocista con la capacidad de correr a velocidades superiores a la luz, miembro de la Liga de la Justicia."
  },
  {
	"nombre": "Star-Lord",
	"año_aparicion": 1976,
	"casa_comic": "Marvel Comics",
	"biografia": "Líder de los Guardianes de la Galaxia, experto en combate y estrategia intergaláctica."
  },
  {
	"nombre": "Superman",
	"año_aparicion": 1938,
	"casa_comic": "DC Comics",
	"biografia": "El Hombre de Acero, uno de los héroes más icónicos de DC con superpoderes sobrehumanos."
  },
  {
	"nombre": "Batman",
	"año_aparicion": 1939,
	"casa_comic": "DC Comics",
	"biografia": "El Caballero Oscuro, detective y luchador experto que protege Gotham City."
  },
  {
	"nombre": "Iron Man",
	"año_aparicion": 1963,
	"casa_comic": "Marvel Comics",
	"biografia": "Tony Stark, genio multimillonario y superhéroe con una armadura tecnológica de alta tecnología."
  },
  {
	"nombre": "Wonder Woman",
	"año_aparicion": 1941,
	"casa_comic": "DC Comics",
	"biografia": "La princesa amazona Diana, guerrera y defensora de la paz y la justicia en el mundo."
  },
  {
	"nombre": "Spider-Man",
	"año_aparicion": 1962,
	"casa_comic": "Marvel Comics",
	"biografia": "Peter Parker, joven héroe con habilidades arácnidas tras ser picado por una araña radiactiva."
  },
  {
	"nombre": "Thor",
	"año_aparicion": 1962,
	"casa_comic": "Marvel Comics",
	"biografia": "Dios nórdico del trueno y miembro de los Vengadores, posee un martillo encantado llamado Mjolnir."
  },
  {
	"nombre": "Aquaman",
	"año_aparicion": 1941,
	"casa_comic": "DC Comics",
	"biografia": "Rey de Atlantis con la capacidad de comunicarse con la vida marina y controlar el agua."
  },
  {
	"nombre": "Green Arrow",
	"año_aparicion": 1941,
	"casa_comic": "DC Comics",
	"biografia": "Oliver Queen, arquero habilidoso y defensor de la justicia con su arco y flechas."
  },
  {
	"nombre": "Hulk",
	"año_aparicion": 1962,
	"casa_comic": "Marvel Comics",
	"biografia": "Bruce Banner, científico transformado en monstruo verde con fuerza increíble."
  },
  {
	"nombre": "Black Widow",
	"año_aparicion": 1964,
	"casa_comic": "Marvel Comics",
	"biografia": "Natasha Romanoff, espía rusa y experta en combate mano a mano y armas."
  },
  {
	"nombre": "Mr. Fantástico",
	"año_aparicion": 1961,
	"casa_comic": "Marvel Comics",
	"biografia": "Líder de los 4 Fantásticos, científico brillante con la capacidad de estirar y deformar su cuerpo."
  },
  {
	"nombre": "La Mujer Invisible",
	"año_aparicion": 1961,
	"casa_comic": "Marvel Comics",
	"biografia": "Miembro de los 4 Fantásticos, posee el poder de hacerse invisible y crear campos de fuerza."
  },
  {
	"nombre": "La Antorcha Humana",
	"año_aparicion": 1961,
	"casa_comic": "Marvel Comics",
	"biografia": "Miembro de los 4 Fantásticos, puede envolverse en llamas y volar a altas velocidades."
  },
  {
	"nombre": "La Cosa",
	"año_aparicion": 1961,
	"casa_comic": "Marvel Comics",
	"biografia": "Miembro de los 4 Fantásticos, posee una fuerza y resistencia sobrehumanas, con piel rocosa."
  },
  {
	"nombre": "Capitán América",
	"año_aparicion": 1941,
	"casa_comic": "Marvel Comics",
	"biografia": "El supersoldado Steve Rogers, símbolo de libertad y justicia con escudo indestructible."
  },
  {
	"nombre": "Ant-Man",
	"año_aparicion": 1962,
	"casa_comic": "Marvel Comics",
	"biografia": "Hanbiografiak Pym o Scott Lang, héroes capaces de cambiar de tamaño y comunicarse con insectos. Usa un traje que lo hace pequeño."
  }
]


# Barrido de personajes_star_wars
for personaje in personajes_star_wars:
	print(personaje)

# Ordenamiento por criterio "name"
ordenar(personajes_star_wars, "especie")

print("-------------------")
for personaje in personajes_star_wars:
	print(personaje)

# Comprensión de listas: Lista con números del 1 al 10
lista = [numero for numero in range(10)]

# La misma lista pero con for
for i in range(10):
	lista.append(i)







"""
# Repaso de los métodos de la clase List
lista = []
print(lista)
lista.append("G")
print(lista)
lista.append("A")
lista.append("K")
print(lista)
lista.sort()
print(lista)
lista.insert(2, "Z")
print(lista)
print(lista.pop(0))
print(lista)
lista.sort(reverse=True)
print(lista)

__barrido_continuo(lista)
"""