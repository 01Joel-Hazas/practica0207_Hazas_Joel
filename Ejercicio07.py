# Escribir un programa que reciba una cadena de caracteres y devuelva un diccionario con cada palabra
# que contiene y su frecuencia. Escribir otra función que reciba el diccionario generado con la función anterior
# y devuelva una tupla con la palabra más repetida y su frecuencia.

def contar_palabras(lorem_ipsum):
    """Función que crea un diccionario con una lista de palabras de un texto recibido.
...
... Parámetros:
...     - lorem_ipsum: Texto.
... Salida:
...     Un diccionario con cada palabra del texto.
... """

    textoObtenido = lorem_ipsum.split()
    colecc_palabras = {}
    for i in textoObtenido:
        if i in colecc_palabras:
            colecc_palabras[i] += 1
        else:
            colecc_palabras[i] = 1
    return colecc_palabras

def mayor_frecuencia(colecc_palabras):
    """Función que crea una tupla con las palabras de mayor frecuencia.
...
... Parámetros:
...     - colecc_palabras: Recibe un diccionario de palabras.
... Salida:
...     Cada palabra con su frecuencia.
... """

    clave_max = " "
    max_freq = 0
    for palabra, freq in colecc_palabras.items():
        if freq > max_freq:
            clave_max = palabra
            max_freq = freq
    return clave_max, max_freq

texto = {"Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna"
         " aliqua. Sollicitudin nibh sit amet commodo nulla facilisi. Proin sagittis nisl rhoncus mattis rhoncus urna neque. "
         "Pellentesque id nibh tortor id aliquet lectus proin. Ut tortor pretium viverra suspendisse potenti nullam. "
         "Volutpat blandit aliquam etiam erat velit scelerisque in. Vulputate eu scelerisque felis imperdiet proin fermentum"
         " leo. Ultrices mi tempus imperdiet nulla. Varius vel pharetra vel turpis nunc eget lorem. Non blandit massa enim "}

contar_palabras(texto)
print(mayor_frecuencia(contar_palabras(texto)))