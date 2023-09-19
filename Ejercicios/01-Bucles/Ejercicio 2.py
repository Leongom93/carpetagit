#-------------------------------------------------------------------------------
# Name:        module1
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
Pedir al usuario que ingrese dos nros
Luego imprimir 3 opciones (1. sumar, 2. restar y 3. multiplicar)
Pedir al usuario que ingrese una opción
Verificar la opción del usuario
Mientras que el usuario no ingrese una opción correcta se volverá a pedir que
ingrese una opción
Ejecutar la operación
Mostrar por pantalla el resultado

"""

nro1 = int(input('Ingrese un nro: '))
nro2 = int(input('Ingrese otro nro: '))

print(" 1. sumar\n 2. restar\n 3. multiplicar")

opcion = int(input('Seleccione una opción: '))

while (opcion not in [1,2,3]) :
    opcion = int(input('Seleccione una opción: '))

if (opcion == 1) :
    resultado = nro1 + nro2
elif (opcion == 2) :
    resultado = nro1 - nro2
else :
    resultado = nro1 * nro2

print(resultado)

