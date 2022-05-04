# -*- coding: utf-8 -*-
# Mauricio Carvajal grupo 05 UTP Telegram: @Mauro_Co
# Resolucion de un ploblema en Python

# Valor intereses = cantidad $ CDT * 3% (0.03) * tiempo / 12
# Valor total = Valor intereses + cantidad $ CDT

# Penalidad = Si se retira antes del periodo se aplica penalidad del 2%.
# Valor a perder = cantidad $ CDT * 2% (0.02)
# Valor total = cantidad $ CDT - valor a perder

####### Variables #######
usuario = 'usuario'
capital = 1000000
plazo = 12
tiempo = 3
interes = 0.03

####### Operaciones en variables #######
CDT = capital * interes * tiempo / plazo
porcentajePerdida = capital * 0.02
valorTotal = CDT + capital
valorPerdida = round(capital - porcentajePerdida)

####### condicional #######
if tiempo == 3:
    print (f'Para el usuario {usuario} La cantidad de dinero a recibir, según el monto inicial {capital} para un tiempo de {tiempo} meses es: {valorTotal}')
elif tiempo == 2:
    print (f'Para el usuario {usuario} La cantidad de dinero a recibir, según el monto inicial {capital} para un tiempo de {tiempo} meses es: {valorPerdida}')
else: print ('Ingrese un numero de meses entre 2 y 3')