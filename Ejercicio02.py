# Escribir una función que reciba un número entero positivo y devuelva su factorial.
# Realiza el ejercicio mediante bucles interactivos y mediante una función recursiva.

def factorial(numero):
    """Función que calcula el factorial de un número.
...
... Parámetros:
...     - numero: Un número entero positivo.
... Salida:
...     El resultado del factorial del número introducido.
... """
    factorial = 1
    for i in range(numero):
        factorial *= i + 1
    return factorial

print(factorial(4))
help(factorial)
