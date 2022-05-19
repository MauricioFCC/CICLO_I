# -*- coding: utf-8 -*-
# Mauricio Carvajal grupo 05 UTP Telegram: @Mauro_Co
# leer un numero y determinar si es de uno o varios caracteres

def tieneDigitos (n):
    count = len(str(numer))
    return (f'El numero tiene {count} digitos')
numer = (input('Ingrese un numero: '))
count = tieneDigitos (numer)
print (count)


num = int (input ('Ingrese un numero: '))
if num < 0:
    num = num * (-1)
if num >= 1 and num <= 9:
        print ('El numero tiene 1 digito')
else:
    if num >= 10 and num <= 99:
            print ('El numero tiene 2 digitos')
    else:
        if num >= 100 and num <= 999:
                print ('El numero tiene 3 digitos')
        else: 
            if num >= 1000 and num <= 9999:
                    print ('El numero tiene 4 digitos')
            else:
                    print ('El numero tiene mas de 4 numeros')