# *args Permite definir n cantidad de parametros en una funcion o metodo "*args" se usa como convencion
def suma(*args):
    total = 0
    for arg in args:
        total += arg
    return total

print(suma(5,6, 5,2))