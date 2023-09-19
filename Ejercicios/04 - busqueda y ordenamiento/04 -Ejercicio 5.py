#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      user
#
# Created:     18/09/2023
# Copyright:   (c) user 2023
# Licence:     <your licence>
#-------------------------------------------------------------------------------
# Definir la lista de películas
peliculas = [
    {"título": "Avengers: Infinity War",        "año": 2018, "recaudación": 2048359754, "valoración": 4},
    {"título": "Star Wars: The Return of Jedi", "año": 1983, "recaudación": 572705079,  "valoración": 5},
    {"título": "Iron Man",                      "año": 2008, "recaudación": 585174222,  "valoración": 4},
    {"título": "tu vieja en tanga",             "año": 2017, "recaudación": 200,        "valoración": 10},
    {"título": "Avengers: el despertar",        "año": 2017, "recaudación": 3012312312, "valoración": 5}
    # Agrega más películas aquí
]

# a) Listado ordenado por título de manera ascendente
peliculas_ordenadas_por_titulo = sorted(peliculas, key=lambda x: x["título"])

# b) Listado ordenado por año de lanzamiento de manera ascendente
peliculas_ordenadas_por_año = sorted(peliculas, key=lambda x: x["año"])

# c) Listado ordenado por recaudación de manera descendente
peliculas_ordenadas_por_recaudacion = sorted(peliculas, key=lambda x: x["recaudación"], reverse=True)

# d) Información de la película que más recaudó
pelicula_mas_recaudada = max(peliculas, key=lambda x: x["recaudación"])

# e) Películas con valoración 5
peliculas_valoracion_5 = [pelicula for pelicula in peliculas if pelicula["valoración"] == 5]

# f) Información de la película "Avengers: Infinity War"
pelicula_avengers = next((pelicula for pelicula in peliculas if pelicula["título"] == "Avengers: Infinity War"), None)

# g) Posición de la película "Star Wars: The Return of Jedi"
posicion_star_wars = next((i for i, pelicula in enumerate(peliculas) if pelicula["título"] == "Star Wars: The Return of Jedi"), None)

# h) Total recaudado por películas con "Avengers" en el título
recaudacion_avengers = sum(pelicula["recaudación"] for pelicula in peliculas if "Avengers" in pelicula["título"])

# i) Películas estrenadas en el año 2017
peliculas_2017 = [pelicula for pelicula in peliculas if pelicula["año"] == 2017]

# j) Películas que comienzan con "Iron"
peliculas_iron = [pelicula for pelicula in peliculas if pelicula["título"].startswith("Iron")]

# Imprimir resultados
print("a) Listado ordenado por título de manera ascendente:")
for pelicula in peliculas_ordenadas_por_titulo:
    print(pelicula["título"])

print("\nb) Listado ordenado por año de lanzamiento de manera ascendente:")
for pelicula in peliculas_ordenadas_por_año:
    print(pelicula["título"])

print("\nc) Listado ordenado por recaudación de manera descendente:")
for pelicula in peliculas_ordenadas_por_recaudacion:
    print(pelicula["título"])

print("\nd) Información de la película que más recaudó:")
print(pelicula_mas_recaudada)

print("\ne) Películas con valoración 5:")
for pelicula in peliculas_valoracion_5:
    print(pelicula["título"])

print("\nf) Información de la película 'Avengers: Infinity War':")
if pelicula_avengers:
    print(pelicula_avengers)
else:
    print("La película 'Avengers: Infinity War' no está en la lista.")

print("\ng) Posición de la película 'Star Wars: The Return of Jedi':")
if posicion_star_wars is not None:
    print("La película 'Star Wars: The Return of Jedi' está en la posición", posicion_star_wars)
else:
    print("La película 'Star Wars: The Return of Jedi' no está en la lista.")

print("\nh) Total recaudado por películas con 'Avengers' en el título:", recaudacion_avengers)

print("\ni) Películas estrenadas en el año 2017:")
for pelicula in peliculas_2017:
    print(pelicula["título"])

print("\nj) Películas que comienzan con 'Iron':")
for pelicula in peliculas_iron:
    print(pelicula["título"])
