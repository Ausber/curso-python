"""
Práctica sobre Argumentos Indefinidos (*args) 1
Crea una función llamada suma_cuadrados que tome una cantidad indeterminada de argumentos numéricos, y que retorne la suma de sus valores al cuadrado.
Por ejemplo para los argumentos suma_cuadrados(1,2,3) deberá retornar 14 (1+4+9).
"""

"""def suma_cuadrados(*args):
    suma = 0
    for num in args:
        suma += (num*num)
    return suma


suma = suma_cuadrados(1, 2, 3)
print(suma)"""

"""
Crea una función llamada suma_absolutos, que tome un conjunto de argumentos de cualquier extensión, y retorne la suma de sus valores 
absolutos (es decir, que tome los valores sin signo y los sume, o lo que es lo mismo, 
los considere a todos -negativos y positivos- como positivos).
"""


"""def suma_absolutos(*args) -> int:
    suma: int = 0
    for num in args:
        if num < 0:
            num = num*-1

        suma += num
    return suma


suma = suma_absolutos(-1, 2, -3)
print(suma)


"""

"""
Crea una función llamada numeros_persona que reciba, como primer argumento, un nombre, y a continuación, una cantidad indefinida de números.

La función debe devolver el siguiente mensaje:

"{nombre}, la suma de tus números es {suma_numeros}"""


def numeros_personas(nombre,*args):
    suma = 0
    for num in args:
        suma += num
    return nombre, suma


data = numeros_personas("Federico",75, 20, 65)
print(f"{data[0]}, la suma de tus números es {data[1]}")


