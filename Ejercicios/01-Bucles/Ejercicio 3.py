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

# a) Pedir al usuario que ingrese un email
email = input("Ingrese su dirección de email: ")

# b) Verificar si el usuario ingresó una dirección de email (con un "@")
tiene_arroba = False  # Inicializamos una variable para verificar la presencia de "@"

if email.startswith("@"):
    tiene_arroba = False

elif email.endswith("@"):
    tiene_arroba = False

elif " " in email:
    tiene_arroba = False

else:
# Recorremos cada carácter en el email
    for caracter in email:
        if caracter == "@":
            tiene_arroba = True
            break  # Si encontramos "@", podemos salir del bucle


# c) Al finalizar, mostrar por pantalla si es un email o no
if tiene_arroba == True:
    print("Es un email.")
else:
    print("No es un email.")