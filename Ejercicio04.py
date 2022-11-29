# Escribir una función que reciba una muestra de números en una lista y devuelva su media.

def media(numeros):
    """Función que calcula la media de una lista de numeros.
... Parámetros:
...     - numeros: Una lista de numeros.
... Salida:
...    Devuelve la media de los numeros introducidos.
    """
    media = sum(numeros)/len(numeros)
    return media

listaNumeros = [8,4,6,2,6,8]
print(media(listaNumeros))
help(media)