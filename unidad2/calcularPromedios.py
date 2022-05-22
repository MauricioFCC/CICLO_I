# -*- coding: utf-8 -*-
# Mauricio Carvajal grupo 05 UTP Telegram: @Mauro_Co
# Funcion que calcula el promedio de una nota en Python

def promedioNota (n1, n2, n3, n4):
    nNotas = 4
    promedio = round((n1 + n2 + n3 + n4)/ nNotas, 2)
    return promedio

print ('El promedio es: ', promedioNota(3.0, 2.1, 5.0, 4.7))

# Encapsulamiento con diccionarios
def promedioNotasd (dicNotas):
    sume = 0 # suma inicia en 0
    sume += dicNotas['n1'] # Se agregan valores a 0
    sume += dicNotas['n2']
    sume += dicNotas['n3']
    sume += dicNotas['n4']
    promedios = round(sume / 4, 2) # se divide y redondea a 2 sifras
    return promedios

dicNotas = {} # Diccionario vacio
dicNotas['n1'] = 3.0 # Agregando valores
dicNotas['n2'] = 2.1
dicNotas['n3'] = 5.0
dicNotas['n4'] = 4.7

print ('El promedio es: ', promedioNotasd(dicNotas))

# Diccionario con valores asignados
dicNotas_s2 = {
    'n1' : 3.0,
    'n2' : 2.1,
    'n3' : 5.0,
    'n4' : 4.7
}

print ('El promedio del semestre 2 es: ', promedioNotasd(dicNotas_s2))

# Paso entre funciones
def reportePromedio (dicReport):
    return dicReport['Estudiante']+' = '+str(dicReport['Promedio'])

def generarReporte(dicNota):
    sume = 0
    sume += dicNota['n1']
    sume += dicNota['n2']
    sume += dicNota['n3']
    sume += dicNota['n4']
    promedio = round(sume / 4, 2)
    reporteNotas = {
        'Promedio' : promedio,
        'Estudiante' : dicNota['Estudiante']
    }
    return reporteNotas
dicNota = {
    'Estudiante' : "Mauro",
    'n1' : 3.0,
    'n2' : 2.1,
    'n3' : 5.0,
    'n4' : 4.7
}
print(reportePromedio(generarReporte(dicNota)))