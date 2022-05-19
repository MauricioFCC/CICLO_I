# -*- coding: utf-8 -*-
# Mauricio Carvajal grupo 05 UTP Telegram: @Mauro_Co
# Resolucion de un ploblema en Python ciclo 2

clientes = {
'cliente' : {'id_cliente' : 1,  'nombre' : 'Johana Fernandez', 'edad' : '20', 'primer_ingreso' : True},
'cliente' : {'id_cliente' : 2,  'nombre' : 'Gloria Suarez', 'edad' : '3', 'primer_ingreso' : True},
'cliente' : {'id_cliente' : 3,  'nombre' : 'Tatiana Suarez', 'edad' : '17', 'primer_ingreso' : True},
'cliente' : {'id_cliente' : 4,  'nombre' : 'Tatiana Ruiz', 'edad' : '8', 'primer_ingreso' : True},
}
atracciones = {
'X-Treme' : {'valor' : 20000, 'edad' : 18, 'primer_ingreso' : True, 'descuento%' : 5},
'Carroschocones' : {'valor' : 5000,'edad' : [15, 18],'primer_ingreso' : True,'descuento%' : 7},
'Sillas voladoras' :  {'valor' : 10000,'edad' : [7, 15],'primer_ingreso' : True,'descuento%' : 5},
}

filtrado = {
"nombre" : "",
"edad" : "",
"atraccion" : "", # N/A si no es apto
"primer_ingreso" : "", # si es true = valor - % descuento, else valor neto
"total_boleta" : "", # N/A si no es apto
"apto" : "" # bool
}

