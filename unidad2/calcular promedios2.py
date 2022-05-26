

def promedionotas(dicNotas: dict):
    sumatoria = 0
    sumatoria += dicNotas["nota1"]
    sumatoria += dicNotas["nota2"]
    sumatoria += dicNotas["nota3"]
    sumatoria += dicNotas["nota4"]
    promedio = round(sumatoria/4, 2)
    if promedio >= 3.0:
        estado = "aprobado"
    else:
        estado = "reprobado"
    definitivo = {
        "prom":promedio,
        "estado":estado
    }
    return definitivo

dicNotas = {}
dicNotas["nota1"] = float(input("ingrese la nota 1"))
dicNotas["nota2"] = float(input("ingrese la nota 2"))
dicNotas["nota3"] = float(input("ingrese la nota 3"))
dicNotas["nota4"] = float(input("ingrese la nota 4"))

total = promedionotas(dicNotas)
print("El promedio total es: " + str(total["prom"]) + " usted ha sido " + total["estado"])
