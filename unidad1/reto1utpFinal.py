# -*- coding: utf-8 -*-
# Mauricio Carvajal grupo 05 UTP Telegram: @Mauro_Co
# Resolucion de un ploblema en Python ciclo 1

def CDT (usuario, capital, tiempo):
    if tiempo > 2: 
        intereses = (capital * 0.03 * tiempo) / 12
        valorTotal = intereses + capital
    else:
        porcentajePenal = capital * 0.02
        valorTotal = round(capital - porcentajePenal)
    
    output = (f'Para el usuario {usuario} La cantidad de dinero a recibir, según el monto inicial {capital} para un tiempo de {tiempo} meses es: {valorTotal}')
    
    return output

usuario = input('Ingrese Usuario: ')
capital = int(input('Ingrese capital: '))
tiempo = int(input('ingrse el tiempo en meses: '))
output = CDT (usuario, capital, tiempo)
print (output)

