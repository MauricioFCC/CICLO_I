# -*- coding: utf-8 -*-
# Mauricio Carvajal grupo 05 UTP Telegram: @Mauro_Co
# Resolucion de un ploblema en Python ciclo 2

# retornar un nuevo diccionario con las llaves nombre, edad, atracción,primer_ingreso, total_boleta y apto del cliente

# apto tendrá como valor una variable True si cumple la edad, en el caso contrario será falsa

# atraccion y total_boleta, si no se cumple el rango de edades se le asignara un valor de ‘N/A’ a cada uno

# Si primer_ingreso es verdadero, el total_boleta será el valor de la boleta menos el descuento de
# lo contrario se pagará el valor neto de la boleta.

def cliente (dic):
    outd = {}
    outd ['nombre'] = dic['nombre']
    outd ['edad'] = dic['edad']
    if dic['edad'] > 18:
        outd ['atraccion'] = 'X-Treme'
        outd ['apto'] = True
    if dic ['edad'] < 7:
        outd ['atraccion'] = 'N/A'
        outd ['atraccion'] = 'N/A'
        outd ['apto'] = False
    outd ['primer_ingreso'] = dic ['primer_ingreso']
    if dic ['edad'] > 18 and dic ['primer_ingreso'] == True:
        outd ['total_boleta'] = 20000 - (20000 * 0.05)
    if dic ['edad'] > 18 and dic ['primer_ingreso'] == False:
        outd ['total_boleta'] = 20000
    if dic ['edad'] < 7:
        outd ['total_boleta'] = 'N/A'
    
           
    return outd

dic1 = {'id_cliente' : 1, 'nombre' :  'Johana Fernandez', 'edad' : 20, 'primer_ingreso' : True}
dic2 = {'id_cliente' : 1, 'nombre' :  'Johana Fernandez', 'edad' : 20, 'primer_ingreso' : False}
dic3 = {'id_cliente' : 2, 'nombre' : 'Gloria Suarez', 'edad' : 3, 'primer_ingreso' : True}
dic4 = {'id_cliente' : 3, 'nombre' : 'Tatiana Suarez', 'edad' : 17, 'primer_ingreso' : True}
dic5 = {'id_cliente' : 3, 'nombre' : 'Tatiana Suarez', 'edad' : 17, 'primer_ingreso' : False}
dic6 = {'id_cliente' : 4, 'nombre' : 'Tatiana Ruiz', 'edad' : 8, 'primer_ingreso' : True}
dic7 = {'id_cliente' : 4, 'nombre' : 'Tatiana Ruiz', 'edad' : 8, 'primer_ingreso' : False}

print (cliente(dic1))
print (cliente(dic2))
print (cliente(dic3))
print (cliente(dic4))