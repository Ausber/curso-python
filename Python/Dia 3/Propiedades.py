#Los string son inmutables
nombre = "Carina"
nombre = "Karina"
print(nombre)

#Los str se pueden concatenar
n1 = "Kari"
n2 = "na"
print(n1 + n2)

#los str se pueden multiplicar
print(n1*5)

#Los str son multilineas
poema = """Mil pequeños peces blancos
como si hirviera
el color del agua"""

print(poema)

#En los str se puede validar si contiene algo devuelve un true o false
print("agua" in poema)

#Se puede saber la cantidad de elementos de un str por medio de la propiedad len
print(len(poema))