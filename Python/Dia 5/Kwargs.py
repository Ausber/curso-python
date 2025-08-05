"""Clase para probar funcionamiento de kwargs"""
def suma(**kwargs):
    """metodo que sirve para sumar numeros
    Args: kwargs
    Return: suma de numeros
    """
    total = 0
    for clave,valor in kwargs.items():
        print(f"{clave} = {valor}")
        total += valor
    return total

print(suma(x=3,y=5,z=2))

def suma2(num1,num2,*args,**kwargs):
    """metodo que sirve para sumar numeros
    Args: kwargs
    Return: suma de numeros
    """
    total = 0
    for clave,valor in kwargs.items():
        print(f"{clave} = {valor}")
        total += valor
    return total



print(suma2(x=3,y=5,z=2))
