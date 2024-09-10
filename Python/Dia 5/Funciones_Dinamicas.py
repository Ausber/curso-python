

def chequear_3_cifras(lista):
    for n in lista:
        if n in range(100,1000):
            return True
        else:
            pass
    return False

resultado = chequear_3_cifras([55,99,60])
print(resultado)