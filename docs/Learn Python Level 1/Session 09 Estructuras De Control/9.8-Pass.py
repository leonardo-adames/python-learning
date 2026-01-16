# BootCamp Python Sesión 9 - Condicionales

# 9.8 Condicionales // `Introducción de pass` en python

# La Declaración De Aprobado
try:
    puntos = 90
    credito_extra = 5

    if puntos >= 90:
        if credito_extra:
            pass            #AQUÍ LA INSTRUCCIÓN PAS DEJA PENDIENTE LA ASIGNACIÓN DELA CONDICIÓN DEL IF ANIDADO
        else:
            print("Grado A+")
    elif puntos >= 80:
        print("Grado B")
    else:
        print("Graco C")

except:
    print("valor Invalido, Ingrese Un valor numérico...")