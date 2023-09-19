#-------------------------------------------------------------------------------
# Name:        module2
# Purpose:
#
# Author:      user
#
# Created:     16/09/2023
# Copyright:   (c) user 2023
# Licence:     <your licence>
#-------------------------------------------------------------------------------

#ISBN
#Nombre del libro
#Stock
#Precio del libro

#Cuando el usuario ingrese un 0 como ISBN se deberá imprimir:
#Todos los datos ingresados
#La cantidad total de libros
#El monto total de todos los libros
#El valor promedio de los libros


#Genere un diccionario vacío que luego se irá llenando según lo que ingrese el
#usuario. Pedir los siguientes datos:

libros= {}

isbn = int(input("ingrese ISBN (0 para salir): "))
total_stock = 0
monto_total = 0


while isbn != 0:


    nombre = input("ingrese Nombre: ")
    stock = int(input("ingrese Stock: "))
    precio = int(input("ingrese precio: $"))
    total_stock = total_stock + stock
    monto_total= monto_total + stock * precio


    # Agregar los datos del libro al diccionario
    libros[isbn] = {"nombre": nombre , 'stock': stock, 'precio': precio}

    isbn = int(input("ingrese ISBN (0 para salir): "))

promedio = float(monto_total / total_stock)

for isbn, libro in libros.items():
    print(f"ISBN: {isbn}, Nombre: {libro['nombre']}, Stock: {libro['stock']}, Precio: {libro['precio']}")

print(f"La cantidad total de libros es: {total_stock}")


print(f"El monto total de todos los libros es: {monto_total}")

print(f"El promedio es: {promedio}")


