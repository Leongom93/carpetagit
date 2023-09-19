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
Genere una lista vacía que luego se irá llenando según lo que ingrese el
usuario. Pedir los siguientes datos:
Nombre de sucursal
Numero de sucursal
Cantidad de ventas
Venta total de la sucursal
Se deberá sacar el promedio de ventas en pesos de esa sucursal
Cuando el usuario ingrese un 0 como nombre de sucursal se deberá imprimir:
Todos los datos ingresados
El promedio de cada sucursal
El total vendido por toda la cadena
'''

lista=[]
numero= int(input("Ingrese sucursal numero: "))
contador = 0
total= 0
promedio = 0
total_ventas=0

while numero != 0:
    nombre= (input("Ingrese nombre de sucursal: "))
    ventas= int(input("Ingrese cantidad de ventas: "))
    total=total+ventas
    promedio = total/ventas
    total_ventas= total_ventas + total



    lista.append(numero)
    lista.append(nombre)
    lista.append(ventas)
    lista.append(total)
    lista.append(promedio)
    lista.append(total_ventas)

    contador = contador + 1


    if contador == 5:
        break
    elif numero ==0:
        break
    else:
        numero= int(input("Ingrese sucursal numero: "))

promedio_total = total/total_ventas

print(lista)
print(f"Nro Sucursal: {numero}")
print(f"Sucursal: {nombre}")
print(f"Ventas: {ventas}")
print(f"Total sucursal: {total}")
print(f"Promedio: {promedio}")
print(f"Promedio: {total_ventas}")






