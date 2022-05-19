# -*- coding: utf-8 -*-
# Mauricio Carvajal grupo 05 UTP Telegram: @Mauro_Co
# Ejercicios de repaso de la unidad 1

# De kilos a libras
from tkinter.tix import INTEGER


LIBRA = 0.453592
kilos = 80 #int(input('Ingrese su peso en Kilogramos: '))
print (kilos / LIBRA)

#pitagoras
# c**2 = (a**2 + b**2)
catetoA = 20
catetoB = 10
hipotenusa = (catetoA ** 0.5) + (catetoB ** 0.5)
print (hipotenusa)

#millas a kilometros
MILLA = 1.60934 #kilometros
KILOMETRO = 0.621371 #millas

milla = 10
kilometro = 3
kAm = (kilometro * MILLA)
mAk = (milla / KILOMETRO)

print (kAm)
print (mAk)

# calculadora
def suma (numA, numB):
    sumando = numA + numB
    return sumando
print (suma (2,2))
def resta (numA, numB):
    restando = numA - numB
    return restando
print (resta (6,2))
def multiplicacion (numA, numB):
    multiplicando = numA * numB
    return multiplicando
print (multiplicacion (6,7))
def division (numA, numB):
    dividiendo = numA / numB
    return dividiendo
print (division (6,3))