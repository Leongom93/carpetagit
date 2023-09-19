#-------------------------------------------------------------------------------
# Name:        module3
# Purpose:
#
# Author:      inap
#
# Created:     05/09/2023
# Copyright:   (c) inap 2023
# Licence:     <your licence>
#-------------------------------------------------------------------------------
"""
Ejercicio 2.

"""

# Utilizar el valor 3.14159 como pi
PI = 3.14159

# Realizar una función que se llame area_circulo()
# que devuelva el área del círculo a partir de su radio.
def area_circulo(radio) :
    # calculo area del circulo
    area = PI * radio ** 2

    # devuelvo valor del area
    return area

radio = int(input('Ingrese un radio: '))

print(area_circulo(radio))

