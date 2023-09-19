#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      user
#
# Created:     10/09/2023
# Copyright:   (c) user 2023
# Licence:     <your licence>
#-------------------------------------------------------------------------------
'''
Ejercicio 4.
Definir una lista
Contar los elementos de esa lista
Al finalizar mostrar por pantalla la cantidad de elementos de la lista
No utilizar función len
'''

lista= [1,3,5,6, "asdf" , 7.5 , "hola", [1,2,3], 1]
contador = 0

for i in lista :
    contador= contador +1
    print(f"elemento: {i}" )

print(f"La cantidad de elementos es: {contador}")