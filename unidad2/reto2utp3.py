


def cliente(informacion: dict):
    Xtreme = 20000
    Carros = 5000
    Sillas = 10000

    if > 18:
        atraccion = "X-Treme"
    elif <= 18:
        atraccion = "Carros chocones"
    elif  < 15:
        atraccion = "Sillas voladoras"
    else:
        atraccion = "N/A"

    if i>= 7:
        apto = True
    else:
        apto = False
        total_boleta = "N/A"
#despues sigue las operacionnes con if y elif y al final el return
return {"nombre": informacion["nombre"],
        "edad": informacion["edad"], 
        "atraccion": atraccion, 
        "apto": apto, 
        "primer_ingreso": informacion["primer_ingreso"], 
        "total_boleta": total_boleta
        }