## **INTRODUCCIÓN INFORMAL A ALGUNOS CONCEPTOS BÁSICOS DE PYTHON**

En los siguientes ejemplos, la entrada y la salida se distinguen por la presencia o ausencia de indicaciones **( >>> y … )**: para repetir el ejemplo, debe escribir todo después de la indicación cuando esta aparezca; las líneas que no comiencen con una indicación se imprimen desde el intérprete. Tenga en cuenta que una indicación secundaria en una línea sola en un ejemplo significa que debe escribir una línea en blanco; esto se utiliza para finalizar un comando de varias líneas.

Puede utilizar **el botón “Copiar”** (aparece en la esquina superior derecha cuando pasa el cursor sobre un ejemplo de código o lo toca), que elimina las indicaciones y omite la salida, para copiar y pegar las líneas de entrada en su intérprete.

Muchos de los ejemplos de este manual, incluso los introducidos en el indicador interactivo, incluyen **comentarios**. En Python, los comentarios comienzan con el carácter **almohadilla (#)** y se extienden hasta el final de la línea. Un comentario puede aparecer al principio de una línea o después de un espacio en blanco o código, pero no dentro de una cadena literal. Un carácter almohadilla dentro de una cadena literal es simplemente un carácter almohadilla. Dado que los comentarios sirven para aclarar el código y Python no los interpreta, pueden omitirse al escribir ejemplos.

Algunos ejemplos:

```python
# este es el primer comentario
spam = 1  # y este es el segundo comentario
          # ... and now a third!
text = "# This is not a comment because it's inside quotes."
```


## **Usar Python como calculadora**

Probemos algunos comandos sencillos de Python. Inicie el intérprete y espere el indicador principal **>>>.** (No debería tardar mucho).

**Números**

El intérprete actúa como una calculadora simple: se escribe una expresión y se escribe el valor. La sintaxis de las expresiones es sencilla: los operadores **+, -, * y /** se pueden usar para realizar operaciones aritméticas; los paréntesis **( ())** se pueden usar para agrupar. 

**Por ejemplo:**

```python
2 + 2

50 - 5*6

(50 - 5*6) / 4

8 / 5  # division always returns a floating-point number
```

Los números enteros **(p. ej. 2, 4, 20)** tienen tipo int, mientras que los que tienen una parte fraccionaria **(p. ej. 5.0, , 1.6)** tienen tipo float. Veremos más sobre los tipos numéricos más adelante en el tutorial.

División **( /)** siempre devuelve un valor de punto flotante. Para realizar una división base y obtener un resultado entero, se puede usar el **//** operador; para calcular el resto, se puede usar **%:**

```python
17 / 3  # classic division returns a float


17 // 3  # floor division discards the fractional part

17 % 3  # the % operator returns the remainder of the division

5 * 3 + 2  # floored quotient * divisor + remainder
```

**Con Python, es posible utilizar el **operador para calcular potencias [ 1 ] :**

```python
5 ** 2  # 5 squared

2 ** 7  # 2 to the power of 7
```

## **Texto**

Python puede manipular texto (representado por tipo str, las llamadas "cadenas"), así como números. Esto incluye caracteres " !", palabras " rabbit", nombres " Paris", oraciones **" ", etc. " ".Se pueden escribir entre comillas simples ( )** o **dobles ( )** con el mismo resultado [ 2 ] Got your back.Yay! **:'...'"..."**

```python
'spam eggs'  # single quotes
'spam eggs'
"Paris rabbit got your back :)! Yay!"  # double quotes
'Paris rabbit got your back :)! Yay!'
'1975'  # digits and numerals enclosed in quotes are also strings
'1975'
```

