# Escribir una función que calcule el área de un círculo y otra que calcule el volumen de un cilindro
# usando la primera función.


def area_circulo(radio):
    """Función que calcula el área de un círculo.
... Parámetros:
...     - radio: Un número real con el radio del círculo.
...    Salida:
...    Devuelve el área del círculo de radio radius.
    """
    pi = 3.14
    return pi * radio ** 2

def volumen_cilindro(radio, altura):
    """Función que calcula el volumen de un cilindro.
... Parámetros:
...     - radio: Un número real con el radio del clindro.
...     - altura: Un número real con la altura del clindro.
... Salida:
... Devuelve el volumen del clindro de radio radius y altura high.
    """
    return area_circulo(radio) * altura

# Cálculo del área de un circulo
print(area_circulo(20));
# Cálculo del volumen de un cilindro
print(volumen_cilindro(5,6));
help(area_circulo)
help(volumen_cilindro)




