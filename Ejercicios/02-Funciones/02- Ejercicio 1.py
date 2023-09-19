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
Ejercicio 1.
Realizar una función que se llame area_rectangulo() que devuelva el área del
cuadrado a partir de su base y altura
'''

def area_rectangulo(base, altura) :
    area = base * altura

    return area

#Es obligatrio poner return cuando los parametros no tienen valor

base = int(input("Ingrese la Base del cuadrado: "))
altura = int(input("Ingrese la Altura del cuadrado: "))

print(f"El area del cuadrado es de: {area_rectangulo(base, altura)}")