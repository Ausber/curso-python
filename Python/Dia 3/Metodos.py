texto = "Este es el texto de Ausberto"
#str.upper() Pasar a Mayuscula un texto
resultado = texto.upper()
print(resultado)

#str.upper() Pasar a Minusculas un texto
resultado = texto.lower()
print(resultado)

#str.split() Devuelve una lista de los caracteres de un string dividios por un caracter
resultado = texto.split(" ")
print(resultado)

#str.join() Une una lista de caracteres por medio de un caracter
resultado = " ".join(resultado)
print(resultado)

#str.find() Buscar un caracter en una cadena de string
resultado = texto.find("e")
print(resultado)

#str.replace() Reemplaza una cadena de texto por otra
resultado = texto.replace("e","w")
print(resultado)