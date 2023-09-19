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
Ejercicio 6.
Realizar una función que se llame separar() que reciba una lista de nros y
devuelva dos listas ordenadas.
La primera con nros pares.
La segunda con nros impares.
'''
def separar(lista):
    pares = []
    impares = []

    for numero in lista:
        if numero % 2 ==0:
            pares.append(numero)

        else:
            impares.append(numero)


    return pares, impares
lista = [1,2,3,4,5,6,7,8,9,10]


# Al primer return "pares" se asigna al primer termino "lista_pares"
# El segundo return "impares" se asigna al segundo termino "lista_impares"

lista_pares, lista_impares = separar(lista)

print("Lista de numeros pares")
print(lista_pares)

print("Lista de numeros impares")
print(lista_impares)