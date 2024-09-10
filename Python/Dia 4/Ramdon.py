from random import *

#randint Numeros aleatorios entre un rango  parametros
aleatorio = randint(1,50)
print(aleatorio)

#randint Numeros decimales aleatorios entre un rango  parametros
aleatorio = round(uniform(1,5),1)
print(aleatorio)

#ramdom Numeros aleatorios entre 0 y 1
aleatorio = random()
print(aleatorio)

#chocie elige valor de una lista
colores = ['azul','rojo','verde','amarillo']
aleatorio = choice(colores)
print(aleatorio)

#shuffle Mezcla valores de una lista, no se almacena, muta la lista
numeros = list(range(5,50,5))
shuffle(numeros)
print(numeros)