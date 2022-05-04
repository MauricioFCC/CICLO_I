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
capital_B = 650000
plazo = 12
tiempo = 3
tiempoMenor = 2
interes = 0.03
interesPenalidad = 0.02

####### Defenicion de funciones #######
def CDT (C, I, T, P):
    totalInteres = C * I * T / P
    return (totalInteres)
CDTMas = (CDT(capital, interes, tiempo, plazo) + capital)
print (f'Para el usuario {usuario} La cantidad de dinero a recibir, según el monto inicial {capital} para un tiempo de {tiempo} meses es: {CDTMas}')

def porPerdida (C, I):
    perdidaCDT = round(C * I)
    return (perdidaCDT)
CDTMenos = (capital_B - porPerdida(capital_B, interesPenalidad))
print (f'Para el usuario {usuario} La cantidad de dinero a recibir, según el monto inicial {capital_B} para un tiempo de {tiempoMenor} meses es: {CDTMenos}')
