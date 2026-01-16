# Practica con la ShortHand-if O Abreviatura if

#PRACTICA CON SHORTHAND IF

'''PorMotivos del Día De La Independencia De República Dpminicana, Se Aplica un descuento del 15% De
Deacuento a los clientes que Acumulen una cantidad de $300 puntos o más en la compra de artículos 
partocinadores De {Esta Promoción, El precio del artículo No determina la cantidad de puntos acumulados.'''

Articulo_1= int(input("Por favor, Ingrese El Precio Del Articulo 1: "))
Articulo_2 = float(input("Por favor Ingrese El Precio Del Articulo 2: "))
Articulo_3 = int(input("Por favor Ingrese El Precio Del Articulo 3: "))
Articulo_4 = float(input("Por favor Ingrese El Precio Del Articulo 4: "))
Consumo = Articulo_1 + Articulo_2 + Articulo_3 + Articulo_4 / 4e2
print("Puntos Acumulados: ", Consumo)
print("\n")
print("Este Cliente Califica Para el Descuento") if Consumo >= 300 else print("Este Cliente No Califica Para El Descuento")