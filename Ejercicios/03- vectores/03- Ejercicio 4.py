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

mi_lista = ["hola1", "hola2", "hola3"]


def inverso(vector, indice):


    #verifica que la lista no este vacia
    if indice < 0:
        return          #si esta vacia retorna y fin

    print(vector[indice])
    inverso(vector, indice - 1)         #indice con -1 para encontrar el ultimo de la lista



inverso(mi_lista, len(mi_lista)-1)      #len para que la loangitud sea la cantidad de elementos de la lista - 1