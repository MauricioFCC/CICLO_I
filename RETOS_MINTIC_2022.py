# -*- coding: utf-8 -*-
# Mauricio Carvajal grupo 05 UTP Telegram: @Mauro_Co
# Reto de Mision TIC 2022 en Python

cantidad_bicicletas = int(input())
i=0
lista = []
while i < cantidad_bicicletas:
    entrada = input().split(" ")
    data=[int(entrada[0]),int(entrada[1]),int(entrada[2]),int(entrada[3]),int(entrada[4])]
    i+=1
    lista.append(data)
    
bicicleta_seleccionada = "NO DISPONIBLE"
for index in range(cantidad_bicicletas):
    aprovada = False
    
    condicion_1 = lista[index][0] > 240 and lista[index][0] < 300
    condicion_2 = lista[index][1] >= 160 and lista[index][1] <= 180
    condicion_3 = lista[index][2] >= 240 and lista[index][2] <= 275
    condicion_4 = lista[index][3] <= 50

    if(condicion_1 and condicion_2 and condicion_3 and condicion_4):
        bicicleta_seleccionada = lista[index][4] 

print(bicicleta_seleccionada)