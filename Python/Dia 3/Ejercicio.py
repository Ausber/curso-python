"""
Enunciado: Pedir al usuario que ingrese un texto.
Ingrese 3 letras a su eleccion.
Cuantas veces aparece cada una de las letras que indico.
Cuantas palabras hay en todo el texto.
Cual es la primera letra y la ultima del texto.
Invertir el texto.
Aparece Python en el texto.
"""

texto = list(input("Ingrese un texto: ").lower())
count = len(texto)
letras_ingresadas = list(input("Ingrese 3 letras: ").lower())


for letra_ingresada in letras_ingresadas:
    print(f"La letra {letra_ingresada} se repite {texto.count(letra_ingresada)} veces en el texto")

print(f"El texto tiene {len(texto)} caracteres")
print(f"La primera letra del texto es {texto[0]} y la ultima letra del texto es {texto[count-1]}")

texto_normalizado = " ".join(texto)
aparece = "python" in texto_normalizado

texto.reverse()
texto_inverso = " ".join(texto)
print(f"El texto inverso es : \n \t{texto_inverso}")

if aparece == True:
    print("La palbra Python si aparece en el texto ingresado.")
else:
    print("La palbra Python no aparece en el texto ingresado.")