# Escribir una función que reciba una muestra de números en una lista y devuelva otra lista con sus cuadrados.

def listaCuadrados(numeros):
    """Función que recibe una muestra de números en una lista y devuelva otra lista con sus cuadrados.
... Parámetros:
...     - numeros: Una lista de numeros.
... Salida:
...    Devuelve otra lista con sus cuadrados.
    """
    listaCuadrados = []
    for i in numeros:
        listaCuadrados.append(i ** 2)
    return listaCuadrados

listaNumeros = [8, 4, 6, 2, 6, 8]
print(listaCuadrados(listaNumeros))
help(listaCuadrados)
