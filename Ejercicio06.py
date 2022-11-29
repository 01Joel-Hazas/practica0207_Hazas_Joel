# Escribir una función que convierta un número decimal en binario y otra que convierta un número binario en decimal.

def decimalAbinario(decimal):
    """Función que convierte un número de decimal a binario.
... Parámetros:
...     - decimal: Un número decimal.
...    Salida:
...    Devuelve la conversión en binario del número decimal.
    """
    return int(bin(decimal)[2:])

def binarioAdecimal(binario):
    """Función que convierte un número de binario a decimal.
... Parámetros:
...     - binario: Un número binario.
...    Salida:
...    Devuelve la conversión en decimal del número en binario.
    """
    return int(str(binario), 2)


# Decimal a Binario
print(decimalAbinario(20));
# Binario a Decimal
print(binarioAdecimal(10101));

help(decimalAbinario)
help(binarioAdecimal)