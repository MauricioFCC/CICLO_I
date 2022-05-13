# -*- coding: utf-8 -*-
# Mauricio Carvajal grupo 05 UTP Telegram: @Mauro_Co
# Resolucion de un ploblema en Python

#print(CDT("AB1012",1000000,3))

####### Variables #######
usuario = 'user' # input('Ingrese nombre Usuario: ')
capital =  1000000 #input('Ingrese Capital: ')
tiempo = 3 #input('Ingrese el Tempo: ')

####### Operaciones en variables #######

def CDT (usuario, operacion,tiempo):
    operacion = capital * 0.03 * tiempo / 12
    porcentajePenal = capital * 0.02
    valorTotal = operacion + capital
    valorPenal = round(capital - porcentajePenal)
    return (operacion)
####### condicional #######
    if tiempo >= '3':
        return (f'Para el usuario {usuario} La cantidad de dinero a recibir, según el monto inicial {capital} para un tiempo de {tiempo} meses es: {valorTotal}')
    else:
        tiempo <= '2'
        return (f'Para el usuario {usuario} La cantidad de dinero a recibir, según el monto inicial {capital} para un tiempo de {tiempo} meses es: {valorPenal}')