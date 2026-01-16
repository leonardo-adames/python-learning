# Aquí puedes practicar libremente con el if
'''edad = 28 #-----------------------> Variable definida - edad vale 28
#if edad >= 18:  #-----------------> Pregunta si la edad es mayor o igual que 18        
#    print("Eres Mayor De Edad")#--> Da salida por consola si la condición anterior se cumple


#Aplicando Sentensia if + else Operador and
#edad = 28 #------------> Definición de variable edad
#licencia = True #------------> Definición de variable licencia

#if edad >= 18 and licencia == True:
#    print("Ya eres Mayor de Edad, tienes:",edad, "Años")
#    print("¿Ya tienes licencia?:",licencia,", entonces puedes conducir")

#Comprobación de control status estudiantes
Calificacion = 65

if Calificacion >= 90:
    print("Aprobado")
elif Calificacion >= 80:
    print("Aprobado")
elif Calificacion >= 70:
    print("Aprobado")
else:
    print("Reprobado")
'''

# Ejemplo practico de Calificación de números
try:
    number = float(input("Por favor, Ingrese un número"))
    
    if number > 0:
        print("El Número es mayor que cero")
    elif number < 0:
        print("El número es menor que cero")
    else:
        print("El numero es cero")

except ValueError:
    print("Error: Caracter invalido, solo ingresar caracrer válido")