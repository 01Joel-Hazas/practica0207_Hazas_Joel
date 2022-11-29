# Escribir una función a la que se le pase una cadena <nombre> y muestre por pantalla el saludo ¡hola <nombre>!.

def saludo(nombre):
    """Función que muestra un saludo.
...
... Parámetros:
...     - nombre: Un nombre de tipo string.
... Salida:
...     Un texto con un saludo que muestra ¡hola <nombre>! .
... """

    return "¡hola",nombre,"!"

print(saludo("Joel"))
help(saludo)
