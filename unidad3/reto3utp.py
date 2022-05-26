# -*- coding: utf-8 -*-
# Mauricio Carvajal grupo 05 UTP Telegram: @Mauro_Co
# Resolucion de un ploblema en Python ciclo 3

# Diccionario de salida:
# Producto consultado : {idProducto} Descripción {dProducto} #Parte {pnProducto} Cantidad vendida {cvProducto} Stock {sProducto} Comprador {nComprador} Documento{cComprador} Fecha Venta {fVenta}
# “No hay registro de venta de ese producto”

# funciones registro de ventas Auto partes
from enum import auto


def AutoPartes(ventas: list):
    resultado = {}
    for i in range(len(ventas)): # desde x en el rango(tamaño(lista))ingresa al diccionario
        resultado[i] = ventas[i] 
    return resultado

# Funcion de consulta de registro
def consultaRegistro(ventas, idProducto):
    resultadoB = {}
    for i in ventas:
        if idProducto == ventas[i][0][0]:
            resultadoB[i] = ventas[i]
    resultadoC = ''
    if len(resultadoB) == 0:
        resultadoC = 'No hay registro de venta de ese producto'
    else:
        for i in resultadoB:
            resultadoC = 'Producto consultado : {ventas[i][0][0]}, Descripción: {ventas[i][0][1]}, #Parte: {ventas[i][0][2]}, Cantidad vendida: {ventas[i][0][3]}, Stock: {ventas[i][0][4]}, Comprador {ventas[i][0][5]}, Documento{ventas[i][0][6]}, Fecha Venta {ventas[i][0][7]} \n'
           # .format(ventas[i][0][0], ventas[i][0][1], ventas[i][0][2], ventas[i][0][3], ventas[i][0][4], ventas[i][0][5], ventas[i][0][6], ventas[i][0][7])
    return print(resultadoC)

# Ejemplo entradas lista de tuplas
ventasA = [
(2001,'rosca', 'PT29872',2, 45,'Luis Molero', 3456,'12/06/2020'),
(2010,'bujía', 'MS9512',4, 15,'Carlos Rondon', 1256,'12/06/2020'),
(2010,'bujía', 'ER6523',9, 36,'Pedro Montes', 1243,'12/06/2020'),
(3578,'tijera', 'QW8523',1, 128,'Pedro Faria', 1456,'12/06/2020'),
(9251,'piñón', 'EN5698',2, 8,'Juan Peña', 565,'12/06/2020')]

#print (AutoPartes(ventasA))
(consultaRegistro(AutoPartes(ventasA),0))