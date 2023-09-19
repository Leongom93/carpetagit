#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      user
#
# Created:     17/09/2023
# Copyright:   (c) user 2023
# Licence:     <your licence>
#-------------------------------------------------------------------------------
'''
Ejercicio 7.
Escriba una función recursiva para contar en cuantos intentos se puede adivinar
el número de un dado.
Pasos a seguir:
Genere un nro random
Solicite al usuario que ingrese un nro
Verifique si es correcto informe que acerto en X intento
Si no acertó, cuente el intento y vuelva a solicitar el nro
'''

# Puede utilizar la siguiente librería para generar los nros random al principiodel archivo

import random

n = random.randint(1,6)


def adivinar(numero, contador=-1):

    contador = contador + 1


    if numero != n:

        numero = int(input("Ingrese un numero: "))
        adivinar(numero, contador)

    else:
        print (f'Adivinaste en {contador} intentos')



numero = 0
adivinar(numero)