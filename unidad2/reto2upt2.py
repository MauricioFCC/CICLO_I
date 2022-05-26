# -*- coding: utf-8 -*-
# Mauricio Carvajal grupo 05 UTP Telegram: @Mauro_Co
# Resolucion de un ploblema en Python ciclo 2

# retornar un nuevo diccionario con las llaves nombre, edad, atracción,primer_ingreso, total_boleta y apto del cliente

# apto tendrá como valor una variable True si cumple la edad, en el caso contrario será falsa

# atraccion y total_boleta, si no se cumple el rango de edades se le asignara un valor de ‘N/A’ a cada uno

# Si primer_ingreso es verdadero, el total_boleta será el valor de la boleta menos el descuento de
# lo contrario se pagará el valor neto de la boleta.

def cliente (informacion : dict) -> dict:
    # uso de variables
    idClient = informacion ['id_cliente']
    name = informacion ['nombre']
    date = informacion ['edad']
    firstIn = informacion ['primer_ingreso']
    # Condicionales
    if date >= 18:
        atraccion = 'X-Treme'
        apto = True
        if firstIn == True:
            total_boleta = 20000 - (20000 * 0.05)
        else:
            firstIn == False
            total_boleta = 20000   
    elif date >= 15 <= 18:
        atraccion = 'Carros chocones'
        apto = True
        if firstIn == True:
            total_boleta = 5000 - (5000 * 0.07)
        else:
            firstIn == False
            total_boleta = 5000
    elif date >= 7 <= 15:
        atraccion = 'Sillas voladoras'
        apto = True
        if firstIn == True:
            total_boleta = 10000 - (10000 * 0.05)
        else:
            firstIn == False
            total_boleta = 10000
    else:
        atraccion = 'N/A'
        apto = False
        total_boleta = 'N/A'
    # Diccionario de salida
    output = {
        'nombre' : name,
        'edad': date, 
        'atraccion': atraccion,
        'apto': apto,
        'primer_ingreso': firstIn,
        'total_boleta': total_boleta
        }
    # Retorno de la funcion
    return output

# diccionarios para pruebas
dic = {'id_cliente' : 1, 'nombre' :  'Johana Fernandez', 'edad' : 20, 'primer_ingreso' : True}
dic2 = {'id_cliente' : 1, 'nombre' :  'Johana Fernandez', 'edad' : 20, 'primer_ingreso' : False}
dic3 = {'id_cliente' : 2, 'nombre' : 'Gloria Suarez', 'edad' : 3, 'primer_ingreso' : True}
dic4 = {'id_cliente' : 3, 'nombre' : 'Tatiana Suarez', 'edad' : 17, 'primer_ingreso' : True}
dic5 = {'id_cliente' : 3, 'nombre' : 'Tatiana Suarez', 'edad' : 17, 'primer_ingreso' : False}
dic6 = {'id_cliente' : 4, 'nombre' : 'Tatiana Ruiz', 'edad' : 8, 'primer_ingreso' : True}
dic7 = {'id_cliente' : 4, 'nombre' : 'Tatiana Ruiz', 'edad' : 8, 'primer_ingreso' : False}
print (cliente (dic))
print (cliente (dic2))
print (cliente (dic3))
print (cliente (dic4))
print (cliente (dic5))
print (cliente (dic6))
print (cliente (dic7))