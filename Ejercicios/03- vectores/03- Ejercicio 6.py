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
Ejercicio 6.
Dado un nro iniciar una cuenta regresiva por medio de una función recursiva,
imprimir la cuenta y al llegar a cero imprimir por pantalla "¡Booom!".
'''

import time

'''
def bomba():
    numero = int(input("Ingrese un numero: "))

    while numero != 0:
        print (numero)
        time.sleep(1)
        numero -= 1

    print(0)
    print("¡Booom!")


bomba()
'''

#Funcion recursiva:  Que se llama asi misma

def bomba (numero):

    #numero = int(input("Ingrese un numero: "))

    if numero == 0:
        print(0)
        time.sleep(1)
        print("¡Booom!")

    else:

        print(numero)
        time.sleep(1)
        bomba(numero-1)


numero = int(input("Ingrese un numero: "))
bomba(numero)

