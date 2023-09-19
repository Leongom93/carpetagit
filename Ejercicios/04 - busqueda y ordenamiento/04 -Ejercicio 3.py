personajes_star_wars = [
    "luke skywalker",
    "darth vader",
    "leia organa",
    "han solo",
    "obi-wan kenobi",
    "yoda",
    "hera syndulla",
    "darth maul",
    "chewbacca",
    "lando calrissian"
]

personajes_ordenados = sorted(personajes_star_wars)

for personaje in personajes_ordenados:
    print(personaje)


if "darth maul" in personajes_star_wars:
    posicion_darth_maul = personajes_star_wars.index("darth maul")
    print(f'darth maul se encuentra en la posicion: {posicion_darth_maul}')

else:
    print("darth maul no se encuentra en la lista de personajes")

if "hera syndulla" in personajes_star_wars:
    indice_hera = personajes_star_wars.index("hera syndulla")
    personaje_antes = personajes_star_wars[indice_hera -1]
    personaje_despues = personajes_star_wars[indice_hera +1]

    print("Personaje antes de Hera Syndulla:", personaje_antes)
    print("Personaje después de Hera Syndulla:", personaje_despues)

else:
    print("Hera Syndulla no se encuentra en la lista")

personajes_con_l= [personaje for personaje in personajes_star_wars if personaje.startswith("l")]

print(f"Los personajes que comienzan con l son: ")

for personaje in personajes_con_l:
    print (personaje)