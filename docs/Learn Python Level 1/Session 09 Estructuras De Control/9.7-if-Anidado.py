# BootCamp Python Sesión 9 - Condicionales

## 9.7 Condicionales // `If Anidados` en python // Practica
# Cálculo de calificación con lógica anidad
try:
    puntos = 90
    credito_extra = 5

    if puntos >= 90:
        if credito_extra > 0:
            print("Grado A+")
        else:
            print("Grado A+")
    elif puntos >= 80:
        print("Grado B")
    else:
        print("Graco C")

except:
    print("valor Invalido, Ingrese Un valor numérico...")